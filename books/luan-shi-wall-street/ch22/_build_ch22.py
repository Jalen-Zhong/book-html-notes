#!/usr/bin/env python3
"""Build full self-contained ZH/EN HTML for ch22 新市场，新思维 / New Markets, New Thinking."""
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
        '<a class="active" href="new-markets-zh.html">中文</a>\n'
        '        <a href="new-markets-en.html">English</a>\n'
        '        ' + home
        if lang == "zh" else
        '<a href="new-markets-zh.html">中文</a>\n'
        '        <a class="active" href="new-markets-en.html">English</a>\n'
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
    ("s1", "冰火两重天：2009 上半年的咸鱼翻身"),
    ("s2", "一对好牌：鲁西的资本优势"),
    ("s3", "福尔摩斯线索：净资本、资产与杠杆"),
    ("s4", "季度末出租资产负债表：宾州债十万"),
    ("s5", "水库与洪水：前危机杠杆 vs 后危机渠道"),
    ("s6", "大券商泄洪不畅：科罗拉多医院债"),
    ("s7", "蔬菜批发市场：地方狼群与分销网"),
    ("s8", "麦当劳不是麦道夫：新思维与关系学"),
    ("diagrams", "人物关系 / 时间线 / 知识图谱"),
]

EN_TOC = [
    ("s1", "Ice and fire: H1 2009 rebound"),
    ("s2", "A pair of aces: Lucy's capital edge"),
    ("s3", "Holmes clues: equity, assets, leverage"),
    ("s4", "Renting the balance sheet: Pennsylvania clip"),
    ("s5", "Reservoirs and floods: leverage vs channels"),
    ("s6", "Big dealers can't drain: Colorado hospital"),
    ("s7", "Vegetable wholesale: regional wolf pack"),
    ("s8", "McDonald's, not Madoff: new mind & guanxi"),
    ("diagrams", "Relationships / timeline / knowledge graph"),
]

ZH_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/New_York_Stock_Exchange_September_2016_05.jpg" alt="纽约证券交易所" loading="lazy" />
        <figcaption>纽约证券交易所——2009 上半年，华尔街从「前途堪忧」翻成「单季创纪录」。来源：Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">冰火两重天：2009 上半年的咸鱼翻身</h2>
      <p>承接 §21：善败者不乱，加州债突围清仓。账本扁了，人却醒了——下一问不是「怎么赌下一把」，而是「今后该怎么赚钱」。2009 年上半年，华尔街经历冰火两重天：年初前景最暗淡，投行业务被看低；几个月后却咸鱼翻身，令旁观大跌眼镜。<a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>事后看，逻辑其实朴素：投行做的是<strong>资本生意</strong>——为有融资需要与投资需要的客户搭桥。海啸后，这两种需求并未消失：各国央行宽松乃至量化宽松，零利率把流动性从「货币市场近海」赶向股票、债券等「远海」，投资需求回升；实体衰退压缩私人新资本需求，但政府举债刺激与问题资产重组，又让公共端与结构调整端的融资需求暴增。当年华尔街「造的孽」，超度还得请同一批和尚道士。<a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>于是高盛等创下单季盈利纪录；渔阳也借大市反弹与 BAB「新游戏」几个月内完成全年任务。高兴之余，他开始找<strong>稳定盈利模式</strong>——反弹不会永远，BAB 也会被熟悉。</p>

      <div class="side-panel">
        <h3 class="panel-title">本章时间锚点 · 2009 春夏 → 下半年建网</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">H1</div><div class="ev">QE · 反弹 · BAB · 单季创纪录</div></div>
          <div class="event-card"><div class="yr">5 月</div><div class="ev">SCAP 压力测试公开</div></div>
          <div class="event-card"><div class="yr">6 月末</div><div class="ev">季末装门面 · 宾州债</div></div>
          <div class="event-card"><div class="yr">下半年</div><div class="ev">分销网 · 「麦当劳」模式</div></div>
        </div>
      </div>

      <div class="scene">
        咸鱼翻身证明需求还在；它不证明旧玩法还能用。
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn1">
          <strong>¹ 2009 H1：华尔街从至暗到单季创纪录</strong>
          2009 年第二季度，高盛公布净收入约 137.6 亿美元、净利润约 34.4 亿美元，固定收益/货币/商品交易收入约 68 亿美元创纪录——公开财报与当代媒体把这次反弹写成「危机后中介业务回暖」的证据。同期美联储量化宽松与近零利率政策，把投资者从现金与货基推向风险资产。脚注锚定公开财务与政策时点，不复述书中个人 P&amp;L。
          <div class="why">为何重要：给「新市场」立下宏观背景——需求回来了，结构却变了。</div>
          <div class="src">来源：Goldman Sachs 2009 Q2 财报/EX-99.1；当代 CNN/WBUR 报道；Fed QE 年表</div>
        </div>
        <div class="fn-item" id="fn2">
          <strong>² 投资需求 vs 融资需求：QE、国债刺激与问题资产重组</strong>
          危机后「投资需求」侧：宽松货币抬高风险偏好；「融资需求」侧：财政刺激推高国债与市政发行，结构化产品持有者需要减持、展期或重组。公开危机史把这两种需求写成华尔街「浴火重生」的供给端借口——不是道德翻篇，而是中介功能暂时不可替代。BAB（建设美国债券）等新工具在 §20 已铺垫。
          <div class="why">为何重要：解释为何「生意红火」与「旧杠杆玩法过时」可以同时成立。</div>
          <div class="src">来源：Treasury / Fed 危机年表；§20 BAB 导读；公开市政发行统计综述</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">一对好牌：鲁西的资本优势</h2>
      <p>扑克桌上：一对 A 有一对 A 的玩法，一对 3 有一对 3 的玩法——最讲究因势利导。交易里也得找准定位。鲁西银行的平台像一手「好牌」，但好在哪里、如何打？直觉很清楚：金融海啸后华尔街生态已变——这是一个<strong>新市场</strong>，需要<strong>新思维</strong>。<a class="fn-link" href="#fn3"><sup class="fn">³</sup></a></p>
      <p>§21 刚教过：善败者不乱。清完加州仓，渔阳没有急着加杠杆追反弹，而是开始像福尔摩斯那样收集线索——把「蛛丝马迹」连成逻辑链。</p>

      <div class="scene">
        好牌不是胜负手；读懂牌桌规则的变化才是。
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn3">
          <strong>³ 后危机「新市场」：从赌场到中介</strong>
          公开试读与目录把本章标为第四部分「峰回路转」的枢纽：在 §21 纪律撤退之后，转向商业模式重构。行业层面，危机后投行普遍检讨「对冲基金式」自营，向客户中介与资本中介回归——Group of Thirty（2009 年 1 月）白皮书与日后 Volcker Rule / Dodd-Frank 讨论，正是把「自营投机 vs 客户服务」写进政策议程的公开坐标。
          <div class="why">为何重要：把个人定位问题接到监管与行业结构变迁。</div>
          <div class="src">来源：公开 TOC / FX110 试读节拍；Group of Thirty 2009 白皮书；Volcker Rule 立法史综述</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">福尔摩斯线索：净资本、资产与杠杆</h2>
      <p><strong>线索一：</strong>雷曼垮台的核心是资本不足、杠杆过高——净资本（equity）再厚一点，债主或许不至于恐慌抽资。<strong>线索二：</strong>各国稳定银行体系，核心动作是注资，并要求清理问题资产、降杠杆。<strong>线索三：</strong>2009 年四五月，美国监管对大中型银行做「压力测试」（SCAP）——极端情景下能否扛住亏损；资本多、资产质量高、杠杆低者更稳。公开测试意在昭告「大部分银行安全」，少数不合格者被迫融资、降杠杆，股价与客户往来俱损。<a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>三条线索汇到同一节点：<strong>净资本、持有资产、杠杆率（asset/equity）</strong>。后危机时代，资本与资产状况甚至比短期盈利更「生死攸关」。既然「面子」比「里子」重要，季报装门面、尽量降低外界可见风险，就成了行业潜台词。</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Marriner_S._Eccles_Federal_Reserve_Board_Building.jpg" alt="美联储大厦" loading="lazy" />
        <figcaption>美联储 Eccles 大楼——SCAP 压力测试把「资本缓冲」变成公开剧场。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        当资本比利润更值钱，资产负债表就成了可交易的稀缺品。
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ SCAP 压力测试（2009 年 5 月）</strong>
          美联储与财政部对 19 家大型银行控股公司实施 Supervisory Capital Assessment Program。公开结果材料估计：若走更不利情景，2009–10 年损失可达约 6000 亿美元量级，并要求部分机构补充资本缓冲（合计约 746 亿美元量级，已计入既有措施后）。高盛等资本充足机构「无需额外缓冲」的公开结论，强化了市场对「资本强弱分化」的定价。脚注用官方概述锚定时点与主题，不复述书中对话。
          <div class="why">为何重要：给后文「季末减仓 / 出租资产负债表」提供监管激励。</div>
          <div class="src">来源：Federal Reserve SCAP Overview of Results（2009-05-07）；Treasury SCAP 结果文件</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">季度末出租资产负债表：宾州债十万</h2>
      <p>六月中旬，鲁西管理层下令严控债券持仓，存货多的交易组被要求减仓——显然是为二季报「好看」。鲁西本是冲击最小、信用风险最低的大行之一；连它都要控资产，被盯得更紧的银行更不必说。若大家同时甩存货，价格会跌——渔阳先降了自己账簿头寸。<a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>六月底，巴克莱的孟仁来电：一千万宾州综合债券，开价市政基准 +30 基点，至少便宜五个点。「你们是要降低季度末存货吧？」他先揭底。孟仁承认。压价吃进，七月初轻松卖掉，赚近 <strong>十万美元</strong>——实质是巴克莱把一千万债券「过」到鲁西账上装门面；鲁西资产负债表不能白用，利润就是「收费」。他把「资本好、信用低风险」这个虚优势，换成了实利润。</p>
      <p>思路一下清晰：后危机时代，<strong>资本最有价值，持有资产的能力最有价值</strong>——这正是鲁西的强项。仅靠季末「出租」不够，还得找可持续模式。</p>

      <div class="scene">
        别人要面子，你收过桥费——前提是你真有桥。
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn5">
          <strong>⁵ 季末「装门面」与资产负债表窗口粉饰</strong>
          学术与监管讨论长期关注银行在季报日附近压低短期借款、收缩风险资产，使期末杠杆看起来更低——即 window dressing。SEC 后来强化短期借款披露，正因平均水平与期末水平可严重偏离。公开报道亦涉及危机前后大型银行的季末会计操作争议（与雷曼 Repo 105 等案件形成对照）。脚注解释「为何六月底突然有人贱卖存货」，交易细节为故事改写尺度。
          <div class="why">为何重要：把「福尔摩斯线索」落到一笔可操作的微观交易。</div>
          <div class="src">来源：Owens &amp; Wu 等 window dressing 研究；SEC 短期借款披露讨论；ProPublica 等当代报道</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">水库与洪水：前危机杠杆 vs 后危机渠道</h2>
      <p>世事轮转：前危机时代，「资本」反而不值钱。长期低利率、流动性泛滥、风险意识淡薄——敢用杠杆，也不得不靠杠杆。§5 杜邦公式已写过：利润率被竞争压薄、周转难再提速时，加杠杆的「华尔街模式」几乎成了抬高 ROE 的唯一出路。<a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>市政债市场里，承销费与做市差价被压低，银行靠扩大资产负债表赚钱。加州政府一年只发几次债，但每次数十亿美元——供给像<strong>洪水</strong>，承销商先自己接下再慢慢卖，资产负债表就是<strong>水库</strong>；对冲基金亦可充水库。流动性充沛时，水库多且大，收费自然低。</p>
      <p>危机后，去杠杆成主流；竞争减少、利润率回升，也不再必须靠高杠杆。贝尔斯登并入摩根大通、美林并入美银、瑞银退出一级市场——大券商少了三个，剩余承销「洪水」更大，而资产负债表又被严控，「水库」变小。套利者退出或瘦身，「下游水库」变成稀缺。鲁西何不经营水库？二季末那笔宾州债，就是实例。</p>
      <p>进一步：高盛等<strong>客户关系强、承销多、资本相对紧</strong>；鲁西在美国「没根」、客户弱，但<strong>资本充足</strong>——正好互补。蓄洪吃进便宜货，只完成一半；还要找「泄洪」渠道。</p>

      <div class="scene">
        前危机拼杠杆；后危机拼谁还能当水库。
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ 市政一级市场整合与「水库」隐喻</strong>
          危机前后公开市场结构：贝尔斯登被摩根大通收购、美林被美国银行收购、部分外资行收缩美国市政一级业务——顶级承销席位减少，而地方政府与机构的发行需求（含刺激相关）并未同比例消失。监管与内部风险限额又压缩交易台存货能力。公开试读用「洪水 / 水库」比喻供给冲击与资产负债表中介；脚注用兼并与去杠杆公开事实支撑隐喻，不粘贴原文。
          <div class="why">为何重要：解释互补——强渠道弱资本 vs 强资本弱渠道。</div>
          <div class="src">来源：危机后投行兼并公开史；市政承销份额讨论；§5 杜邦公式导读</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">大券商泄洪不畅：科罗拉多医院债</h2>
      <p>他发现大券商往往不是好「泄洪」口。五月下旬医院债发行扎堆，他从摩根大通低价吃进科罗拉多医院债；一个多月后想出货，请摩根大通销售帮忙找买家——对方不热心，出价很低；高盛、花旗甚至给不出像样的价。<a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>
      <p>换位思考：危机后大券商承销忙，一级都顾不过来，二级注意力有限，只盯刚发行、流动性最好的券；「热乎气儿」过了的存量，兴趣自然淡——当初低价卖给你，就说明他们自己也找不到更好客户。</p>
      <p>改让地方券商卖：几天内，丹佛一家本地券商就卖出好价钱，买家是当地小银行。启发很大：最好的泄洪渠道，是<strong>地方性中小券商</strong>。</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Goldman_Sachs.svg" alt="高盛标志" loading="lazy" />
        <figcaption>高盛——强承销、强大客户；危机后一级「洪水」涌来时，二级存量未必是他们的优先。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        谁把货卖给你，往往也最难帮你把货卖出去。
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ 一级忙碌 vs 二级存量：做市注意力配置</strong>
          固定收益微观结构常识：新券（new issue）享有承销团支持、销售清单与短期流动性；「热乎气」过后的 seasoned paper 依赖二次分销与本地买家。危机后一级交易商资本与风险限额收紧，大台更倾向把稀缺注意力与资产负债表留给新发与大客户。公开试读用医院债例子说明「大对大」二级泄洪失灵；规模为故事尺度。
          <div class="why">为何重要：推动下一节——从华尔街中心走向地方分销网。</div>
          <div class="src">来源：MSRB / 市政二级市场流动性讨论；固定收益新券 vs seasoned 文献综述</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">蔬菜批发市场：地方狼群与分销网</h2>
      <p>前危机：套利者主导，大单、大券商渠道；中小券商边缘化，大家靠杠杆挤利润。后危机：职业玩家少了、出手小了，市场返璞归真——有真实配置需求的传统投资者（富人、中小机构）占主导，地理分散，单笔中小；大券商销售鞭长莫及，地方券商与本地富人、小机构关系更深。<a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>
      <p>扑克上避开其他高手；债券上尽量不与套利者对砍。中小投资者不太抠最后一个基点——像存款利率 3.80% 还是 3.90%，差不多就行。水库囤便宜货，卖给有需要的人，收服务费。渠道在地方券商手里，他们才是泄洪口。</p>
      <p>他开始建网：与近 <strong>20 家</strong>中小券商常往来——东北、中西、西部、南部……「狼群」覆盖地图。鲁西自己几乎没有市政销售，却借地方网触达千千万万中小投资者。地方券商资本弱、水库小；鲁西资本强、渠道无——又是互补。券商之间竞争、不共享销售网；他对所有券商都是客户，理论上可借用所有人的网——有的放矢，找本地最强的那一家。</p>
      <p>形象说法：在城乡结合部开一个<strong>蔬菜批发市场</strong>——从高盛等「大菜农」进货，经地方「小贩」零售到市民手中。平凡，却折射生态巨变。前危机：模型 + 杠杆 + 大单 = 投机场；后危机：市场回归融资方与投资方之间的<strong>资本流通渠道</strong>。谁抛弃旧思维、拥抱<strong>资本 + 渠道 + 分销式交易</strong>，谁占先机。</p>

      <div class="scene">
        不是更聪明的模型，是更老实的生意。
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn8">
          <strong>⁸ 市政买家结构：富人、保险、地方银行与区域经纪</strong>
          美国市政债传统持有者包括高净值个人（联邦税免）、共同基金、保险公司与地方存款机构等；区域经纪商/独立券商长期在本地零售与小机构账户上有粘性。危机后杠杆套利资本撤离，使「配置型」买家权重相对上升——公开市场结构讨论与 MSRB 投资者类型统计支持这一方向性判断。书中「近 20 家」「狼群」为叙事尺度的销售网建设。
          <div class="why">为何重要：给「蔬菜批发市场」隐喻装上真实的买方地理结构。</div>
          <div class="src">来源：MSRB / Fed 市政持有者结构统计；区域经纪商业模式综述；公开试读节拍（改写）</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">麦当劳不是麦道夫：新思维与关系学</h2>
      <p>2009 下半年，策略核心变成：扩销售网、加交易量。杜邦视角——利润率不低，就该加快周转，甚至可牺牲一点利润率换份额。对大券商：做可靠水库；对地方券商：保证供货、留足利润空间。中小券商交易量暴增还有附加收获：反馈信息帮他囤货——例如精于田纳西的券商预告某日大批债券到期再投资，指定评级与价格带会好卖，他便可提前备货。<a class="fn-link" href="#fn9"><sup class="fn">⁹</sup></a></p>
      <p>这已不只靠「猜对方向」赚钱，而是靠<strong>平台与商业模式</strong>。他像商人一样看销售数据：交易量较 2008 年大增；与大券商买多卖少、利润率低，与地方买少卖多、利润率高——分销特征清晰，利润像开店般稳定，不再赌大小般大起大落。</p>
      <p>大老板看他近乎直线上升、波动极小的盈亏图，开玩笑：「简直怀疑你是麦道夫。」他答：「我不是麦道夫，是<strong>麦当劳</strong>。守着商店靠流转赚钱，当然比赌波动性低。」</p>
      <p>古人云：<strong>世异则事异，事异则备变</strong>。危机后投行检讨「对冲基金」模式，向传统中介回归；监管侧 Volcker Rule 与 Dodd-Frank 的讨论，正把「自营投机」往政策围栏里赶。<a class="fn-link" href="#fn10"><sup class="fn">¹⁰</sup></a> 新市场呼唤新思维：利用鲁西相对资本优势，建分销网络，把「交易」当成「生意」来做。下一章 §23「关系学」——网建起来之后，人情、互惠与长期客户关系，才是分销模式的润滑剂。</p>

      <div class="scene">
        麦当劳式利润曲线：不靠神秘，靠周转与网络。
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn9">
          <strong>⁹ 信息反馈回路与「配置型」再投资日历</strong>
          地方销售网的价值不只在出口，也在需求情报：到期再投资（maturity reinvestment）、本地评级偏好、价格带（如平价附近）都会造成短暂供需错配。公开固定收益实务把「知道谁在哪天需要什么」写成分销优势；与纯相对价值模型交易形成对照。脚注说明商业模式逻辑，不提供可复制的非公开客户名单。
          <div class="why">为何重要：解释为何「波动变小」——赚的是中介租金，不是方向彩票。</div>
          <div class="src">来源：固定收益销售/分销实务综述；公开试读「田纳西到期」节拍（改写）</div>
        </div>
        <div class="fn-item" id="fn10">
          <strong>¹⁰ 「世异则事异」与 Volcker / Dodd-Frank 伏笔</strong>
          「世异则事异，事异则备变」语出《韩非子》等法家文献传统（亦见战国策士话语），公开试读用作本章收束。政策坐标：2009 年 1 月 Group of Thirty 白皮书已建议限制大型银行自营交易与私募基金投资；2010 年奥巴马政府推动、写入 Dodd-Frank 的 Volcker Rule，把「与客户无关的自营」推向长期限制。本章故事时点（2009）是<strong>伏笔与心态转变</strong>，不是法案生效日详解——为 §23 关系学、§24 分合主题留接口。
          <div class="why">为何重要：把个人「麦当劳模式」接到行业监管与下一章关系网络。</div>
          <div class="src">来源：《韩非子》公开文本；Group of Thirty 2009；CRS / 立法史 Volcker Rule 综述；公开 TOC §23</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>人物关系 / 时间线 / 知识图谱</h2>

        <div class="mermaid-wrap">
          <div class="caption">分销生态：大菜农 → 批发水库 → 地方小贩 → 市民</div>
          <div class="mermaid">
flowchart LR
  GS[高盛等大投行] -->|一级洪水/廉价存货| YY[渔阳·鲁西水库]
  BR[巴克莱等] -->|季末装门面| YY
  YY -->|蓄洪吃进| INV[市政债库存]
  INV --> RA[地方券商狼群]
  RA --> NE[东北]
  RA --> MW[中西部]
  RA --> W[西部]
  RA --> S[南部]
  NE --> BUY[中小投资者/本地银行]
  MW --> BUY
  W --> BUY
  S --> BUY
  BUY -->|需求情报| YY
  YY --> NEXT[§23 关系学]
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">时间线：新市场，新思维（2009 H1 → 下半年）</div>
          <div class="mermaid">
timeline
    title New Markets New Thinking
    early 2009 : Dark outlook · then QE rebound
    May 2009 : SCAP stress tests public
    June 2009 : Quarter-end window dressing
    June-end : Pennsylvania clip · rent BS
    mid 2009 : Colorado hospital · regionals win
    H2 2009 : Build ~20-dealer wolf pack
    late 2009 : McDonald not Madoff P and L
    bridge : Toward §23 guanxi / relationships
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">知识图谱：旧思维 → 新思维</div>
          <div class="mermaid">
flowchart TB
  S21[§21 善败者不乱] --> FLAT[清仓·纪律]
  FLAT --> ASK[今后如何赚钱]
  ASK --> CLUES[资本/资产/杠杆线索]
  CLUES --> SCAP[SCAP·去杠杆]
  SCAP --> EDGE[鲁西资本优势]
  EDGE --> OLD[旧: 模型+杠杆+大单]
  EDGE --> NEW[新: 资本+渠道+分销]
  OLD --> CASINO[投机场]
  NEW --> WHOLE[蔬菜批发市场]
  WHOLE --> STABLE[麦当劳式稳定利润]
  STABLE --> REG[Volcker/Dodd-Frank 伏笔]
  STABLE --> S23[§23 关系学]
          </div>
        </div>
      </section>
'''

EN_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/New_York_Stock_Exchange_September_2016_05.jpg" alt="New York Stock Exchange" loading="lazy" />
        <figcaption>New York Stock Exchange—in H1 2009 Wall Street flipped from “bleak” to “record quarter.” Source: Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">Ice and fire: H1 2009 rebound</h2>
      <p>After §21—skilled defeat, no chaos—the California book was flat and the mind was clear. The next question was not “how to bet the next tape,” but “how to make money from here.” In the first half of 2009 Wall Street lived ice and fire: early-year gloom said investment banking would freeze; months later the street flipped like a salted fish, stunning onlookers. <a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>In hindsight the logic is plain: banks sell a <strong>capital business</strong>—bridging clients who need funding with clients who need to invest. After the tsunami, both needs survived. Central banks eased, even into QE; zero rates pushed liquidity from the “near-shore” money markets toward the “deep water” of stocks and bonds, lifting investment demand. The real-economy slump cut private new capital needs, but government stimulus borrowing and restructuring of toxic structured products spiked public and balance-sheet repair demand. The Street that “built the mess” was still hired to perform the rites. <a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>Goldman and peers posted record quarters; Yuyang, riding the rebound and the BAB “new game,” hit his full-year number in months. Then he hunted a <strong>stable profit model</strong>—rallies end; BAB would be learned.</p>

      <div class="side-panel">
        <h3 class="panel-title">Chapter anchors · 2009 H1 → H2 network build</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">H1</div><div class="ev">QE · rebound · BAB · record quarters</div></div>
          <div class="event-card"><div class="yr">May</div><div class="ev">SCAP stress tests published</div></div>
          <div class="event-card"><div class="yr">Jun-end</div><div class="ev">Window dressing · PA bonds</div></div>
          <div class="event-card"><div class="yr">H2</div><div class="ev">Distribution net · “McDonald’s” mode</div></div>
        </div>
      </div>

      <div class="scene">
        A rebound proves demand still exists; it does not prove the old playbook still works.
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn1">
          <strong>¹ H1 2009: from darkest hour to record quarters</strong>
          In Q2 2009 Goldman reported about $13.76bn net revenue and $3.44bn net earnings, with FICC near $6.8bn—a public “intermediation is back” print. Fed QE and near-zero rates pushed investors out of cash and money funds into risk assets. The footnote anchors public filings and policy dates, not the book’s personal P&amp;L.
          <div class="why">Why it matters: macro stage for a “new market”—demand returned, structure changed.</div>
          <div class="src">Source: Goldman Sachs 2009 Q2 EX-99.1; contemporary CNN/WBUR; Fed QE chronologies</div>
        </div>
        <div class="fn-item" id="fn2">
          <strong>² Investment vs funding demand: QE, fiscal issuance, toxic-asset repair</strong>
          Post-crisis “investment demand” rose with easier money; “funding demand” rose with fiscal stimulus and the need to unwind or refinance structured holdings. Public crisis histories treat both as why the Street’s intermediary function briefly could not be skipped. BABs were foreshadowed in §20.
          <div class="why">Why it matters: explains how “busy desks” and “obsolete leverage plays” can coexist.</div>
          <div class="src">Source: Treasury/Fed chronologies; §20 BAB guide; public muni issuance surveys</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">A pair of aces: Lucy's capital edge</h2>
      <p>At the poker table, a pair of aces and a pair of threes want different lines—the art is reading the situation. Trading needs the same positioning. Lucy Bank’s platform looked like a strong hand—but wherein, and how to play it? Instinct was clear: after the tsunami the ecology had changed. This was a <strong>new market</strong>, needing <strong>new thinking</strong>. <a class="fn-link" href="#fn3"><sup class="fn">³</sup></a></p>
      <p>§21 had just taught skilled defeat. Flat on California, Yuyang did not lever up into the bounce; he collected clues like Holmes—linking traces into a chain.</p>

      <div class="scene">
        A strong hand is not the win; reading when the table rules changed is.
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn3">
          <strong>³ Post-crisis “new market”: casino to intermediary</strong>
          Public TOC places this chapter as a Part-4 hinge after §21’s disciplined exit: rebuild the business model. Industry-wide, banks revisited hedge-fund-like prop and edged back toward client intermediation. The Group of Thirty’s January 2009 white paper and later Volcker Rule / Dodd-Frank debates publicly framed “prop speculation vs client service.”
          <div class="why">Why it matters: plugs personal positioning into regulatory and industry structure shift.</div>
          <div class="src">Source: public TOC / FX110 beat map; Group of Thirty 2009; Volcker Rule legislative surveys</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">Holmes clues: equity, assets, leverage</h2>
      <p><strong>Clue one:</strong> Lehman failed first from thin capital and high leverage—thicker equity might have kept creditors from a panic run. <strong>Clue two:</strong> governments stabilized banks by injecting capital and forcing cleanup and de-leveraging. <strong>Clue three:</strong> in April–May 2009 U.S. supervisors ran SCAP stress tests—could banks absorb extreme losses? More capital, better assets, lower leverage meant survival; the public show aimed to restore confidence; weak names had to raise capital and shrink, hitting stock and franchise. <a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>All three point to one knot: <strong>equity, assets held, and leverage (assets/equity)</strong>. After the crisis, capital and asset posture could matter more than a quarter’s P&amp;L. When “face” outranks “substance,” quarter-end cosmetics and hiding visible risk become industry subtext.</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Marriner_S._Eccles_Federal_Reserve_Board_Building.jpg" alt="Federal Reserve Eccles Building" loading="lazy" />
        <figcaption>Fed Eccles Building—SCAP made capital buffers a public theater. Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        When capital outprices profit, the balance sheet itself becomes scarce inventory.
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ SCAP stress tests (May 2009)</strong>
          The Fed and Treasury ran the Supervisory Capital Assessment Program on 19 large BHCs. Public materials sketched ~$600bn potential 2009–10 losses under a more adverse path and required additional buffers on the order of ~$74.6bn after credited actions. Names like Goldman needing “no extra buffer” publicly priced a capital divide. The footnote anchors official overviews, not book dialogue.
          <div class="why">Why it matters: regulatory motive for quarter-end cuts and “renting” balance sheets.</div>
          <div class="src">Source: Federal Reserve SCAP Overview (2009-05-07); Treasury SCAP results PDF</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">Renting the balance sheet: Pennsylvania clip</h2>
      <p>In mid-June Lucy management ordered tight bond-inventory control—clearly for a prettier Q2 print. Lucy was among the least damaged, lowest-credit-risk large banks; if even it had to shrink assets, watched names would dump harder. Simultaneous dumps mean lower prices—so Yuyang cut his book early. <a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>At month-end Barclays’ Meng Ren called: $10mm Pennsylvania GOs, offered at muni benchmark +30 bp, at least five cheap. “You’re clearing quarter-end inventory?” He named the motive. Meng admitted. After haggling he bought, sold easily in early July, made nearly <strong>$100,000</strong>—in substance Barclays parked ten million on Lucy’s sheet for cosmetics; Lucy’s balance sheet is not free; the P&amp;L was the toll. A soft edge—“strong capital, low credit risk”—became hard cash.</p>
      <p>The thought crystallized: post-crisis, <strong>capital and the ability to hold assets</strong> are what pay—Lucy’s strength. Quarter-end rental alone is not a franchise; he needed a durable model.</p>

      <div class="scene">
        They need face; you charge bridge tolls—only if you actually own a bridge.
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn5">
          <strong>⁵ Quarter-end window dressing of balance sheets</strong>
          Research and regulators have long watched banks compress short-term borrowings and risk assets near reporting dates so leverage looks cleaner—window dressing. The SEC later pushed richer short-term borrowing disclosure precisely because period-end and period-average can diverge. Contemporary coverage also flagged large-bank quarter-end accounting disputes (set beside cases like Lehman Repo 105). The footnote explains why late June suddenly offered cheap inventory; ticket sizes are story scale.
          <div class="why">Why it matters: lands Holmes clues in one operable micro-trade.</div>
          <div class="src">Source: Owens &amp; Wu window-dressing work; SEC short-term borrowing disclosure debate; ProPublica-era coverage</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">Reservoirs and floods: leverage vs channels</h2>
      <p>Cycles turn: before the crisis, capital was the cheap input. Low rates, plenty of liquidity, thin risk memory—leverage was both tempting and almost mandatory. §5’s DuPont path already said: when margins are competed away and turnover stalls, the “Wall Street mode” of more leverage is nearly the only ROE lever left. <a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>In munis, underwriting fees and market-making spreads were crushed; banks earned by growing the balance sheet. A state like California might issue only a few times a year—but tens of billions at a clip. Supply is a <strong>flood</strong>; the underwriter warehouses paper and dribbles it out—the balance sheet is a <strong>reservoir</strong>; hedge funds can be reservoirs too. When liquidity is abundant, reservoirs are many and large, so tolls are low.</p>
      <p>After the crisis, de-leveraging ruled; with fewer rivals and fatter margins, high leverage was less necessary. Bear into JPMorgan, Merrill into Bank of America, UBS exiting the primary muni business—three big seats gone—left more “flood” for survivors while risk limits shrank the “reservoirs.” Arb capital fled or dieted; downstream storage became scarce. Why shouldn’t Lucy run a reservoir? The Pennsylvania clip was a prototype.</p>
      <p>Further: Goldman-class firms are <strong>franchise-rich and relatively capital-tight</strong>; Lucy is <strong>capital-rich and franchise-thin</strong> in U.S. munis—complements. Absorbing the flood cheaply is only half the trade; he still needed a drain.</p>

      <div class="scene">
        Pre-crisis competed on leverage; post-crisis competes on who can still be a reservoir.
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ Primary-muni consolidation and the reservoir metaphor</strong>
          Public structure: Bear into JPM, Merrill into BofA, some foreign banks shrinking U.S. primary munis—top seats fell while issuer needs (including stimulus-linked) did not vanish one-for-one. Internal risk caps further cut warehouse capacity. Trial-reads use flood/reservoir imagery for supply shocks vs balance-sheet intermediation; the footnote supports the metaphor with merger and de-leveraging facts, without pasting prose.
          <div class="why">Why it matters: frames the complement—strong channel/weak capital vs strong capital/weak channel.</div>
          <div class="src">Source: post-crisis IB merger histories; muni underwriting-share discussions; §5 DuPont guide</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">Big dealers can't drain: Colorado hospital</h2>
      <p>He learned big dealers are often poor drains. In late May hospital issuance clustered; he lifted Colorado hospital paper cheap from JPMorgan. More than a month later he asked JPM sales to help find a bid—lukewarm, low; Goldman and Citi barely showed. <a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>
      <p>Stand in their shoes: post-crisis primary desks are slammed; secondary attention is scarce and reserved for the hottest new issues. Seasoned paper past its “warmth” is not their priority—and the cheap sale to you already meant they lacked a better home.</p>
      <p>He switched to regionals: within days a Denver broker printed a strong sale to a local small bank. Lesson: the best drains are <strong>regional mid-size dealers</strong>.</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Goldman_Sachs.svg" alt="Goldman Sachs logo" loading="lazy" />
        <figcaption>Goldman—strong underwriting, strong large accounts; when primary floods arrive, seasoned secondary is not always priority. Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        Whoever sold you the bonds is often the least able to help you sell them on.
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ Primary busy vs secondary seasoned: attention rationing</strong>
          Microstructure basics: new issues enjoy syndicate support and short-run liquidity; seasoned paper needs secondary distribution and local buyers. Post-crisis capital limits push big desks to spend scarce attention and sheet on new issue and large accounts. Trial-reads use the hospital-bond beat to show “street-to-street” secondary drains fail; sizes are story scale.
          <div class="why">Why it matters: pushes the next section—from money-center desks to regional distribution.</div>
          <div class="src">Source: MSRB / muni secondary liquidity discussions; new-issue vs seasoned FI surveys</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">Vegetable wholesale: regional wolf pack</h2>
      <p>Pre-crisis: arb money dominated—block size, big-dealer channels; regionals marginalized; everyone levered thin margins. Post-crisis: fewer pros, smaller tickets; the market returned to form—traditional allocators (wealthy households, mid-size institutions) led, geographically scattered, mid-ticket; big salesforces cannot cover them all, while local brokers own sticky ties to local wealth and small institutions. <a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>
      <p>At poker, avoid other sharks; in bonds, avoid arb-vs-arb knife fights. Mid-size buyers rarely nick the last basis point—like caring whether a deposit pays 3.80% or 3.90%. Warehouse cheap paper, serve real need, take a service fee. Channels sit with regionals; they are the drains.</p>
      <p>He built a net: regular flow with nearly <strong>twenty</strong> regionals—Northeast, Midwest, West, South—a “wolf pack” covering the map. Lucy itself had almost no muni salesforce, yet reached countless mid-size end buyers through locals. Regionals are channel-strong and capital-weak; Lucy is the reverse—another complement. Brokers compete and do not share sales nets; to every broker he is a client, so in theory he can borrow everyone’s net—then aim at the strongest local name for each print.</p>
      <p>Image: open a <strong>vegetable wholesale market</strong> at the urban–rural edge—buy from Goldman-class “growers,” retail through local “hawkers” to citizens. Ordinary—and exactly the ecological flip. Pre-crisis: models + leverage + blocks = casino. Post-crisis: markets revert to a <strong>capital channel</strong> between issuers and investors. Who drops the old mind and hugs <strong>capital + channel + distribution trading</strong> seizes the edge.</p>

      <div class="scene">
        Not a smarter model—a more honest business.
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn8">
          <strong>⁸ Muni buyer mix: wealth, insurers, local banks, regional brokers</strong>
          Traditional U.S. muni holders include high-net-worth individuals (tax exemption), funds, insurers, and local depository institutions; regional/independent brokers long owned sticky local retail and small-institution accounts. After levered arb capital left, allocator buyers weighed more—directionally supported by MSRB investor-type stats and market-structure surveys. “~20 firms” and “wolf pack” are narrative-scale network building.
          <div class="why">Why it matters: puts real buyer geography under the wholesale-market metaphor.</div>
          <div class="src">Source: MSRB / Fed muni holder stats; regional-broker business surveys; public trial-read beats (rewritten)</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">McDonald's, not Madoff: new mind &amp; guanxi</h2>
      <p>In H2 2009 the core became: grow the sales net, grow turnover. DuPont logic—if margins are decent, accelerate turns, even trading a bit of margin for share. To big dealers: be a reliable reservoir. To regionals: keep supply flowing and leave them room to earn. Surging regional volume also fed intelligence: a Tennessee specialist might flag a large maturity reinvestment day and which rating/price band would clear—so he could pre-stock. <a class="fn-link" href="#fn9"><sup class="fn">⁹</sup></a></p>
      <p>This was no longer mostly “call the tape”; it was <strong>platform and business model</strong>. He watched sales data like a merchant: volume multiples vs 2008; buy-heavy/low-margin vs big dealers, sell-heavy/high-margin vs regionals—classic distribution; P&amp;L steadier like a shop, not a coin-flip book.</p>
      <p>The big boss, seeing a near-linear, low-vol P&amp;L chart, joked: “I almost suspect you’re Madoff.” Reply: “I’m not Madoff—I’m <strong>McDonald’s</strong>. Mind the store, earn on turnover; of course vol is lower than gambling the tape.”</p>
      <p>The ancients: <strong>when the world changes, affairs change; when affairs change, preparations must change</strong>. Post-crisis banks revisited hedge-fund modes and returned toward classic intermediation; on the policy side, Volcker Rule and Dodd-Frank talk began fencing off prop speculation. <a class="fn-link" href="#fn10"><sup class="fn">¹⁰</sup></a> New markets demand new minds: use Lucy’s relative capital edge, build distribution, run trading as a <strong>business</strong>. Next, §23 “Relationships” (关系学)—once the net exists, reciprocity and long-client care are the lubricant of distribution.</p>

      <div class="scene">
        A McDonald’s P&amp;L curve: not mystery—turnover and network.
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn9">
          <strong>⁹ Feedback loops and allocator reinvestment calendars</strong>
          A regional sales net’s value is exit <em>and</em> demand intel: maturity reinvestment, local rating taste, price bands near par can create brief mismatches. Public FI practice treats “knowing who needs what on which day” as a distribution edge—versus pure relative-value model trading. The footnote explains business logic; it does not publish non-public client lists.
          <div class="why">Why it matters: why vol falls—you earn intermediation rent, not a direction lottery.</div>
          <div class="src">Source: FI sales/distribution practice surveys; public trial-read “Tennessee maturity” beat (rewritten)</div>
        </div>
        <div class="fn-item" id="fn10">
          <strong>¹⁰ “When the world changes…” and Volcker / Dodd-Frank foreshadow</strong>
          The classical line is associated with Legalist texts such as Han Feizi (and related Warring-States rhetoric); trial-reads use it to close the chapter. Policy map: Group of Thirty’s January 2009 paper already urged limits on large-bank prop trading and private-fund investing; the 2010 Volcker Rule inside Dodd-Frank pushed “prop unrelated to clients” toward lasting restraint. The chapter’s 2009 story time is <strong>foreshadow and mindset shift</strong>, not a statute effective-date brief—and it bridges to §23 relationships and §24’s merge/split themes.
          <div class="why">Why it matters: plugs the personal “McDonald’s mode” into industry regulation and the next chapter’s network craft.</div>
          <div class="src">Source: Han Feizi public text; Group of Thirty 2009; CRS / Volcker Rule legislative surveys; public TOC §23</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>Relationships / timeline / knowledge graph</h2>

        <div class="mermaid-wrap">
          <div class="caption">Distribution ecology: growers → wholesale reservoir → local hawkers → citizens</div>
          <div class="mermaid">
flowchart LR
  GS[Goldman-class dealers] -->|primary flood / cheap inventory| YY[Yuyang · Lucy reservoir]
  BR[Barclays et al.] -->|quarter-end cosmetics| YY
  YY -->|warehouse| INV[Muni inventory]
  INV --> RA[Regional wolf pack]
  RA --> NE[Northeast]
  RA --> MW[Midwest]
  RA --> W[West]
  RA --> S[South]
  NE --> BUY[Mid-size investors / local banks]
  MW --> BUY
  W --> BUY
  S --> BUY
  BUY -->|demand intel| YY
  YY --> NEXT[§23 Relationships]
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Timeline: New Markets, New Thinking (2009 H1 → H2)</div>
          <div class="mermaid">
timeline
    title New Markets New Thinking
    early 2009 : Dark outlook · then QE rebound
    May 2009 : SCAP stress tests public
    June 2009 : Quarter-end window dressing
    June-end : Pennsylvania clip · rent BS
    mid 2009 : Colorado hospital · regionals win
    H2 2009 : Build ~20-dealer wolf pack
    late 2009 : McDonald not Madoff P and L
    bridge : Toward §23 guanxi / relationships
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Knowledge graph: old mind → new mind</div>
          <div class="mermaid">
flowchart TB
  S21[§21 Skilled defeat] --> FLAT[Flat book · discipline]
  FLAT --> ASK[How to earn from here]
  ASK --> CLUES[Equity / assets / leverage clues]
  CLUES --> SCAP[SCAP · de-leveraging]
  SCAP --> EDGE[Lucy capital edge]
  EDGE --> OLD[Old: models + leverage + blocks]
  EDGE --> NEW[New: capital + channel + distribution]
  OLD --> CASINO[Casino tape]
  NEW --> WHOLE[Vegetable wholesale market]
  WHOLE --> STABLE[McDonald-style stable P and L]
  STABLE --> REG[Volcker / Dodd-Frank foreshadow]
  STABLE --> S23[§23 Relationships]
          </div>
        </div>
      </section>
'''

def main():
    zh = page(
        "zh",
        "《乱世华尔街》第22集：新市场，新思维",
        "故事导读 · 据公开试读改写 · 场外研究补充",
        "新市场，新思维",
        "《乱世华尔街》第二十二章「新市场，新思维」· 渔阳 · 故事改写 + 脚注研究 · 第四部分「峰回路转」",
        "下面按作者经历与公开时间线讲述本章故事，用自己的话改写，方便跟读；不是全书/全章原文照搬。脚注、配图与知识图谱为场外公开资料补充。完整内容请读正版。",
        ZH_TOC,
        "CHAPTER TWENTY-TWO · 新市场，新思维 · 第四部分 峰回路转",
        ZH_BODY,
        "《乱世华尔街》· 渔阳 · 第二十二章故事导读（原创改写）",
    )
    en = page(
        "en",
        "Chaos on Wall Street §22: New Markets, New Thinking",
        "Story guide · rewritten from public trial reads · off-book research",
        "New Markets, New Thinking",
        "Chaos on Wall Street, Chapter 22 “New Markets, New Thinking” · Yuyang · story rewrite + footnote research · Part 4 “The Road Turns”",
        "A story-first retelling from the author’s arc and public timelines, in our own words for guided reading—not a verbatim copy of the copyrighted chapter. Footnotes, figures, and graphs are off-book public research. For the full text, support the official edition.",
        EN_TOC,
        "CHAPTER TWENTY-TWO · New Markets, New Thinking · Part 4 The Road Turns",
        EN_BODY,
        "Chaos on Wall Street · Yuyang · Ch.22 story guide (original rewrite)",
    )
    (DIR / "new-markets-zh.html").write_text(zh, encoding="utf-8")
    (DIR / "new-markets-en.html").write_text(en, encoding="utf-8")
    print("Wrote", DIR / "new-markets-zh.html", len(zh))
    print("Wrote", DIR / "new-markets-en.html", len(en))

if __name__ == "__main__":
    main()
