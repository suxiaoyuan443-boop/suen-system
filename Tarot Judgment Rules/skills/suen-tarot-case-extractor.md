---
name: suen-tarot-case-extractor
description: 从私有塔罗课程字幕、转录、讲义或实占记录中抽取结构化案例，不补猜未知信息。
category: tarot-training
---

# Suen Tarot Case Extractor

按 `templates/case.schema.json` 输出一个或多个独立案例。

硬规则：
1. 只抽材料真实存在的信息。
2. 不知道牌位 / 正逆位写 unknown。
3. 老师明确理由标 explicit；上下文推断标 inferred。
4. 同一案例跨 chunk 优先合并，不重复计数。
5. 可能需要前后文时标 `needs_context`。
6. 去掉可识别客户身份。
7. 不大量复制课程原文，以概括 + 时间戳追溯。
8. 老师结论与模型归纳分字段。
9. D 级碎片 `rule_eligible=false`。

优先抽：问题、背景、牌阵、牌面、正逆位、第一判断、改判点、降权牌、补牌逻辑、最终判断、后验、规则候选。
