#!/usr/bin/env python3
"""Build full self-contained ZH/EN HTML for ch19 曙光初现 / Dawn Appears."""
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
        '<a class="active" href="dawn-appears-zh.html">中文</a>\n'
        '        <a href="dawn-appears-en.html">English</a>\n'
        '        ' + home
        if lang == "zh" else
        '<a href="dawn-appears-zh.html">中文</a>\n'
        '        <a class="active" href="dawn-appears-en.html">English</a>\n'
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
    ("s1", "除旧迎新：2009 的死寂交易台"),
    ("s2", "哈得孙奇迹：一架飞机带来的喜气"),
    ("s3", "法儒道：凯恩斯主义回潮"),
    ("s4", "刺激计划：四国政府替百姓花钱"),
    ("s5", "收藏重启：优质市政债解冻"),
    ("s6", "鱼肚白：债市涨潮、股市仍在退"),
    ("s7", "最后一张牌：量化宽松与直升机大本"),
    ("s8", "曙光初现：风险资产抬头"),
    ("diagrams", "人物关系 / 时间线 / 知识图谱"),
]

EN_TOC = [
    ("s1", "Out with the old: a dead trading floor in 2009"),
    ("s2", "Miracle on the Hudson: a plane brings cheer"),
    ("s3", "Legalists, Confucians, Daoists: Keynes returns"),
    ("s4", "Stimulus: governments spend when households won't"),
    ("s5", "Collectors return: quality munis thaw"),
    ("s6", "First light: bonds flood in, equities still ebb"),
    ("s7", "Last card: QE and Helicopter Ben"),
    ("s8", "Dawn appears: risk assets lift"),
    ("diagrams", "Relationships / timeline / knowledge graph"),
]

ZH_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Times_Square_New_Year%27s_ball_2008.jpg" alt="时代广场新年彩球" loading="lazy" />
        <figcaption>纽约时代广场——2009 年元旦，人们仍挤着等彩球落下；华尔街那边，裁员与寂静才是主旋律。来源：Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">除旧迎新：2009 的死寂交易台</h2>
      <p>承接 §18：田纳西住房债甩掉了，「明天又是新的一天」说出口了——可<strong>2009 年新年</strong>真正到来时，纽约时代广场依旧人潮汹涌，交易楼层却死气沉沉。苦难的 2008 终于过去，人们问同一个问题：新的一年，会不会给深陷金融危机的世界一点点好运？</p>
      <p>华尔街一片萧条，各银行裁员不断。鲁西银行交易台上，渔阳注意到四周<strong>噪音明显变小</strong>——不是纪律变好了，是士气低落、人手变少。CNBC 像被熊派接管：专家们反复论证危机「还有一条腿」（has another leg）。<a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>再来一腿？交易员们自嘲：大家都要被扫进哈得孙河里去了。</p>

      <div class="side-panel">
        <h3 class="panel-title">本章时间锚点 · 2009-01 → 2009-03</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">01-01</div><div class="ev">新年·裁员·交易台死寂</div></div>
          <div class="event-card"><div class="yr">01-15</div><div class="ev">哈得孙奇迹·士气一振</div></div>
          <div class="event-card"><div class="yr">02</div><div class="ev">ARRA 刺激·市政债解冻</div></div>
          <div class="event-card"><div class="yr">03-09→18</div><div class="ev">股指见底·QE 宣布·曙光</div></div>
        </div>
      </div>

      <div class="scene">
        除旧迎新的钟声很响；交易台的钟，却几乎停了。
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn1">
          <strong>¹ 2008–09 冬春华尔街裁员与「另一条腿」叙事</strong>
          雷曼破产后数月，大型投行与商业银行持续公布裁员与重组计划；就业与产出数据在 2009 年初仍急剧恶化。公开媒体与策略师常用「another leg down」形容危机尚未结束的预期——股市要到 2009 年 3 月初才真正见危机低点。交易台「噪音变小」是人手与风险偏好双降的微观侧面。
          <div class="why">为何重要：把 §18「最黑暗」接到 §19 开篇——黑暗并未一夜散去，曙光要靠后面几节一点点攒。</div>
          <div class="src">来源：BLS 就业数据；当代金融媒体熊市叙事；FCIC 宏观年表</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">哈得孙奇迹：一架飞机带来的喜气</h2>
      <p>1 月中旬的一个下午，死水般的交易楼层忽然有人大叫：「快看电视！飞机！」对经历过 9·11 的纽约人，「飞机」二字仍能触动神经。屏幕上，一架大客机漂在<strong>哈得孙河</strong>里，机翼上站着人——几分钟后机身下沉，有人以为美国又添了新乱子。<a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>真相很快出来：美航 1549 航班从拉瓜迪亚起飞后遭遇鸟击，双发失效；资深机长果断避开桥梁，在河面迫降；轮渡与救援船在飞机沉没前把乘客与机组全部救起。播音员甚至还能幽默一句：行李损失惨重，人命却全保住了。</p>
      <p>交易楼层爆出欢呼，阴霾一扫。当晚各台把机组与乘客请进演播室；有主持人把这场「哈得孙奇迹」（Miracle on the Hudson）上纲上线：过去一年凡能出错的都出错了，今天每个人都做对了——只要齐心协力，衰退中的美国也能创造奇迹。渔阳感叹：祥瑞已出，或许国家将有转机？</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/US_Airways_Flight_1549.jpg" alt="美航 1549 哈得孙河迫降" loading="lazy" />
        <figcaption>2009-01-15：美航 1549 迫降哈得孙河——「哈得孙奇迹」成了那年冬天纽约难得的集体喜气。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        金融海啸教会人「凡事出错」；一架飞机教会人：有时，人人做对也能成真。
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn2">
          <strong>² 美航 1549「哈得孙奇迹」（2009-01-15）</strong>
          美航 Flight 1549（拉瓜迪亚飞往夏洛特）起飞后因鸟击双发失效，机长 Chesley 「Sully」Sullenberger 与副驾驶将空客 A320 迫降于哈得孙河；机上约 155 人全部获救，纽约州长称之为 Miracle on the Hudson。NTSB 后来称其为航空史上最成功的水面迫降之一。事件与金融危机无直接因果，却成为当年美国叙事中的「希望符号」。
          <div class="why">为何重要：本章用公共事件做情绪转折——故事从「再来一腿」转到「或许有转机」。</div>
          <div class="src">来源：NTSB 报告摘要；Wikipedia / 当代 NYT·NPR 报道</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">法儒道：凯恩斯主义回潮</h2>
      <p>2009 年初，全球性衰退阴云密布：金融体系暂稳，经济危机却已坐实。各国几乎不约而同翻出<strong>凯恩斯主义</strong>药方——老百姓不肯花钱，政府替你们花。<a class="fn-link" href="#fn3"><sup class="fn">³</sup></a></p>
      <p>作者用中国思想史做类比：凯恩斯主义强调政府反周期介入，近似「法家」；供给学派重减税、少干预、鼓励创造财富，近似「儒家」修身齐家再治国；货币主义主张管好货币供应、少折腾，近似「道家」无为。美国自里根以来多奉供给学派与货币主义（新自由主义），金融监管一路放松；海啸之后，视政府干预为洪水猛兽的极端看法开始松动——政策风向集体向凯恩斯主义靠拢。</p>

      <div class="scene">
        危机改写的不只是资产负债表，还有哪一派经济学突然变得「正确」。
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn3">
          <strong>³ 凯恩斯主义、供给学派与货币主义（危机语境）</strong>
          凯恩斯主义强调总需求不足时用财政扩张托底就业与产出；供给学派侧重减税与激励供给；货币主义强调货币规则与通胀锚、警惕财政货币化。2008–09 年多国同时扩大财政赤字并逼近零利率下界，政策实践明显向积极财政与非常规货币（后文 QE）倾斜——公开宏观史常将此称为对「大缓和」时期新自由主义信条的反思时刻。
          <div class="why">为何重要：给后文中国四万亿、美国 ARRA、美联储 QE 一张「思想地图」，避免只见政策不见争论。</div>
          <div class="src">来源：宏观经济学通识；IMF / 各国财政应对综述；Bernanke 等危机回顾</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">刺激计划：四国政府替百姓花钱</h2>
      <p>中国先行动：2008 年 11 月推出约<strong>四万亿元</strong>人民币刺激，以基建与公共开支对冲出口塌陷。美国大选后民主党掌控白宫与国会，奥巴马 2009 年 1 月就职后约一个月内推动国会通过约<strong>7870 亿美元</strong>的《美国复苏与再投资法案》（ARRA）。<a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>长远效果——是真拉动增长，还是只堆赤字与通胀——当时未定；短期效果却清楚：一剂剂强心针下，世界经济从雷曼后的休克里慢慢苏醒。金融市场的风向，也悄然变了。</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Obama_signs_ARRA.jpg" alt="奥巴马签署经济刺激法案" loading="lazy" />
        <figcaption>2009-02-17：奥巴马签署《美国复苏与再投资法案》——财政政策把「政府替你花钱」写成法律。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        央行把利率砸到零还不够时，财政部就得亲自上场。
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ 中国四万亿与美国 ARRA（2008–09）</strong>
          中国于 2008-11 宣布约 4 万亿元刺激计划（含中央与地方配套口径的公开表述）。美国《American Recovery and Reinvestment Act of 2009》于 2009-02-17 由奥巴马签署，规模约 7870–7890 亿美元量级（开支+减税组合）。同期多国亦推出财政扩张。这些措施与 TARP/央行流动性工具并行，目标从「救银行」扩展到「托实体」。
          <div class="why">为何重要：解释为何债市/情绪能在 2009 年初先于全面复苏出现转机——政策火力已从金融稳定扩到总需求。</div>
          <div class="src">来源：中国发改委/当代新华社报道；U.S. Congress / White House ARRA 文本与签署日期；IMF 财政监测</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">收藏重启：优质市政债解冻</h2>
      <p>乱世买黄金，盛世兴收藏——2009 年初，一些投资者开始对「收藏」露出谨慎兴趣。销售电话重新忙碌：谁有债券要卖？经验告诉渔阳：市场或许要转好了。</p>
      <p>收藏往往从「明官窑」式优质资产开始。优质市政债信用风险低、流动性尚可、利息免税，海啸后收益率一度<strong>高于国债</strong>——对「安全第一」又想多一点回报的买家，这是自然选择；连非传统买家也来捡便宜。二级成交回升，一级市场出现解冻：信誉最好的发行人重新卖得出去。公开试读里的标志性例子：AAA 的<strong>普林斯顿大学</strong>发售约 7 亿美元债券，相对国债利差一度约 280 基点（接近危机前垃圾债利差量级）；渔阳试探买入约 500 万美元，开盘后利差收至约 250、再向 220 基点靠拢，轻松兑现近十万利润。<a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>一只便宜券被追捧不稀奇；高开还能高走，说明买盘有厚度。渔阳隐约觉得：黑暗天际，露出一抹<strong>鱼肚白</strong>。</p>

      <div class="scene">
        当电话从「谁要抛」变成「谁有货」，潮水的方向就变了。
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn5">
          <strong>⁵ 2009 年初优质市政债利差收窄与高校发债</strong>
          危机高峰期高等级市政债相对国债利差异常走阔（§18「金融奇境」）；2009 年初随着风险偏好局部修复与避险资金再配置，部分 AAA/AA 市政与大学发行人重新打开一级市场，二级利差开始收窄。高校与公立机构发债在危机后的「质量下沉—再分层」过程中常作为早期解冻样本出现在当代市场评论中。书中普林斯顿发债与作者小仓位试探，是交易员视角的微观证据（导读改写，非原文照搬）。
          <div class="why">为何重要：把「曙光」落到渔阳本行——市政债微观流动性，而不是抽象指数。</div>
          <div class="src">来源：市政市场危机后修复研究；SIFMA / 当代债券市场评论；本书公开试读情节节拍（改写）</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">鱼肚白：债市涨潮、股市仍在退</h2>
      <p>债市趋于稳定，根子是<strong>流动性局部好转</strong>：该破产的破产了，该减仓的减得差不多了，去杠杆卖压减弱；美联储已把短期利率压到近零，基础货币上升；从高风险资产逃出的钱也要找「新家」。优质债买家增多、卖压减轻，债券市场局部涨潮。<a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>可金融市场反转从来不同步。2007 年房贷退潮时，能源与新兴市场还在涨；2009 年初，债市已局部涨潮，<strong>股市仍在退潮</strong>——3 月初美股创十余年新低，标普 500 跌到约 <strong>670</strong> 点附近，较 2007 年 10 月高点腰斩有余。股市悲观到极点时，债市回暖也可能只是「小阳春」流星。政府很想再加一把火：财政牌（ARRA）已打出，短端利率已近零——美联储还剩最后一张王牌：印钞票。</p>

      <div class="scene">
        鱼肚白出现在债市地平线时，股市屏幕却仍是深夜。
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ 2009-03-09 美股危机低点与信用利差缓和</strong>
          标普 500 于 2009-03-09 收于约 676.53，被广泛视为本轮危机股市底部；此前数月 LIBOR–OIS 等银行间压力指标已自 2008-10 峰值显著回落，显示信贷恐慌缓和但风险资产仍在「寻底」。公开危机史强调：跨资产的底部与修复并不同步——信用与高等级债往往领先权益。
          <div class="why">为何重要：解释作者「鱼肚白」为何先出现在债市，以及为何政府仍要打出 QE 这张牌。</div>
          <div class="src">来源：S&amp;P / CRSP 指数序列；NY Fed LIBOR–OIS；FCIC / Fed 危机回顾</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">最后一张牌：量化宽松与直升机大本</h2>
      <p>短端利率到零之后仍大量购入国债，等于开动印钞机——学名<strong>量化宽松</strong>（quantitative easing）。副作用是通胀风险。二三月金融圈争论美联储会不会打出这张牌；结果又是英国人先动手：英格兰银行宣布大规模购债，打响主要央行 QE 的一枪。<a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>
      <p>数日后，美联储 FOMC（2009-03-18）宣布扩大资产购买：在已有机构债/MBS 计划上，增加大规模<strong>长期国债</strong>购买，并显著上调机构 MBS 购买上限——公开表述常概括为向金融体系注入万亿量级流动性。购国债与奥巴马财政刺激「唱双簧」，近乎为赤字融资托底；购房贷相关证券则直接对着房市输液。<a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>
      <p>伯南克外号「直升机大本」（Helicopter Ben）——源于他讨论极端情况下可用「直升机撒钱」对抗通缩。2009 年 3 月，这张王牌落地：政策信号极其明确——先把经济与市场稳住，赤字与通胀以后再说。</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Marriner_S._Eccles_Federal_Reserve_Board_Building.jpg" alt="美联储埃克尔斯大楼" loading="lazy" />
        <figcaption>美联储理事会大楼——2009-03-18，FOMC 把「最后一张牌」摊在桌上。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        零利率不是终点；印钞机才是危机剧本的终章标题。
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ 英格兰银行 2009 年 QE 启动</strong>
          2009-03-05，英格兰银行货币政策委员会宣布启动资产购买（QE），初期规模 750 亿英镑，随后在 2009 年内多次上调（年底前累计购买授权升至约 2000 亿英镑量级）。英央行的行动被当代市场视为主要央行「零利率下扩表」竞赛的重要信号，并与数日后美联储扩购形成共振。
          <div class="why">为何重要：呼应书中「又是英国人先开枪」的叙事，并把 QE 放进国际政策协调/竞赛框架。</div>
          <div class="src">来源：Bank of England MPC 公告与 QE 年表；BIS 综述</div>
        </div>
        <div class="fn-item" id="fn8">
          <strong>⁸ 美联储 2009-03-18 QE1 扩容（公开数字）</strong>
          2009-03-18 FOMC 声明：在未来约六个月购买最多约 <strong>3000 亿美元</strong>较长期国债；将机构 MBS 购买目标上调至约 <strong>1.25 万亿美元</strong>；将机构债购买上调至约 <strong>2000 亿美元</strong>（具体以声明原文为准）。加上此前已宣布的购债路径，市场读出的信号是「万亿级流动性 + 财政货币化托底」。脚注采用美联储公开数字；故事叙述保留「最后一张牌/直升机」修辞。
          <div class="why">为何重要：把「曙光」钉在可核验的政策日历上，并校正坊间对购债规模的口误式概括。</div>
          <div class="src">来源：Federal Reserve FOMC statement 2009-03-18；Fed 大额资产购买（LSAP）年表；FRASER</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">曙光初现：风险资产抬头</h2>
      <p>王牌落地后，流动性潮水预期大涨，股市与其他<strong>风险资产</strong>快速反弹。天际那一抹鱼肚白，终于变成章名所说的——<strong>曙光初现</strong>。<a class="fn-link" href="#fn9"><sup class="fn">⁹</sup></a></p>
      <p>渔阳在交易台上的体感是：人还没死透。信贷利差自峰值回落，优质债能卖能买，政策层「不惜代价」的信号已写在墙上。风险当然仍在——失业、止赎、银行有毒资产、监管清算都还在后头——但第四部分「峰回路转」的第一缕光，已经照进鲁西银行那层曾经死寂的楼面。</p>
      <p>下一章，是「圣经故事」：曙光之后，市场与人性会怎样重读危机中的寓言。</p>

      <div class="scene">
        曙光不是胜利宣言；它只是说：今晚，也许不用再准备后事。
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn9">
          <strong>⁹ 2009 年 3 月起风险资产反弹与 TALF 等配套</strong>
          股指自 3 月 9 日低点反弹；同月 TALF（定期资产支持证券贷款便利）开始实际操作，旨在重启车贷、信用卡等 ABS 发行。TARP 资本注入的后续批次、压力测试预期与 QE 预期共同推升风险偏好。公开市场史将 2009 年春视为「政策底/情绪底」重叠期——并非实体已痊愈，而是金融资产率先定价复苏概率。
          <div class="why">为何重要：收束本章「不是死了」的交易台直觉，并桥接 §20。</div>
          <div class="src">来源：Fed TALF 操作年表；S&amp;P 反弹序列；财政部 TARP 105(a) 报告；当代市场评论</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>人物关系 / 时间线 / 知识图谱</h2>

        <div class="mermaid-wrap">
          <div class="caption">人物与机构关系图：从死寂交易台到曙光</div>
          <div class="mermaid">
flowchart LR
  YY[渔阳·鲁西交易台] --> DESK[死寂·裁员·熊派叙事]
  HUD[哈得孙奇迹] --> MOOD[士气与希望符号]
  CN[中国四万亿] --> STIM[全球财政刺激]
  OB[奥巴马·ARRA] --> STIM
  STIM --> DEM[总需求托底]
  MUNI[优质市政债] --> YY
  YY --> TRADE[普林斯顿券试探获利]
  BOE[英格兰银行QE] --> RACE[主要央行扩表]
  FED[美联储QE1扩容] --> RACE
  RACE --> RISK[风险资产反弹]
  DEM --> RISK
  TRADE --> DAWN[曙光初现]
  RISK --> DAWN
  DAWN --> NEXT[§20 圣经故事]
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">时间线：曙光初现（2009-01 → 2009-03）</div>
          <div class="mermaid">
timeline
    title 曙光初现
    2009-01初 : 新年·交易台死寂·裁员
    2009-01-15 : 哈得孙奇迹
    2009-02-17 : 奥巴马签署 ARRA
    2009-02至03 : 优质市政债解冻·鱼肚白
    2009-03-09 : 标普危机低点
    2009-03-05至18 : 英央行QE·美联储扩购
    2009-03下旬 : 风险资产反弹·曙光
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">知识图谱：鱼肚白如何变成曙光</div>
          <div class="mermaid">
flowchart TB
  DARK[§18 最黑暗] --> QUIET[去杠杆尾声·交易台死寂]
  QUIET --> SYMBOL[哈得孙奇迹·情绪转折]
  KEYN[凯恩斯主义回潮] --> FISCAL[四万亿·ARRA]
  FISCAL --> BOND[高等级债局部涨潮]
  QUIET --> BOND
  BOND --> FISH[鱼肚白]
  EQ[股市仍寻底] --> NEED[还需货币王牌]
  ZLB[零利率下界] --> QE[QE1·直升机大本]
  NEED --> QE
  QE --> LIQ[流动性预期大涨]
  FISH --> DAWN[曙光初现]
  LIQ --> DAWN
  DAWN --> PART4[第四部分 峰回路转]
          </div>
        </div>
      </section>
'''

EN_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Times_Square_New_Year%27s_ball_2008.jpg" alt="Times Square New Year ball" loading="lazy" />
        <figcaption>Times Square—on New Year’s Day 2009 crowds still waited for the ball to drop; across town on Wall Street, layoffs and silence set the tone. Source: Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">Out with the old: a dead trading floor in 2009</h2>
      <p>After §18—Tennessee housing bond sold, “tomorrow is another day” spoken aloud—<strong>New Year 2009</strong> arrived with Times Square still packed and trading floors still hollow. The hard year of 2008 was over. The question was the same everywhere: would the new year give a crisis-struck world even a little luck?</p>
      <p>Wall Street was bleak; banks kept cutting staff. On Lucy Bank’s desk, Yuyang noticed the <strong>noise had fallen</strong>—not better discipline, but lower morale and fewer people. CNBC sounded captured by the bears: experts kept proving the crisis had “another leg.”<a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>Another leg? Traders joked they were all about to be swept into the Hudson.</p>

      <div class="side-panel">
        <h3 class="panel-title">Chapter anchors · Jan 2009 → Mar 2009</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">Jan 1</div><div class="ev">New Year · layoffs · dead desks</div></div>
          <div class="event-card"><div class="yr">Jan 15</div><div class="ev">Hudson miracle · morale lift</div></div>
          <div class="event-card"><div class="yr">Feb</div><div class="ev">ARRA stimulus · munis thaw</div></div>
          <div class="event-card"><div class="yr">Mar 9–18</div><div class="ev">Equity low · QE · dawn</div></div>
        </div>
      </div>

      <div class="scene">
        The New Year bells rang loud; the trading-floor clock had nearly stopped.
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn1">
          <strong>¹ Winter–spring 2008–09 Wall Street layoffs and the “another leg” narrative</strong>
          For months after Lehman, major banks announced waves of cuts and restructurings; jobs and output kept deteriorating into early 2009. Media and strategists used “another leg down” for the view that the crisis was unfinished—U.S. equities would not print their crisis low until early March 2009. A quieter desk is the micro face of fewer bodies and less risk appetite.
          <div class="why">Why it matters: bridges §18’s darkest hour into §19’s opening—darkness does not lift overnight; dawn is assembled section by section.</div>
          <div class="src">Source: BLS employment; contemporary bear-market commentary; FCIC macro chronology</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">Miracle on the Hudson: a plane brings cheer</h2>
      <p>One mid-January afternoon, someone shouted across the still floor: “TV—plane!” For New Yorkers who lived through 9/11, the word still jolted. On screen a jet floated in the <strong>Hudson</strong>, people standing on the wings—then it sank, and for a moment America seemed to have found a new disaster.<a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>The truth landed fast: US Airways Flight 1549 hit birds after takeoff from LaGuardia, lost both engines; a veteran captain ditched clear of the bridges; ferries and rescue boats pulled every passenger and crew member off before the fuselage went under. Anchors could even joke: baggage ruined, lives saved.</p>
      <p>The floor erupted; the gloom broke. That night networks booked crew and passengers; one host moralized the “Miracle on the Hudson”: for a year everything that could go wrong did; today everyone did the right thing—together, a recession country could still make a miracle. Yuyang wondered: an omen already? Might the nation be turning?</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/US_Airways_Flight_1549.jpg" alt="US Airways Flight 1549 Hudson ditching" loading="lazy" />
        <figcaption>15 Jan 2009: Flight 1549 ditches in the Hudson—the “Miracle on the Hudson,” rare collective cheer in that winter. Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        The tsunami taught “everything fails”; one airplane taught that sometimes everyone gets it right.
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn2">
          <strong>² US Airways 1549, “Miracle on the Hudson” (15 Jan 2009)</strong>
          Flight 1549 (LaGuardia–Charlotte) suffered dual engine failure after a bird strike; Captain Chesley “Sully” Sullenberger and First Officer Skiles ditched an Airbus A320 in the Hudson; all ~155 aboard survived. New York’s governor dubbed it the Miracle on the Hudson; NTSB later called it among the most successful ditchings in aviation history. No direct causal link to the financial crisis—yet it became a national hope symbol that winter.
          <div class="why">Why it matters: the chapter’s emotional hinge—from “another leg” to “maybe a turn.”</div>
          <div class="src">Source: NTSB summary; Wikipedia / contemporary NYT·NPR</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">Legalists, Confucians, Daoists: Keynes returns</h2>
      <p>In early 2009 a global recession cloud hung over everything: finance was patched; the real economy was not. Governments reached, almost in unison, for the <strong>Keynesian</strong> prescription—if households will not spend, the state will spend for them.<a class="fn-link" href="#fn3"><sup class="fn">³</sup></a></p>
      <p>The author maps schools onto Chinese political thought: Keynesian counter-cyclical state action ≈ Legalism; supply-side tax cuts and incentives ≈ Confucian self-cultivation before governing; monetarist rules and non-interference ≈ Daoist wuwei. Since Reagan, America had leaned supply-side and monetarist (neo-liberal), loosening finance along the way; after the tsunami, treating state intervention as pure poison looked extreme—and policy swung back toward Keynes.</p>

      <div class="scene">
        Crises rewrite more than balance sheets—they rewrite which economics suddenly sounds “right.”
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn3">
          <strong>³ Keynesianism, supply-side, and monetarism in the crisis</strong>
          Keynesians stress fiscal expansion when aggregate demand collapses; supply-siders stress tax cuts and incentives; monetarists stress monetary rules and inflation anchors, wary of fiscal monetization. In 2008–09 many countries widened deficits and hit the zero lower bound, tilting toward active fiscal policy and unconventional money (QE below)—a moment public macro histories often cast as a reckoning with Great-Moderation neo-liberal habits.
          <div class="why">Why it matters: gives China’s package, ARRA, and Fed QE an ideas map, not only a policy list.</div>
          <div class="src">Source: macro textbooks; IMF fiscal-response surveys; Bernanke and other crisis retrospectives</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">Stimulus: governments spend when households won't</h2>
      <p>China moved first: in November 2008 a stimulus on the order of <strong>RMB 4 trillion</strong>, leaning on infrastructure and public outlays against collapsing exports. After Democrats took the White House and Congress, Obama—within roughly a month of inauguration—pushed through the ~<strong>$787 billion</strong> American Recovery and Reinvestment Act (ARRA).<a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>Long-run verdicts—true growth versus deficits and inflation—were open; the short-run effect was clearer: shot after shot of adrenaline, and the world economy began to climb out of post-Lehman shock. Quietly, market winds shifted too.</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Obama_signs_ARRA.jpg" alt="Obama signs the stimulus act" loading="lazy" />
        <figcaption>17 Feb 2009: Obama signs ARRA—fiscal policy writing “the government will spend” into law. Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        When the central bank has smashed rates to zero, the Treasury has to walk onto the field.
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ China’s RMB 4 trillion package and U.S. ARRA (2008–09)</strong>
          China announced a ~RMB 4 trillion stimulus in Nov 2008 (public figures often blend central and local components). The U.S. American Recovery and Reinvestment Act of 2009 was signed 17 Feb 2009 at roughly $787–789 billion (spending plus tax relief). Peer countries launched expansions too. Together with TARP and central-bank liquidity tools, the aim widened from “save banks” to “backstop demand.”
          <div class="why">Why it matters: explains why bond markets and sentiment could turn in early 2009 before a full recovery—policy firepower had moved from financial stability to aggregate demand.</div>
          <div class="src">Source: NDRC / contemporary Xinhua; U.S. Congress/White House ARRA text and signing date; IMF Fiscal Monitor</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">Collectors return: quality munis thaw</h2>
      <p>In chaos, buy gold; in calm, collect—early 2009, some investors showed cautious interest in “collecting” again. Sales lines got busy: who has bonds to sell? Experience told Yuyang the tape might be turning.</p>
      <p>Collecting starts with “imperial kiln” quality. Top munis—low credit risk, usable liquidity, tax-exempt—had been left yielding <strong>more than Treasuries</strong> after the tsunami. For buyers still in “safety first” mode but hungry for a bit more return, that was the natural hunt; even nontraditional buyers came to pick bargains. Secondary volume rose; the primary market thawed for the best names. In the public trial-read beat, AAA <strong>Princeton University</strong> sold about $700 million of bonds at roughly 280 bp over Treasuries (junk-like for the rating); Yuyang probed with ~$5 million, watched the spread tighten toward 250 then ~220 bp, and booked nearly $100k. <a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>One cheap bond being chased is normal; opening strong and keeping going means real bid depth. He sensed a strip of <strong>fish-belly white</strong> on the dark horizon.</p>

      <div class="scene">
        When the phone flips from “who must sell?” to “who has inventory?”, the tide has changed.
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn5">
          <strong>⁵ Early-2009 quality-muni spread compression and university issuance</strong>
          At the peak, high-grade munis cheapened sharply versus Treasuries (§18 Wonderland); in early 2009, as risk appetite patched and safe-haven cash reallocated, some AAA/AA munis and university issuers reopened primary markets and secondary spreads began to tighten. University and public-name deals often appear in contemporary commentary as early thaw samples. Princeton’s deal and the author’s small probe are desk-level micro-evidence (guide rewrite, not verbatim book text).
          <div class="why">Why it matters: lands “dawn” in Yuyang’s home market—muni micro-liquidity, not an abstract index.</div>
          <div class="src">Source: post-crisis muni recovery research; SIFMA / contemporary bond commentary; public trial-read beats (rewritten)</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">First light: bonds flood in, equities still ebb</h2>
      <p>Bond stability rested on <strong>locally better liquidity</strong>: the bankruptcies that had to happen had happened; forced selling had slowed; the Fed had pinned short rates near zero and grown base money; cash that fled risky assets needed a new home. More buyers of quality paper, less deleveraging supply—bond markets began a local flood tide.<a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>Reversals never sync. In 2007 mortgages ebbed while energy and EM still flooded; in early 2009 bonds were flooding locally while <strong>equities still ebbed</strong>—by early March the S&amp;P 500 printed a multi-year low near <strong>670</strong>, more than halved from the Oct 2007 peak. With stocks that bleak, the bond thaw might still be a false-spring meteor. Officials wanted another fire under the embers: the fiscal card (ARRA) was played, short rates near zero—the Fed still held a last trump: the printing press.</p>

      <div class="scene">
        Fish-belly white on the bond horizon while equity screens still read midnight.
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ 9 Mar 2009 equity crisis low and easing credit stress</strong>
          The S&amp;P 500 closed near 676.53 on 9 Mar 2009, widely treated as the cycle trough; for months before, LIBOR–OIS and related stress gauges had already fallen hard from Oct 2008 peaks—credit panic easing while risk assets still hunted a bottom. Crisis histories stress asynchronous bottoms: credit and high-grade bonds often lead equities.
          <div class="why">Why it matters: explains why the author’s “first light” shows in bonds first—and why QE still had to land.</div>
          <div class="src">Source: S&amp;P/CRSP series; NY Fed LIBOR–OIS; FCIC/Fed retrospectives</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">Last card: QE and Helicopter Ben</h2>
      <p>Buying swathes of Treasuries after short rates hit zero is running the printing press—formal name <strong>quantitative easing</strong>, with inflation as the feared side effect. In February–March the Street argued whether the Fed would play it; again the British moved first: the Bank of England announced large-scale gilt purchases, firing a major-central-bank QE shot.<a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>
      <p>Days later the Fed’s FOMC (18 Mar 2009) expanded purchases: large-scale <strong>longer-term Treasuries</strong> on top of agency debt/MBS programs already underway, and a sharp lift in the agency MBS ceiling—read in markets as trillion-scale liquidity. Buying Treasuries duetted with Obama’s fiscal stimulus, backstopping deficit finance; buying mortgage-related paper aimed liquidity straight at housing.<a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>
      <p>Bernanke’s nickname “Helicopter Ben” came from discussing helicopter drops against deflation. In March 2009 the trump landed: stabilize the economy and markets first; deficits and inflation later.</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Marriner_S._Eccles_Federal_Reserve_Board_Building.jpg" alt="Eccles Federal Reserve Board Building" loading="lazy" />
        <figcaption>The Fed’s Eccles Building—on 18 Mar 2009 the FOMC laid the last card on the table. Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        Zero rates are not the final act; the printing press is the crisis script’s end-title card.
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ Bank of England QE launch in 2009</strong>
          On 5 Mar 2009 the MPC announced asset purchases (QE), initially £75 billion, later raised through 2009 (authorization reaching on the order of £200 billion by year-end). Markets read BoE action as a signal in the major-central-bank race to expand sheets at the ZLB, resonating with the Fed’s expansion days later.
          <div class="why">Why it matters: matches the book’s “British fired first” beat and places QE in an international frame.</div>
          <div class="src">Source: Bank of England MPC releases and QE chronology; BIS surveys</div>
        </div>
        <div class="fn-item" id="fn8">
          <strong>⁸ Fed 18 Mar 2009 QE1 expansion (public figures)</strong>
          The 18 Mar 2009 FOMC statement: purchase up to about <strong>$300 billion</strong> of longer-term Treasuries over roughly six months; raise agency MBS purchases to about <strong>$1.25 trillion</strong>; raise agency debt purchases to about <strong>$200 billion</strong> (see the statement for exact wording). Together with prior purchase paths, markets heard “trillion-scale liquidity + fiscal monetization backstop.” Footnotes use Fed figures; narrative keeps the “last card / helicopter” rhetoric.
          <div class="why">Why it matters: pins “dawn” to a verifiable policy calendar and corrects casual size mix-ups.</div>
          <div class="src">Source: Federal Reserve FOMC statement 18 Mar 2009; Fed LSAP chronology; FRASER</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">Dawn appears: risk assets lift</h2>
      <p>Once the trump landed, expected liquidity surged; equities and other <strong>risk assets</strong> bounced hard. The strip of fish-belly white became what the chapter title names—<strong>dawn appears</strong>.<a class="fn-link" href="#fn9"><sup class="fn">⁹</sup></a></p>
      <p>On the desk, Yuyang’s read was simple: not dead yet. Credit spreads off their peaks, quality bonds tradable again, “whatever it takes” written on the wall. Risks remained—jobs, foreclosures, toxic bank assets, regulatory reckoning—but the first light of Part 4, “The Road Turns,” was already on Lucy Bank’s once-silent floor.</p>
      <p>Next comes “A Bible Story”: after dawn, how markets and people reread the crisis’s parables.</p>

      <div class="scene">
        Dawn is not a victory speech; it only says tonight you may not need to plan the funeral.
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn9">
          <strong>⁹ Risk-asset rebound from March 2009 and TALF companions</strong>
          Equities bounced from the 9 Mar low; the same month TALF began live operations to restart auto and credit-card ABS. Further TARP capital batches, stress-test expectations, and QE expectations lifted risk appetite together. Market histories treat spring 2009 as overlapping “policy bottom / sentiment bottom”—not a healed real economy, but financial assets repricing recovery odds first.
          <div class="why">Why it matters: closes the chapter’s “not dead yet” desk intuition and bridges to §20.</div>
          <div class="src">Source: Fed TALF chronologies; S&amp;P rebound series; Treasury TARP 105(a) reports; contemporary market commentary</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>Relationships / timeline / knowledge graph</h2>

        <div class="mermaid-wrap">
          <div class="caption">People and institutions: from a dead desk to dawn</div>
          <div class="mermaid">
flowchart LR
  YY[Yuyang · Lucy desk] --> DESK[Silence · layoffs · bear narrative]
  HUD[Hudson miracle] --> MOOD[Morale and hope symbol]
  CN[China RMB 4tn] --> STIM[Global fiscal stimulus]
  OB[Obama · ARRA] --> STIM
  STIM --> DEM[Demand backstop]
  MUNI[Quality munis] --> YY
  YY --> TRADE[Princeton probe trade]
  BOE[BoE QE] --> RACE[Major-CB sheet race]
  FED[Fed QE1 expansion] --> RACE
  RACE --> RISK[Risk-asset rebound]
  DEM --> RISK
  TRADE --> DAWN[Dawn appears]
  RISK --> DAWN
  DAWN --> NEXT[§20 A Bible Story]
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Timeline: Dawn Appears (Jan 2009 → Mar 2009)</div>
          <div class="mermaid">
timeline
    title Dawn Appears
    early Jan 2009 : New Year · dead desks · layoffs
    2009-01-15 : Miracle on the Hudson
    2009-02-17 : Obama signs ARRA
    Feb–Mar 2009 : Quality munis thaw · fish-belly white
    2009-03-09 : S&P crisis low
    2009-03-05 to 18 : BoE QE · Fed expansion
    late Mar 2009 : Risk assets bounce · dawn
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Knowledge graph: how fish-belly white becomes dawn</div>
          <div class="mermaid">
flowchart TB
  DARK[§18 Darkest Hour] --> QUIET[Deleveraging tail · quiet desk]
  QUIET --> SYMBOL[Hudson miracle · mood turn]
  KEYN[Keynesian return] --> FISCAL[RMB 4tn · ARRA]
  FISCAL --> BOND[High-grade local flood]
  QUIET --> BOND
  BOND --> FISH[Fish-belly white]
  EQ[Equities still bottoming] --> NEED[Still need monetary trump]
  ZLB[Zero lower bound] --> QE[QE1 · Helicopter Ben]
  NEED --> QE
  QE --> LIQ[Liquidity expectations surge]
  FISH --> DAWN[Dawn appears]
  LIQ --> DAWN
  DAWN --> PART4[Part 4 The Road Turns]
          </div>
        </div>
      </section>
'''

def main():
    zh = page(
        "zh",
        "《乱世华尔街》第19集：曙光初现",
        "故事导读 · 据公开试读改写 · 场外研究补充",
        "曙光初现",
        "《乱世华尔街》第十九章「曙光初现」· 渔阳 · 故事改写 + 脚注研究 · 第四部分「峰回路转」开篇",
        "下面按作者经历与公开时间线讲述本章故事，用自己的话改写，方便跟读；不是全书/全章原文照搬。脚注、配图与知识图谱为场外公开资料补充。完整内容请读正版。",
        ZH_TOC,
        "CHAPTER NINETEEN · 曙光初现 · 第四部分 峰回路转",
        ZH_BODY,
        "《乱世华尔街》· 渔阳 · 第十九章故事导读（原创改写）",
    )
    en = page(
        "en",
        "Chaos on Wall Street §19: Dawn Appears",
        "Story guide · rewritten from public trial reads · off-book research",
        "Dawn Appears",
        "Chaos on Wall Street, Chapter 19 “Dawn Appears” · Yuyang · story rewrite + footnote research · opening of Part 4 “The Road Turns”",
        "A story-first retelling from the author’s arc and public timelines, in our own words for guided reading—not a verbatim copy of the copyrighted chapter. Footnotes, figures, and graphs are off-book public research. For the full text, support the official edition.",
        EN_TOC,
        "CHAPTER NINETEEN · Dawn Appears · Part 4 The Road Turns",
        EN_BODY,
        "Chaos on Wall Street · Yuyang · Ch.19 story guide (original rewrite)",
    )
    (DIR / "dawn-appears-zh.html").write_text(zh, encoding="utf-8")
    (DIR / "dawn-appears-en.html").write_text(en, encoding="utf-8")
    print("Wrote", DIR / "dawn-appears-zh.html", len(zh))
    print("Wrote", DIR / "dawn-appears-en.html", len(en))

if __name__ == "__main__":
    main()
