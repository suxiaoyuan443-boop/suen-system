---
name: suen-tarot-rule-inducer
description: 从已去重的结构化塔罗案例中寻找重复规律、反例、适用条件与冲突。
category: tarot-training
---

# Suen Tarot Rule Inducer

只使用已去重、来源可追溯案例；A/B 优先，C 辅助，D 不进入统计。

步骤：
1. 按问题、牌位、关键牌、组合、现实背景聚类；
2. 找重复处理方式；
3. 区分老师明示与模型归纳；
4. 主动搜反例；
5. 排除同一案例重复传播；
6. 写适用条件 / 例外；
7. 按证据规则标 O1/O2/O3；
8. 输出 `templates/rule.schema.json`；
9. suen_status 默认 observe，除非 Suen 明确采用。

禁止：单例升规则、只找支持、相关写必然、后验倒推老师明示、自动记 adopted。
