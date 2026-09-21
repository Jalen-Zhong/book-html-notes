#!/usr/bin/env python3
"""Build full self-contained ZH/EN HTML for ch21 善败者不乱 / Skilled Defeat, No Chaos."""
from pathlib import Path

DIR = Path(__file__).resolve().parent

MERMAID_INIT = """
  <script>
    mermaid.initialize({
      startOnLoad: true,
      theme: "dark",
      securityLevel: "loose",
      timeline: { useMaxWidth: true },
      flowchart: { useMaxWidth: true, htmlLabels: true, curve: "basis" }
    });
  </script>
"""

def page(lang, title, hero_badge, h1, subtitle, note, toc_items, chapter_mark, body, footer_label):
    home = (
        '<a href="../../../index.html">返回首页</a>'
        if lang == "zh" else
        '<a href="../../../index.html">Back to home</a>'
    )
    switch = (
        '<a class="active" href="skilled-defeat-zh.html">中文</a>\n'
        '        <a href="skilled-defeat-en.html">English</a>\n'
        '        ' + home
        if lang == "zh" else
        '<a href="skilled-defeat-zh.html">中文</a>\n'
        '        <a class="active" href="skilled-defeat-en.html">English</a>\n'
        '        ' + home
    )
    toc = "\n".join(f'          <li><a href="#{aid}">{atxt}</a></li>' for aid, atxt in toc_items)
    return f"""<!DOCTYPE html>
<html lang="{"zh-CN" if lang == "zh" else "en"}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <link rel="stylesheet" href="chapter.css" />
</head>
<body>

  <div class="wrap">
    <div class="hero">
      <div class="lang-switch" aria-label="{"语言" if lang == "zh" else "Language"}">
        {switch}
      </div>
      <div class="badge">{hero_badge}</div>
      <h1>{h1}</h1>
      <p class="subtitle">{subtitle}</p>
      <div class="note">
        {note}
      </div>
      <nav class="toc" aria-label="{"章节导航" if lang == "zh" else "Section navigation"}">
        {"本节导览" if lang == "zh" else "In this chapter"}
        <ul>
{toc}
        </ul>
      </nav>
    </div>
    <article class="story">
      <div class="chapter-mark">{chapter_mark}</div>
{body}
    </article>

    <footer>
      {footer_label} ·
      <a href="SOURCES.md">SOURCES.md</a> ·
      <a href="../../../index.html">{"返回首页" if lang == "zh" else "Back to home"}</a>
    </footer>
  </div>
{MERMAID_INIT}
</body>
</html>
"""

ZH_TOC = [
    ("s1", "顺风满帆：加州债差价生意"),
    ("s2", "自鸣得意：离失败不远了"),
    ("s3", "巴克莱的「便宜货」：245 基点成交"),
    ("s4", "高盛只买二百五十万：报价后退"),
    ("s5", "加州财政警报：监视名单与枯竭"),
    ("s6", "淮海战役隐喻：别忘了架浮桥"),
    ("s7", "三天突围：多路撤退与八十万学费"),
    ("s8", "善败者不乱：趋势与流动性"),
    ("diagrams", "人物关系 / 时间线 / 知识图谱"),
]

EN_TOC = [
    ("s1", "Fair winds: California bid-offer scrapes"),
    ("s2", "Smugness: failure is near"),
    ("s3", "Barclays' \"cheap\" paper: filled at 245"),
    ("s4", "Goldman buys only 2.5: quote walks back"),
    ("s5", "California fiscal alarm: watch list & dry tape"),
    ("s6", "Huaihai metaphor: don't forget pontoons"),
    ("s7", "Three-day breakout: multi-path exit, $800k tuition"),
    ("s8", "Skilled defeat, no chaos: trend vs liquidity"),
    ("diagrams", "Relationships / timeline / knowledge graph"),
]

ZH_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/California_State_Capitol,_Sacramento.jpg" alt="加州州议会大厦" loading="lazy" />
        <figcaption>加州州议会大厦——2009 年春天，财政僵局与评级压力把市政债流动性变成「大运河」。来源：Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">顺风满帆：加州债差价生意</h2>
      <p>承接 §20：BAB 新游戏开盘，动量交易让四月账本亮眼。2009 年春天，全球市场复苏迹象渐显——压力测试、量化宽松、零利率把资金从「货币市场防空洞」里往外赶。市政债也红火：新生事物 BAB 消息散开，越来越多买家涌入；早一步的渔阳搭上顺风车。<a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>手中约 <strong>五千万美元</strong>加州债券，让他体会到「掌握稀缺资源」：地方券商从他进货，客户想卖时他也愿报略优于大行的价——有进有出，稳稳赚差价；需要调节就与高盛、巴克莱对敲，存货大致锁在五千万左右。盈利稳步上升，自信跟着上升：债券交易……好像挺容易。</p>

      <div class="side-panel">
        <h3 class="panel-title">本章时间锚点 · 2009 春 → 6 月突围</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">春</div><div class="ev">复苏 · BAB 余温 · 加州存货 ~5千万</div></div>
          <div class="event-card"><div class="yr">6 上旬</div><div class="ev">零售变冷 · 巴克莱抛货</div></div>
          <div class="event-card"><div class="yr">次日</div><div class="ev">财政新闻 · 评级监视</div></div>
          <div class="event-card"><div class="yr">三天</div><div class="ev">多路撤退 · 清仓</div></div>
        </div>
      </div>

      <div class="scene">
        顺风不是技能证明；它只是把「自鸣得意」的陷阱擦得更亮。
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn1">
          <strong>¹ 2009 春：压力测试、QE 与风险偏好回升</strong>
          2009 年 2–5 月，美国银行业压力测试（SCAP）、美联储量化宽松与近零利率政策，把投资者从现金与货基「防空洞」推向风险资产。市政债与建设美国债券（BAB）同期升温（见 §20）。公开危机年表强调：流动性注入先修复「造血」，再修复价格——交易台最容易在这一段误把顺风当成能力。
          <div class="why">为何重要：本章冲突的起点不是「看空加州」，而是「赢了之后如何不乱」。</div>
          <div class="src">来源：Fed / Treasury 危机年表；SCAP 公开材料；§20 BAB 导读</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">自鸣得意：离失败不远了</h2>
      <p>债券交易当然不容易。顺风满帆之际，礁石往往就在船头。某位对冲基金前辈说过一句被公开试读反复引用的话：<strong>「每当我自鸣得意之时，就离失败不远了。」</strong>此言不虚。<a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>§20 刚讲完「挖出金币」；本章立刻翻面——金币挖出来之后，若把「容易」当成常态，流动性一旦抽走，五千万头寸就会变成淮海战场上的重兵。</p>

      <div class="scene">
        善败，从承认「我可能正在自鸣得意」开始。
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn2">
          <strong>² 「自鸣得意」与交易心理学</strong>
          公开试读与读者摘录都将此句标为本章金句。行为金融学把「赢后过度自信／归因偏差」写成常见风险：连续盈利会压缩主观波动估计、放大仓位、推迟止损。脚注不考证那位「前辈」身份，只锚定主题：得意是撤退纪律的敌人。
          <div class="why">为何重要：给后文「坚决果断撤退」立下心理前提。</div>
          <div class="src">来源：公开试读金句摘录；行为金融过度自信文献综述</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">巴克莱的「便宜货」：245 基点成交</h2>
      <p>六月上旬，加州债零售生意明显变冷，价格略回落。巴克莱销售孟仁来电恭维：「小渔，最近加州债做得不错嘛！」渔阳从不把雷曼系市政台的夸奖当糖果——他知道必有戏。<a class="fn-link" href="#fn3"><sup class="fn">³</sup></a></p>
      <p>孟仁推销：交易员山姆手里还有约 <strong>一千万</strong>五年期加州债，想腾手支持新券流动性；报价利差约 <strong>235 基点</strong>（相对同期国债）。渔阳心想：危机后各行控存货，巴克莱减仓或许真是捡便宜。他知高盛报价约 240/230，故意报了更「苛刻」的 <strong>245</strong>——按说对方不该接。</p>
      <p>几秒后：<strong>「山姆说 245 可以，卖了。」</strong>心头一咯噔——2007 年 10 月田纳西住房债的阴影闪过。他还是决定立刻把刚接的一千万转给高盛。</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Barclays_Bank_logo.svg" alt="巴克莱标志" loading="lazy" />
        <figcaption>巴克莱——危机后承接雷曼北美业务的一角；本章里「指导价」与真买盘的落差，是突围的第三座浮桥伏笔。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        当你故意报一个「不可能成交」的价，对方一口答应——那往往不是礼物。
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn3">
          <strong>³ 市政债报价惯例与销售「无辜信使」角色</strong>
          市政/信用债常以相对国债的利差（basis points）双边报价；销售把客户出价喊给交易员、再回传，口头上像「中立传话」，实务上仍服务本台存货与风险。雷曼倒闭后，其北美投行与部分资本市场业务由巴克莱承接——公开史把「雷曼市政风格」与「巴克莱资产负债表」叠在同一电话线两端。脚注用市场惯例解释「245 成交」的刺耳感，不复述书中对话原文。
          <div class="why">为何重要：解释为何「便宜货」成交本身就是信息。</div>
          <div class="src">来源：MSRB / 固定收益微观结构入门；巴克莱收购雷曼北美业务公开报道</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">高盛只买二百五十万：报价后退</h2>
      <p>他拨通高盛销售，先问五年期加州债报价——仍是 240/230。他按 240 卖一千万。电话静音了好几分钟。坏消息：交易员伊森<strong>只买二百五十万美元</strong>；做完这笔，报价要退到 250/240。<a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>为了区区一小单，手里其余五千万多的市价全被拖低。更糟的是：他隐约觉得加州债要出问题——流动性正在从「双边畅通」收成「独木桥」。</p>

      <div class="scene">
        出口报价不能改，但「买多少」从来没说死——尺寸本身就是风控武器。
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ 做市商尺寸限额与「报价后退」</strong>
          固定收益做市商常对报价附加隐性或显性的 size limit；成交后立即 widening / backing the quote，是管理存货与信息风险的标准动作。危机后资本与风险限额更紧，大单「照单全收」的时代短暂结束。公开微观结构文献称之为 inventory control 与 adverse-selection defense——对手一问大尺寸，你就收窄承诺。
          <div class="why">为何重要：把「包围圈」从隐喻落到可操作的市场结构。</div>
          <div class="src">来源：固定收益做市商库存模型综述；危机后一级交易商风险限额讨论</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">加州财政警报：监视名单与枯竭</h2>
      <p>次日，媒体报道加州财政恶化：开支庞大、税基依赖资本利得与房产、危机后收入塌、福利升——州政府面临巨额赤字。联邦可以发国债补窟窿；多数州宪法却限制「借债过日子」。民主党要增税、共和党要砍开支，议会卡在 60% 增税门槛；州长施瓦辛格束手。主计长警告：金库将告罄，可能只能开「白条」（IOU）。<a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>三大评级机构相继把加州债放入<strong>监视名单</strong>。流动性枯竭——大券商里几乎只剩高盛还做市，且明码每单约 250 万。渔阳试探卖一单，报价立刻再退。包围圈合拢：五年内破产概率仍极低，但短期价格由供求决定——买家驻足、长线户重估、卖盘凭空出现，稀疏成交量里随时可能雪崩。</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Arnold_Schwarzenegger_speaking_at_CPAC_2015_by_Michael_Vadon_10.jpg" alt="施瓦辛格" loading="lazy" />
        <figcaption>阿诺·施瓦辛格——银幕「终结者」遇上议会算术；2009 年加州预算僵局把评级与 IOU 推上头条。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        内在价值可以慢慢算；流动性可以一夜消失。
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn5">
          <strong>⁵ 2009 年加州预算危机、评级监视与 IOU</strong>
          2009 年夏，加州面对约 240–260 亿美元量级的预算缺口；两党在增税（需议会超多数）与开支削减上僵持。主计长 John Chiang 警告现金耗尽；7 月初州政府开始向部分债权人开出 registered warrants（俗称 IOU）。S&amp;P 等机构将州债评级置于负面监视或下调；Fitch、Moody's 随后跟进（公开 STO 评级史可核对）。脚注锚定公开财政与评级事实；书中交易数字为导读改写。
          <div class="why">为何重要：解释为何「基本面未破产」仍可触发流动性围剿。</div>
          <div class="src">来源：LA Times 2009-07 IOU 报道；California STO GO 评级史；S&amp;P/Fitch/Moody's 当代新闻</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">淮海战役隐喻：别忘了架浮桥</h2>
      <p>焦虑中他想起历史：1948 年淮海战役，黄百韬兵团本有时间西撤徐州，却为接应友军在运河以东耽搁，更致命的是<strong>忘记在运河上架设浮桥</strong>——十万大军挤唯一铁路桥，延误后在碾庄陷入重围。<a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>映射清晰：五千万加州债 ≈ 黄兵团；下跌价格 ≈ 南下华野；稀疏流动性 ≈ 大运河；每单只买 250 万的高盛 ≈ 唯一铁路桥。若等老板强制减仓，连锁反应可能毁掉整个交易计划。</p>
      <p>总退却两条原则：<strong>马上行动</strong>（别在「新安镇」傻等）；<strong>多路撤退</strong>（立刻「架设浮桥」）。</p>

      <div class="scene">
        独木桥不是出口策略；浮桥才是。
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ 淮海战役 · 黄百韬与运河铁路桥</strong>
          1948 年 11 月，华东野战军包围徐州以东黄百韬第七兵团。公开战史叙述常强调：兵团在新安镇一带滞留接应，且未能充分开辟运河渡口／浮桥，撤退高度依赖铁路桥，延误后在碾庄圩地区被歼。作者用军事史作流动性隐喻——「铁路桥＝唯一大做市商，浮桥＝备用买家渠道」。此处为公开战史摘要 + 章节寓意，非军事论文。
          <div class="why">为何重要：本章标题「善败者不乱」的战术图像——败要有队形、有退路。</div>
          <div class="src">来源：公开淮海战役战史综述；中国军事史通识读物</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">三天突围：多路撤退与八十万学费</h2>
      <p><strong>浮桥一</strong>：通知地方券商，电子平台上的加州债大幅降价，并找中小机构客户推销——广撒网。<strong>浮桥二</strong>：搜索报价单，发现花旗对五年期仍有买价——危机后花旗士气低、「慢半拍」；别人已杀到更紧，他的出价反而成了救命通道。渔阳故意报一个有零有整的奇怪面额，装成「就这么多」——花旗照单全收，随后出价后退。<a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>
      <p><strong>浮桥三</strong>：巴克莱挂着指导性报价；真要卖时对方称「只是 indicative」。渔阳拍案：放报价却不买、还套我动机——以「以后怎么做生意」施压，最终以略差价格甩出近千万。然后才动用高盛这座「铁路桥」，连续砸单，报价被打退。</p>
      <p>第一天撤出约六成；他知道市场已被惊动，次日可能雪崩——果然有人还在讨价还价。他一律 hit：花旗、高盛、地方网来的出价，见价就打。抛出最后一笔时，高盛报价已退得很宽。三天损失约 <strong>八十万美元</strong>，但脱离险境。几天后价格继续大跌；若未平仓，残余头寸损失可能接近三百万量级。大老板问还剩多少加州债——「零。」「很好。」</p>

      <div class="scene">
        八十万是学费；三百万是「忘记架浮桥」的发票。
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ 多渠道退出与 indicative vs firm 报价</strong>
          机构债市常区分 firm（可成交）与 indicative（意向／广告）报价；流动性紧张时，挂牌价可能迅速「变成风景」。危机管理实务强调：提前铺设多家对手方、零售与机构分流、接受滑点以换确定性——即「架浮桥」。公开试读把花旗「慢半拍」、巴克莱指导价、高盛尺寸限额写成三条退路；数字为故事尺度，非可复核成交回报。
          <div class="why">为何重要：把「善败」落成可执行的退出工程，而非鸡汤。</div>
          <div class="src">来源：固定收益交易实务入门；危机流动性管理综述；公开试读情节节拍（改写）</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">善败者不乱：趋势与流动性</h2>
      <p>这场突围有典型意义：流动性是债券投资者的生死题——次贷里，杠杆债投资者曾「牺牲在包围圈中」。但硬币另一面：流动性差的市场，趋势往往更强；流动性极强的成熟股市，趋势反而难抓——成交量、衍生品与套利把供求撕碎，有效市场叙事下「跑赢大盘」极难。<a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>
      <p>债券与房地产更接近「真实需求」驱动：发行人要融资、买家要配置、购房者要住——价格不唯一目标；稀疏流动性又让套利难瞬间抹平失衡，趋势得以延伸。作者总结口诀：<strong>紧跟趋势，注意流动性（Follow trend, manage liquidity）</strong>。</p>
      <p>富豪中靠地产起家者远多于纯炒股；债市大腕亦然。地产与债券常用杠杆——周期性流动性危机是生存课。最好的投资者，往往是最<strong>善败</strong>的投资者：撤退必须坚决果断，别忘了架设浮桥（拓宽流动性渠道）。</p>
      <p>古典句出自棋经／兵法谱系：<strong>善败者不乱</strong>——会输的人，队形不溃。<a class="fn-link" href="#fn9"><sup class="fn">⁹</sup></a> 下一章 §22「新市场，新思维」：清仓之后，如何在后海啸秩序里换脑子。</p>

      <div class="scene">
        善败者不乱——不是从不亏损，而是亏损时仍保持队形与退路。
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn8">
          <strong>⁸ 流动性—趋势张力与有效市场</strong>
          市场微观结构与资产定价文献常讨论：高换手、低摩擦市场更接近「信息迅速进入价格」，可预测趋势更弱；高摩擦、分割的信用/市政/房地产市场，供需冲击可持续更久。有效市场假说（EMH）对股票指数的「难以持续跑赢」叙述与此相容，但并不否定非完美市场中的风险管理溢价。导读写「Follow trend, manage liquidity」，是交易纪律口诀，不是学术定理声明。
          <div class="why">为何重要：把个人突围升成可迁移的投资原则，并桥接 §22。</div>
          <div class="src">来源：EMH 综述；信用债／房地产流动性研究；公开试读收束段（改写）</div>
        </div>
        <div class="fn-item" id="fn9">
          <strong>⁹ 「善败者不乱」出典</strong>
          句式见于《棋经十三篇·合战篇》：「善胜者不争，善阵者不战；善战者不败，善败者不乱。」《西游记》第十回弈棋段亦引近文。兵法谱系另有《汉书·刑法志》「善败者不亡」、诸葛亮《将苑》等变体——核心都是：会败者能保存建制、不溃乱。本章借棋/兵法语，讲交易台回撤纪律。
          <div class="why">为何重要：点题；并标明这是古典成语在金融叙事中的借用，而非《孙子》逐字原文。</div>
          <div class="src">来源：《棋经十三篇》公开文本；《汉书·刑法志》；成语／兵法语源辞书</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>人物关系 / 时间线 / 知识图谱</h2>

        <div class="mermaid-wrap">
          <div class="caption">人物与机构：从顺风存货到多路浮桥</div>
          <div class="mermaid">
flowchart LR
  YY[渔阳 · 鲁西交易台] --> INV[加州债存货 ~5千万]
  BR[巴克莱 · 孟仁/山姆] --> SELL[抛售 1千万 @245]
  SELL --> YY
  YY --> GS[高盛 · 伊森]
  GS --> LIM[每单 ~250万 · 报价后退]
  NEWS[加州财政新闻] --> WL[评级监视名单]
  WL --> DRY[流动性枯竭]
  YY --> P1[浮桥1 地方券商/零售]
  YY --> P2[浮桥2 花旗慢半拍]
  YY --> P3[浮桥3 巴克莱指导价]
  LIM --> RAIL[铁路桥 高盛]
  P1 --> EXIT[三天清仓]
  P2 --> EXIT
  P3 --> EXIT
  RAIL --> EXIT
  EXIT --> NEXT[§22 新市场新思维]
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">时间线：善败者不乱（2009 春 → 6 月突围）</div>
          <div class="mermaid">
timeline
    title Skilled Defeat No Chaos
    spring 2009 : Recovery · BAB afterglow · CA inventory
    early June : Retail cools · Barclays fills 245
    next day : Fiscal headlines · rating watch · dry tape
    day 1 exit : Pontoons 1-3 · 60 percent out
    day 2-3 : Hit all bids · flat book · ~800k loss
    days later : Price gaps wider · boss asks zero
    bridge : Toward §22 new market new mind
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">知识图谱：善败如何保持队形</div>
          <div class="mermaid">
flowchart TB
  S20[§20 圣经故事] --> WIN[动量盈利 · 自信上升]
  WIN --> SMUG[自鸣得意风险]
  SMUG --> SHOCK[对手倒货 · 尺寸限额]
  SHOCK --> NEWS[财政/评级冲击]
  NEWS --> LIQ[流动性包围圈]
  HUAI[淮海隐喻] --> RULES[马上走 · 多架浮桥]
  LIQ --> RULES
  RULES --> EXIT[坚决撤退 · 接受滑点]
  EXIT --> PRINCIPLE[Follow trend manage liquidity]
  PRINCIPLE --> SAYING[善败者不乱]
  SAYING --> S22[§22 新市场新思维]
          </div>
        </div>
      </section>
'''

EN_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/California_State_Capitol,_Sacramento.jpg" alt="California State Capitol" loading="lazy" />
        <figcaption>California State Capitol—in spring 2009, budget deadlock and rating pressure turned muni liquidity into a “Grand Canal.” Source: Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">Fair winds: California bid-offer scrapes</h2>
      <p>After §20: the BAB new game opened, and momentum made April’s P&amp;L shine. By spring 2009, recovery signs thickened—stress tests, QE, and near-zero rates pushed cash out of the money-market “bomb shelter.” Munis were hot too: BAB chatter drew buyers; Yuyang, early, caught a tailwind. <a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>Roughly <strong>$50 million</strong> of California bonds felt like scarce inventory: regional dealers bought from him; when their clients sold, he bid a touch better than the big banks—two-way scrapes, steady edge; when he needed to adjust, he crossed with Goldman or Barclays and kept the box near fifty. Rising P&amp;L fed rising confidence: bond trading… seemed easy.</p>

      <div class="side-panel">
        <h3 class="panel-title">Chapter anchors · Spring 2009 → June breakout</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">Spring</div><div class="ev">Recovery · BAB afterglow · CA ~$50mm</div></div>
          <div class="event-card"><div class="yr">Early Jun</div><div class="ev">Retail cools · Barclays dumps</div></div>
          <div class="event-card"><div class="yr">Next day</div><div class="ev">Fiscal news · rating watch</div></div>
          <div class="event-card"><div class="yr">3 days</div><div class="ev">Multi-path exit · flat</div></div>
        </div>
      </div>

      <div class="scene">
        A fair wind is not proof of skill; it only polishes the trap labeled “I have this.”
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn1">
          <strong>¹ Spring 2009: stress tests, QE, and risk appetite</strong>
          In Feb–May 2009, U.S. bank stress tests (SCAP), Fed QE, and near-zero rates pulled investors out of cash and money funds into risk assets. Munis and Build America Bonds warmed in parallel (see §20). Crisis chronologies stress: liquidity repairs the “bloodstream” before prices—desks most easily mistake the wind for talent in that window.
          <div class="why">Why it matters: the chapter conflict is not “short California,” but “how not to riot after winning.”</div>
          <div class="src">Source: Fed/Treasury crisis chronologies; SCAP public materials; §20 BAB guide</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">Smugness: failure is near</h2>
      <p>Bond trading is never easy. In a fair wind, the reef is often just ahead. A hedge-fund elder’s line, echoed in public trial-reads, lands as chapter gospel: <strong>“Whenever I get smug, failure is not far.”</strong> True enough. <a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>§20 just dug the coin up; this chapter flips it—once “easy” feels normal, a liquidity vacuum can turn a $50mm book into a Huaihai-scale army trapped against a canal.</p>

      <div class="scene">
        Skilled defeat begins by admitting: I may be getting smug right now.
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn2">
          <strong>² Smugness and trading psychology</strong>
          Public trial-reads and reader annotations flag the line as a chapter gold quote. Behavioral finance files post-win overconfidence / attribution bias as common risk: streaks shrink subjective vol, inflate size, delay cuts. The footnote does not ID the “elder”—only the theme: smugness is the enemy of exit discipline.
          <div class="why">Why it matters: psychological premise for the later “decisive retreat.”</div>
          <div class="src">Source: public trial-read quote digests; overconfidence literature surveys</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">Barclays' "cheap" paper: filled at 245</h2>
      <p>In early June, California retail cooled and prices slipped a touch. Barclays salesperson Meng Ren called with praise: “Not bad on California lately!” Yuyang never took Lehman-style muni flattery as candy—he knew a pitch was coming. <a class="fn-link" href="#fn3"><sup class="fn">³</sup></a></p>
      <p>Meng pitched: trader Sam still held about <strong>$10 million</strong> five-year California, wanted dry powder for new-issue liquidity support; offered around <strong>235 bp</strong> over Treasuries. Yuyang thought: post-crisis banks hated inventory; maybe this was a real clearance. Knowing Goldman’s market near 240/230, he deliberately bid a harsher <strong>245</strong>—they “shouldn’t” lift.</p>
      <p>Seconds later: <strong>“Sam says 245 works. Sold.”</strong> A lurch—October 2007 Tennessee housing-bond déjà vu. Still, he decided to flip the fresh ten straight to Goldman.</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Barclays_Bank_logo.svg" alt="Barclays logo" loading="lazy" />
        <figcaption>Barclays—one heir to Lehman’s North American franchise; the later gap between “indicative” and real bids becomes pontoon three. Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        When you bid a “never fills” price and it fills instantly—that is usually not a gift.
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn3">
          <strong>³ Muni quote convention and the “innocent messenger” salesperson</strong>
          Credit/munis often show two-way spreads in basis points vs Treasuries; sales shout a client bid to the trader and relay back—orally “neutral,” in practice serving desk inventory and risk. After Lehman’s failure, Barclays took parts of the North American franchise—public history stacks “Lehman muni style” and “Barclays balance sheet” on one phone line. The footnote uses market custom to explain why a 245 fill stings; it does not paste book dialogue.
          <div class="why">Why it matters: explains why the “cheap” fill is itself information.</div>
          <div class="src">Source: MSRB / fixed-income microstructure primers; Barclays–Lehman NA acquisition coverage</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">Goldman buys only 2.5: quote walks back</h2>
      <p>He called Goldman sales, asked the five-year California market—still 240/230—and offered $10mm at 240. Hold music stretched minutes. Bad news: trader Ethan would buy only <strong>$2.5 million</strong>; after that print, the quote would back to 250/240. <a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>For a tiny clip, the mark on the remaining fifty-plus got dragged. Worse: he sensed California was about to break—liquidity shrinking from two-way street to single plank.</p>

      <div class="scene">
        The posted bid may be firm on price; size was never a blank check—size is a risk weapon.
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ Dealer size limits and backing the quote</strong>
          Fixed-income market-makers often attach implicit or explicit size limits; widening or backing after a fill is standard inventory and adverse-selection control. Post-crisis capital and risk caps ended the era of “any size, any time.” Microstructure calls it inventory control—ask for large, and the promise shrinks.
          <div class="why">Why it matters: lands the “encirclement” in operable market structure.</div>
          <div class="src">Source: dealer inventory-model surveys; post-crisis primary-dealer risk-limit discussions</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">California fiscal alarm: watch list &amp; dry tape</h2>
      <p>Next day, headlines hit California’s fiscal mess: heavy spending, tax base tied to capital gains and property, crash-era revenue collapse and rising welfare—double-digit-billion deficits. The federal government can issue Treasuries; most state constitutions curb “living on debt.” Democrats wanted taxes, Republicans cuts; a supermajority tax rule jammed the legislature; Governor Schwarzenegger looked stuck. The Controller warned the till could run dry—IOUs incoming. <a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>Major rating agencies put California on <strong>watch</strong>. Liquidity evaporated—among big dealers, barely Goldman still made a market, and only about $2.5mm a clip. A probe sale backed the quote again. The ring closed: five-year default odds still tiny, but short-run price is supply and demand—buyers freeze, longs reassess, phantom offers appear; in a thin tape, avalanche risk is real.</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Arnold_Schwarzenegger_speaking_at_CPAC_2015_by_Michael_Vadon_10.jpg" alt="Arnold Schwarzenegger" loading="lazy" />
        <figcaption>Arnold Schwarzenegger—the screen Terminator met legislative arithmetic; 2009’s budget deadlock put ratings and IOUs on the front page. Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        Fundamentals can be argued slowly; liquidity can vanish overnight.
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn5">
          <strong>⁵ 2009 California budget crisis, rating watches, and IOUs</strong>
          In summer 2009 California faced a budget hole on the order of $24–26 billion; parties deadlocked on tax hikes (supermajority) versus cuts. Controller John Chiang warned of a cash crunch; in early July the state began issuing registered warrants (IOUs) to some payees. S&amp;P and peers placed or cut GO ratings on watch/downgrade; Fitch and Moody’s followed (STO rating history is public). Footnotes anchor public fiscal/rating facts; desk sizes in the guide are rewrite scale.
          <div class="why">Why it matters: explains why “not bankrupt in five years” can still trigger a liquidity siege.</div>
          <div class="src">Source: LA Times July 2009 IOU coverage; California STO GO rating history; contemporary S&amp;P/Fitch/Moody’s news</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">Huaihai metaphor: don't forget pontoons</h2>
      <p>In the anxiety he recalled history: Huaihai, 1948—Huang Baitao’s army had time to fall back on Xuzhou, lingered east of the Grand Canal for a rendezvous, and fatally <strong>forgot to throw pontoons</strong>—a hundred thousand men jammed on one railway bridge, then were encircled at Nianzhuang. <a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>The map clicked: $50mm California ≈ Huang’s corps; falling prices ≈ the advancing East China Field Army; thin liquidity ≈ the Canal; Goldman’s $2.5mm clips ≈ the only railway bridge. Wait for a boss-forced cut, and chain reactions could wreck the whole book plan.</p>
      <p>Two rules for a general retreat: <strong>move now</strong> (do not dawdle in “Xin’an”); <strong>leave on many paths</strong> (build pontoons at once).</p>

      <div class="scene">
        A single plank is not an exit plan; pontoons are.
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ Huaihai Campaign · Huang Baitao and the canal railway bridge</strong>
          In November 1948 the East China Field Army encircled the Nationalist 7th Army (Huang Baitao) east of Xuzhou. Public military histories often stress delay near Xin’an to link with other units, and insufficient canal crossings/pontoons—withdrawal leaned on the railway bridge, then collapse at Nianzhuang. The author borrows the campaign as a liquidity metaphor—“railway bridge = sole big market-maker; pontoons = spare buyer channels.” Public war-history digest plus chapter allegory, not a monograph.
          <div class="why">Why it matters: tactical image for the title—lose with formation and exits.</div>
          <div class="src">Source: public Huaihai Campaign summaries; general Chinese military histories</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">Three-day breakout: multi-path exit, $800k tuition</h2>
      <p><strong>Pontoon one:</strong> tell regional dealers to slash California offers on retail e-platforms and hunt mid-size accounts—cast a wide net. <strong>Pontoon two:</strong> scan quote sheets—Citi still showed a five-year bid. Post-bailout Citi was sluggish, “half a beat slow”; while others had already tightened, that stale bid became a lifeline. Yuyang offered an odd notional as if “that’s all I have”—Citi lifted the lot, then backed. <a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>
      <p><strong>Pontoon three:</strong> Barclays showed an indicative market; when he hit it, sales said “only indicative.” He exploded: post a market, refuse to buy, and fish my motive—pressuring with “how do we trade after this,” he finally unloaded nearly ten at a worse print. Only then did he use Goldman’s “railway bridge,” chaining hits until the quote staggered back.</p>
      <p>Day one: about 60% out; he knew the tape was spooked—day two could avalanche. Others still haggled; he hit everything: Citi, Goldman, regional bids. On the last clip, Goldman’s market was already wide. Three days cost about <strong>$800,000</strong>—but he was free. Days later the market gaped further; residual risk could have approached a ~$3mm hole. The fixed-income boss asked how much California remained—“Zero.” “Good.”</p>

      <div class="scene">
        Eight hundred thousand is tuition; three million is the invoice for forgetting pontoons.
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ Multi-venue exit and indicative vs firm markets</strong>
          Institutional credit often distinguishes firm (tradable) from indicative (advertised) markets; in a squeeze, posted levels can turn into scenery. Crisis playbooks stress pre-wired counterparties, retail vs institutional splits, and paying slippage for certainty—“build pontoons.” Public trial-read beats cast Citi’s lag, Barclays indicatives, and Goldman size caps as three exits; sizes are story scale, not auditable tickets.
          <div class="why">Why it matters: turns “skilled defeat” into exit engineering, not slogans.</div>
          <div class="src">Source: fixed-income trading primers; crisis liquidity-management surveys; public trial-read beats (rewritten)</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">Skilled defeat, no chaos: trend vs liquidity</h2>
      <p>The breakout is archetypal: liquidity is life-or-death for bond investors—subprime already showed levered holders “dying inside the ring.” The other face of the coin: thin markets often trend harder; ultra-liquid equity indexes are harder to “ride”—volume, derivatives, and arb shred supply-demand, and EMH-style narratives say beating the tape is rare. <a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>
      <p>Bonds and real estate sit closer to real-use demand: issuers need funding, buyers need allocation, households need shelter—price is not the only objective; sparse liquidity also slows arb from erasing imbalances, so trends can run. The author’s shorthand: <strong>Follow trend, manage liquidity</strong>.</p>
      <p>More fortunes rise from property than from pure stock-picking; many fixed-income names rhyme. Both sleeves use leverage—cyclical liquidity crises are the survival course. The best investors are often the best <strong>losers</strong>: retreat hard and fast, and never forget pontoons (widen liquidity channels).</p>
      <p>The classical line sits in go/military lineages: <strong>those skilled at defeat do not fall into chaos</strong>—a good loser keeps formation. <a class="fn-link" href="#fn9"><sup class="fn">⁹</sup></a> Next, §22 “New Market, New Mind”: after the flat book, how to rewire for the post-tsunami order.</p>

      <div class="scene">
        Skilled defeat, no chaos—not zero losses, but losses without broken ranks or blocked exits.
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn8">
          <strong>⁸ Liquidity–trend tension and efficient markets</strong>
          Microstructure and asset-pricing work often note: high-turnover, low-friction markets price information faster and show weaker tradable trends; high-friction, segmented credit/muni/housing markets can sustain supply shocks longer. EMH-style “hard to beat the index” stories fit equities without denying risk premia in imperfect markets. “Follow trend, manage liquidity” is desk discipline, not a theorem claim.
          <div class="why">Why it matters: lifts a personal breakout into a portable rule and bridges to §22.</div>
          <div class="src">Source: EMH surveys; credit/real-estate liquidity research; public trial-read closing beats (rewritten)</div>
        </div>
        <div class="fn-item" id="fn9">
          <strong>⁹ Provenance of 「善败者不乱」</strong>
          The wording appears in the Classic of Go (Qijing), “Combined Battle”: “Who wins well does not quarrel; who arrays well need not fight; who fights well is not defeated; who is defeated well does not fall into chaos.” Journey to the West ch.10 echoes it in a chess passage. Military lineages include Hanshu “who is defeated well does not perish” and Zhuge Liang’s Jiang Yuan variants—the shared core: lose without losing the army. The chapter borrows classical diction for drawdown discipline.
          <div class="why">Why it matters: titles the chapter and flags a classical loan into finance narrative—not a verbatim Sunzi quote.</div>
          <div class="src">Source: Qijing public text; Hanshu treatise on punishments; idiom/military-phrase dictionaries</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>Relationships / timeline / knowledge graph</h2>

        <div class="mermaid-wrap">
          <div class="caption">People and firms: from fair-wind inventory to pontoon exits</div>
          <div class="mermaid">
flowchart LR
  YY[Yuyang · Lucy desk] --> INV[CA inventory ~$50mm]
  BR[Barclays sales/trader] --> SELL[Dump $10mm @245]
  SELL --> YY
  YY --> GS[Goldman trader]
  GS --> LIM[~2.5mm clips · quote backs]
  NEWS[CA fiscal headlines] --> WL[Rating watch list]
  WL --> DRY[Liquidity dries]
  YY --> P1[Pontoon1 regionals/retail]
  YY --> P2[Pontoon2 Citi lag bid]
  YY --> P3[Pontoon3 Barclays indicative]
  LIM --> RAIL[Railway bridge Goldman]
  P1 --> EXIT[3-day flat book]
  P2 --> EXIT
  P3 --> EXIT
  RAIL --> EXIT
  EXIT --> NEXT[§22 New market new mind]
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Timeline: Skilled Defeat, No Chaos (spring 2009 → June exit)</div>
          <div class="mermaid">
timeline
    title Skilled Defeat No Chaos
    spring 2009 : Recovery · BAB afterglow · CA inventory
    early June : Retail cools · Barclays fills 245
    next day : Fiscal headlines · rating watch · dry tape
    day 1 exit : Pontoons 1-3 · 60 percent out
    day 2-3 : Hit all bids · flat book · ~800k loss
    days later : Price gaps wider · boss asks zero
    bridge : Toward §22 new market new mind
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Knowledge graph: how skilled defeat keeps formation</div>
          <div class="mermaid">
flowchart TB
  S20[§20 Bible Stories] --> WIN[Momentum P and L · confidence up]
  WIN --> SMUG[Smugness risk]
  SMUG --> SHOCK[Dealer dump · size limits]
  SHOCK --> NEWS[Fiscal/rating shock]
  NEWS --> LIQ[Liquidity encirclement]
  HUAI[Huaihai metaphor] --> RULES[Move now · build pontoons]
  LIQ --> RULES
  RULES --> EXIT[Decisive retreat · pay slippage]
  EXIT --> PRINCIPLE[Follow trend manage liquidity]
  PRINCIPLE --> SAYING[Skilled defeat no chaos]
  SAYING --> S22[§22 New market new mind]
          </div>
        </div>
      </section>
'''

def main():
    zh = page(
        "zh",
        "《乱世华尔街》第21集：善败者不乱",
        "故事导读 · 据公开试读改写 · 场外研究补充",
        "善败者不乱",
        "《乱世华尔街》第二十一章「善败者不乱」· 渔阳 · 故事改写 + 脚注研究 · 第四部分「峰回路转」",
        "下面按作者经历与公开时间线讲述本章故事，用自己的话改写，方便跟读；不是全书/全章原文照搬。脚注、配图与知识图谱为场外公开资料补充。完整内容请读正版。",
        ZH_TOC,
        "CHAPTER TWENTY-ONE · 善败者不乱 · 第四部分 峰回路转",
        ZH_BODY,
        "《乱世华尔街》· 渔阳 · 第二十一章故事导读（原创改写）",
    )
    en = page(
        "en",
        "Chaos on Wall Street §21: Skilled Defeat, No Chaos",
        "Story guide · rewritten from public trial reads · off-book research",
        "Skilled Defeat, No Chaos",
        "Chaos on Wall Street, Chapter 21 “Skilled Defeat, No Chaos” · Yuyang · story rewrite + footnote research · Part 4 “The Road Turns”",
        "A story-first retelling from the author’s arc and public timelines, in our own words for guided reading—not a verbatim copy of the copyrighted chapter. Footnotes, figures, and graphs are off-book public research. For the full text, support the official edition.",
        EN_TOC,
        "CHAPTER TWENTY-ONE · Skilled Defeat, No Chaos · Part 4 The Road Turns",
        EN_BODY,
        "Chaos on Wall Street · Yuyang · Ch.21 story guide (original rewrite)",
    )
    (DIR / "skilled-defeat-zh.html").write_text(zh, encoding="utf-8")
    (DIR / "skilled-defeat-en.html").write_text(en, encoding="utf-8")
    print("Wrote", DIR / "skilled-defeat-zh.html", len(zh))
    print("Wrote", DIR / "skilled-defeat-en.html", len(en))

if __name__ == "__main__":
    main()
