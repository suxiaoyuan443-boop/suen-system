# 百度网盘塔罗课程索引工具

这组工具只做**只读索引**。不会下载 328GB 视频，不会移动、删除、重命名百度网盘文件。

## 0. 安全规则

- Access Token 只保存在自己的电脑；
- 不把 Token 发到聊天；
- 不把 Token 写入 GitHub；
- 不截图包含 Token 的终端；
- 输出的 CSV / JSONL 不包含 Token；
- 建议首次只扫描“塔罗课程”总文件夹，不扫描无关私人网盘。

## 1. 电脑准备

需要 Python 3.10+。脚本仅使用 Python 标准库，不需要 pip install。

检查：

```bash
python --version
```

Windows 如果 `python` 不可用，可以试：

```powershell
py --version
```

## 2. 获取百度网盘 Access Token

按百度网盘官方 MCP / 开放平台的 OAuth 授权流程获取。

Token 等同于网盘访问凭证，只在本机使用。

## 3. 在本机临时设置 Token

### Windows PowerShell

```powershell
$env:BAIDU_NETDISK_ACCESS_TOKEN="你的Token"
```

关闭当前 PowerShell 后该临时变量自然失效。

### macOS / Linux

```bash
export BAIDU_NETDISK_ACCESS_TOKEN='你的Token'
```

关闭当前终端后该临时变量自然失效。

## 4. 运行索引

在仓库根目录执行。

### Windows

```powershell
py "Tarot Judgment Rules/tools/baidu_tarot_index.py" --root "/你的塔罗课程总文件夹"
```

### macOS / Linux

```bash
python3 "Tarot Judgment Rules/tools/baidu_tarot_index.py" --root "/你的塔罗课程总文件夹"
```

如果还不知道课程总文件夹的准确网盘路径，可先用一个较小的已知课程目录测试；不建议第一次直接扫整个 `/`。

## 5. 输出

默认生成到：

```text
tarot_index_output/
├── tarot_master_index.csv
├── tarot_master_index.jsonl
└── tarot_master_index.summary.json
```

CSV 方便人工查看 / 表格处理；JSONL 方便后续批处理；summary 用于先判断资料规模。

## 6. 第一轮跑完后做什么

先看 `tarot_master_index.summary.json`。

随后将**索引文件**作为下一阶段输入，而不是上传原视频。下一阶段会：

1. 按路径 / 文件名筛高概率案例；
2. 调百度官方 MCP 的 `file_semantics_search` 查文件名看不出的案例课；
3. 对候选 fsid 定向调用 `file_meta`，检查已有视频字幕 / 音频文稿 / 摘要；
4. 先用已有文字抽案例；
5. 只有明确缺字幕的高价值视频才进入下载 / 转录队列。

## 7. 已知限制

百度开放平台行为可能随接口版本、账号权限或个人体验策略变化。脚本遇到非零 `errno / error_code` 会停止，不会自动改动文件。

`listall` 没返回 `content / abstract` 不等于百度一定没有字幕；官方 MCP 的文件工具可能返回更丰富的内容字段，因此字幕检查放在第二阶段。
