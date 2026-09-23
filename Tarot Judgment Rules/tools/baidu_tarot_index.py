#!/usr/bin/env python3
"""Read-only Baidu Netdisk recursive indexer for Suen tarot training assets.

The access token is read only from BAIDU_NETDISK_ACCESS_TOKEN.
No token is written to output files or logs.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API = "https://pan.baidu.com/rest/2.0/xpan/multimedia"
DEFAULT_FIELDS = [
    "fsid", "path", "filename", "isdir", "category", "size", "md5",
    "server_ctime", "server_mtime", "local_ctime", "local_mtime",
    "has_content", "has_abstract", "abstract", "extension", "candidate_hint"
]

HIGH_HINTS = (
    "实占", "案例", "个案", "咨询", "复合", "关系", "第三者", "感情", "婚姻",
    "事业", "工作", "辞职", "求职", "财运", "金钱", "时间", "人物", "宫廷牌",
    "逆位", "牌阵", "答疑", "学员", "直播", "复盘", "现场占卜", "补牌"
)
LOW_HINTS = ("招生", "开课", "介绍", "冥想", "历史", "基础牌义", "牌卡介绍")


def _token() -> str:
    token = os.getenv("BAIDU_NETDISK_ACCESS_TOKEN", "").strip()
    if not token:
        raise SystemExit(
            "缺少环境变量 BAIDU_NETDISK_ACCESS_TOKEN。请只在本机设置，不要把 Token 写进脚本、GitHub 或聊天。"
        )
    return token


def _request_json(params: dict[str, Any], timeout: int, retries: int) -> dict[str, Any]:
    url = API + "?" + urlencode(params)
    last: Exception | None = None
    for attempt in range(retries + 1):
        try:
            req = Request(url, headers={"User-Agent": "SuenTarotIndexer/1.0"})
            with urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
            last = exc
            if attempt >= retries:
                break
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError(f"请求百度网盘失败：{last}")


def _api_error(data: dict[str, Any]) -> str | None:
    for key in ("errno", "error_code"):
        value = data.get(key)
        if value not in (None, 0, "0"):
            message = data.get("errmsg") or data.get("error_msg") or data.get("error") or ""
            return f"{key}={value}, message={message}"
    return None


def _ext(path: str) -> str:
    return Path(Path(path).name).suffix.lower().lstrip(".")


def _hint(path: str) -> str:
    text = path.lower()
    high = [k for k in HIGH_HINTS if k.lower() in text]
    low = [k for k in LOW_HINTS if k.lower() in text]
    if high:
        return "high:" + "|".join(high[:8])
    if low:
        return "low:" + "|".join(low[:8])
    return "unknown"


def _normalize(item: dict[str, Any]) -> dict[str, Any]:
    path = str(item.get("path") or "")
    filename = str(item.get("filename") or item.get("server_filename") or Path(path).name)
    content = item.get("content")
    abstract = item.get("abstract")
    fsid = item.get("fsid", item.get("fs_id"))
    return {
        "fsid": fsid if fsid is not None else "",
        "path": path,
        "filename": filename,
        "isdir": item.get("isdir", ""),
        "category": item.get("category", ""),
        "size": item.get("size", ""),
        "md5": item.get("md5", ""),
        "server_ctime": item.get("server_ctime", item.get("ctime", "")),
        "server_mtime": item.get("server_mtime", item.get("mtime", "")),
        "local_ctime": item.get("local_ctime", ""),
        "local_mtime": item.get("local_mtime", ""),
        "has_content": bool(content),
        "has_abstract": bool(abstract),
        "abstract": abstract if isinstance(abstract, str) else "",
        "extension": _ext(path or filename),
        "candidate_hint": _hint(path or filename),
    }


def fetch_all(root: str, page_size: int, timeout: int, retries: int) -> list[dict[str, Any]]:
    token = _token()
    start = 0
    rows: list[dict[str, Any]] = []
    seen: set[str] = set()

    while True:
        params = {
            "method": "listall",
            "openapi": "xpansdk",
            "access_token": token,
            "path": root,
            "recursion": 1,
            "start": start,
            "limit": page_size,
            "order": "name",
            "desc": 0,
        }
        data = _request_json(params, timeout=timeout, retries=retries)
        err = _api_error(data)
        if err:
            raise RuntimeError(f"百度网盘 API 返回错误：{err}")

        items = data.get("list") or []
        if not isinstance(items, list):
            raise RuntimeError("百度网盘 API 响应中 list 不是数组，已停止，避免写入错误索引。")
        if not items:
            break

        added = 0
        for item in items:
            if not isinstance(item, dict):
                continue
            row = _normalize(item)
            key = str(row["fsid"] or row["path"])
            if key in seen:
                continue
            seen.add(key)
            rows.append(row)
            added += 1

        print(f"已读取 {len(rows)} 项（本页 {len(items)}，新增 {added}）", file=sys.stderr)
        start += len(items)

        if len(items) < page_size:
            break
        if start > 10_000_000:
            raise RuntimeError("索引项超过安全上限，已停止。请缩小 --root 后重试。")

    return rows


def write_csv(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=DEFAULT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def write_jsonl(rows: list[dict[str, Any]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_summary(rows: list[dict[str, Any]], path: Path, root: str) -> None:
    video_ext = {"mp4", "mov", "mkv", "avi", "flv", "m4v", "wmv", "ts"}
    doc_ext = {"pdf", "doc", "docx", "txt", "md", "srt", "vtt"}
    videos = [r for r in rows if str(r.get("category")) == "1" or r.get("extension") in video_ext]
    docs = [r for r in rows if str(r.get("category")) == "4" or r.get("extension") in doc_ext]
    high = [r for r in rows if str(r.get("candidate_hint", "")).startswith("high:")]
    summary = {
        "root": root,
        "total_items": len(rows),
        "video_items": len(videos),
        "document_items": len(docs),
        "filename_high_hint_items": len(high),
        "items_with_content_from_listall": sum(bool(r.get("has_content")) for r in rows),
        "items_with_abstract_from_listall": sum(bool(r.get("has_abstract")) for r in rows),
        "note": "listall 未返回 content/abstract 不代表百度没有生成字幕；下一阶段可通过官方 MCP file_meta/file_semantics_search 定向补充。"
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="只读递归索引百度网盘中的塔罗课程资产，不下载文件。")
    ap.add_argument("--root", default="/", help="百度网盘起始目录，默认 /。建议首次指向塔罗课程总文件夹。")
    ap.add_argument("--out-dir", default="./tarot_index_output", help="输出目录。")
    ap.add_argument("--page-size", type=int, default=500, help="分页大小，默认 500。")
    ap.add_argument("--timeout", type=int, default=30, help="单次请求超时秒数。")
    ap.add_argument("--retries", type=int, default=3, help="请求失败重试次数。")
    args = ap.parse_args()

    if args.page_size < 1 or args.page_size > 1000:
        raise SystemExit("--page-size 必须在 1..1000 之间。")

    out_dir = Path(args.out_dir).expanduser().resolve()
    rows = fetch_all(args.root, args.page_size, args.timeout, args.retries)
    write_csv(rows, out_dir / "tarot_master_index.csv")
    write_jsonl(rows, out_dir / "tarot_master_index.jsonl")
    write_summary(rows, out_dir / "tarot_master_index.summary.json", args.root)

    print(f"完成：{len(rows)} 项", file=sys.stderr)
    print(str(out_dir / "tarot_master_index.csv"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
