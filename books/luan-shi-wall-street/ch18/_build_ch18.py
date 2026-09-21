#!/usr/bin/env python3
"""Build full self-contained ZH/EN HTML for ch18 最黑暗的时刻 / The Darkest Hour."""
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
        '<a class="active" href="darkest-hour-zh.html">中文</a>\n'
        '        <a href="darkest-hour-en.html">English</a>\n'
        '        ' + home
        if lang == "zh" else
        '<a href="darkest-hour-zh.html">中文</a>\n'
        '        <a class="active" href="darkest-hour-en.html">English</a>\n'
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
    ("s1", "各回各家：全球注资浪潮"),
    ("s2", "造血停摆：信贷冻结与休克经济"),
    ("s3", "伯南克学乖了：美联储扩表"),
    ("s4", "严重衰退：实体经济崩塌"),
    ("s5", "变革当选：奥巴马与政治左转"),
    ("s6", "国之将亡：麦道夫现形"),
    ("s7", "金融奇境：价格挣脱引力"),
    ("s8", "反伽马地狱：奇异衍生品的教训"),
    ("s9", "甩掉包袱：田纳西住房债与明天"),
    ("diagrams", "人物关系 / 时间线 / 知识图谱"),
]

EN_TOC = [
    ("s1", "Everyone goes home: global recapitalizations"),
    ("s2", "The blood stops: credit freeze and shock economy"),
    ("s3", "Bernanke learned: the Fed expands its balance sheet"),
    ("s4", "Severe recession: the real economy collapses"),
    ("s5", "Change wins: Obama and the leftward turn"),
    ("s6", "When a state falters: Madoff unmasked"),
    ("s7", "Financial Wonderland: prices escape gravity"),
    ("s8", "Negative-gamma hell: exotic derivatives' lesson"),
    ("s9", "Drop the bag: Tennessee housing bond and tomorrow"),
    ("diagrams", "Relationships / timeline / knowledge graph"),
]

ZH_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/New_York_Stock_Exchange_Building.jpg" alt="纽约证券交易所大楼" loading="lazy" />
        <figcaption>纽约证券交易所大楼——2008 年秋冬，屏幕上的数字不再像「市场」，更像「休克监护仪」。来源：Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">各回各家：全球注资浪潮</h2>
      <p>承接上一章：保尔森计划过关、九大行被迫接受注资之后，<strong>2008 年 10 月中旬</strong>起，各国政府纷纷以注资、债务担保等形式抢救本国银行。危机前，跨国银行集团以「世界公民」自居，在海外广开分支；海啸一来，却只能<strong>各回各家、各找各妈</strong>。<a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>公开记录里：荷兰向 ING 等注入约百亿美元量级资本；瑞士向瑞银（UBS）注资并以巨资承接问题资产；法国向巴黎银行、兴业银行等注资逾百亿欧元。美国与英国的方案已经写在 §17；此刻全球同台，资金与担保成了「国籍」游戏。</p>

      <div class="side-panel">
        <h3 class="panel-title">本章时间锚点 · 2008-10 中旬 → 2008-12</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">10 中</div><div class="ev">全球注资/担保·信贷仍冻结</div></div>
          <div class="event-card"><div class="yr">10–11</div><div class="ev">美联储扩表·实体衰退加深·大选</div></div>
          <div class="event-card"><div class="yr">11-04</div><div class="ev">奥巴马当选·民主党大胜</div></div>
          <div class="event-card"><div class="yr">12-10</div><div class="ev">麦道夫骗局曝光·金融奇境</div></div>
        </div>
      </div>

      <div class="scene">
        护照救得了银行的命；救不了去杠杆的惯性。
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn1">
          <strong>¹ 2008 年 10 月欧洲银行注资潮</strong>
          继英国 10 月 8 日银行注资与债务担保方案、美国 10 月 14 日公布九大行资本购买计划后，荷兰、瑞士、法国等相继公布对本国大型银行的注资、担保或问题资产承接安排（公开报道常提及 ING、UBS、BNP/Société Générale 等）。跨国银行在危机中「国籍化」——海外扩张的全球叙事让位于母国财政后盾。
          <div class="why">为何重要：说明为何 TARP 过关仍不等于全球恐慌结束——各国同步抢救，去杠杆却仍在滚。</div>
          <div class="src">来源：BIS Quarterly Review 2008-12；各国财政部/央行当代公告；FCIC 国际对照</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">造血停摆：信贷冻结与休克经济</h2>
      <p>政府紧急援救让金融体系免于当场崩溃，却挡不住<strong>去杠杆</strong>的洪流。美国资本市场融资几近关闭：股票与公司债难卖，一向被视为「稳定可靠」的<strong>短期票据（商业票据）</strong>市场大幅缩水；消费信贷中介用的资产证券化发行几乎停摆。影子银行失灵；传统商业银行要么自己中了弹，要么为防衰退信用损失而收紧放贷。<a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>银行体系「造血」骤停，高度金融化的美国经济像严重供血不足的病人陷入<strong>休克</strong>：个人难购房购车，企业周转困难，活动减少推高失业，失业再压消费——恶性循环。普通人担心的已不只是衰退（recession），而是萧条（depression）。雷曼后货币基金「破净」、众议院否决日道指千点级崩盘的余震，此时汇成更长的信贷冬夜。</p>

      <div class="scene">
        救了银行的壳，未必救得了银行愿意借钱的心。
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn2">
          <strong>² 商业票据冻结、影子银行与货币基金余震</strong>
          雷曼破产后，Reserve Primary Fund 于 2008-09-16「破净」（break the buck），引发货币基金赎回潮并冲击商业票据市场。10 月前后，资产支持商业票据与部分 ABS 发行接近停顿；批发融资依赖型机构被迫去杠杆。公开危机史把「信贷冻结」视为金融冲击传导至实体经济的主通道。
          <div class="why">为何重要：把交易台恐慌翻译成实体「造血停摆」——本章从华尔街延到美国经济本体。</div>
          <div class="src">来源：Yale YPFS Reserve Primary 案例；FRASER；BIS / Fed 商业票据与 ABS 数据叙述</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">伯南克学乖了：美联储扩表</h2>
      <p>1930 年代大萧条里，美联储曾在银行危机中错误收紧货币供应，被史家视为加剧萧条的要因之一。2008 年的美联储「学乖了」：研究大萧条出身的<strong>伯南克</strong>坚决降息、扩大基础货币，并把「终极贷款人」角色再往前推——用多项新<strong>便利工具（facilities）</strong>替银行业向实体经济输送信贷。<a class="fn-link" href="#fn3"><sup class="fn">³</sup></a></p>
      <p>公开措施包括：购买短期商业票据以助企业周转；购买房贷抵押债券以支撑房市融资；购买基于车贷、信用卡等消费信贷的证券化产品，间接支持占经济大半的消费。美联储资产负债表迅速膨胀，在一定程度上缓冲银行缩表对实体的冲击。财政部也将注资范围扩大到更多中小银行。作者的判断是：正是这些超常规行动，使美国没有重演 1929 后那种全面大萧条——但<strong>严重衰退</strong>仍不可避免。</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Marriner_S._Eccles_Federal_Reserve_Board_Building.jpg" alt="美联储埃克尔斯大楼" loading="lazy" />
        <figcaption>美联储理事会大楼（华盛顿）——伯南克团队在此把「终极贷款人」扩成一张更宽的网。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        大萧条课本变成操作手册：这一次，央行选择先把水灌进管道。
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn3">
          <strong>³ 美联储危机便利与资产负债表扩张</strong>
          2008 年秋冬，美联储在降息之外推出/扩展多项便利，包括商业票据融资便利（CPFF）、定期拍卖工具、对 MBS 与机构债的大规模购买路径，以及面向消费/小企业 ABS 的融资支持思路（如日后 TALF 的政策脉络）。美联储总资产在危机期间显著上升。公开论述强调：目标是替代失灵的私人信贷中介，而非传统意义上的「只救银行」。
          <div class="why">为何重要：解释为何「政府注资了」仍不够——还需央行直接对接实体融资管道。</div>
          <div class="src">来源：Federal Reserve 危机工具年表；FRASER；Bernanke 演讲与 FCIC</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">严重衰退：实体经济崩塌</h2>
      <p>工业产出跌幅创战后纪录；新房开工同比可跌约七成量级；按人口调整的汽车销量掉到二战后低谷，通用与克莱斯勒濒临生存危机。零售端，Circuit City、Linens 'n Things 等连锁宣告破产。企业裁员加速——公开叙述里，仅九、十两个月美国就业岗位损失可达约<strong>六十万</strong>量级。<a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>对渔阳而言，交易屏上的基点与利差，第一次密集地翻译成邻居失业、店面关门、底特律告急。金融海啸不再只是「华尔街内战」。</p>

      <div class="scene">
        当屏幕上的价差开始对应工厂的烟囱，危机才真正叫「海啸」。
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ 2008 年末实体指标与汽车/零售冲击</strong>
          美国工业产出、住房开工、汽车销售在 2008 年下半年急剧恶化；通用汽车与克莱斯勒随后进入政府援助/破产重组轨道。Circuit City 于 2008 年底申请破产保护；Linens 'n Things 亦在危机前后倒闭。劳工统计显示 2008 年秋就业岗位大幅净减少。这些「实体脚注」是金融信贷冻结的下游证据。
          <div class="why">为何重要：把本章「最黑暗」从价差叙事锚定到可核验的宏观与产业事实。</div>
          <div class="src">来源：BLS / Fed G.17 / Census 住房开工；当代破产与汽车援助报道</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">变革当选：奥巴马与政治左转</h2>
      <p>2008 年是总统大选年。<strong>巴拉克·奥巴马</strong>形象清新、口才出众，是首位非洲裔主要政党总统候选人，深受少数族裔与年轻选民支持；共和党<strong>约翰·麦凯恩</strong>有显赫军旅与战俘经历，议会生涯以敢言著称，中间选民口碑不差。8 月底共和党大会后，选情一度咬得很紧。<a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>雷曼破产与金融海啸成了气势此消彼长的分水岭：执政共和党支持率下滑；奥巴马把「变革」（change）做成核心口号，把麦凯恩打成「旧势力」。11 月 4 日，奥巴马以二十多年来罕见优势当选；民主党在参众两院亦大胜——众议院约 257 对 178，参议院民主党团约 60 对 40 的优势，使重大法案在共和党集体反对下仍可能强推。经济政策风向预期左转：更严监管、更大政府角色、对华尔街自由化路线的清算。</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Obama08acceptance.jpg" alt="奥巴马 2008 年大选之夜胜选演说" loading="lazy" />
        <figcaption>2008-11-04：奥巴马在芝加哥格兰特公园发表胜选演说——政治时钟与金融时钟在同一个冬天重叠。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        半路杀出的雷曼，改写的不只是资产负债表，还有选票分布。
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn5">
          <strong>⁵ 2008-11-04 奥巴马当选与国会格局</strong>
          巴拉克·奥巴马击败约翰·麦凯恩当选第 44 任总统；民主党在众议院与参议院均扩大优势（公开席位统计常记众议院约 257–178、参议院民主党团约 60–40 量级，含独立人士结盟）。当代分析普遍认为：金融危机显著改变了选情叙事，使「变革」压过「经验」。政策含义对华尔街：监管与税制预期重定价。
          <div class="why">为何重要：本章把「最黑暗」从市场延到政局——下一阶段规则将由新多数书写。</div>
          <div class="src">来源：FEC / 国会席位公开统计；当代选举分析；FCIC 政治背景</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">国之将亡：麦道夫现形</h2>
      <p>2008 年冬天，华尔街走进书名标出的<strong>最黑暗时刻</strong>。12 月 10 日前后，<strong>伯纳德·麦道夫（Bernard Madoff）</strong>规模约数百亿美元的庞氏骗局曝光——作者借用古语感叹：国之将亡，必有妖孽。<a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>读者若跟过前面章节，不会太意外：从花朵基金崩盘到科维尔式欺诈，金融市场的「妖孽」常在流动性退潮时现形。雷曼后去杠杆迫使投资者从各类基金拼命提款，隐藏极深的骗局才失去续命的「新钱」。彼时股市跌至十余年低位，波动前所未有，价格行为像失去了常识。</p>

      <div class="scene">
        潮水退去，才看得见谁在裸泳——有时裸的是骗子，有时是模型。
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ 麦道夫庞氏骗局（2008-12）</strong>
          2008 年 12 月，伯纳德·麦道夫向子嗣承认其资产管理业务实为庞氏骗局，随即被捕；公开估计受损规模常以约 500–650 亿美元量级的名义账户价值被引用（实际净本金损失较低但仍属史诗级）。曝光时点正值赎回潮与流动性枯竭——骗局依赖持续申购，退潮即崩。
          <div class="why">为何重要：把「最黑暗」钉在可核验的丑闻日历上，并呼应全书「流动性退潮见妖孽」母题。</div>
          <div class="src">来源：DOJ / SEC 起诉与新闻稿；当代 NYT/WSJ；法院文件摘要</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">金融奇境：价格挣脱引力</h2>
      <p>危机前，套利者像「地球引力」：产品间不合理价差会被迅速抹平。海啸后，市场仿佛飞入太空——树长在天花板上，家具漂在半空。渔阳戏称所见所闻够写一本《小渔漫游金融奇境》。<a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>
      <p>怪例俯拾即是：十年期国债利率约 3% 时，最优级市政债利率竟可超过 4%——免税muni 相对国债的「倒挂」前所罕见；银行信用风险高于国债，按理 LIBOR 应高于国债利率，可 2008 年冬，三十年 LIBOR 互换利率一度<strong>低于</strong>三十年国债利率；美国出了这么大的事，美元却异常坚挺，澳元、加元等对美元大贬，日元反而升值。阴谋论趁虚而入，作者却给出更冷的解释：<strong>强迫性资本回流</strong>——跨国银行与对冲基金收缩战线，「各回各家」推升融资货币、压垮高收益/大宗商品货币。</p>

      <div class="scene">
        不是美国人更聪明，是资本在逃命——逃命的路径会改写所有相对价格。
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ 危机中的相对价格「奇境」与资本回流</strong>
          2008 年秋冬，高质量市政债相对国债利差异常走阔；部分长期利率互换与国债出现非常规相对定价；美元与日元作为融资/避险货币走强，澳元等高息货币大幅贬值。公开宏观金融文献常以「去杠杆 + 跨境资本回流 + 融资货币升值」解释这些看似违背教科书基本面的汇率与利差现象。
          <div class="why">为何重要：给交易台「看不懂的价格」一个可讲述的资本流动框架，而非神秘主义。</div>
          <div class="src">来源：BIS 2008-12 综述；Fed / Treasury 市场功能报告；当代 FX 与市政债市场评论</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">反伽马地狱：奇异衍生品的教训</h2>
      <p>最依赖数学模型的生意之一是<strong>奇异衍生品</strong>。投行靠定价公式「算出」利润，但要兑现，交易员必须动态对冲；大量期权头寸意味着<strong>反伽马（negative gamma）</strong>——越涨越买、越跌越卖，与 1987 年组合保险同一逻辑，流动性一枯竭就自我强化。<a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>
      <p>鲁西银行市政相关奇异衍生品的负责人布莱恩成了苦主。前几年银行卖出不少挂钩市政指数（SIFMA）的中期票据，渔阳是主要设计者之一——公式假设波动不大、买卖价差可控。海啸后，SIFMA 比例掉期交易成本飙升、波动放大十余倍：比例涨到 90，布莱恩冲过来要买；跌回 80，又要卖——高买低卖，左右挨打。<a class="fn-link" href="#fn9"><sup class="fn">⁹</sup></a></p>
      <p>渔阳由此追问：华尔街模型到底错在哪？直观看，反伽马对流动性要求极高；可转债套利、并购套利等相对价值策略同样假设「想买能买到」。更深一层，无套利理论的两大支柱——无限流动性与可无限融资——在危机里被证伪。他不是模型无用论者，只是看见象牙塔建在沙地上。</p>

      <div class="scene">
        公式在平静的湖面很美；风暴里，伽马会变成绞索。
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn8">
          <strong>⁸ 反伽马对冲与 1987 组合保险平行</strong>
          Negative-gamma 头寸在价格上涨时需买入标的/对冲工具、下跌时需卖出，从而在压力市况放大波动。1987 年组合保险（portfolio insurance）的动态对冲被广泛讨论为助推崩盘的机制之一；2008 年部分利率/信用奇异衍生品与结构性产品的对冲需求，在流动性枯竭时产生类似的「追涨杀跌」压力。
          <div class="why">为何重要：把「金融奇境」从现象描述推进到交易机制——谁在被迫买卖。</div>
          <div class="src">来源：布莱迪报告等对 1987 的公开总结；衍生品风险管理教材综述；危机时期市场功能文献</div>
        </div>
        <div class="fn-item" id="fn9">
          <strong>⁹ SIFMA 市政指数与比率掉期</strong>
          SIFMA（证券业与金融市场协会）市政掉期指数是浮动市政利率的重要基准之一；比率掉期（ratio swap）将市政浮动利率与 LIBOR 等的比率作为交易对象。危机中市政市场流动性恶化、折价扩大，使依赖低波动、窄价差假设的动态对冲成本急剧上升——与书中交易台场景一致的市场微观结构背景。
          <div class="why">为何重要：把作者的市政债券本行，接到「模型失效」的具体产品上。</div>
          <div class="src">来源：SIFMA 指数公开说明；市政市场危机研究；市场惯例手册</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s9">甩掉包袱：田纳西住房债与明天</h2>
      <p>渔阳自己也只是五十步笑百步。2008 年他其实抓到过几次机会——小阳春、雷曼余波里的短债交易——利润以百万美元计；可危机前「收藏」的市政住房债多次减记，吃掉大半战果，流动性又差。他陆续出清一些，最后只剩 2007 年 10 月买入的那只<strong>田纳西住房债</strong>：越觉得「便直」，越不舍得卖；直到承认便直的东西还能更便直，才决定放手。<a class="fn-link" href="#fn10"><sup class="fn">¹⁰</sup></a></p>
      <p>他请老熟人胡优推销。胡优在贝尔斯登事件里伤得很重，却仍在摩根大通旗下跑市场，开口就是「6.00% 收益率，不还价。」渔阳想起一年前的对话，半开玩笑问要不要趁客户没改主意快卖；胡优笑说这回不好说，也许市场要反转，倒怕你改主意——「忘记不愉快的过去总是个好主意。」</p>
      <p>渔阳接受建议，甩掉包袱。在 2008 年冬天那个最黑暗的时刻，他不知道曙光何时到来，却想起《乱世佳人》的收束：<strong>明天又是新的一天</strong>。全书下一章，正是「曙光初现」——第三部分金融海啸在此收束，第四部分峰回路转即将起笔。</p>

      <div class="scene">
        最黑暗的时刻不是结局；它是愿意卖掉错误、好看见明天的那一秒。
      </div>

      <div class="footnotes" id="fn-block-9">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn10">
          <strong>¹⁰ 住房类市政债流动性与「便宜还可以更便宜」</strong>
          危机中许多住房相关市政与项目收入债出现深度折价，同时二级市场买卖价差急剧扩大，持仓难以按「模型公允」变现。行为金融与交易实务都强调：流动性枯竭时，账面便直不等于可执行退出；止损与「沉没成本」决策成为生存技能。本章用一笔具体债券收束交易员视角，并过渡到 §19。
          <div class="why">为何重要：把宏观黑暗拉回作者本人的头寸决策——故事导读的「人」回到台前。</div>
          <div class="src">来源：市政市场危机流动性研究；本书公开试读情节节拍（改写）；交易实务通识</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>人物关系 / 时间线 / 知识图谱</h2>

        <div class="mermaid-wrap">
          <div class="caption">人物与机构关系图：从全球注资到交易台奇境</div>
          <div class="mermaid">
flowchart LR
  GOV[各国政府注资/担保] --> BANKS[跨国银行各回各家]
  FED[美联储扩表·便利工具] --> CREDIT[替代失灵信贷管道]
  BANKS -->|去杠杆| FREEZE[信贷冻结]
  FREEZE --> REAL[实体衰退·失业]
  REAL --> VOTE[奥巴马当选·政策左转]
  LIQ[流动性退潮] --> MADOFF[麦道夫现形]
  LIQ --> WONDER[相对价格奇境]
  FLOW[跨境资本回流] --> WONDER
  YY[渔阳·鲁西] --> DES[SIFMA奇异票据设计]
  BRIAN[布莱恩·反伽马对冲] --> DES
  YY --> BOND[田纳西住房债止损]
  HU[胡优·销售] --> BOND
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">时间线：最黑暗的时刻（2008-10 → 2008-12）</div>
          <div class="mermaid">
timeline
    title 最黑暗的时刻
    2008-10中 : 全球银行注资潮·信贷仍冻
    2008-10至11 : 美联储扩表·实体指标塌陷
    2008-11-04 : 奥巴马当选·民主党大胜
    2008-11至12 : 金融奇境·模型失效
    2008-12-10 : 麦道夫骗局曝光
    2008冬 : 田纳西债出手·望向曙光
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">知识图谱：为何价格「飞入太空」</div>
          <div class="mermaid">
flowchart TB
  SHOCK[雷曼+破净+信贷冻结] --> DELEV[强制去杠杆]
  DELEV --> HOME[资本各回各家]
  HOME --> FX[融资货币升值·高息货币贬值]
  DELEV --> SPREAD[muni/国债等相对价格失序]
  MODEL[无套利假设] -->|无限流动性·无限融资| FAIL[假设证伪]
  EXOTIC[奇异衍生品] --> NEGG[反伽马追涨杀跌]
  NEGG --> FAIL
  FAIL --> WONDER[金融奇境]
  FX --> WONDER
  SPREAD --> WONDER
  WONDER --> NEXT[§19 曙光初现]
          </div>
        </div>
      </section>
'''

EN_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/New_York_Stock_Exchange_Building.jpg" alt="New York Stock Exchange Building" loading="lazy" />
        <figcaption>The New York Stock Exchange Building—in the autumn and winter of 2008, the numbers on the screens felt less like a market than a shock monitor. Source: Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">Everyone goes home: global recapitalizations</h2>
      <p>After §17—TARP authorized, the nine largest U.S. banks marched into capital injections—from <strong>mid-October 2008</strong> governments everywhere raced to rescue “their” banks with equity and debt guarantees. Before the crisis, cross-border banking giants posed as corporate world citizens; in the tsunami they could only <strong>go home and find mother</strong>.<a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>Public records show the Netherlands injecting capital on the order of tens of billions into ING and peers; Switzerland injecting into UBS and absorbing troubled assets; France injecting more than €10 billion into BNP Paribas, Société Générale and others. The U.S. and U.K. plans were §17’s story; now the whole world shared one stage—and capital suddenly rediscovered nationality.</p>

      <div class="side-panel">
        <h3 class="panel-title">Chapter anchors · mid-Oct 2008 → Dec 2008</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">mid-Oct</div><div class="ev">Global capital/guarantees · credit still frozen</div></div>
          <div class="event-card"><div class="yr">Oct–Nov</div><div class="ev">Fed expands sheet · real recession · election</div></div>
          <div class="event-card"><div class="yr">Nov 4</div><div class="ev">Obama wins · Democratic sweep</div></div>
          <div class="event-card"><div class="yr">Dec 10</div><div class="ev">Madoff unmasked · Financial Wonderland</div></div>
        </div>
      </div>

      <div class="scene">
        A passport can save a bank’s life; it cannot cancel the inertia of deleveraging.
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn1">
          <strong>¹ Europe’s October 2008 bank-capital wave</strong>
          After the U.K.’s 8 Oct recapitalization/guarantee package and the U.S. 14 Oct Capital Purchase Program announcement, the Netherlands, Switzerland, France and others announced equity, guarantees, or asset backstops for domestic champions (ING, UBS, BNP/SocGen among those commonly cited). Cross-border banks were renationalized by necessity—global branding yielded to home-country fiscal backing.
          <div class="why">Why it matters: TARP’s passage did not end global panic—rescues ran in parallel while deleveraging kept rolling.</div>
          <div class="src">Source: BIS Quarterly Review Dec 2008; national Treasury/central-bank releases; FCIC international context</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">The blood stops: credit freeze and shock economy</h2>
      <p>Emergency rescues kept the system from collapsing on the spot; they could not stop <strong>deleveraging</strong>. U.S. capital-market funding nearly shut: equities and bonds hard to place, once-reliable <strong>commercial paper</strong> shriveling; ABS issuance that intermediate consumer credit almost halted. Shadow banking failed; traditional banks either took direct hits or tightened lending to pre-empt recession losses.<a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>When the banking system stopped “making blood,” a highly financialized U.S. economy went into <strong>shock</strong>: households could not buy homes or cars, firms could not roll working capital, activity fell, unemployment rose, consumption fell again. People feared not only recession but depression. Aftershocks of money-fund break-the-buck and the House-rejection crash now stretched into a longer credit winter.</p>

      <div class="scene">
        Saving a bank’s charter is not the same as saving its willingness to lend.
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn2">
          <strong>² CP freeze, shadow banking, and the money-fund aftershock</strong>
          After Lehman, the Reserve Primary Fund broke the buck on 16 Sep 2008, sparking money-fund redemptions that slammed commercial paper. Into October, ABCP and parts of ABS issuance nearly stopped; wholesale-funding-dependent firms were forced to delever. Crisis histories treat the credit freeze as the main bridge from market panic to real-economy shock.
          <div class="why">Why it matters: translates desk panic into an economy that cannot circulate credit—this chapter leaves Wall Street for Main Street.</div>
          <div class="src">Source: Yale YPFS Reserve Primary case; FRASER; BIS/Fed CP and ABS narratives</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">Bernanke learned: the Fed expands its balance sheet</h2>
      <p>In the 1930s the Fed wrongly tightened money amid banking stress—a policy error historians blame for deepening the Depression. In 2008 the Fed “had learned”: Depression scholar <strong>Bernanke</strong> cut rates, expanded base money, and stretched the lender-of-last-resort role—using new <strong>facilities</strong> to pipe credit toward the real economy when banks would not.<a class="fn-link" href="#fn3"><sup class="fn">³</sup></a></p>
      <p>Public tools included buying short-term commercial paper to keep firms liquid; buying mortgage-backed securities to support housing finance; supporting securitizations of auto and credit-card loans that underwrite the bulk of consumption. The Fed’s balance sheet ballooned, cushioning bank deleveraging. Treasury also widened capital injections beyond the giants. The author’s judgment: these extraordinary steps helped America avoid a 1929-style depression—even as a <strong>severe recession</strong> still arrived.</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Marriner_S._Eccles_Federal_Reserve_Board_Building.jpg" alt="Eccles Federal Reserve Board Building" loading="lazy" />
        <figcaption>The Fed’s Eccles Building in Washington—where Bernanke’s team widened the lender-of-last-resort net. Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        The Depression textbook became an operations manual: this time, the central bank filled the pipes first.
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn3">
          <strong>³ Fed crisis facilities and balance-sheet expansion</strong>
          In autumn–winter 2008 the Fed, beyond rate cuts, launched or expanded facilities including the Commercial Paper Funding Facility (CPFF), term auction tools, large-scale purchases of agency MBS and related debt, and financing support for consumer/small-business ABS (the policy lineage of TALF). Fed total assets rose sharply. The aim was to replace broken private intermediation, not merely to “bail out banks.”
          <div class="why">Why it matters: capital injections alone were not enough—the central bank had to reconnect real-economy funding pipes.</div>
          <div class="src">Source: Federal Reserve crisis-tool chronologies; FRASER; Bernanke speeches; FCIC</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">Severe recession: the real economy collapses</h2>
      <p>Industrial output posted postwar-record declines; housing starts plunged on the order of ~70% year-over-year; auto sales per capita sank to postwar lows, with GM and Chrysler near existential crisis. Retailers such as Circuit City and Linens 'n Things entered bankruptcy. Layoffs accelerated—public narratives put U.S. job losses around <strong>600,000</strong> in September–October alone.<a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>For Yuyang, basis points on a screen suddenly mapped onto neighbors out of work, storefronts dark, Detroit on the brink. The tsunami was no longer a Wall Street civil war.</p>

      <div class="scene">
        When screen spreads start matching factory smokestacks, a crisis earns the name tsunami.
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ Late-2008 real indicators and auto/retail shock</strong>
          U.S. industrial production, housing starts, and auto sales deteriorated sharply in H2 2008; GM and Chrysler later required government aid/bankruptcy restructuring. Circuit City filed for bankruptcy protection in late 2008; Linens 'n Things also failed around the crisis. BLS data show large net job losses that autumn. These real footnotes are the downstream evidence of the credit freeze.
          <div class="why">Why it matters: anchors “darkest hour” rhetoric to verifiable macro and industry facts.</div>
          <div class="src">Source: BLS / Fed G.17 / Census housing starts; contemporary bankruptcy and auto-aid coverage</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">Change wins: Obama and the leftward turn</h2>
      <p>2008 was a presidential year. <strong>Barack Obama</strong>—fresh, eloquent, the first African American major-party nominee—drew minority and young voters; Republican <strong>John McCain</strong> brought a storied military and POW record and a Senate reputation for candor that played well with independents. After the late-August Republican convention, the race tightened.<a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>Lehman and the financial tsunami became the momentum watershed: the incumbent Republican brand collapsed in the polls; Obama made “change” the core slogan and cast McCain as the old guard. On 4 November Obama won by the widest margin in decades; Democrats also swept Congress—House roughly 257–178, Senate Democratic caucus about 60–40—enough to force major bills past unified Republican opposition. Economic policy was expected to turn left: heavier regulation, a larger state role, a reckoning with Wall Street liberalization.</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Obama08acceptance.jpg" alt="Obama election-night acceptance speech 2008" loading="lazy" />
        <figcaption>4 Nov 2008: Obama’s victory speech in Chicago’s Grant Park—political and financial clocks overlapping in one winter. Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        Lehman, arriving mid-campaign, rewrote more than balance sheets—it rewrote the electoral map.
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn5">
          <strong>⁵ 4 Nov 2008: Obama elected and the congressional map</strong>
          Barack Obama defeated John McCain to become the 44th president; Democrats expanded House and Senate majorities (commonly cited ~257–178 in the House and a ~60–40 Democratic Senate caucus including allied independents). Contemporary analysis held that the financial crisis reshaped the race toward “change” over “experience.” For Wall Street, regulation and tax expectations repriced overnight.
          <div class="why">Why it matters: extends “darkest hour” from markets into politics—the next rulebook would be written by a new majority.</div>
          <div class="src">Source: FEC / congressional seat tallies; contemporary election analysis; FCIC political background</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">When a state falters: Madoff unmasked</h2>
      <p>In the winter of 2008 Wall Street entered the hour named in the chapter title. Around <strong>10 December</strong>, <strong>Bernard Madoff</strong>’s multi-tens-of-billions Ponzi scheme broke into the open—the author borrows the old saying: when a state falters, demons appear.<a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>Readers of earlier chapters should not be shocked: from the flower-fund collapse to Kerviel-style fraud, market demons often surface when liquidity ebbs. Post-Lehman deleveraging forced redemptions across funds; only then did a deeply hidden fraud lose the “new money” that kept it alive. Equities sat at multi-year lows; volatility was unprecedented; prices seemed to abandon common sense.</p>

      <div class="scene">
        Only when the tide goes out do you see who swam naked—sometimes a fraudster, sometimes a model.
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ The Madoff Ponzi scheme (Dec 2008)</strong>
          In December 2008 Bernard Madoff confessed to his sons that his asset-management business was a Ponzi scheme and was arrested; public estimates often cite ~$50–65 billion of nominal account value (net principal losses lower but still historic). The reveal coincided with redemption pressure and liquidity drought—Ponzi schemes die when inflows stop.
          <div class="why">Why it matters: pins “darkest hour” to a verifiable scandal date and echoes the book’s motif that ebb tides reveal demons.</div>
          <div class="src">Source: DOJ/SEC complaints and releases; contemporary NYT/WSJ; court-document summaries</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">Financial Wonderland: prices escape gravity</h2>
      <p>Before the crisis, arbitrageurs acted like gravity: odd relative prices were stamped flat. After the tsunami, markets seemed to float into space—trees on the ceiling, furniture in mid-air. Yuyang jokes that what he saw could fill a volume called <em>Yuyang in Financial Wonderland</em>.<a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>
      <p>Oddities piled up: with 10-year Treasuries near 3%, top-grade munis could yield over 4%—a rare “wrong-way” tax-exempt spread; bank credit risk should keep LIBOR above Treasuries, yet that winter 30-year LIBOR swap rates traded <strong>below</strong> 30-year Treasuries; America was the epicenter, yet the dollar stayed strong while AUD and CAD plunged and the yen rose. Conspiracy theories bloomed; the colder explanation was <strong>forced capital repatriation</strong>—global banks and hedge funds pulling home, lifting funding currencies and crushing high-carry ones.</p>

      <div class="scene">
        Americans were not suddenly geniuses—capital was fleeing, and flight paths rewrite every relative price.
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ Crisis relative-price “Wonderland” and capital repatriation</strong>
          In autumn–winter 2008, high-grade munis cheapened sharply versus Treasuries; some long-dated swap-versus-Treasury relationships inverted; the dollar and yen strengthened as funding/safe-haven currencies while high-yield commodity currencies sold off. Macro-finance accounts emphasize deleveraging plus cross-border repatriation as the mechanism behind textbook-defying FX and spread moves.
          <div class="why">Why it matters: gives desk “nonsense prices” a capital-flow story instead of mysticism.</div>
          <div class="src">Source: BIS Dec 2008 overview; Fed/Treasury market-function reports; contemporary FX and muni commentary</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">Negative-gamma hell: exotic derivatives' lesson</h2>
      <p>Among the most model-dependent businesses were <strong>exotic derivatives</strong>. Banks booked model “profits,” but realizing them required dynamic hedging; option-heavy books meant <strong>negative gamma</strong>—buy as prices rise, sell as they fall, the same logic as 1987 portfolio insurance, self-reinforcing once liquidity dies.<a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>
      <p>Brian, who ran Lucy Bank’s muni-linked exotics, became the punchline. Years earlier the bank had sold medium-term notes tied to the SIFMA municipal index—Yuyang among the designers—assuming modest volatility and manageable bid-offer. After the tsunami, SIFMA ratio-swap costs exploded and volatility jumped more than tenfold: ratio to 90, Brian rushed in to buy; back to 80, he had to sell—buying high, selling low, hit from both sides.<a class="fn-link" href="#fn9"><sup class="fn">⁹</sup></a></p>
      <p>Yuyang asked where Wall Street’s models failed. Visibly, negative-gamma needs abundant liquidity; convertible arb, merger arb, and other relative-value books make the same bet. Deeper still, no-arbitrage theory’s twin pillars—infinite liquidity and unlimited leverage—were falsified in the crisis. He is no anti-model zealot; he simply saw the ivory tower standing on sand.</p>

      <div class="scene">
        Formulas look elegant on a calm lake; in a storm, gamma becomes a noose.
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn8">
          <strong>⁸ Negative-gamma hedging and the 1987 portfolio-insurance parallel</strong>
          Negative-gamma positions require buying into strength and selling into weakness, amplifying moves under stress. Dynamic hedging behind 1987 portfolio insurance is widely discussed as a crash accelerant; in 2008, hedging demand from some rate/credit exotics and structured products produced similar chase-flow pressure once liquidity vanished.
          <div class="why">Why it matters: pushes Wonderland from phenomenology to mechanism—who is forced to trade.</div>
          <div class="src">Source: Brady Report summaries of 1987; derivatives risk texts; crisis market-function literature</div>
        </div>
        <div class="fn-item" id="fn9">
          <strong>⁹ The SIFMA municipal index and ratio swaps</strong>
          The SIFMA Municipal Swap Index is a key floating muni-rate benchmark; ratio swaps trade the ratio of that rate to LIBOR (or similar). In the crisis, muni liquidity worsened and discounts widened, blowing up dynamic-hedging costs that assumed low vol and tight spreads—the market-microstructure backdrop to the desk scenes.
          <div class="why">Why it matters: ties the author’s muni franchise to a concrete product where models broke.</div>
          <div class="src">Source: SIFMA index documentation; muni-market crisis research; market-convention manuals</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s9">Drop the bag: Tennessee housing bond and tomorrow</h2>
      <p>Yuyang himself was only fifty steps from Brian’s hundred. In 2008 he caught real opportunities—the false spring, short-bond trades in the Lehman aftershock—profits in the millions; yet pre-crisis “collector” housing munis marked down again and again, erasing most of the score, and liquidity was awful. He sold some when he could; last left was a <strong>Tennessee housing bond</strong> bought in October 2007: the cheaper it looked, the harder to sell—until he admitted cheap can get cheaper, and let go.<a class="fn-link" href="#fn10"><sup class="fn">¹⁰</sup></a></p>
      <p>He asked old contact Hu You to place it. Hu You had been mauled in the Bear Stearns affair yet still worked the market under JPMorgan, opening with “6.00% yield, no haggle.” Yuyang remembered a year-earlier exchange and joked about selling before the client changed his mind; Hu You laughed that this time it was unclear—maybe the market was about to turn, and he feared Yuyang would change his mind—“forgetting an unhappy past is usually a good idea.”</p>
      <p>Yuyang took the advice and dropped the bag. In that darkest winter hour he did not know when dawn would come, yet he recalled <em>Gone with the Wind</em>: <strong>tomorrow is another day</strong>. The next chapter is “First Light”—Part 3’s financial tsunami closes here; Part 4’s turn in the road begins.</p>

      <div class="scene">
        The darkest hour is not an ending; it is the second you are willing to sell the mistake so you can see tomorrow.
      </div>

      <div class="footnotes" id="fn-block-9">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn10">
          <strong>¹⁰ Housing-muni liquidity and “cheap can get cheaper”</strong>
          In the crisis many housing-related munis and project-revenue bonds traded at deep discounts while secondary bid-offer exploded, so model “fair value” was not an executable exit. Behavioral finance and desk practice agree: in a liquidity drought, paper cheapness ≠ ability to sell; cutting losses and ignoring sunk cost become survival skills. The chapter closes the trader’s arc on one bond and hands the baton to §19.
          <div class="why">Why it matters: pulls macro darkness back to the author’s own position decision—the human returns to center stage.</div>
          <div class="src">Source: muni-market crisis liquidity research; public trial-read beat alignment (rewrite); trading practice</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>Relationships / timeline / knowledge graph</h2>

        <div class="mermaid-wrap">
          <div class="caption">People and institutions: from global capital to desk Wonderland</div>
          <div class="mermaid">
flowchart LR
  GOV[Gov capital/guarantees] --> BANKS[Banks go home]
  FED[Fed sheet + facilities] --> CREDIT[Replace broken credit pipes]
  BANKS -->|delever| FREEZE[Credit freeze]
  FREEZE --> REAL[Real recession · jobs]
  REAL --> VOTE[Obama win · policy left]
  LIQ[Liquidity ebb] --> MADOFF[Madoff unmasked]
  LIQ --> WONDER[Relative-price Wonderland]
  FLOW[Cross-border repatriation] --> WONDER
  YY[Yuyang · Lucy] --> DES[SIFMA exotic note design]
  BRIAN[Brian · neg-gamma hedge] --> DES
  YY --> BOND[Tennessee housing stop-loss]
  HU[Hu You · sales] --> BOND
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Timeline: The Darkest Hour (Oct → Dec 2008)</div>
          <div class="mermaid">
timeline
    title The Darkest Hour
    mid-Oct 2008 : Global bank capital wave · credit still frozen
    Oct-Nov 2008 : Fed expands sheet · real indicators collapse
    2008-11-04 : Obama elected · Democratic sweep
    Nov-Dec 2008 : Financial Wonderland · models fail
    2008-12-10 : Madoff scheme exposed
    Winter 2008 : Tennessee bond sold · looking toward dawn
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Knowledge graph: why prices “flew into space”</div>
          <div class="mermaid">
flowchart TB
  SHOCK[Lehman + break-buck + credit freeze] --> DELEV[Forced deleveraging]
  DELEV --> HOME[Capital goes home]
  HOME --> FX[Funding FX up · high-carry FX down]
  DELEV --> SPREAD[Muni/Treasury relative disorder]
  MODEL[No-arbitrage assumptions] -->|infinite liquidity · infinite leverage| FAIL[Assumptions falsified]
  EXOTIC[Exotic derivatives] --> NEGG[Neg-gamma chase flows]
  NEGG --> FAIL
  FAIL --> WONDER[Financial Wonderland]
  FX --> WONDER
  SPREAD --> WONDER
  WONDER --> NEXT[§19 First Light]
          </div>
        </div>
      </section>
'''

SOURCES = """# Sources — 《乱世华尔街》第十八章「最黑暗的时刻」 enrichment

Research and image sources used for footnotes, side panels, and figures. Facts were cross-checked against public pages; footnotes cite source *names* in the HTML. Book-side rhetoric (global banks “go home,” credit-freeze shock economy, Bernanke facilities, recession/auto/retail collapse, Obama election watershed, Madoff as ebb-tide demon, Financial Wonderland relative prices, negative-gamma/SIFMA desk pain, Tennessee housing stop-loss and *Gone with the Wind* close toward §19) is rewrite/guide aligned to public trial-read *beats*; public events are off-book supplements. Not a verbatim reproduction of the copyrighted book.

## Images (Wikimedia Commons / Special:FilePath)

| Subject | Wikimedia path | Notes |
|---|---|---|
| New York Stock Exchange Building | `File:New_York_Stock_Exchange_Building.jpg` | Chapter opener; equity/credit panic stage |
| Marriner S. Eccles Federal Reserve Board Building | `File:Marriner_S._Eccles_Federal_Reserve_Board_Building.jpg` | Fed facilities / balance-sheet expansion beat |
| Obama election-night acceptance | `File:Obama08acceptance.jpg` | 4 Nov 2008 Grant Park victory speech |

HTML embeds via `https://commons.wikimedia.org/wiki/Special:FilePath/...` so the GitHub Pages push stays text-sized.

## Fact / footnote research URLs

### Global recapitalizations and credit freeze
- BIS Quarterly Review, December 2008 (overview of policy actions and market stress)
- HM Treasury / U.S. Treasury October 2008 bank capital announcements (bridge from §17)
- Yale YPFS: Reserve Primary Fund break-the-buck case (money-market → CP channel)

### Fed facilities and real economy
- Federal Reserve crisis facility chronologies (CPFF, MBS purchases, TALF lineage)
- BLS employment; Fed G.17 industrial production; Census housing starts
- Contemporary coverage of GM/Chrysler stress; Circuit City bankruptcy

### Politics and Madoff
- 4 Nov 2008 election results / congressional seat tallies
- DOJ/SEC materials on Bernard Madoff arrest and Ponzi scheme (Dec 2008)

### Wonderland prices and model failure
- BIS / Fed market-function discussions of FX repatriation and funding currencies
- Brady Report tradition on 1987 portfolio insurance (negative-gamma parallel)
- SIFMA Municipal Swap Index documentation; muni liquidity stress notes

### Book chapter framing (public trial / catalog only — rewrite, do not paste)
- Public TOC: §18「最黑暗的时刻」 closes Part 3 金融海啸 (§13–§18), before §19「曙光初现」
- Public trial-read page (FX110 `/book/read/597-50232`) used only for beat alignment: global recaps → credit freeze/shock → Fed facilities → real recession → Obama win → Madoff → Wonderland prices/capital flows → exotic neg-gamma/SIFMA → Tennessee bond / tomorrow → foreshadow Part 4

## Delivery notes
- Full self-contained HTML (`darkest-hour-zh.html` / `darkest-hour-en.html`) — no `document.write` loaders
- Story rewrite for reading along; official edition required for the complete copyrighted text
- Home links use `../../../index.html` from `books/luan-shi-wall-street/ch18/`
"""

def main():
    zh = page(
        "zh",
        "《乱世华尔街》第18集：最黑暗的时刻",
        "故事导读 · 据公开试读改写 · 场外研究补充",
        "最黑暗的时刻",
        "《乱世华尔街》第十八章「最黑暗的时刻」· 渔阳 · 故事改写 + 脚注研究",
        "下面按作者经历与公开时间线讲述本章故事，用自己的话改写，方便跟读；不是全书/全章原文照搬。脚注、配图与知识图谱为场外公开资料补充。完整内容请读正版。",
        ZH_TOC,
        "CHAPTER EIGHTEEN · 最黑暗的时刻",
        ZH_BODY,
        "《乱世华尔街》· 渔阳 · 第十八章故事导读（原创改写）",
    )
    en = page(
        "en",
        "Chaos on Wall Street §18: The Darkest Hour",
        "Story guide · rewritten from public trial beats · off-book research",
        "The Darkest Hour",
        "Chaos on Wall Street, Chapter 18 “The Darkest Hour” · Yuyang · story rewrite + footnote research",
        "The narrative below retells this chapter’s beats in original wording for guided reading; it is not a verbatim copy of the copyrighted book. Footnotes, figures, and diagrams add public off-book research. Please support the official edition for the full text.",
        EN_TOC,
        "CHAPTER EIGHTEEN · The Darkest Hour",
        EN_BODY,
        "Chaos on Wall Street · Yuyang · Chapter 18 story guide (original rewrite)",
    )
    (DIR / "darkest-hour-zh.html").write_text(zh, encoding="utf-8")
    (DIR / "darkest-hour-en.html").write_text(en, encoding="utf-8")
    (DIR / "SOURCES.md").write_text(SOURCES, encoding="utf-8")
    print("Wrote", DIR / "darkest-hour-zh.html", len(zh))
    print("Wrote", DIR / "darkest-hour-en.html", len(en))
    print("Wrote", DIR / "SOURCES.md", len(SOURCES))

if __name__ == "__main__":
    main()
