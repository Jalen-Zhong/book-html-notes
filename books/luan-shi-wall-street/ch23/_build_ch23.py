#!/usr/bin/env python3
"""Build full self-contained ZH/EN HTML for ch23 关系学 / Relationships."""
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
        '<a class="active" href="relationships-zh.html">中文</a>\n'
        '        <a href="relationships-en.html">English</a>\n'
        '        ' + home
        if lang == "zh" else
        '<a href="relationships-zh.html">中文</a>\n'
        '        <a class="active" href="relationships-en.html">English</a>\n'
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
    ("s1", "谁认识谁：场外世界的关系网"),
    ("s2", "老滑与小滑：销售里的两档境界"),
    ("s3", "西雅图自来水：周五掉下的馅饼"),
    ("s4", "利益链条：资本何以成为关键一环"),
    ("s5", "关系即利益：周转、甜头与路径选择"),
    ("s6", "辛迪的七毛五：奖金结构里的和谐"),
    ("s7", "做人别小气：文森、抠门精与时代分寸"),
    ("s8", "最铁一起分过赃：通向 §24"),
    ("diagrams", "人物关系 / 时间线 / 知识图谱"),
]

EN_TOC = [
    ("s1", "Who you know: the OTC relationship net"),
    ("s2", "Lao Hua & Xiao Hua: two grades of sales craft"),
    ("s3", "Seattle water: a Friday pie from the sky"),
    ("s4", "The profit chain: why capital is the hinge"),
    ("s5", "Guanxi is interest: turnover, sweets, path choice"),
    ("s6", "Cindy's seventy-five cents: harmony in bonuses"),
    ("s7", "Don't be stingy: Vincent, the miser, era dial"),
    ("s8", "Strongest bond: sharing the spoils → §24"),
    ("diagrams", "Relationships / timeline / knowledge graph"),
]

ZH_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/New_York_Stock_Exchange_September_2016_05.jpg" alt="纽约证券交易所" loading="lazy" />
        <figcaption>纽约证券交易所——§22 建好了「麦当劳」分销网，§23 问的是网怎么润滑：关系，还是利益？来源：Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">谁认识谁：场外世界的关系网</h2>
      <p>承接 §22：新市场、新思维，「麦当劳」模式靠分销网赚稳定过手费。网铺开之后，下一课更土、也更硬——华尔街靠什么把货从一边搬到另一边？美国谚语说得很直：不是你懂什么，而是你认识谁。<a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>市政债券几乎全是<strong>场外交易</strong>（over-the-counter）：没有像股票那样坐在交易所中央竞价，买卖靠电话、彭博消息、邮件和熟人圈。关系网大、消息灵，才做得动；关系薄，连「谁急着卖、谁急着买」都听不到。对渔阳而言，最要紧的生意关系，就是各家券商对口的<strong>销售</strong>——他们既是市场里的眼线，又是通向客户的管道。<a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>用中国人常说的「关系学」去看美国金融，并不违和：客户、销售、交易员、监管各自占一环；忠诚口号挂在墙上，真正决定流量的，往往是谁能帮谁把钱赚到口袋里。</p>

      <div class="side-panel">
        <h3 class="panel-title">本章时间锚点 · 后危机分销日常</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">§22 后</div><div class="ev">分销网已立 · 要润滑</div></div>
          <div class="event-card"><div class="yr">周五</div><div class="ev">西雅图自来水债「馅饼」</div></div>
          <div class="event-card"><div class="yr">两日</div><div class="ev">过手分销 · 各方分利</div></div>
          <div class="event-card"><div class="yr">日常</div><div class="ev">甜头 → 周转 → §24</div></div>
        </div>
      </div>

      <div class="scene">
        场外世界没有中央广场；关系网本身就是市场微观结构。
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn1">
          <strong>¹ 「It's not what you know, it's who you know」</strong>
          这句英语谚语在商业与职场叙事里极常见，强调网络资本（social capital）常压过纸面技能。公开试读把本章开篇钉在这句上，用来对照华尔街场外债券台：信息与订单流沿着熟人电话线走。脚注只锚定谚语与主题，不复述书中长对话。
          <div class="why">为何重要：给「关系学」立下跨文化入口——不是请客吃饭的刻板印象，而是网络即流动性。</div>
          <div class="src">来源：英语谚语通识；公开 TOC / FX110 试读节拍</div>
        </div>
        <div class="fn-item" id="fn2">
          <strong>² 市政债场外市场：电话、做市与搜索成本</strong>
          与股票交易所不同，美国市政债券二级市场长期以 OTC 为主：投资者通过券商下单，券商或以自有资本做市（principal），或以代理寻价（agency）。MSRB 等公开材料强调：流动性依赖「搜索」——谁知道买家、谁愿意出库存。销售（sales）正是搜索引擎的人形节点。
          <div class="why">为何重要：解释为何「搞好销售关系」不是人情戏，而是微观结构里的路由问题。</div>
          <div class="src">来源：MSRB《How Are Municipal Bonds Priced?》；MSRB 交易成本 / 流动性讨论</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">老滑与小滑：销售里的两档境界</h2>
      <p>销售水平差距极大。圈里口碑好的「老滑」——某地方券商资深销售——做生意时让人觉得他在替你出主意、帮你挣钱；事后翻彭博记录，又常发现他自己差价吃得很狠。既能自己赚钱，又能让客户满意，才是关系学高手。</p>
      <p>徒弟「小滑」声音语气都像师傅，道行却差一截：和渔阳对价时，差价常被压到最低。生意越做越多，渔阳在这两人身上慢慢摸到「关系」的层次——不是嘴甜，而是<strong>让对方觉得跟你合作划算</strong>。</p>

      <div class="scene">
        高手让你觉得他在帮你；事后才发现，他也帮了自己——两边都对。
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn3">
          <strong>³ 销售 vs 交易员：同一屋檐下的微妙利益</strong>
          华尔街固收台常见分工：销售覆盖客户、传递报价与订单；交易员管理库存与风险、决定是否吃进/吐出。公开岗位描述与行业通识都指出：销售提成常与成交量/中介收入挂钩，交易员奖金更绑在账簿 P&amp;L 与风险贡献上——激励并不自动一致。本节人物名为故事化称呼，脚注只说明结构张力。
          <div class="why">为何重要：为后文「领导哥们儿」绕过本公司交易员埋下制度伏笔。</div>
          <div class="src">来源：投行 Sales &amp; Trading 岗位通识；§4「宇宙的中心」导读连续性</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">西雅图自来水：周五掉下的馅饼</h2>
      <p>一个周五下午，生意本该清淡，小滑却打来「紧急军情」：单线客户要出约八百万西雅图自来水债，要价收益率约 2.90%；他声称怎么也值 2.80%——收益率越低，价格越高，听上去像送钱。<a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>渔阳用彭博核对结构与供给：发行已有年头，结构受欢迎，西雅图公用事业类供给不算滥，要价似乎真便宜。可教训太多，他先套话：卖家是谁？为何这么急？小滑神秘兮兮「不太方便讲」——越神秘，越像套。</p>
      <p>不到一分钟，老滑亲自上线：相信我，可以略砍到约 2.92% 拿下，但要快。老滑终究老道，点破卖家是地方政府机构、渠道在他们公司手里——或许某位销售与「领导」关系铁，才搞来便宜货。渔阳出价吃进。</p>
      <p>仍不放心，他请美林销售艾米帮忙估个价。他进场时已想好：这类结构常受信托/零售渠道欢迎。艾米很快回电：自己交易员愿出约 2.85% 囤货——不费吹灰之力，账面已浮出好几个基点的空间。<a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>他没有立刻全卖给艾米：做人讲义气——老滑弄来的货，也得给他二次机会。老滑又报来类似两只，他略砍价全吃。两千多万便宜货到手，正得意又困惑：怎么会有天上掉馅饼？苹果砸醒牛顿，「馅饼」却把他砸糊涂。</p>
      <p>更怪的是：不到一小时，小滑又要买回两百万——零售经纪人要。渔阳报 2.80%；小滑嫌涨得快。他用对方刚才的话回敬，再松到 2.82%「友情价」成交。脸给过了，立刻打给艾米：有了这笔印记，美林网络照同样价出手几百万。再回头告诉老滑「特地给你留了一部分」——老滑只好加紧推剩余。</p>
      <p>两天内，货通过老滑与艾米迅速分销干净，轻松获利约十五万美元量级。数目不算天文，却是<strong>皆大欢喜</strong>：老滑先卖后买做两遍生意；艾米赚提成又有面子；渔阳赚过手利润，关系更牢。</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Seattle_skyline_from_Kerry_Park.jpg" alt="西雅图天际线" loading="lazy" />
        <figcaption>西雅图天际线——公用事业收益债（自来水等）常因本地需求与结构偏好，成为零售/信托渠道的「好卖货」。来源：Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        馅饼不砸糊涂人；砸醒人的，是「我凭什么出现在这条链上」。
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ 收益率与价格：市政债报价直觉</strong>
          固定票息债券：市场要求的收益率上升 → 价格下跌；收益率下降 → 价格上升。卖方「要价 2.90%」而买方认为「值 2.80%」，意思是卖方开的价格偏便宜（愿意以更高收益率卖出）。公开投资者教育（MSRB 等）用这一对偶关系解释二级市场讨价还价。故事中的具体数字为改写尺度，脚注只讲计价语言。
          <div class="why">为何重要：读懂「便宜货」在收益率语言里长什么样，才能跟上分销差价。</div>
          <div class="src">来源：MSRB 市政债定价教育页；固定收益教科书通识</div>
        </div>
        <div class="fn-item" id="fn5">
          <strong>⁵ 公用事业债与零售/信托偏好</strong>
          供水、供电等收入债券（revenue bonds）常因现金流故事相对直观、部分结构适合中小票面分销，而进入经纪零售与信托渠道。公开市场结构讨论强调：新券有银团支持，老券则更依赖「谁认识终端买家」。美林式大型零售网络在故事里扮演「泄洪渠」——与 §22 地方狼群逻辑同族。
          <div class="why">为何重要：解释为何渔阳一进货就想到艾米，而不是只找大行同业。</div>
          <div class="src">来源：市政收入债通识；MSRB / 二级流动性讨论；公开试读节拍（改写）</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">利益链条：资本何以成为关键一环</h2>
      <p>得意之余他追问：老滑有关系，艾米有渠道，我何德何能捡十五万？想通之后茅塞顿开——自己充当了<strong>利益分配链条里关键的一环</strong>。<a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>概括：某地方政府机构愿以低于市价约二十个基点出售一批债；华尔街迅速分销，以略高于市价的价格卖给小投资者。整条链大约二十五个基点的「饼」，谁占住分销环节，谁分羹。</p>
      <p>政府客户单线握在老滑公司某位「领导哥们儿」手里。关系再铁，也得把债卖掉才能把关系变成提成。他可以让本公司交易员囤货——但大头利润就归交易员。对销售最理想的，是绕过自家交易员，找另一条销售路径倒卖，马上兑现，两销售分钱。谁能快速找到能吃下两千万的对手盘？老滑想到渔阳：反应快、资本厚、而且是<strong>交易员</strong>——今天买了还得卖，货源渠道仍可握在老滑手里，还能做第二遍生意。投资者吃进去会沉睡；交易员是活水库。</p>
      <p>债到渔阳账上后：一部分经老滑回流零售（投桃报李），一部分经艾米走美林网（快速出货 + 拉关系 + 让两边竞争出好价）。粗分：领导哥们儿与老滑合计约十个基点，渔阳约十个基点，二次销售/艾米/零售经纪人约五个基点。他能卡住关键位置，是因为掌握一种销售没有的资源：<strong>资本</strong>——鲁西银行的资产负债表。</p>
      <p>更有趣：销售提成体制竟造成销售与<strong>本公司</strong>的利益摩擦。若让自家交易员囤便宜货，销售创造的可见价值难立刻兑现，提成往往「意思意思」；转手加价卖给外部交易员，利润马上落地，提成干净，还附带二次生意。老滑肯当「活雷锋」送馅饼，正因为渔阳能帮他实现利益。</p>

      <div class="scene">
        所谓关系，其实就是利益；关键位置，比称兄道弟更值钱。
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ 基点、加价与「公平合理」价格</strong>
          一个基点（bp）= 0.01%。市政债 OTC 里，做市商的报酬常嵌在全价里的 markup/markdown；代理成交则收显式佣金。MSRB Rule G-30 要求价格与佣金「公平合理」，并考虑市值判断、费用、利润权等。公开试读用「约 25bp 分销饼」讲利益分割——脚注提供监管语言坐标，不把故事数字当作市场统计。
          <div class="why">为何重要：把「分赃」叙事接到公开规则：差价不是江湖暗语，而是受监管审视的中介租金。</div>
          <div class="src">来源：MSRB Rule G-30；MSRB 定价教育；公开试读利益链节拍（改写）</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">关系即利益：周转、甜头与路径选择</h2>
      <p>逻辑想清后，关系学忽然浅显：搞关系最好的办法，不是吃饭喝酒勾肩搭背，而是在利益链上占关键位，在帮助别人实现利益的同时实现自己的利益。</p>
      <p>§22 已从杜邦公式角度说：后危机利润率不薄，就应抬高周转。落到关系学操作面：搞好各路销售，让更多债从自己这里「过手」。分销路径很多，如何吸引别人走你这条？最有效的是<strong>以利诱之</strong>——多给销售甜头，让他们把生意往你这儿送。<a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>

      <div class="scene">
        理论叫周转；实务叫：让路由经过你，并让路由器愿意。
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ 杜邦分解与「关系学」操作面</strong>
          杜邦分析把 ROE 拆成利润率 × 周转 × 杠杆。§5 / §22 已铺垫：危机后杠杆受限、利润率尚可时，加速资产周转是正道。「让债从我这儿过手」正是提高周转的微观动作；给销售留甜头，则是购买订单流的显性成本——用小额确定成本换更大期望流量。脚注连回前章公式，不引入非公开客户数据。
          <div class="why">为何重要：证明关系学不是玄学，而是 ROE 会计在人脉上的投影。</div>
          <div class="src">来源：§5 / §22 导读；公司金融杜邦通识</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">辛迪的七毛五：奖金结构里的和谐</h2>
      <p>一天，中型券商销售辛迪来电诉苦：一千万能佐治亚燃气债，渔阳已同意对方 3.50% 要价，卖家却连中介费都不肯出。辛迪人到中年，家里还有不听话的孩子，偶尔抱怨两句；今天也确实背——对方一毛不拔。</p>
      <p>「你要是能付我一张债五毛钱中介费，这单就成。」一张面值一千美元的债五毛，若是老滑，开口起码一块。渔阳灵机一动：机会是你找来的——我给你七毛五。多塞两千五，辛迪连声道谢。此后她对渔阳的交易格外热心，主承销热门债分配也常向他倾斜。「他们都很喜欢你」——送钱的，谁不喜欢？</p>
      <p>细想，这与奖金制度有关。销售不能随便下大注，多赚中介类「太平小钱」，但分成比例往往较高（尤其中小券商，故事尺度举例约 20%）；交易员能用资本下赌注，可能赚大钱，分成比例却较低（举例约 5%）。五千美元对渔阳意义有限，大可送给销售换关系，让对方拿一千提成；若出现十万量级、胜率略优的机会，销售自己下不了注，就会送到交易员这里。有风险的大钱我来赚，无风险的小钱让给他——利益分配达到一种「和谐」。<a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>

      <div class="scene">
        关系学精髓：找准定位，建立信任，各取所需；帮伙伴赚钱，自己才有更多机会。
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn8">
          <strong>⁸ 销售激励 vs 交易员激励（公开结构）</strong>
          公开招聘与薪酬讨论里，销售侧常强调客户覆盖、佣金/激励与产品推介；交易侧强调风险限额内的做市 P&amp;L。具体分成比例因公司、年份、产品线而异——书中 20% / 5% 是帮助学生理解「小钱确定性 vs 大钱风险性」的故事尺度，不是行业普查。监管侧持续关注的是对客户价格是否公平（G-30），而非内部谁拿提成。
          <div class="why">为何重要：把「多给七毛五」从人情上升到激励相容设计。</div>
          <div class="src">来源：S&amp;T 薪酬结构通识；MSRB G-30；公开试读奖金对比节拍（改写）</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">做人别小气：文森、抠门精与时代分寸</h2>
      <p>道理说透都浅显：关系学无非「做人别小气，有钱大家赚」。对渔阳却是思维方式飞跃。刚进鲁西时曾见文森对中介很大方——对方主动要把中介费零头抹掉，他都不同意。当时诧异：能省为何不省？后来明白：保持与中介的良好关系，才能在信息上抢先。文森「富 N 代」背景，热衷免费午餐，但该花时不手软；渔阳成长于物质相对匮乏年代，勤俭是美德——若把勤俭搬进交易，像「抠门精」那样锱铢必较、把销售当敌人，就大错特错。「干大事而惜身，见小利而忘命」，难成大器。</p>
      <p>再深一层：关系学的<strong>分寸</strong>随危机前后而变。利润率单薄的前危机时代，对销售确实不能太大方；利润率丰厚、需要拼命加快周转的后危机时代，销售是伙伴，是实现利益不可或缺的上下游。<a class="fn-link" href="#fn9"><sup class="fn">⁹</sup></a></p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Goldman_Sachs.svg" alt="高盛标志" loading="lazy" />
        <figcaption>高盛——公司箴言把「客户利益优先」写成可公开引用的文化坐标；本章借它对照「帮别人赚钱，自己才有机会」。来源：Wikimedia Commons</figcaption>
      </figure>

      <p>他想起高盛那句公开商业原则：如果我们为客户提供了优质服务，我们自己的成功就会随之而来。——不全是唱高调，其中大有道理。<a class="fn-link" href="#fn10"><sup class="fn">¹⁰</sup></a></p>

      <div class="scene">
        勤俭是生活美德；在交易里把销售当零和对手，是自己切断订单流。
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn9">
          <strong>⁹ 前危机 vs 后危机的「大方」阈值</strong>
          §22 已说明：危机前拼杠杆与薄利；危机后资本稀缺、中介价差更厚、周转更值钱。公开市场结构材料亦显示危机后做市能力收缩、交易成本与搜索成本上升——在这种环境下，「购买」销售注意力与订单路由，经济账更说得通。分寸随制度与价差制度而调，不是道德忽然变好。
          <div class="why">为何重要：防止读者把本章读成永恒鸡汤；它是周期条件句。</div>
          <div class="src">来源：§22 导读；MSRB 流动性 / 交易成本讨论；危机后做市研究综述</div>
        </div>
        <div class="fn-item" id="fn10">
          <strong>¹⁰ 高盛商业原则第一条（公开文本）</strong>
          高盛长期公开的 Business Principles 首条大意：客户利益永远放在第一位；经验表明，若我们服务好客户，我们自己的成功就会随之而来（"Our clients' interests always come first… if we serve our clients well, our own success will follow."）。1979 年 John Whitehead 整理的原则体系仍被公司治理文件引用。本章用它作文化对照，不是暗示任何非公开交易安排。
          <div class="why">为何重要：把中文「关系学」接到华尔街可核验的公开箴言。</div>
          <div class="src">来源：Goldman Sachs Business Principles（SEC 历史披露 / 公司行为准则公开页）</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">最铁一起分过赃：通向 §24</h2>
      <p>几年前中国流传过一首说「铁」的顺口溜：一起同过窗、一起扛过枪……最铁的，是一起分过赃。渔阳跟老滑、小滑、艾米、辛迪等人——在利益链上一起分过「赃」——所以最铁。这当然是玩笑口吻的比喻：合法中介租金与犯罪分赃不是一回事；点睛的是<strong>共同实现利益</strong>比空洞忠诚更黏合网络。</p>
      <p>华尔街画像至此更完整：监管画格子，P&amp;L 算分数，真正让订单流起来的，是一张张互惠的关系网。忠诚口号很动听；能持续的，是激励相容。下一章 §24「分久必合，合久必分」——网络会重组，合与分都按利益重新洗牌。<a class="fn-link" href="#fn11"><sup class="fn">¹¹</sup></a></p>

      <div class="scene">
        关系学读完：不是会做人，而是会站位——站在别人也需要你的那一环上。
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">本节脚注</div>
        <div class="fn-item" id="fn11">
          <strong>¹¹ 「关系 / 关系学」透镜与 §24 预告</strong>
          汉语「关系」在商业社会学里常被讨论为互惠网络、信任与资源交换（guanxi literature）。本章是用这副透镜读美国市政债 OTC，不是把华尔街等同于送礼饭局刻板印象。公开目录中 §23「关系学」紧接 §22「新市场，新思维」，其后 §24「分久必合，合久必分」——网络建好之后，合与分的组织叙事才会登场。
          <div class="why">为何重要：收束本章，并把读者注意力推向下一章的分合主题。</div>
          <div class="src">来源：公开 TOC（豆瓣 / 人大社目录）；guanxi 商业研究通识；FX110 试读收束节拍（改写）</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>人物关系 / 时间线 / 知识图谱</h2>

        <div class="mermaid-wrap">
          <div class="caption">利益分配链：政府卖家 → 销售路由 → 资本水库 → 零售泄洪</div>
          <div class="mermaid">
flowchart LR
  GOV[地方政府卖家] -->|单线便宜货| LG[领导哥们儿 销售]
  LG -->|可走虚线自家交易员| OWN[本公司交易员]
  LG -->|倒卖兑现| LH[老滑]
  LH -->|需要资本吃货| YY[渔阳 鲁西资本]
  YY -->|二次货源| LH
  YY -->|零售网| AM[艾米 美林]
  LH --> RET[零售经纪人]
  AM --> RET
  RET --> END[终端小投资者]
  YY --> NEXT[§24 分合]
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">时间线：关系学（西雅图馅饼 → 甜头日常 → §24）</div>
          <div class="mermaid">
timeline
    title Relationships Guanxi
    after §22 : Distribution net stands · need lubricant
    Friday : Seattle water offer · Xiao Hua then Lao Hua
    same day : Bid 2.92 · Amy marks 2.85
    hours : Partial sellback · Merrill print
    two days : Full distribution · shared spread
    later : Cindy 0.75 · buy order flow
    mindset : Guanxi equals interest chain
    bridge : Toward §24 merge and split
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">知识图谱：关系学核心概念</div>
          <div class="mermaid">
flowchart TB
  S22[§22 New markets] --> NET[Distribution net]
  NET --> Q[How does flow choose a path]
  Q --> GX[Relationships / guanxi]
  GX --> INT[Interest not banquets]
  INT --> CAP[Capital as scarce hinge]
  INT --> SAL[Sales channels]
  CAP --> YY[Trader warehouse]
  SAL --> FLOW[Order flow routing]
  FLOW --> SWEET[Leave sweets / markup share]
  SWEET --> TURN[Higher turnover ROE]
  TURN --> GS[Goldman client-first motto]
  TURN --> ERA[Post-crisis generosity dial]
  ERA --> S24[§24 Merge and split]
          </div>
        </div>
      </section>
'''

EN_BODY = r'''
      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/New_York_Stock_Exchange_September_2016_05.jpg" alt="New York Stock Exchange" loading="lazy" />
        <figcaption>NYSE—§22 built the “McDonald’s” distribution net; §23 asks what lubricates it: relationships, or interests? Source: Wikimedia Commons</figcaption>
      </figure>

      <h2 id="s1">Who you know: the OTC relationship net</h2>
      <p>After §22—new markets, new thinking, a McDonald’s-style franchise earning steady intermediation tolls—the next lesson is earthier and harder. What actually moves bonds from one side to the other on Wall Street? The American saying is blunt: it is not what you know, it is who you know. <a class="fn-link" href="#fn1"><sup class="fn">¹</sup></a></p>
      <p>Municipal bonds trade almost entirely <strong>over the counter</strong>: no central exchange auction like equities. Deals run on phones, Bloomberg messages, email, and acquaintance circles. A wide net and live color get you filled; a thin net and you never hear who is urgent to sell or buy. For Yuyang the most important commercial ties are the <strong>salespeople</strong> covering him at various dealers—they are both market eyes and pipes to end clients. <a class="fn-link" href="#fn2"><sup class="fn">²</sup></a></p>
      <p>Reading U.S. finance through a Chinese “guanxi” lens is not a stretch: clients, sales, traders, and regulators each occupy a node. Loyalty slogans hang on walls; what usually decides flow is who helps whom get paid.</p>

      <div class="side-panel">
        <h3 class="panel-title">Chapter anchors · post-crisis distribution days</h3>
        <div class="event-timeline">
          <div class="event-card"><div class="yr">After §22</div><div class="ev">Net built · needs lubricant</div></div>
          <div class="event-card"><div class="yr">Friday</div><div class="ev">Seattle water “pie”</div></div>
          <div class="event-card"><div class="yr">Two days</div><div class="ev">Pass-through · shared spread</div></div>
          <div class="event-card"><div class="yr">Daily</div><div class="ev">Sweets → turnover → §24</div></div>
        </div>
      </div>

      <div class="scene">
        OTC has no central square; the relationship net <em>is</em> the microstructure.
      </div>

      <div class="footnotes" id="fn-block-1">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn1">
          <strong>¹ “It's not what you know, it's who you know”</strong>
          The proverb is a staple of business and career talk: social capital often outweighs résumé skills. Public trial reads pin the chapter open on this line to frame OTC municipal desks—information and order flow travel along familiar phone lines. The footnote anchors the proverb and theme only; it does not paste long book dialogue.
          <div class="why">Why it matters: a cross-cultural door into “relationships”—not banquet stereotypes, but network-as-liquidity.</div>
          <div class="src">Source: English proverb usage; public TOC / FX110 beat map</div>
        </div>
        <div class="fn-item" id="fn2">
          <strong>² Muni OTC: phones, market-making, search costs</strong>
          Unlike equity exchanges, the U.S. municipal secondary market has long been OTC: investors route through dealers who either commit capital (principal) or search as agent. MSRB materials stress that liquidity is a search problem—who knows the buyer, who will show inventory. Salespeople are human routers in that search engine.
          <div class="why">Why it matters: “cultivating sales” is not soap opera; it is routing in microstructure.</div>
          <div class="src">Source: MSRB “How Are Municipal Bonds Priced?”; MSRB transaction-cost / liquidity notes</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s2">Lao Hua &amp; Xiao Hua: two grades of sales craft</h2>
      <p>Sales skill gaps are huge. The well-known “Lao Hua”—a senior salesperson at a regional dealer—makes counterparties feel he is thinking for them and helping them earn; afterward Bloomberg blotters often show he took a fat spread himself. Earning for yourself while leaving the client glad is real guanxi craft.</p>
      <p>Apprentice “Xiao Hua” sounds like the master; the craft is thinner—when he faces Yuyang, spreads get squeezed to the floor. Doing more business with both, Yuyang learns layers of “relationship”: not sweet talk, but making the other side feel the partnership <strong>pays</strong>.</p>

      <div class="scene">
        Masters make you feel helped; only later you see they helped themselves—and both can be true.
      </div>

      <div class="footnotes" id="fn-block-2">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn3">
          <strong>³ Sales vs traders: subtle conflict under one roof</strong>
          Fixed-income desks commonly split coverage (sales) from inventory and risk (traders). Public role write-ups note sales pay often tracks volume or intermediary revenue, while trader bonuses track book P&amp;L and risk contribution—incentives do not auto-align. Character nicknames are story labels; the footnote is about structure.
          <div class="why">Why it matters: foreshadows “Leadership Buddy” bypassing the house trader.</div>
          <div class="src">Source: IB Sales &amp; Trading role primers; continuity with §4 guide</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s3">Seattle water: a Friday pie from the sky</h2>
      <p>One quiet Friday afternoon, Xiao Hua brings “urgent intel”: a single-line client wants to sell about $8mm Seattle water bonds at a ~2.90% yield ask; he claims they are easily worth 2.80%—lower yield means higher price, so it sounds like free money. <a class="fn-link" href="#fn4"><sup class="fn">⁴</sup></a></p>
      <p>Yuyang checks structure and supply on Bloomberg: seasoned issue, popular structure, Seattle utility paper not over-abundant; the ask looks genuinely cheap. Too many past traps, though—he probes: who is the seller, why the fire sale? Xiao Hua goes mysterious—“not convenient to say”—and mystery smells like a snare.</p>
      <p>Within a minute Lao Hua himself is on the line: trust me, shade to about 2.92% and lift, but move. The veteran finally names it: a local-government seller, channel owned by their firm—perhaps some salesperson’s iron tie to an official unlocked the cheap lot. Yuyang bids and buys.</p>
      <p>Still uneasy, he asks Merrill sales Amy to mark it. He had already guessed: this structure often suits trust/retail channels. Amy calls back fast: her trader would bid about 2.85% to warehouse—several basis points of air already. <a class="fn-link" href="#fn5"><sup class="fn">⁵</sup></a></p>
      <p>He does not dump everything to Amy at once: loyalty matters—Lao Hua sourced it, so leave him a second swing. Lao Hua then offers two similar names; Yuyang shades and lifts the lot. Twenty-plus million of cheap paper in hand, pleased and puzzled: why do pies fall from the sky? Apples woke Newton; this pie only confuses him.</p>
      <p>Stranger still: within an hour Xiao Hua wants $2mm back—a retail broker needs them. Yuyang offers 2.80%; Xiao Hua flinches at the jump. Yuyang returns the earlier pitch, then eases to 2.82% “friendship.” Face given, he rings Amy: with that print as mark, Merrill’s net works several million at the same level. He loops Lao Hua—“I saved you a piece”—and Lao Hua must hustle the rest.</p>
      <p>Within two days the bonds clear through Lao Hua and Amy; he banks on the order of <strong>~$150,000</strong>. Not cosmic—but a win-win: Lao Hua books round-trip commission, Amy earns and looks good, Yuyang takes the pass-through and deepens the tie.</p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Seattle_skyline_from_Kerry_Park.jpg" alt="Seattle skyline" loading="lazy" />
        <figcaption>Seattle skyline—utility revenue bonds (water, etc.) often fit retail/trust “easy-to-place” demand. Source: Wikimedia Commons</figcaption>
      </figure>

      <div class="scene">
        Pies do not confuse forever; what wakes you is: why am I on this chain at all?
      </div>

      <div class="footnotes" id="fn-block-3">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn4">
          <strong>⁴ Yield vs price: muni quoting intuition</strong>
          For fixed-coupon bonds, higher required yield → lower price; lower yield → higher price. A seller “asking 2.90%” while a buyer thinks “worth 2.80%” means the seller’s price looks cheap (willing to sell at a higher yield). MSRB investor education uses this duality for secondary haggling. Story yields are rewrite scale; the footnote is the language only.
          <div class="why">Why it matters: you need yield-speech to follow distribution spreads.</div>
          <div class="src">Source: MSRB muni pricing education; fixed-income primers</div>
        </div>
        <div class="fn-item" id="fn5">
          <strong>⁵ Utility bonds and retail/trust preference</strong>
          Water/power revenue bonds often carry an intuitive cash-flow story and structures suited to mid-ticket retail placement, so they show up in broker retail and trust channels. Market-structure notes stress: new issues get syndicate support; seasoned paper needs whoever knows the end buyer. A Merrill-scale retail net plays “drain”—kin to §22’s regional wolf pack.
          <div class="why">Why it matters: why Amy is the first call after the lift, not only Street-to-Street.</div>
          <div class="src">Source: muni revenue-bond primers; MSRB secondary liquidity; public trial-read beat (rewritten)</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s4">The profit chain: why capital is the hinge</h2>
      <p>Pleasure turns into a question: Lao Hua has relationships, Amy has channels—why do I skim ~$150k? Then it clicks—he is the <strong>hinge link in the interest-distribution chain</strong>. <a class="fn-link" href="#fn6"><sup class="fn">⁶</sup></a></p>
      <p>Capsule: a local-government body sells a packet ~20 bp cheap to the Street; Wall Street distributes quickly to small investors a bit rich to mid-market. Roughly ~25 bp is the pie; occupy a distribution node and you share it.</p>
      <p>The government account sits single-line with a powerful salesperson at Lao Hua’s firm—“Leadership Buddy.” Iron ties still need a sale to become commission. He could warehouse via his house trader—but then the fat goes to the trader. Ideal for sales: bypass the house book, flip via another sales path, crystallize P&amp;L, split. Who can eat twenty million fast? Lao Hua thinks of Yuyang: quick, capital-rich, and a <strong>trader</strong>—buys today must sell tomorrow, so Lao Hua still owns the scarce-goods channel for a second print. An investor might sleep on the bonds; a trader is a live reservoir.</p>
      <p>Once on Yuyang’s sheet: some flow back through Lao Hua to retail (reciprocity); some through Amy’s Merrill net (speed, relationship, and competitive pricing). Rough split: Leadership Buddy + Lao Hua ~10 bp, Yuyang ~10 bp, second sales/Amy/retail brokers ~5 bp. He can hold the hinge because he controls what sales lack: <strong>capital</strong>—Lucy Bank’s balance sheet.</p>
      <p>Odder still: sales-comp systems can put sales at odds with <strong>their own firm</strong>. If the house trader warehouses the cheap lot, visible sales value is fuzzy and the cut is token; flipping at +10 bp to an outside trader crystallizes commission now plus a second-trade option. Lao Hua plays “Lei Feng” with pies because Yuyang helps him get paid.</p>

      <div class="scene">
        Relationship is interest; a hinge seat beats shoulder-slapping brotherhood.
      </div>

      <div class="footnotes" id="fn-block-4">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn6">
          <strong>⁶ Basis points, markups, and “fair and reasonable”</strong>
          One basis point = 0.01%. In muni OTC, dealer compensation often embeds in all-in markup/markdown; agency trades charge an explicit commission. MSRB Rule G-30 requires fair and reasonable prices/commissions given market judgment, expense, and a right to profit. Trial reads use a “~25 bp distribution pie” to teach splitting—the footnote supplies the regulatory vocabulary, not a market census of the story numbers.
          <div class="why">Why it matters: plugs “sharing the spoils” into public rules: the spread is scrutinized intermediation rent.</div>
          <div class="src">Source: MSRB Rule G-30; MSRB pricing education; public trial-read chain beat (rewritten)</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s5">Guanxi is interest: turnover, sweets, path choice</h2>
      <p>Once the logic is clear, guanxi turns simple: the best way to “work relationships” is not banquets and back-slapping—it is occupying a hinge on the interest chain, helping others realize theirs while realizing yours.</p>
      <p>§22 already said via DuPont: post-crisis margins are decent, so raise turnover. On the guanxi operating surface: cultivate sales everywhere so more bonds <strong>pass through</strong> you. Many distribution paths exist; how to pull flow onto yours? Most effective: <strong>sweeten the route</strong>—leave sales room to earn so they send tickets your way. <a class="fn-link" href="#fn7"><sup class="fn">⁷</sup></a></p>

      <div class="scene">
        Theory says turnover; practice says: make routing pass through you—and make the router willing.
      </div>

      <div class="footnotes" id="fn-block-5">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn7">
          <strong>⁷ DuPont and the operating face of guanxi</strong>
          DuPont splits ROE into margin × turnover × leverage. §§5/22 already argued: when leverage is capped and margins still exist, accelerating asset turns is the path. “Let bonds pass through me” is the micro turn; leaving sales a sweet is the explicit cost of buying order flow—small certain cost for larger expected volume. The footnote links prior chapters; it does not publish non-public client lists.
          <div class="why">Why it matters: proves guanxi is not mysticism—it is ROE accounting projected onto people.</div>
          <div class="src">Source: §5 / §22 guides; corporate-finance DuPont primers</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s6">Cindy's seventy-five cents: harmony in bonuses</h2>
      <p>One day mid-size-dealer sales Cindy calls to vent: $10mm Georgia gas bonds—Yuyang already lifted the 3.50% ask—yet the seller will not pay even a broker’s fee. Mid-career, with a difficult kid at home, she vents; today she is also unlucky—the other side is stone-broke on fees.</p>
      <p>“If you can pay me fifty cents per bond, we can print.” Fifty cents on a $1,000 face—Lao Hua would open at a dollar. Yuyang improvises: you found the ticket—I’ll pay seventy-five. An extra ~$2,500; Cindy thanks him warmly. Afterward she is keen on his flow; hot deals her firm leads often tilt his way. “They all like you”—who doesn’t like the person who pays?</p>
      <p>Incentive design explains it. Sales cannot casually take big directional bets; they earn steadier intermediary nickels, often at a higher payout ratio (story-scale ~20% at smaller firms). Traders can bet firm capital for larger P&amp;L, often at a lower payout ratio (story-scale ~5%). Five thousand means little to Yuyang and a lot as relationship capital so sales can pocket ~$1,000; when a ~$100k ticket with a mild edge appears, sales cannot warehouse it—so it routes to the trader. Risky big money on his book; riskless small money to them—a kind of harmony. <a class="fn-link" href="#fn8"><sup class="fn">⁸</sup></a></p>

      <div class="scene">
        Guanxi’s core: find your seat, build trust, take what each needs; help partners earn, and more tickets follow.
      </div>

      <div class="footnotes" id="fn-block-6">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn8">
          <strong>⁸ Sales vs trader incentives (public structure)</strong>
          Public hiring and pay talk usually ties sales to coverage, commissions/incentives, and product placement; traders to market-making P&amp;L inside risk limits. Exact splits vary by firm, year, and product—the book’s 20%/5% is teaching scale for “certain small vs risky large,” not a survey. Regulators watch whether customer prices are fair (G-30), not who pockets the internal cut.
          <div class="why">Why it matters: upgrades “extra twenty-five cents” from niceness to incentive compatibility.</div>
          <div class="src">Source: S&amp;T pay-structure primers; MSRB G-30; public trial-read bonus beat (rewritten)</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s7">Don't be stingy: Vincent, the miser, era dial</h2>
      <p>Once said aloud, the doctrine is plain: guanxi is little more than “don’t be stingy—let everyone eat.” For Yuyang it is still a mindset leap. Early at Lucy he watched Vincent stay generous with brokers—even refusing when the other side offered to waive a fee stub. Why not save? Later: keep the broker warm to win information races. Vincent’s “rich Nth generation” background loves a free lunch yet spends when it counts; Yuyang grew up tighter with money—thrift is a virtue in life, a vice if you treat sales as zero-sum enemies like the “miser” on the Georgia ticket. Spare the body for great affairs, forget life for petty gain—and you stay small.</p>
      <p>Deeper: the <strong>dial</strong> of guanxi shifts across the crisis. In the thin-margin pre-crisis years, you could not be too generous to sales; in the fat-margin, turn-or-die post-crisis years, sales are partners—upstream and downstream of realizing interest. <a class="fn-link" href="#fn9"><sup class="fn">⁹</sup></a></p>

      <figure class="figure">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Goldman_Sachs.svg" alt="Goldman Sachs logo" loading="lazy" />
        <figcaption>Goldman—public Business Principles make “clients first” a citable cultural coordinate; this chapter pairs it with “help others earn so you earn.” Source: Wikimedia Commons</figcaption>
      </figure>

      <p>He recalls Goldman’s public principle: if we serve our clients well, our own success will follow—not only piety; there is operating truth in it. <a class="fn-link" href="#fn10"><sup class="fn">¹⁰</sup></a></p>

      <div class="scene">
        Thrift is a life virtue; treating sales as zero-sum in trading cuts your own order flow.
      </div>

      <div class="footnotes" id="fn-block-7">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn9">
          <strong>⁹ Pre- vs post-crisis “generosity” budgets</strong>
          §22 already: pre-crisis competed on leverage and thin margins; post-crisis scarce capital, thicker intermediation spreads, turnover more valuable. Public structure work also shows post-crisis market-making capacity and search costs shifting—“buying” sales attention and routing pencils out better. The dial follows institutions and spreads, not a sudden moral upgrade.
          <div class="why">Why it matters: stops readers from mistaking the chapter for timeless chicken soup; it is a cyclical conditional.</div>
          <div class="src">Source: §22 guide; MSRB liquidity/cost notes; post-crisis market-making surveys</div>
        </div>
        <div class="fn-item" id="fn10">
          <strong>¹⁰ Goldman Business Principle #1 (public text)</strong>
          Goldman’s long-published Business Principles open roughly: clients’ interests always come first; experience shows that if we serve clients well, our own success follows. John Whitehead’s 1979 framing still appears in firm governance materials. The chapter uses it as cultural contrast—not as evidence of any non-public trade arrangement.
          <div class="why">Why it matters: docks Chinese “guanxi” to a verifiable Wall Street motto.</div>
          <div class="src">Source: Goldman Sachs Business Principles (historical SEC disclosures / public code pages)</div>
        </div>
      </div>

      <hr class="divider" />

      <h2 id="s8">Strongest bond: sharing the spoils → §24</h2>
      <p>A Chinese doggerel about “iron” bonds once circulated: classmates, army buddies… the strongest iron is those who split the spoils together. Yuyang with Lao Hua, Xiao Hua, Amy, Cindy—having shared the chain’s “spoils”—are iron. Joke register only: lawful intermediation rent is not crime; the point is that <strong>co-realized interest</strong> glues networks tighter than empty loyalty.</p>
      <p>The Wall Street portrait is fuller: regulators draw grids, P&amp;L keeps score, but reciprocal nets move tickets. Loyalty slogans sound fine; what lasts is incentive compatibility. Next, §24 “Long divided must unite; long united must divide”—networks reorganize; merge and split reshuffle by interest. <a class="fn-link" href="#fn11"><sup class="fn">¹¹</sup></a></p>

      <div class="scene">
        Guanxi finished: not “be nice”—be seated where others need you on the chain.
      </div>

      <div class="footnotes" id="fn-block-8">
        <div class="fn-head">Section notes</div>
        <div class="fn-item" id="fn11">
          <strong>¹¹ The guanxi lens and the §24 preview</strong>
          Chinese <em>guanxi</em> in business sociology often means reciprocal networks, trust, and resource exchange. This chapter reads U.S. muni OTC through that lens—not the banquet-and-gift stereotype of Wall Street. Public TOC places §23「关系学」after §22 and before §24「分久必合，合久必分」—once the net exists, organizational merge/split narratives arrive.
          <div class="why">Why it matters: closes the chapter and points attention to the next theme of division and reunion.</div>
          <div class="src">Source: public TOC (Douban / CUP catalog); guanxi business literature primers; FX110 closing beat (rewritten)</div>
        </div>
      </div>

      <section class="diagrams-section" id="diagrams">
        <h2>Relationships / timeline / knowledge graph</h2>

        <div class="mermaid-wrap">
          <div class="caption">Interest chain: government seller → sales routing → capital reservoir → retail drain</div>
          <div class="mermaid">
flowchart LR
  GOV[Local gov seller] -->|single-line cheap lot| LG[Leadership Buddy sales]
  LG -->|dashed: house trader| OWN[House trader]
  LG -->|flip to crystallize| LH[Lao Hua]
  LH -->|needs capital lift| YY[Yuyang Lucy capital]
  YY -->|second supply| LH
  YY -->|retail net| AM[Amy Merrill]
  LH --> RET[Retail brokers]
  AM --> RET
  RET --> END[End retail investors]
  YY --> NEXT[§24 merge split]
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Timeline: Relationships (Seattle pie → daily sweets → §24)</div>
          <div class="mermaid">
timeline
    title Relationships Guanxi
    after §22 : Distribution net stands · need lubricant
    Friday : Seattle water offer · Xiao Hua then Lao Hua
    same day : Bid 2.92 · Amy marks 2.85
    hours : Partial sellback · Merrill print
    two days : Full distribution · shared spread
    later : Cindy 0.75 · buy order flow
    mindset : Guanxi equals interest chain
    bridge : Toward §24 merge and split
          </div>
        </div>

        <div class="mermaid-wrap">
          <div class="caption">Knowledge graph: Relationships core ideas</div>
          <div class="mermaid">
flowchart TB
  S22[§22 New markets] --> NET[Distribution net]
  NET --> Q[How does flow choose a path]
  Q --> GX[Relationships / guanxi]
  GX --> INT[Interest not banquets]
  INT --> CAP[Capital as scarce hinge]
  INT --> SAL[Sales channels]
  CAP --> YY[Trader warehouse]
  SAL --> FLOW[Order flow routing]
  FLOW --> SWEET[Leave sweets / markup share]
  SWEET --> TURN[Higher turnover ROE]
  TURN --> GS[Goldman client-first motto]
  TURN --> ERA[Post-crisis generosity dial]
  ERA --> S24[§24 Merge and split]
          </div>
        </div>
      </section>
'''

def main():
    zh = page(
        "zh",
        "《乱世华尔街》第23集：关系学",
        "故事导读 · 据公开试读改写 · 场外研究补充",
        "关系学",
        "《乱世华尔街》第二十三章「关系学」· 渔阳 · 故事改写 + 脚注研究 · 第四部分「峰回路转」",
        "下面按作者经历与公开时间线讲述本章故事，用自己的话改写，方便跟读；不是全书/全章原文照搬。脚注、配图与知识图谱为场外公开资料补充。完整内容请读正版。",
        ZH_TOC,
        "CHAPTER TWENTY-THREE · 关系学 · 第四部分 峰回路转",
        ZH_BODY,
        "《乱世华尔街》· 渔阳 · 第二十三章故事导读（原创改写）",
    )
    en = page(
        "en",
        "Chaos on Wall Street §23: Relationships",
        "Story guide · rewritten from public trial reads · off-book research",
        "Relationships",
        "Chaos on Wall Street, Chapter 23 “Relationships” (Guanxi) · Yuyang · story rewrite + footnote research · Part 4 “The Road Turns”",
        "A story-first retelling from the author’s arc and public timelines, in our own words for guided reading—not a verbatim copy of the copyrighted chapter. Footnotes, figures, and graphs are off-book public research. For the full text, support the official edition.",
        EN_TOC,
        "CHAPTER TWENTY-THREE · Relationships · Part 4 The Road Turns",
        EN_BODY,
        "Chaos on Wall Street · Yuyang · Ch.23 story guide (original rewrite)",
    )
    (DIR / "relationships-zh.html").write_text(zh, encoding="utf-8")
    (DIR / "relationships-en.html").write_text(en, encoding="utf-8")
    print("Wrote", DIR / "relationships-zh.html", len(zh))
    print("Wrote", DIR / "relationships-en.html", len(en))

if __name__ == "__main__":
    main()
