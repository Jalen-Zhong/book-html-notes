#!/usr/bin/env python3
"""Build full self-contained ZH/EN HTML for ch20 圣经故事 / Bible Stories."""
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
        '<a class="active" href="bible-stories-zh.html">中文</a>\n'
        '        <a href="bible-stories-en.html">English</a>\n'
        '        ' + home
        if lang == "zh" else
        '<a href="bible-stories-zh.html">中文</a>\n'
        '        <a class="active" href="bible-stories-en.html">English</a>\n'
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
    ("s1", "反攻集结号：头寸从空仓到加码"),
    ("s2", "马太福音：三个仆人与金币"),
    ("s3", "索罗斯式鼓劲：关键时刻下大注"),
    ("s4", "建设美国债券：给钱不如给政策"),
    ("s5", "新游戏开盘：BAB 被热捧"),
    ("s6", "加州综合债：申购五千万只拿两百万"),
    ("s7", "福尔摩斯推理：债券都给了谁"),
    ("s8", "动量交易：该出手时就出手"),
    ("diagrams", "人物关系 / 时间线 / 知识图谱"),
]

EN_TOC = [
    ("s1", "Assembly call: from cash to size"),
    ("s2", "Matthew 25: three servants and the coins"),
    ("s3", "Soros-style push: size when it matters"),
    ("s4", "Build America Bonds: policy over cash"),
    ("s5", "New game opens: BABs get chased"),
    ("s6", "California GO: bid 50, get 2"),
    ("s7", "Holmes on the Street: who got the bonds?"),
    ("s8", "Momentum: when it's time to swing"),
    ("diagrams", "Relationships / timeline / knowledge graph"),
]

ZH_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Charging_Bull_statue.jpg" alt="华尔街铜牛" loading="lazy" />
        <figcaption>华尔街铜牛——危机后的「公牛」叙事尚未坐实；本章讲的是：曙光之后，敢不敢把金币从土里挖出来。来源：Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">反攻集结号：头寸从空仓到加码</h2>
      <p>承接 §19：量化宽松的消息已经传开，鱼肚白变成了「曙光」。渔阳在「战壕」里猫了一整个冬天——基本空仓，偶尔打一枪冷枪。现在风向真要变了，他觉得该出击了。</p>
      <p>他兴冲冲向文森报告：准备把头寸加到大约<strong>五千万美元</strong>。文森却摇头：「才五千万？一个亿还差不多。」危机前他们玩过十亿级债券头寸，那时波动小，账上输赢也不吓人；危机后债券像股票、股票像过山车，波动放大数倍——渔阳觉得五千万已经保守，文森却开口一个亿，活像「人有多大胆，地有多大产」。<a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>渔阳搬出上级口径：严格控风险、压低头寸；又自评：去年那么糟的市，自己还保本没赔。文森再摇头：去年许多人成了惊弓之鸟，不敢再冒险——「此一时也，彼一时也，你该换脑子。」</p>

      <div class="side-panel">
        <h3 class="panel-title">本章时间锚点 · 2009 春 → 4 月</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">QE 后</div><div class="ev">空仓→拟加仓 5千万</div></div>
          <div class="event-card"><div class="yr">圣经</div><div class="ev">马太福音才干寓言</div></div>
          <div class="event-card"><div class="yr">4 月初</div><div class="ev">BAB 登场·热捧</div></div>
          <div class="event-card"><div class="yr">4 月中</div><div class="ev">加州 GO·动量出击</div></div>
        </div>
      </div>

      <div class="scene">
        曙光不是保险箱；它只是问你：还要把金币埋在土里吗？
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn1">
          <strong>¹ 危机前后波动率与头寸尺度</strong>
          2008–09 年信用与利率市场波动显著抬升：高评级利差、VIX 与债券日波动相对危机前「大缓和」时代大幅放大。同样名义头寸，P&amp;L 波动可放大数倍——因此「以前玩十亿、现在谈五千万」在风控上并不矛盾。公开危机史常强调：去杠杆与风险限额收紧后，交易员要在「保本惯性」与「政策底后的机会」之间重新定尺。
          <div class="why">为何重要：把 §19 的政策曙光落到交易台决策——头寸大小本身就是本章冲突的起点。</div>
          <div class="src">来源：公开波动率与信用利差序列；FCIC / 美联储危机回顾</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">马太福音：三个仆人与金币</h2>
      <p>接着，文森讲了一个《圣经》故事——<strong>《新约·马太福音》第 25 章</strong>「才干／金币」寓言。<a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>一位严厉的主人要出远门，按能力把财产交给三个仆人：甲五个金币，乙两个，丙一个。甲拿五个去做生意，又赚五个；乙也赚回两个；丙怕赔、怕挨骂，把唯一那个金币<strong>埋进地里</strong>。主人回来，夸甲、夸乙，却对捧出「原物奉还」的丙大怒：既然知道我苛刻，就该拿去放贷挣利息——现在连你这唯一的金币也要夺走，交给会赚钱的甲。</p>
      <p>渔阳一愣：这不就是投行吗？管理层像那位主人——又要你赚钱，又不让你乱冒风险；而自己像胆小的<strong>仆人丙</strong>，一心保本、把金币埋土里。丛林式竞争里，畏缩的交易员没有前途；看准机会敢出手的人，才能赢得信任和更大权限。他佩服文森用典恰到好处，立刻表态：抛弃「丙式思维」，向甲学习——该出手时就出手。</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Parable_of_the_Talents.jpg" alt="才干寓言画作" loading="lazy" />
        <figcaption>才干／金币寓言的古典图像传统——埋在土里的那枚，在华尔街口语里常被翻译成「空仓保本」。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        保本不是美德本身；在错误的季节把金币埋进土里，才是真正的浪费。
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn2">
          <strong>² 《马太福音》25:14–30「才干寓言」（Parable of the Talents）</strong>
          经文大意：主人按仆人能力分派「他连得」（talent，一笔巨额货币单位），勤勉交易者受奖赏，把银子埋藏者受责罚；主题常被读作「受托责任」与「机会成本」。公开试读中作者以「金币／甲乙丙」口语复述，并映射投行激励：既要回报又要控险——埋金币＝过度保本。此处为场外圣经背景 + 章节寓意改写，非经文或书稿照搬。
          <div class="why">为何重要：本章标题「圣经故事」的核心隐喻；后面 BAB 交易是「挖出金币」的实操答卷。</div>
          <div class="src">来源：马太福音 25 公开译本；圣经百科词条 Parable of the Talents</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">索罗斯式鼓劲：关键时刻下大注</h2>
      <p>这件事让渔阳想起华尔街轶闻：1992 年索罗斯量子基金做空英镑，最终迫使英镑贬值并退出欧洲汇率机制，一役成名。公开叙事里，先嗅到英镑弱点的往往是基金经理朱肯米勒；索罗斯的「贡献」是在关键时刻把头寸<strong>加到足够大</strong>——据说朱肯米勒汇报一笔成功交易后，索氏不屑：「才十亿？这也叫头寸？马上翻倍！」<a class="fn-link" href="#fn3"><sup class="fn">³</sup></a></p>
      <p>文森讲圣经，与索罗斯鼓劲朱肯米勒异曲同工。而渔阳觉得：自己也撞上了某种「英镑式」机会——只是战场换成了 2009 年春天的市政债。</p>

      <div class="scene">
        洞见人人可能有；敢在拐点把尺寸加到位的人，才少。
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn3">
          <strong>³ 1992 年「黑色星期三」与索罗斯／朱肯米勒</strong>
          1992-09-16，英镑在投机压力下退出欧洲汇率机制（ERM）；乔治·索罗斯的量子基金因做空英镑获得巨额利润并广为人知。公开采访与回忆常提到斯坦利·朱肯米勒在策略形成中的角色，以及索罗斯推动加大仓位的管理风格。数字与对话细节在坊间版本不一，脚注只锚定「关键时刻放大正确头寸」这一被广泛复述的主题。
          <div class="why">为何重要：给「抛弃丙式思维」一个华尔街同构案例——尺寸是策略的一部分。</div>
          <div class="src">来源：英格兰银行／当代报道；公开金融史与当事人访谈摘要</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">建设美国债券：给钱不如给政策</h2>
      <p>2009 年春，市政债市场出现新生事物：<strong>建设美国债券</strong>（Build America Bonds，BAB）。传统市政债利息多免联邦所得税，买家以高税率富人、保险公司为主；退休基金、海外资金往往不碰——它们本就不交或少交美国所得税，不会为「免税但票息偏低」买单。金融危机后富人资产缩水、杠杆套利者撤退，市政债需求塌、利率攀升；地方政府赤字叠高息，只得向联邦求援。<a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>联邦的招数是「给钱不如给政策」：BAB <strong>应税</strong>，但联邦直接补贴发行人约 <strong>35%</strong> 的利息支出。效果像四两拨千斤——没有免税标签、票息更高，养老金与海外资金成了潜在买家；发行人拿补贴后实际融资成本常低于传统免税债；联邦付补贴，却能从利息税收回一部分，净成本远小于直接拨款。公开估算常把「花小钱撬动大规模州地融资」写成 BAB 的政策卖点。</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/United_States_Department_of_the_Treasury_Seal.svg" alt="美国财政部徽标" loading="lazy" />
        <figcaption>美国财政部——BAB 的利息直补机制，把「刺激」写进了市政融资管道。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        危机里最贵的往往不是钱，而是一条能把新买家请进场的规则。
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ Build America Bonds（BAB）与 35% 直补</strong>
          BAB 由 2009 年《美国复苏与再投资法案》（ARRA）创设：应税市政债，发行人可选择接受财政部对利息的直接补贴（Direct Pay，常见为应付利息的 35%）或税收抵免结构。2009–2010 年 BAB 显著扩大了市政债买家结构（保险、养老金、海外等），并压低部分发行人净融资成本。计划后于 2010 年末到期停止新发。脚注用公开项目规则；书中「花小钱办大事」的算术为作者导读改写。
          <div class="why">为何重要：本章「新游戏」的制度底座——没有 BAB，就没有后文的动量战场。</div>
          <div class="src">来源：U.S. Treasury / IRS BAB 说明；MSRB 早期 BAB 市场报告；ARRA 文本</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">新游戏开盘：BAB 被热捧</h2>
      <p>BAB 将开闸的消息一出，渔阳意识到：机构最爱分散风险；地方政府运营逻辑与企业不同，又有征税权，市政敞口本是分散与增厚回报的好工具——只是传统免税低息把许多买家挡在门外。有了 BAB，他脑补出董事会议里的一句话：「那就拨 5% 资金买 BAB 吧。」若机构按比例划拨，资金洪流会涌进新市场。赌场老经验：<strong>新游戏里最好赚钱</strong>。<a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>4 月初 BAB 正式登场。最初几只果然被热捧——公开试读写到诸如新泽西高速公路债开盘大涨的量级，一日浮盈可远超危机前同类交易的「正常利润」。机构抢额，场面有点像 A 股「打新」。可惜前几只多为超长期，不在渔阳职责带；他摩拳擦掌，等一星期后第一笔大型<strong>短期</strong>供给：加州综合债（general obligation）。</p>

      <div class="scene">
        新标签、新买家、新失衡——动量往往藏在「第一次」里。
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn5">
          <strong>⁵ 2009 年 4 月 BAB 初期发行热度</strong>
          当代媒体与 MSRB 早期统计显示：BAB 启动后数周内多笔州与机构发行获超额认购，应税市政利差与传统免税市场结构被改写；加州等大州迅速跟进大型综合债务发行。公开报道常强调「新买家进场」与「刺激项目融资」双叙事。具体个券涨跌幅度以当时盘口为准，导读只保留「开盘即受追捧」的节拍。
          <div class="why">为何重要：证实「新游戏」并非空想——一级市场热度是后文二级动量的前提。</div>
          <div class="src">来源：MSRB BAB 报告（2009）；LA Times / 当代市政市场报道</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">加州综合债：申购五千万只拿两百万</h2>
      <p>加州是美国最大州，却也常被写成财务最吃紧的州之一：公务支出、移民与社福压力、衰退期税收下滑，令评级承压，部分投资者对加州纸谨慎。本次 BAB 规模巨大（公开试读量级约数十亿美元，含短期部分）；渔阳判断承销商（高盛）对「又大又难看」的发行没十足把握，定价会偏便宜——于是下了入行以来最大一单：申购约 <strong>5000 万美元</strong>面额五年期。<a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>临近定价，销售来电：申购约三倍覆盖，分配明早揭晓。他兴奋——按比例大概能拿一千多万，开盘应涨。第二天清晨电话却沉重：「坏消息，你只拿到 <strong>200 万美元</strong>。」应得一千六、实得两百万，他怒斥「不讲江湖道义」，扬言要重新考虑与高盛的关系；销售同情附和，答应再争——很快又回：「抱歉，还是两百万。」</p>
      <p>冷静后他换策略：幽怨地搬出高盛祖训式口号——「若我们为客户提供优质服务，我们自己的成功会随之而来」——问：老客户鲁西银行呢？销售画饼「下次一定」，并透露关键一句：像你们这样的<strong>套利账户</strong>（arbitrage accounts）这次拿的都很少。</p>

      <div class="scene">
        一级市场的「分配」往往比定价更能决定谁能在二级市场玩动量。
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ 2009 年 4 月加州大型 GO／BAB 发行</strong>
          2009 年 4 月加州进行危机后标志性的大型一般义务债券发行，并包含大额 BAB／应税结构（当代报道总量常在数十亿美元量级，具体分券随批次变化）。发行用于基础设施等投票授权项目，并借助 35% 利息补贴降低净成本。导读中的申购／分配数字来自公开试读节拍的改写，用作交易台微观证据，不等同于官方分配表。
          <div class="why">为何重要：把「丙式思维」的破局，钉在一笔可感知的加州 BAB 上。</div>
          <div class="src">来源：California STO / CDIAC 档案；当代 LA Times、East Bay Times 等报道</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">福尔摩斯推理：债券都给了谁</h2>
      <p>「套利炒家拿得少」——灵光一现：债券都给谁了？高盛不会无故得罪中等客户，一定是遇上更难缠的「横主」。市传 PIMCO、加州公务员退休系统（CalPERS）等巨型买家要进 BAB；他们管着千亿级固收，下单有时很「蛮」：「五亿，少一个子儿就不要。」对巨头，承销商要逢迎——BAB 市场才刚开，以后还得靠他们捧场。惹不起比尔·格罗斯之流，就只能委屈倒卖债券的「小商贩」。<a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>
      <p>他发动销售情报网：大机构对分配大体满意；套利客破口大骂；许多中小买家几乎零分配——既无 PIMCO 体量，又无长期交易关系。轮廓清楚了：整体可能只是三倍认购，但绝不是平均切蛋糕。</p>

      <div class="scene">
        分配不公的牢骚里，常常藏着二级市场的供需地图。
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ 危机后大型固收买家与 BAB 配置</strong>
          PIMCO、CalPERS 等公共与准公共巨型账户在 2009 年积极寻找收益率与分散化工具；BAB 的应税＋补贴结构正好打开传统免税市政之外的买家池。承销分配向「长线真实钱」（real money）倾斜、套利／短线账户获配偏少，是一级市场常见但少被写进教科书的微观结构——公开试读把它写成侦探推理，便于理解后文「抛压薄、买盘厚」。
          <div class="why">为何重要：没有「谁拿到券」的地图，动量交易只是口号。</div>
          <div class="src">来源：机构投资者 BAB 评论；市政一级市场实务通识；公开试读节拍（改写）</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">动量交易：该出手时就出手</h2>
      <p>战场态势给出绝佳的<strong>动量交易</strong>窗口：供求严重失衡时搭顺风车。新发券有时跳高后就熄火——打新的套利盘会砸、长线没拿够的会买，多空难辨。加州这单却特殊：倒卖盘几乎没券→抛压薄；格罗斯类长线→不会立刻倒出；真正想持有的中小买家→只能去二级市场。买盘将远大于卖盘，价格更可能<strong>接着涨</strong>。<a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>
      <p>强势市里，犹豫的人常付学费。作者借楼市比喻：纠结「贵不贵」时，下一盘又更贵——大趋势里不必拘泥毛刺；经验是：<strong>第一个卖价往往是最好的卖价</strong>（The first offer is often the best offer）。谁会卖？赚了就绷不住的人——像拿到好牌就保守离场的赌客。</p>
      <p>加州综合债开盘大幅收紧利差；渔阳见价就吃，几天把头寸做到约五千万。销售本以为他会把分到的两百万倒掉走人——几个月前普林斯顿那笔或许会；如今「士别三日」：利差从发行附近数百基点向收窄方向走，账上利润进百万美元量级。4 月全面出击，尤其吃透 BAB 新游戏，一个月盈利达数百万——顺风满帆。</p>
      <p>文森的圣经故事完成了思维跃迁：永远把金币埋土里的交易员没有前途；看准了就出手，才是王道。下一章「善败者不乱」：赢了之后，如何不乱。</p>

      <div class="scene">
        挖出金币之后，真正的功课才开始——善败者，亦不乱于胜。
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn8">
          <strong>⁸ 动量交易与新发券二级失衡</strong>
          动量／趋势跟随在供需冲击、强制配置或结构性买家进场时更易奏效。新发后的「free float」若大部分锁在长线账户、短线倒卖供给稀缺，二级常出现持续收窄或价格上漂。这与「平均打新」后套利盘集中兑现的路径不同。导读保留公开试读中的利差收窄与头寸结果量级，作为故事节拍，而非可复现的交易指令。
          <div class="why">为何重要：把寓言落地为可理解的市场微观结构，并桥接 §21。</div>
          <div class="src">来源：固定收益微观结构通识；2009 年市政／BAB 二级市场评论；公开试读节拍（改写）</div>
        </div>
        <div class="fn-item" id="fn9">
          <strong>⁹ 2009 年春夏风险偏好修复与交易员心理</strong>
          QE1、财政刺激与 BAB 等管道政策叠加后，信用与市政市场局部出现「政策底后的风险再定价」。交易台常经历从「惊弓之鸟」到「错失恐惧（FOMO）」的摆动——本章用圣经寓言处理的，正是这种心理制度：在风控框架内，何时允许把风险预算重新打开。
          <div class="why">为何重要：把个人决策嵌入 2009 年政策／市场恢复的颜色，避免孤立英雄叙事。</div>
          <div class="src">来源：美联储／财政部危机应对年表；当代风险资产修复研究</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>人物关系 / 时间线 / 知识图谱</h2>

        <div class="mermaid-wrap">
          <div class="caption">人物与机构：从「仆人丙」到 BAB 战场</div>
          <div class="mermaid">
flowchart LR
  YY[渔阳 · 鲁西交易台] --> CASH[冬春空仓 · 保本]
  VIN[文森] --> BIBLE[马太福音才干寓言]
  BIBLE --> YY
  YY --> SIZE[拟加仓 · 弃丙式思维]
  GS[高盛承销 / 销售] --> ALLOC[一级分配]
  PIMCO[PIMCO / CalPERS 等] --> ALLOC
  YY --> ALLOC
  ALLOC --> THIN[套利盘获配稀薄]
  BAB[建设美国债券 BAB] --> CA[加州综合债]
  CA --> SEC[二级买盘 &gt; 卖盘]
  THIN --> SEC
  SIZE --> MOM[动量建仓 ~5千万]
  SEC --> MOM
  MOM --> NEXT[§21 善败者不乱]
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">时间线：圣经故事（QE 后 → 2009-04）</div>
          <div class="mermaid">
timeline
    title Bible Stories
    after QE : Flat book · plan +50mm · Vincent wants 100mm
    parable : Matthew 25 talents · bury vs deploy
    Soros echo : Size the right idea · 1992 GBP lore
    early Apr 2009 : BABs launch · hot primary
    mid Apr 2009 : CA GO BAB · 50mm bid · 2mm fill
    days after : Secondary momentum · P&amp;L leap
    bridge : Toward §21 win without chaos
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">知识图谱：金币如何从土里回到风险预算</div>
          <div class="mermaid">
flowchart TB
  DAWN[§19 曙光初现] --> QE[流动性预期上升]
  QE --> FEAR[惊弓之鸟 · 丙式保本]
  TALENT[才干寓言] --> MIND[受托要运用资本]
  FEAR --> MIND
  MIND --> RISK[风控内放大正确头寸]
  ARRA[ARRA] --> BAB[BAB 35% 直补]
  BAB --> NEWBUY[养老金 / 海外等新买家]
  NEWBUY --> IMBAL[一级分配偏向真实钱]
  IMBAL --> MOM[二级动量]
  RISK --> MOM
  MOM --> WIN[4 月盈利跃升]
  WIN --> S21[§21 善败者不乱]
          </div>
        </div>
      </section>
'''

EN_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Charging_Bull_statue.jpg" alt="Wall Street Charging Bull" loading="lazy" />
        <figcaption>Wall Street’s Charging Bull—after the crash, “bull” was still a hope more than a fact. This chapter asks: once dawn shows, will you dig the coin out of the dirt? Source: Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">Assembly call: from cash to size</h2>
      <p>After §19, QE talk was abroad and fish-belly white had a name—dawn. Yuyang had spent the winter in the trench: mostly flat, the odd sniper shot. Now the wind really seemed to turn; time to attack.</p>
      <p>He reported cheerfully to Vincent: he would take risk up toward about <strong>$50 million</strong>. Vincent shook his head: “Only fifty? A hundred is more like it.” Before the crisis they had run billion-scale bond books when vol was tame; after it, bonds traded like stocks and stocks like roller coasters—vol many times higher. Fifty already felt conservative to Yuyang; Vincent’s one hundred sounded like “boldness makes the harvest.” <a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>Yuyang cited risk memos—keep size down—and his own scorecard: in a wretched year he had not lost money. Vincent shook his head again: last year many traders became startled birds. “That was then. Change how you think.”</p>

      <div class="side-panel">
        <h3 class="panel-title">Chapter anchors · spring 2009 → April</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">Post-QE</div><div class="ev">Flat → plan +$50mm</div></div>
          <div class="event-card"><div class="yr">Bible</div><div class="ev">Matthew talents parable</div></div>
          <div class="event-card"><div class="yr">Early Apr</div><div class="ev">BABs debut · chased</div></div>
          <div class="event-card"><div class="yr">Mid Apr</div><div class="ev">CA GO · momentum</div></div>
        </div>
      </div>

      <div class="scene">
        Dawn is not a safe; it only asks whether you will keep burying the coin.
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn1">
          <strong>¹ Pre- vs post-crisis volatility and position scale</strong>
          In 2008–09, credit and rates vol jumped far above Great Moderation norms: spread moves, VIX, and bond day-to-day P&amp;L swings made the same notional feel several times riskier. “We used to run a billion; now we debate fifty million” is coherent risk math. Crisis histories stress the tension between post-deleveraging limits and post-policy-bottom opportunity.
          <div class="why">Why it matters: lands §19’s policy dawn on the desk—size itself is the chapter’s opening conflict.</div>
          <div class="src">Source: public vol/spread series; FCIC / Fed retrospectives</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">Matthew 25: three servants and the coins</h2>
      <p>Vincent then told a Bible story—the <strong>Parable of the Talents</strong> in Matthew 25. <a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>A hard master leaves town and entrusts servants by ability: five coins, two, and one. The first trades and makes five more; the second makes two; the third, fearing loss and blame, <strong>buries</strong> his single coin. On return the master praises the first two and rages at the third who returns the principal intact: if you knew I was harsh, you should have lent at interest—now even this coin is taken and given to the one who earns.</p>
      <p>Yuyang startled: that is the bank. Management is the hard master—demanding profit while capping risk—and he is timid <strong>servant C</strong>, burying capital to “not lose.” In a jungle desk, timid traders have no future; those who size the right chance win trust and more rope. He admired the fit of the parable and vowed to drop “C-thinking,” learn from A—and swing when it is time.</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Parable_of_the_Talents.jpg" alt="Parable of the Talents artwork" loading="lazy" />
        <figcaption>Classical imagery of the talents parable—the buried coin is Wall Street slang for “flat and proud of it.” Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        Preservation is not a virtue by itself; burying the coin in the wrong season is the real waste.
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn2">
          <strong>² Matthew 25:14–30, Parable of the Talents</strong>
          A master allocates “talents” (a large monetary unit) by ability; industrious stewards are rewarded, the burier is punished—often read as stewardship and opportunity cost. Public trial-read retellings use “coins / A-B-C” and map bank incentives: earn, but do not blow up—burying = over-preservation. This is off-book Bible background plus chapter-theme rewrite, not scripture or book text pasted.
          <div class="why">Why it matters: core metaphor behind the chapter title; the BAB trade is the practical “dig the coin up” exam.</div>
          <div class="src">Source: public Matthew 25 translations; encyclopedia entries on the Parable of the Talents</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">Soros-style push: size when it matters</h2>
      <p>The talk recalled Street lore: in 1992 Soros’s Quantum fund shorted sterling, helping force a devaluation and ERM exit—a legendary score. Public tellings often credit Druckenmiller with spotting the weakness; Soros’s edge was sizing the idea <strong>large enough</strong> at the hinge—one anecdote has him scoffing at a “mere” billion and ordering a double. <a class="fn-link" href="#fn3"><sup class="fn">³</sup></a></p>
      <p>Vincent’s Bible story rhymed with that push. And Yuyang felt he had found a “sterling-like” chance—only the battlefield was spring-2009 munis.</p>

      <div class="scene">
        Insight is common; people who add size at the hinge are rare.
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn3">
          <strong>³ Black Wednesday 1992 and Soros / Druckenmiller</strong>
          On 16 Sep 1992 sterling left the ERM under speculative pressure; George Soros’s fund became famous for profits on the short. Interviews and histories often note Stanley Druckenmiller’s role and Soros’s habit of pressing winners. Exact numbers and dialogue vary by teller; the footnote anchors the widely retold theme: size the right idea at the hinge.
          <div class="why">Why it matters: a Wall Street isomorphic case for dropping “C-thinking”—size is part of the strategy.</div>
          <div class="src">Source: Bank of England / contemporary coverage; public financial histories and interview digests</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">Build America Bonds: policy over cash</h2>
      <p>In spring 2009 the muni market birthed <strong>Build America Bonds</strong> (BABs). Traditional munis are often federally tax-exempt, so buyers skew to high-bracket households and insurers; pensions and foreign money often skip them—they already owe little U.S. income tax and will not buy low taxable-equivalent yields. After the crash, rich balance sheets shrank and levered arb desks fled; muni demand fell and yields rose; local deficits met higher interest and begged Washington. <a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>Washington’s move was “policy beats cash transfers”: BABs are <strong>taxable</strong>, but the Treasury directly subsidizes about <strong>35%</strong> of issuer interest. Leverage by rule—no tax stamp, higher coupons, pensions and foreigners become natural buyers; issuers’ net cost often beats traditional tax-exempts; the federal outlay is partly offset by tax on the interest. Public write-ups cast BABs as spending a little to unlock a lot of state-local finance.</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/United_States_Department_of_the_Treasury_Seal.svg" alt="U.S. Treasury seal" loading="lazy" />
        <figcaption>U.S. Treasury seal—BAB direct-pay interest subsidies wrote stimulus into the muni pipe. Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        In a crisis the scarce resource is often not cash but a rule that invites new buyers in.
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ Build America Bonds and the 35% direct subsidy</strong>
          BABs were created under the 2009 American Recovery and Reinvestment Act: taxable munis with a Direct Pay interest subsidy (commonly 35% of interest) or a tax-credit variant. In 2009–10 they broadened the buyer base (insurers, pensions, overseas) and cut many issuers’ net borrowing costs. New issuance sunset after 2010. Footnotes follow public program rules; the book’s “small money, big leverage” arithmetic is guide rewrite.
          <div class="why">Why it matters: institutional base of the chapter’s “new game”—no BABs, no later momentum battlefield.</div>
          <div class="src">Source: U.S. Treasury / IRS BAB explainers; early MSRB BAB market reports; ARRA text</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">New game opens: BABs get chased</h2>
      <p>As soon as BABs were imminent, Yuyang saw it: institutions love diversification; local governments are not corporates and can tax—muni exposure is a natural diversifier that tax-exempt low coupons had barred. With BABs, he pictured a board saying, “Put 5% in BABs.” Pro-rata flows would flood the new market. Old gambling rule: <strong>new games are where money is easiest</strong>. <a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>Early April, BABs launched. The first names were chased—trial-read color includes turnpike-style deals gaping higher, one-day marks dwarfing “normal” pre-crisis scrapes. Allocations felt like IPO lotteries. Early deals were mostly ultra-long, outside his sleeve; he waited for the first big <strong>shorter</strong> print: a California general obligation.</p>

      <div class="scene">
        New label, new buyers, new imbalance—momentum often hides in the first time.
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn5">
          <strong>⁵ Early-April 2009 BAB primary heat</strong>
          Contemporary press and early MSRB stats show oversubscribed state and agency BAB prints in the program’s first weeks, rewriting taxable-muni buyer structure; California and other large issuers followed with jumbo GOs. Coverage stressed “new buyers” and “stimulus project finance.” Exact gap sizes are tape-dependent; the guide keeps the beat “hot from the open.”
          <div class="why">Why it matters: proves the “new game” was not fantasy—primary heat sets up secondary momentum.</div>
          <div class="src">Source: MSRB BAB report (2009); LA Times / contemporary muni coverage</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">California GO: bid 50, get 2</h2>
      <p>California is the largest state and was often cast as one of the most fiscally strained: payroll and benefits, migration/social costs, recession tax drops—ratings pressure, wary investors. This BAB was huge (trial-read scale in the multi-billion range, including shorts). Yuyang figured the underwriter (Goldman) was unsure about a large, optically weak credit, so pricing would be cheap—and put in his biggest order yet: about <strong>$50 million</strong> face of five-years. <a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>Near pricing, sales called: ~3× subscribed, allotments in the morning. He was up—pro-rata maybe teens of millions, should gap. Dawn call: “Bad news—you got <strong>$2 million</strong>.” Expecting ~16, getting 2, he blasted “no honor,” threatened to rethink the franchise; sales sympathized, promised to fight—then: “Still two.”</p>
      <p>Cooler, he switched tone: invoked a Goldman-ish credo—“If we serve our clients well, our own success will follow”—and asked about Lucy Bank, the old account. Sales painted “next time” and dropped the key line: <strong>arbitrage accounts</strong> like yours all got little.</p>

      <div class="scene">
        Primary “allocation” often decides who can even play secondary momentum.
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ April 2009 California jumbo GO / BAB</strong>
          In April 2009 California printed a crisis-era landmark general-obligation package with large BAB/taxable sleeves (contemporary totals often cited in the multi-billion range by tranche). Proceeds backed voter-authorized infrastructure; the 35% interest subsidy cut net cost. Bid/fill figures in the guide rewrite public trial-read beats as desk micro-evidence—not an official allotment table.
          <div class="why">Why it matters: nails the break from “C-thinking” to a tangible California BAB.</div>
          <div class="src">Source: California STO / CDIAC archives; contemporary LA Times, East Bay Times coverage</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">Holmes on the Street: who got the bonds?</h2>
      <p>“Arbs got little”—flash: who got them? Goldman would not gratuitously offend a mid-tier client; someone harder to refuse had arrived. Street chatter put PIMCO, CalPERS, and other giants into BABs; with hundred-billion fixed-income books they sometimes order “brutally”: “Five hundred million—or nothing.” Lead managers court giants—BAB is newborn; future calendars need them. Cannot anger a Gross; can shortchange the bond “hawkers.” <a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>
      <p>His sales intel net reported: big accounts mostly pleased; arbs furious; many smaller real-money accounts near zero—neither PIMCO-scale nor long trading history. The picture clarified: overall cover might be only 3×, but the cake was never sliced evenly.</p>

      <div class="scene">
        Inside allocation grievances, a secondary supply-demand map is often hiding.
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ Post-crisis real-money buyers and BAB allocation</strong>
          PIMCO, CalPERS, and other public/quasi-public giants hunted yield and diversification in 2009; BAB taxable-plus-subsidy structures opened the pool beyond traditional tax-exempt buyers. Skewing allotments toward long-only “real money” and starving arb/fast money is common primary microstructure rarely in textbooks—the trial-read casts it as detective work so thin float / thick bids make sense later.
          <div class="why">Why it matters: without a “who got paper” map, momentum is just a slogan.</div>
          <div class="src">Source: institutional BAB commentary; muni primary practice; public trial-read beats (rewritten)</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">Momentum: when it's time to swing</h2>
      <p>The battlefield offered a clean <strong>momentum</strong> window: ride a one-way tape when supply and demand are badly skewed. New issues sometimes gap and die—IPO-style arbs sell, longs who missed buy, fog either way. This California print was different: flippers got almost nothing → thin sell pressure; Gross-style longs → will not dump at once; mid-size holders who wanted paper → must buy secondary. Bids should swamp offers; price can <strong>keep rising</strong>. <a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>
      <p>In strong markets, hesitation taxes you. The author borrows a property-market image: haggle “too expensive?” and the next project is higher—do not nitpick pips in a bull; lore says <strong>the first offer is often the best offer</strong>. Who sells? People who cannot sit on a winner—gamblers who cash good hands too early.</p>
      <p>The CA GO gapped spreads tighter; Yuyang lifted offers and built toward ~$50mm in days. Sales had expected him to flip the $2mm allotment—months earlier, on the Princeton scrap, maybe; now, three days make a new man: spreads compressed from issue levels by roughly a hundred basis points of story-scale move, marks into seven figures. April became a full offensive, especially the BAB new game—monthly P&amp;L in the millions, wind at his back.</p>
      <p>Vincent’s Bible story finished the mental jump: traders who forever bury coins have no future; sizing the right chance is the way. Next, §21 “Those Who Fail Well Do Not Panic”: after a win, how not to lose your head.</p>

      <div class="scene">
        After you dig up the coin, the real lesson begins—those who fail well also refuse to riot in victory.
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn8">
          <strong>⁸ Momentum trading and post-deal secondary imbalance</strong>
          Trend/momentum works best under supply shocks, forced allocation, or structural new buyers. If free float is locked in long-only hands and short-horizon inventory is scarce, secondary can grind tighter or drift up—unlike average “IPO” paths where arbs dump together. The guide keeps trial-read spread and P&amp;L magnitudes as story beats, not reproducible trade tickets.
          <div class="why">Why it matters: lands the parable in microstructure and bridges to §21.</div>
          <div class="src">Source: fixed-income microstructure primers; 2009 muni/BAB secondary commentary; public trial-read beats (rewritten)</div>
        </div>
        <div class="fn-item" id="fn9">
          <strong>⁹ Spring–summer 2009 risk-appetite repair and trader psychology</strong>
          After QE1, fiscal stimulus, and pipe programs like BABs, credit and munis locally re-priced recovery odds. Desks swung from “startled bird” to FOMO—the parable’s job is that institutional psychology: inside risk limits, when to reopen risk budget.
          <div class="why">Why it matters: embeds the personal decision in 2009 policy/market recovery color, avoiding lone-hero myth.</div>
          <div class="src">Source: Fed/Treasury crisis chronologies; contemporary risk-asset rebound research</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>Relationships / timeline / knowledge graph</h2>

        <div class="mermaid-wrap">
          <div class="caption">People and institutions: from servant C to the BAB battlefield</div>
          <div class="mermaid">
flowchart LR
  YY[Yuyang · Lucy desk] --> CASH[Winter flat · preserve]
  VIN[Vincent] --> BIBLE[Matthew talents parable]
  BIBLE --> YY
  YY --> SIZE[Add size · drop C-thinking]
  GS[Goldman syndicate / sales] --> ALLOC[Primary allocation]
  PIMCO[PIMCO / CalPERS et al.] --> ALLOC
  YY --> ALLOC
  ALLOC --> THIN[Thin arb allotments]
  BAB[Build America Bonds] --> CA[California GO]
  CA --> SEC[Secondary bids &gt; offers]
  THIN --> SEC
  SIZE --> MOM[Momentum book ~$50mm]
  SEC --> MOM
  MOM --> NEXT[§21 Fail well, stay calm]
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Timeline: Bible Stories (post-QE → Apr 2009)</div>
          <div class="mermaid">
timeline
    title Bible Stories
    after QE : Flat book · plan +50mm · Vincent wants 100mm
    parable : Matthew 25 talents · bury vs deploy
    Soros echo : Size the right idea · 1992 GBP lore
    early Apr 2009 : BABs launch · hot primary
    mid Apr 2009 : CA GO BAB · 50mm bid · 2mm fill
    days after : Secondary momentum · P&amp;L leap
    bridge : Toward §21 win without chaos
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Knowledge graph: how the coin leaves the dirt</div>
          <div class="mermaid">
flowchart TB
  DAWN[§19 Dawn Appears] --> QE[Liquidity expectations up]
  QE --> FEAR[Startled birds · C-preservation]
  TALENT[Talents parable] --> MIND[Stewardship means deploying capital]
  FEAR --> MIND
  MIND --> RISK[Resize winners inside risk]
  ARRA[ARRA] --> BAB[BAB 35% direct pay]
  BAB --> NEWBUY[Pensions / foreign new buyers]
  NEWBUY --> IMBAL[Primary skew to real money]
  IMBAL --> MOM[Secondary momentum]
  RISK --> MOM
  MOM --> WIN[April P&amp;L jump]
  WIN --> S21[§21 Fail well, stay calm]
          </div>
        </div>
      </section>
'''

def main():
    zh = page(
        "zh",
        "《乱世华尔街》第20集：圣经故事",
        "故事导读 · 据公开试读改写 · 场外研究补充",
        "圣经故事",
        "《乱世华尔街》第二十章「圣经故事」· 渔阳 · 故事改写 + 脚注研究 · 第四部分「峰回路转」",
        "下面按作者经历与公开时间线讲述本章故事，用自己的话改写，方便跟读；不是全书/全章原文照搬。脚注、配图与知识图谱为场外公开资料补充。完整内容请读正版。",
        ZH_TOC,
        "CHAPTER TWENTY · 圣经故事 · 第四部分 峰回路转",
        ZH_BODY,
        "《乱世华尔街》· 渔阳 · 第二十章故事导读（原创改写）",
    )
    en = page(
        "en",
        "Chaos on Wall Street §20: Bible Stories",
        "Story guide · rewritten from public trial reads · off-book research",
        "Bible Stories",
        "Chaos on Wall Street, Chapter 20 “Bible Stories” · Yuyang · story rewrite + footnote research · Part 4 “The Road Turns”",
        "A story-first retelling from the author’s arc and public timelines, in our own words for guided reading—not a verbatim copy of the copyrighted chapter. Footnotes, figures, and graphs are off-book public research. For the full text, support the official edition.",
        EN_TOC,
        "CHAPTER TWENTY · Bible Stories · Part 4 The Road Turns",
        EN_BODY,
        "Chaos on Wall Street · Yuyang · Ch.20 story guide (original rewrite)",
    )
    (DIR / "bible-stories-zh.html").write_text(zh, encoding="utf-8")
    (DIR / "bible-stories-en.html").write_text(en, encoding="utf-8")
    print("Wrote", DIR / "bible-stories-zh.html", len(zh))
    print("Wrote", DIR / "bible-stories-en.html", len(en))

if __name__ == "__main__":
    main()
