# Foolish Fish｜近一年公开数据基线

状态：首批建档｜行级数据部分取得  
抓取 / 整理日期：2026-09-24  
主平台：YouTube + Patreon / 独立站商业桥  
账号：@foolishfishbooks  
观察窗：滚动近365天

## 数据源与口径

当前公开来源：
- Patreon sitemap｜https://www.patreon.com/foolishfish/sitemap
- SponsorRadar｜https://sponsorradar.com/channels/foolishfishbooks
- YouTube公开结果 / 第三方索引用于部分单条快照

Patreon负责证明固定更新节奏、会员权益与商业产品；SponsorRadar只作第三方赞助检测 / 估算，不能当实际成交或实际收入。

## 当前频道规模

当前公开第三方统计：
- YouTube订阅约163K；
- 视频总量约877；
- SponsorRadar 当前显示平均约3.8K views / video（第三方估计口径，不能视为官方年度中位数）；
- SponsorRadar当前：73 tracked deals、2 distinct brands；
- 最新检测到的deal日期：2026-09-12；
- SponsorRadar估算 sponsored video rate：$76–$151 / 条；
- SponsorRadar估算 AdSense：$23–$57 / 条。

后两项全部是第三方模型估算，**不进入真实收入 / GMV判断**。

## 来源冲突处理｜2026-09-24

当前已经确认，同一条视频在不同公开索引里可能出现明显不同的累计播放快照。

实例：
- 2026-09-16 Pick a Symbol：
  - YouTube公开结果：4,529播放 / 228赞；
  - 第三方当前快照：6.3K播放。
- 2026-09-03 Pick a Symbol：
  - YouTube公开结果：1,514播放 / 123赞；
  - 第三方当前快照：6.2K播放。

这不是允许“挑一个更喜欢的数字”。

正式处理：
- `FoolishFish-已核YouTube样本.csv`：只放YouTube公开结果；
- `FoolishFish-第三方快照-2026-09-24.csv`：只放第三方同源快照；
- 两轨都保留抓取日期；
- 类型内精确比较优先使用YouTube原页同来源样本；
- Sponsor / 商业容器判断可以使用第三方检测，但必须标明第三方；
- 任何冲突都不互相覆盖。

## 当前已取得的行级样本

注意：来源与抓取时点不同，下面先保存原始公开快照，**暂不拿这批混合时点数据直接计算全年中位数**。

| 发布日期 / 标题日期 | 内容 | 公开快照播放 | 点赞 | 类型 / 来源 |
|---|---|---:|---:|---|
| 2026-09-19 | Foolish Fish Esoteric News｜18 Sep Updates | 3.2K | N/A | SponsorRadar当前快照 |
| 2026-09-16 | Pick a Symbol Tarot｜16–22 Sep | 6.3K | N/A | SponsorRadar当前快照 |
| 2026-09-12 | Esoteric News｜11 Sep Updates | 2.6K | N/A | SponsorRadar当前快照 |
| 2026-09-03 | Pick a Symbol Tarot｜3–8 Sep | 6.2K | N/A | SponsorRadar当前快照 |
| 2026-08-01 | Esoteric News｜31 Jul Updates | 2,413 | 204 | YouTube公开结果 |
| 2026-06-27 | Esoteric News｜26 Jun Updates | 2,154 | 181 | YouTube公开结果 |

| 2026-04-25 | Esoteric News｜24 Apr Updates | 2,170 | 190 | YouTube当前直取｜video 4zYIT3XEUW8 |
| 2026-04-18 | Esoteric News｜17 Apr Updates | 2,776 | 221 | YouTube当前直取｜video KQ0P7Hr9EOA |
| 2026-04-10 | Esoteric News｜10 Apr Updates | 约2.1K | N/A | RUclips历史快照 |
| 2026-04-08 | Pick a Symbol Tarot｜8–14 Apr | 约2.4K | N/A | RUclips历史快照 |
| 2026-04-03 | Esoteric News｜3 Apr Updates | 约2.5K | N/A | RUclips历史快照 |
| 2026-04-01 | Pick a Symbol Tarot｜1–7 Apr | 约1.8K | N/A | RUclips历史快照 |
| 2026-03-27 | Esoteric News｜27 Mar Updates | 约2.0K | N/A | RUclips历史快照 |
| 2026-03-25 | Pick a Symbol Tarot｜25–31 Mar | 约1.6K | N/A | RUclips历史快照 |
| 2026-03-20 | Esoteric News｜20 Mar Updates | 约2.5K | N/A | RUclips历史快照 |
| 2026-03-18 | Pick a Symbol Tarot｜18 Mar | 约1.4K | N/A | RUclips历史快照 |
| 2026-03-13 | Esoteric News｜13 Mar Updates | 约2.4K | N/A | RUclips历史快照 |
| 2026-03-11 | Pick a Symbol Tarot｜11 Mar | 约1.8K | N/A | RUclips历史快照 |
| 2026-03-03 | Esoteric News｜3 Mar Updates | 约3.2K | N/A | RUclips历史快照 |
| 2026-03-04 | Pick a Symbol Tarot｜4 Mar | 约2.0K | N/A | RUclips历史快照 |

### 3—4月历史同源快照

RUclips 在 2026年4月中旬抓取到一批相邻视频，当时这些视频都处于相近的早期累计阶段。只取同一页面当前明确显示的 2026-03-03—04-10：

#### Esoteric News
- 03/03｜3.2K
- 03/13｜2.4K
- 03/20｜2.5K
- 03/27｜2.0K
- 04/03｜2.5K
- 04/10｜2.1K

中位：约 **2.45K**

#### Pick a Symbol Tarot
- 03/04｜2.0K
- 03/11｜1.8K
- 03/18｜1.4K
- 03/25｜1.6K
- 04/01｜1.8K
- 04/08｜2.4K

中位：约 **1.80K**

这段历史快照里，News 中位约为 Tarot 的 **1.36×**。

但 2026-08—09 SponsorRadar 同源快照里：
- Tarot中位约3.35K；
- News中位约2.60K；
- Tarot约为News的1.29×。

所以这个账号已经给出一个非常有价值的反例：

> **同一账号、同一两种固定栏目，相对播放优势会随时间变化。**

因此不能从8—9月直接总结“参与型塔罗永远比News强”，也不能用3—4月说“News永远更强”。

真正应该跟踪的是：
- 账号阶段；
- 观众对固定栏目的疲劳 / 新鲜度；
- 商业密度；
- 题材；
- 发布间隔；
- 累计时间。

### SponsorRadar 2026-08—09统一快照

同一抓取页面当前可见：

| 日期 | 内容 | 当前累计播放 | 检测赞助 |
|---|---|---:|---|
| 2026-09-19 | Esoteric News｜18 Sep | 3.2K | — |
| 2026-09-16 | Pick a Symbol Tarot｜16–22 Sep | 6.3K | — |
| 2026-09-12 | Esoteric News｜11 Sep | 2.6K | Miskatonic Books |
| 2026-09-03 | Pick a Symbol Tarot｜3–8 Sep | 6.2K | — |
| 2026-08-29 | Esoteric News｜28 Aug | 5.6K | Miskatonic Books |
| 2026-08-26 | Pick a Symbol Tarot｜26 Aug–1 Sep | 4.1K | — |
| 2026-08-22 | Esoteric News｜21 Aug | 2.8K | Miskatonic Books |
| 2026-08-19 | Pick a Symbol Tarot｜19–25 Aug | 2.2K | — |
| 2026-08-16 | Esoteric News｜14 Aug | 2.2K | Miskatonic Books |
| 2026-08-12 | Pick a Symbol Tarot｜12–18 Aug | 2.6K | — |
| 2026-08-08 | Esoteric News｜07 Aug | 2.0K | Miskatonic Books |
| 2026-08-05 | Pick a Symbol Tarot｜05 Aug–11 Aug | 2.4K | — |
| 2026-08-01 | Esoteric News｜31 Jul | 2.3K | Miskatonic Books |

同页当前频道快照：
- 订阅约163K；
- 平均每视频约3.8K views（SponsorRadar估计口径）；
- 73个tracked deals；
- 2个distinct brands；
- Miskatonic Books检测72条赞助；
- Jenx's Thai Occult Course检测1条。

这批数据比旧的“约2K / 3K”更适合做同源比较，但仍然是抓取时累计播放，不是统一发布后24小时。

这些 sponsor / 收入均为第三方检测与估算，不代表品牌或创作者官方确认。

### 当前SponsorRadar最近13条的另一层解释

当前13条里：
- 6条 Pick a Symbol Tarot；
- 7条 Esoteric News；
- 检测到 Sponsor 的全部集中在 News；
- Tarot 当前最高 6.3K / 6.2K；
- News 当前最高 5.6K，但多数2K—3K。

所以这组样本同时显示两种不同功能：

**参与型内容**
- 更容易形成阶段性高播放；
- 不承担Sponsor时也能独立存在。

**商业容器**
- 播放未必最高；
- 但结构稳定、Sponsor可重复插入；
- 不需要破坏其它研究 / 塔罗内容的观看体验。

这对 Suen 的直接意义：
> 以后不能要求每条内容同时完成 A流量 + D商业承接。固定商业容器本身就可以是一种独立内容产品。

### 8—9月同源样本的类型中位数

只计算 SponsorRadar 同一批 13 条当前累计快照：

- Pick a Symbol Tarot：6条，中位播放 **3.35K**，平均约3.97K；
- Esoteric News：7条，中位播放 **2.60K**，平均约2.96K。

Pick a Symbol 当前这小批样本的中位播放约为 News 的 **1.29×**。

但：
- 只有13条；
- 累计时间不同；
- News承担 sponsor / 商业更新；
- Pick a Symbol更偏参与 / 观看。

因此只记为：
**参与型内容当前更容易出现高播放，但 News 有独立商业功能。**

不能升级成“以后商业内容不要做 News”。

### 这一小段同源样本先说明什么

仅看8—9月这13条：
- Pick a Symbol Tarot 当前有 2.2K—6.3K；
- Esoteric News 当前有 2.0K—5.6K；
- 两类高度重叠，不能说“塔罗稳定碾压News”；
- 但9月两个 Pick a Symbol 都在6K+，明显高于当月两条 News；
- News 则承担了更稳定的 Sponsor 容器功能。

所以目前更合理的拆法是：
- **Pick a Symbol：观看 / 参与型内容；**
- **Esoteric News：稳定更新 + 商业承载型内容。**

不能只用播放量评估二者谁“更好”。

## 2026-08—09统一抓取样本

SponsorRadar 2026-09-24 当前页可直接取得13条连续公开视频的 lifetime views。这个窗口虽然只有约7周，但**抓取时点一致**，比之前混合时间点的快照更适合做短期类型比较。

| 日期 | 内容 | 当前播放 | Sponsor |
|---|---|---:|---|
| 2026-09-19 | Esoteric News｜18 Sep Updates | 3.2K | 未检测 |
| 2026-09-16 | Pick a Symbol Tarot｜16–22 Sep | 6.3K | 未检测 |
| 2026-09-12 | Esoteric News｜11 Sep Updates | 2.6K | Miskatonic Books |
| 2026-09-03 | Pick a Symbol Tarot｜3–8 Sep | 6.2K | 未检测 |
| 2026-08-29 | Esoteric News｜28 Aug Updates | 5.6K | Miskatonic Books |
| 2026-08-26 | Pick a Symbol Tarot｜26 Aug–1 Sep | 4.1K | 未检测 |
| 2026-08-22 | Esoteric News｜21 Aug Updates | 2.8K | Miskatonic Books |
| 2026-08-19 | Pick a Symbol Tarot｜19–25 Aug | 2.2K | 未检测 |
| 2026-08-16 | Esoteric News｜14 Aug Updates | 2.2K | Miskatonic Books |
| 2026-08-12 | Pick a Symbol Tarot｜12–18 Aug | 2.6K | 未检测 |
| 2026-08-08 | Esoteric News｜07 Aug Updates | 2.0K | Miskatonic Books |
| 2026-08-05 | Pick a Symbol Tarot｜05 Aug–11 Aug | 2.4K | 未检测 |
| 2026-08-01 | Esoteric News｜31 Jul Updates | 2.3K | Miskatonic Books |

这13条当前：
- 中位播放约 **2.6K**；
- 平均约 **3.42K**；
- 最高两条都是 Pick a Symbol Tarot（6.3K / 6.2K）；
- Esoteric News 大多数集中在2K—3K，但 8/29 有5.6K。

这只能回答**2026-08—09这一小段**，不能冒充全年分布。

### YouTube直取样本

- 2026-07-29｜Pick a Symbol Tarot - Your message for 22 July - 4 August 2026｜3,060播放｜399赞；
- 2026-08-12｜Pick a Symbol Tarot - Your message for 12 August - 18 August 2026｜2,618播放｜346赞。

这两条验证 SponsorRadar 当前量级大体合理，但抓取时点不同，不强行要求数字完全一致。

## 直接YouTube同口径对照

已建立：
`FoolishFish-已核YouTube样本.csv`

当前直接从 YouTube 公开结果取得 **31 条**可比样本：News 24条、Tarot 7条。

### Esoteric News｜n=24
- 中位播放：**2,304.5**
- P75：**2,465**
- P90：**2,737**
- 平均播放：约 **2,479**
- 中位点赞率：**8.22%**
- 当前范围：2,034—5,382
- IQR：**295**
- MAD：**145**
- MAD / 中位数：约 **6.3%**

### Pick a Symbol Tarot｜n=7
- 中位播放：**2,618**
- P75：**3,588.5**
- P90：**4,281.8**
- 平均播放：约 **2,960**
- 中位点赞率：**13.04%**
- 当前范围：1,902—4,529
- IQR：**1,342.5**
- MAD：**539**
- MAD / 中位数：约 **20.6%**

### 当前解释

补到24条News以后，一个重要修正出现了：

- News大多数样本仍高度集中在约2.0K—2.8K；
- 但 2026-08-29《28 August Updates》达到 **5,382**，证明News也会出现明显放量；
- 普通CV因此会被单个高端异常值拉高，不再适合单独描述稳定性；
- 用IQR / MAD看，News的**典型分布**仍明显比Tarot集中；
- Tarot则从主体分布到高端样本都更分散。

因此正式判断从“News低波动”修正为：

> **Esoteric News = 日常底盘高度集中、偶尔出现高放量异常值的稳定商业容器；Pick a Symbol = 典型分布本身就更宽、互动更深的参与容器。**

这比旧版“Tarot播放明显高于News”更准确：
- Tarot中位播放只约为News的 **1.14×**；
- 真正明显的差异是点赞深度与典型波动范围；
- News虽然多数不爆，但并非没有高上限。

商业含义仍成立：
- News长期承载Sponsor / affiliate / membership / consultation / product；
- 参与型内容更适合互动 / 放大；
- 两类内容不使用同一个成功KPI。

## 近一年发布结构｜Patreon sitemap

Patreon 当前索引显示 2026 年稳定存在：
- 几乎每周的 Esoteric News；
- 每月 planetary rituals；
- 折扣码 / 商店优惠；
- 会员专属咨询优惠；
- 课程 launch；
- Discord / Patreon / YouTube membership承接。

仅2026年7—9月即可看到：
- Jul 3 / 10 / 17 / 24 / 31 Esoteric News；
- Aug 7 / 14 / 21 / 28 Esoteric News；
- Sep 11 / 18 Esoteric News；
- 月初 planetary rituals / discount code；
- Sep 18 On-Demand Courses launch promo。

### 2026年News月度节点数

按 Patreon sitemap 当前 2026 区间逐月数：

| 月份 | Esoteric News节点 |
|---|---:|
| Jan | 4 |
| Feb | 4 |
| Mar | 4 |
| Apr | 4 |
| May | 5 |
| Jun | 4 |
| Jul | 5 |
| Aug | 4 |
| Sep（截至18日） | 2 |

2026-01—09当前共 **36 个** News 节点。

这不是36个“高流量研究视频”，而是36次稳定内容/商业容器触点。

同一时期还能确认每月重复存在：
- Planetary Rituals；
- Black Letter Press折扣；
- Lv.∞ 咨询优惠；
- 课程 / workshop / meditation 等节点。

这进一步说明 Foolish Fish 的后端不是靠单一爆款，而是靠**高频稳定容器 + 多产品承接**。

### 2026固定节奏已可确认

Patreon sitemap 当前支持一条非常稳定的节奏：

- Esoteric News：大致每周一次；
- Planetary Rituals：月度固定；
- Black Letter Press折扣码：月度固定；
- Lv.∞ 咨询优惠：月度固定；
- 课程 / 特别产品：按节点插入；
- 其它会员内容：冥想、课程、社群活动等。

从2026年3—9月可以连续看到：
- Mar 3 / 13 / 20 / 27 News；
- Apr 3 / 10 / 17 / 24 News；
- May 1 / 8 / 15 / 22 / 29 News；
- Jun 5 / 12 / 19 / 26 News；
- Jul 3 / 10 / 17 / 24 / 31 News；
- Aug 7 / 14 / 21 / 28 News；
- Sep 11 / 18 News。

这已经足够支持：
**Esoteric News不是偶发栏目，而是稳定商业承载骨架。**

## 近一年固定发布结构｜机器可读

已新增：
`FoolishFish-固定发布结构-近一年.csv`

当前滚动窗口内共整理出 **49 条** weekly news / roundup 类 Patreon 发布节点（2025-09-25—2026-09-18）。

这49条不是“49个YouTube独立研究视频”，而是用来证明：
- 固定商业 / 更新容器长期连续存在；
- 2025年11月下旬前主要以“Most Anticipated Occult Books and Events”命名；
- 2025-11-27以后稳定转为 Foolish Fish Esoteric News；
- 2026年3—9月周更节奏高度连续。

因此 Foolish Fish 的年度数据以后明确拆两类：
1. **流量内容**：Tarot / book review / long-form / 其它公开视频；
2. **商业容器**：News / sponsor / affiliate / membership / consultation / course。

不能拿49条固定商业容器去计算“研究视频年度中位播放”。

## Patreon近一年全节点

已新增：
- `FoolishFish-Patreon近一年原始索引.md`
- `FoolishFish-Patreon近一年全节点.csv`

当前滚动窗口内共 **85 个** Patreon 原始节点，按当前粗分：

- News / weekly roundup：**45**
- Planetary Rituals：**11**
- Consultation offer：**11**
- Discount / store code：**13**
- Guided meditation：**2**
- Course / product：**2**
- Event promo：**1**

这比旧的“49条 weekly/news”更完整：
- 49条旧表只证明固定更新容器；
- 85条新表同时把**更新、仪式、折扣、咨询、产品与活动**放在同一商业节奏里。

所以 Foolish Fish 的后端结构现在可以更准确地写成：

> **高频News触点 + 月度固定会员权益 + 商店折扣 + 咨询优惠 + 课程/产品节点。**

### 当前 Patreon 会员层级

Patreon当前公开会员页可确认：

**Lv.1 Patronus Beatus｜$2/月**
- Discord；
- News约提前24小时；
- Early access；
- 在提前期内无广告内容。

**Lv.2 Adeptus Occultorum｜$5/月**
- 包含前级；
- Tree of Life Pathworking Guided Meditations；
- Black Letter Press 每月7%折扣。

**Lv.3 Magister Venerabilis｜$10/月**
- 包含前级；
- 加入其每日 planetary ritual；
- 月度 guided visualisation；
- 名字出现在 Saturday videos；
- 继续保留Discord / 折扣等权益。

**Lv.∞ Lux Aeterna｜$100/月**
- 包含前级；
- 页面正文写“monthly code to get **95% off** a conversation”；
- 同页权益列表又写“Monthly **90% discount** voucher for a 1-to-1 chat”。

因此这里必须保留一个来源内部冲突：
**90% vs 95% 当前页面本身不一致，不替它统一成一个数。**

这对 Suen 很有价值：
会员梯度不是简单“多看几篇内容”，而是逐步加入：
**社群 → 提前看 → 折扣 → 仪式参与 → 冥想 → 展示 → 一对一咨询。**

但这只是对标结构，不代表 Suen 当前应该恢复 Patreon。

### Patreon滚动一年完整节点

已新增：
- `FoolishFish-Patreon近一年原始索引.md`
- `FoolishFish-Patreon近一年全节点.csv`

当前滚动365天 Patreon 原始节点：**85**。

按当前机器分类：
- News / weekly roundup：**45**
- Planetary Rituals：**11**
- Consultation offer：**11**
- Discount / store code：**13**
- Guided meditation：**2**
- Course / product：**2**
- Event promo：**1**

这比旧的49条 weekly/news 固定容器更完整：
- 49条表只回答“固定周更商业容器是否长期存在”；
- 85条全节点表把**更新、仪式、折扣、咨询、课程/产品与活动**放进同一时间线。

所以当前商业节奏可以更准确地概括为：

> **高频 News 触点 + 月度 ritual + 月度折扣 + 月度咨询优惠 + 少量课程 / 冥想 / 活动节点。**

### 当前 Patreon 会员权益

Patreon 公开会员页当前可确认：

**Lv.1 Patronus Beatus｜$2/月**
- Discord；
- News约提前24小时；
- Early access；
- 提前期内无广告。

**Lv.2 Adeptus Occultorum｜$5/月**
- 包含前级；
- Tree of Life Pathworking Guided Meditations；
- Black Letter Press 每月7%折扣。

**Lv.3 Magister Venerabilis｜$10/月**
- 包含前级；
- 加入其 daily planetary ritual；
- 月度 guided visualisation；
- 名字出现在 Saturday Videos；
- 保留Discord / 折扣等权益。

**Lv.∞ Lux Aeterna｜$100/月**
- 包含前级；
- 页面正文写每月获得 **95% off** conversation code；
- 同页权益列表又写 **90% discount** voucher for a 1-to-1 chat。

因此仓库保留这个来源内部冲突：
**90% 与95%当前页面自己不一致，不替来源统一成一个数字。**

这套梯度最值得迁移的是：
**社群 → 提前看 → 折扣 → 仪式参与 → 冥想 → 展示 → 一对一。**

它证明会员价值不必只是“多几篇文章”。

## 当前商业桥是这个账号最值得学的部分

SponsorRadar 当前检测：
- Miskatonic Books 被识别为约72条视频赞助；
- 另有 Jenx's Thai Occult Course；
- Esoteric News 长期稳定承载 sponsor。

公开视频描述还能看到：
- Amazon affiliate links；
- Patreon；
- YouTube membership；
- Discord membership benefit；
- workshop / course；
- personal consultation；
- oracle / card products；
- book recommendations。

所以 Foolish Fish 对 Suen 最重要的 benchmark 不是“怎么冲大播放”，而是：

> **同一个专业内容品牌怎样长期把书、课程、咨询、会员、赞助、商品放在一起，而不让每条视频都变成硬广告。**

## 当前内容结构初判

已有样本里：
- Esoteric News 多落在约2K—3K这一档；
- Pick a Symbol Tarot 当前几个样本约1.6K—6.3K，存在比 News 更高的单条；
- 但这些快照不是统一统计时点，不能直接下“塔罗一定比News强”的结论；
- News 的真正商业价值可能不是播放上限，而是**高频、稳定、赞助可插入、产品更新可承接**。

这对 Suen 很关键：
不是每一种内容都必须承担 A｜流量。
有些内容应该被评价为 **C｜服务认知 / D｜商业承接 / 稳定触达**。

## 年度数据缺口

还缺：
- 近365天完整 YouTube 公开视频行级列表；当前已有2026-08—09连续13条统一抓取样本 + 其它历史快照，但仍不足全年；
- 固定商业容器已另用49条 Patreon weekly/news 节点建成机器可读表，不再混进YouTube主内容样本；
- 统一抓取日后的 views / likes / comments；
- 正式时长；
- Book review / Esoteric Saturday / Tarot / News 不同类型的完整样本量；
- 年度中位数、P75、P90；
- 各类型分别计算中位数；
- 真实 sponsor / affiliate conversion不可见，因此不得估算成交。

## 当前可直接迁移

1. **固定可复用商业容器**：Esoteric News 本身就是稳定赞助 / 新书 / affiliate 承载框架；
2. **内容与产品不必一一对应**：频道的研究、塔罗、书评、News共同把人带向同一个后端生态；
3. **会员权益具体化**：提前看、Discord、折扣、课程、咨询等价值明确；
4. **商业密度通过固定栏目吸收**，而不是让每条专业内容结尾都突然卖东西。
