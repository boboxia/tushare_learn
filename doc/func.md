---
title:vscode中markdown
tags:vscode markdown
notebook :blogs
---

# tushare中的主要函数
>tushare的内置函数，不是api的函数，与api的函数有重叠但也以后不一样的地方
##函数清单(字母序)
MailMerge,合并邮件输出
TraderAPI，股票实盘交易接口，用于下单买入卖出的
bar，交易数据接口 ，
MACD的一个辅助指标——柱状线 (BAR)。在大多数技术分析软件中，柱状线是有颜色的，在低于0轴以下是绿色，高于0轴以上是红色，前者代表趋势较弱，后者代表趋势较强。 
~~~
获取连接备用
cons = ts.get_apis()
指数日行情, 设置asset='INDEX'
df = ts.bar('000300', conn=cons, asset='INDEX', start_date='2016-01-01', end_date='')
股票日线行情
df = ts.bar('600000', conn=cons, freq='D', start_date='2016-01-01', end_date='')
带因子的行情
factors因子数据，目前支持以下两种：
vr:量比,默认不返回，返回需指定：factor=['vr']
tor:换手率，默认不返回，返回需指定：factor=['tor']
以上两种都需要：factor=['vr', 'tor']
adj:复权类型,None不复权,qfq:前复权,hfq:后复权
ma:均线,支持自定义均线频度，如：ma5/ma10/ma20/ma60/maN
df = ts.bar('600000', conn=cons, start_date='2016-01-01', end_date='', ma=[5, 10, 20], factors=['vr', 'tor'])
复权行情, adj=qfq(前复权)， hfq（后复权），默认None不复权
df = ts.bar('600000', conn=cons, adj='qfq', start_date='2016-01-01', end_date='')
分钟数据, 设置freq参数，分别为1min/5min/15min/30min/60min，D(日)/W(周)/M(月)/Q(季)/Y(年)
df = ts.bar('600000', conn=cons, freq='1min', start_date='2016-01-01', end_date='')
期货数据, 设置asset='X'
df = ts.bar('CU1801', conn=cons, asset='X', start_date='2016-01-01', end_date='')
港股数据, 设置asset='X'
df = ts.bar('00981', conn=cons, asset='X', start_date='2016-01-01', end_date='')
美股数据, 设置asset='X'
df = ts.bar('BABA', conn=cons, asset='X', start_date='2016-01-01', end_date='')
df.head(5)
~~~

bdi,龙虎榜数据

broker_tops,龙虎榜数据，获取营业部近5、10、30、60日上榜次数、累积买卖等情况。好像没什么大作用
如平安证券有限责任公司深圳深南东路罗湖商务中心证券营业部

cap_tops，获取个股上榜统计数据，获取近5、10、30、60日个股上榜统计数据,包括上榜次数、累积购买额、累积卖出额、净额、买入席位数和卖出席位数。有用

close_apis,关闭连接

coins_bar,获取各类k线数据,返回日期时间，开盘价，最高价，最低价，收盘价，成交量

coins_snapshot,获取实时快照数据
coins_tick,币市行情，实时tick行情
coins_trade,币市行情，获取实时交易数据,
day_boxoffice,获取单日电影票房数据
day_cinema,获取影院单日票房排行数据
forecast_data,获取业绩预告数据
返回，股票代码,名称，业绩变动类型【预增、预亏等】，发布日，上年同期每股收益，业绩变动范围
fund_holdings,获取基金持股数据,
返回,股票代码,名称,报告日期,基金家数与上期相比（增加或减少了）,基金持股数（万股）,与上期相比,基金持股市值,占流通盘比率

get_apis()建立连接
get_area_classified,获取地域分类数据
get_balance_sheet,获取某股票的历史所有时期资产负债表
get_cash_flow,获取某股票的历史所有时期现金流表
get_cashflow_data,获取现金流量数据
返回,股票代码,名称,经营现金净流量对销售收入比率,资产的经营现金流量回报率,经营现金净流量与净利润的比率,经营现金净流量对负债比率,现金流量比率
get_cffex_daily,获取中金所日交易数据
返回,合约代码,日期,开盘价,最高价,最低价,收盘价,成交量,持仓量,成交额,结算价,前结算价,合约类别
get_concept_classified,获取概念分类数据
返回,股票代码,股票名称,概念名称
get_cpi,获取居民消费价格指数数据,
返回,统计月份,价格指数
get_czce_daily,获取郑商所日交易数据(期货)
返回,合约代码,日期,开盘价,最高价,最低价,收盘价,成交量,持仓量,成交额,结算价,前结算价,合约类别
或者
合约代码,日期,开盘价,最高价,最低价,收盘价, 前结算价,结算价, 对冲值  , 成交量,持仓量,持仓变化,成交额,隐含波动率, 行权量,合约类别

get_day_all,获取每日收盘行情
返回,股票代码, 名称, 涨幅%,现价, 涨跌, 今开, 最高,最低, 昨收, 市盈(动),量比,换手%, 振幅%%,总量,  内盘, 外盘, 总金额,总股本(万), 细分行业,地区, 流通股本(万), 流通市值, AB股总市值, 均价,  强弱度%,活跃度,  笔换手, 攻击波%,近3月涨幅 ,近6月涨幅

get_dce_daily, 获取大连商品交易所日交易数据(期货)
返回大商所日交易数据(DataFrame): 合约代码,日期,开盘价, 最高价,最低价,收盘价,成交量,持仓量,成交额,结算价,前结算价,合约类别
或者郑商所每日期权交易数据
合约代码， 日期，开盘价，最高价，最低价，收盘价，前结算价，结算价， 对冲值  ， 成交量， 持仓量，持仓变化， 成交额， 隐含波动率， 行权量，合约类别

get_debtpaying_data,获取偿债能力数据
返回,代码,名称,流动比率,速动比率,现金比率,利息支付倍数,股东权益比率,股东权益增长率

get_deposit_rate,获取存款利率数据,
返回,变动日期,存款种类,利率（%）

get_fund_info,获取基金基本信息
返回,基金全称,基金简称,基金代码,成立日期,上市日期,存续期限,上市地点,运作方式,基金类型,二级分类,基金规模(亿元),基金总份额(亿份),上市流通份额(亿份),基金份额日期,上市季度,基金管理人,基金托管人

get_future_daily,获取中金所日交易数据
返回,  合约代码,日期,开盘价,最高价,最低价, 收盘价,成交量, 持仓量,成交额,结算价,前结算价,合约类别

get_gdp_contrib,获取三大产业贡献率数据
返回,统计年度,国内生产总值,第一产业献率(%),第二产业献率(%),其中工业献率(%),第三产业献率(%)

get_gdp_for,获取三大需求对GDP贡献数据
返回,统计年度,最终消费支出贡献率(%),最终消费支出拉动(百分点),资本形成总额贡献率(%),资本形成总额拉动(百分点),货物和服务净出口贡献率(%),货物和服务净出口拉动(百分点)

get_gdp_pull,获取三大产业对GDP拉动数据
返回,统计年度,国内生产总值同比增长(%),第一产业拉动率(%),第二产业拉动率(%),其中工业拉动(%),第三产业拉动率(%)

get_gdp_quarter,获取季度国内生产总值数据
返回,季度,国内生产总值(亿元),国内生产总值同比增长(%),第一产业增加值(亿元),第一产业增加值同比增长(%),第二产业增加值(亿元),第二产业增加值同比增长(%),第三产业增加值(亿元),第三产业增加值同比增长(%)

get_gdp_year,获取年度国内生产总值数据
返回,统计年度,国内生产总值(亿元),人均国内生产总值(元),国民生产总值(亿元),第一产业(亿元),第二产业(亿元),工业(亿元),建筑业(亿元),第三产业(亿元),交通运输仓储邮电通信业(亿元),批发零售贸易及餐饮业(亿元)

get_gem_classified,获取创业板股票
返回, 股票代码,股票名称

get_gold_and_foreign_reserves,获取外汇储备
返回,统计时间,黄金储备(万盎司),外汇储备(亿美元)

get_growth_data,获取成长能力数据
返回,股票代码,名称,主营业务收入增长率(%),净利润增长率(%),净资产增长率,总资产增长率,每股收益增长率,股东权益增长率

get_h_data,获取历史复权数据
autype:string,复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
drop_factor : bool, 默认 True 是否移除复权因子，在分析过程中可能复权因子意义不大，但是如需要先储存到数据库之后再分析的话，有该项目会更加灵活

返回,交易日期 (index),open 开盘价,最高价,收盘价,最低价,成交量,成交金额

get_hist_data,获取个股历史交易记录
ktype：string 数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D
返回,日期 ，开盘价， 最高价， 收盘价， 最低价， 成交量， 价格变动 ，涨跌幅，5日均价，10日均价，20日均价，5日均量，10日均量，20日均量，换手率

get_hists,批量获取历史行情数据，具体参数和返回数据类型请参考get_hist_data接口

get_hs300s,获取沪深300当前成份股及所占权重
返回,股票代码,股票名称,日期,权重

get_index,获取大盘指数行情
返回,指数代码,指数名称,涨跌幅,开盘价,昨日收盘价,收盘价,最高价,最低价,成交量(手),成交金额（亿元）

get_industry_classified,获取行业分类数据
返回,股票代码,股票名称,行业名称

get_instrument,获取证券列表
get_intlfuture,
get_k_data,获取k线数据
返回,交易日期 (index),开盘价,最高价,收盘价,最低价,成交量,成交额,换手率,股票代码

get_latest_news,获取即时财经新闻
返回,新闻类别,新闻标题,发布时间,新闻链接,新闻内容（在show_content为True的情况下出现）

get_loan_rate,获取贷款利率数据
返回,执行日期,存款种类,利率（%）
get_markets,获取市场代码

get_money_supply,获取货币供应量数据
返回,month :统计时间
m2 :货币和准货币（广义货币M2）(亿元)
m2_yoy:货币和准货币（广义货币M2）同比增长(%)
m1:货币(狭义货币M1)(亿元)
m1_yoy:货币(狭义货币M1)同比增长(%)
m0:流通中现金(M0)(亿元)
m0_yoy:流通中现金(M0)同比增长(%)
cd:活期存款(亿元)
cd_yoy:活期存款同比增长(%)
qm:准货币(亿元)
qm_yoy:准货币同比增长(%)
ftd:定期存款(亿元)
ftd_yoy:定期存款同比增长(%)
sd:储蓄存款(亿元)
sd_yoy:储蓄存款同比增长(%)
rests:其他存款(亿元)
rests_yoy:其他存款同比增长(%)

get_money_supply_bal,获取货币供应量(年底余额)数据
返回,year :统计年度
m2 :货币和准货币(亿元)
m1:货币(亿元)
m0:流通中现金(亿元)
cd:活期存款(亿元)
qm:准货币(亿元)
ftd:定期存款(亿元)
sd:储蓄存款(亿元)
rests:其他存款(亿元)

get_nav_close,获取封闭型基金净值数据
返回,开放型基金净值数据(DataFrame):
基金代码,基金名称,单位净值,累计净值,增长率(%),折溢价率(%),净值日期,成立日期,到期日期,基金经理,基金类型,基金总份额
get_nav_grading,获取分级子基金净值数据
type:string
            封闭基金类型:
                1. all      所有分级基金
                2. fjgs     分级-固收
                3. fjgg     分级-杠杆

        sub_type:string
            基金子类型(type=all sub_type无效):
                *all    全部分级债券
                *wjzq   稳健债券型
                *czzq   纯债债券型
                *jjzq   激进债券型
                *gp     股票型
                *zs     指数型
返回,开放型基金净值数据(DataFrame):
基金代码,基金名称,单位净值,累计净值,增长率(%),折溢价率(%),净值日期,成立日期,到期日期,基金经理,基金类型,基金总份额

get_nav_history,获取历史净值数据
返回date 发布日期 (index)
value 基金净值(股票/混合/QDII型基金) / 年华收益(货币/债券基金)
total 累计净值(股票/混合/QDII型基金) / 万分收益(货币/债券基金)
change 净值增长率(股票/混合/QDII型基金)

get_nav_open,获取开放型基金净值数据
type:string 开放基金类型:
1. all 		所有开放基金
2. equity	股票型开放基金
3. mix 		混合型开放基金
4. bond		债券型开放基金
5. monetary	货币型开放基金
6. qdii		QDII型开放基金

返回,开放型基金净值数据(DataFrame):
基金代码,基金名称,单位净值,累计净值,前一日净值,涨跌额,增长率(%),净值日期,基金经理,基金类型,基金总份额

get_notices,个股信息地雷
返回,信息标题,信息类型,公告日期,信息内容URL

get_operation_data,获取营运能力数据
返回,代码,名称,应收账款周转率(次),应收账款周转天数(天),存货周转率(次),存货周转天数(天),流动资产周转率(次),流动资产周转天数(天)

get_ppi,获取工业品出厂价格指数数据
返回,统计月份
ppiip :工业品出厂价格指数
ppi :生产资料价格指数
qm:采掘工业价格指数
rmi:原材料工业价格指数
pi:加工工业价格指数    
cg:生活资料价格指数
food:食品类价格指数
clothing:衣着类价格指数
roeu:一般日用品价格指数
dcg:耐用消费品价格指数

get_profit_data,获取盈利能力数据
返回,代码,名称,净资产收益率(%),净利率(%),毛利率(%),净利润(万元)
,每股收益,营业收入(百万元),每股主营业务收入(元)

get_profit_statement,获取某股票的历史所有时期利润表
get_realtime_quotes,获取实时交易数据 getting real time quotes data
用于跟踪交易情况（本次执行的结果-上一次执行的数据）
get_report_data,获取业绩报表数据
股票代码,名称,每股收益,每股收益同比(%),每股净资产,净资产收益率(%),每股现金流量(元),净利润(万元),净利润同比(%),分配方案,发布日期

get_rrr,获取存款准备金率数据
变动日期,调整前存款准备金率(%),调整后存款准备金率(%),调整幅度(%)

get_shfe_daily,获取上期所日交易数据
合约代码,日期, 开盘价,最高价,最低价,收盘价,成交量,持仓量,成交额,结算价,前结算价,合约类别

get_shfe_vwap,获取上期所日成交均价数据
郑商所日交易数据(DataFrame):
合约代码, 日期,时段，分09:00-10:15和09:00-15:00两类,加权平均成交均价

get_sina_dd,获取sina大单数据
当日所有股票交易数据(DataFrame)
股票代码,股票名称,交易时间,价格,成交量,前一笔价格,类型（买、卖、中性盘）

get_sme_classified,获取中小板股票
股票代码,股票名称
get_st_classified,获取风险警示板股票
股票代码,股票名称

get_stock_basics,获取沪深上市公司基本情况
返回,股票代码,名称,细分行业,地区,市盈率,流通股本,总股本(万),总资产(万)
,流动资产,固定资产,公积金,每股公积金,每股收益,每股净资,市净率,上市日期

get_suspended,获取暂停上市股票列表
返回,股票代码,股票名称,上市日期,终止上市日期 

get_sz50s,获取上证50成份股
返回,日期,股票代码,股票名称

get_terminated,获取终止上市股票列表
返回,股票代码,股票名称,上市日期,终止上市日期 

get_tick_data, 获取分笔数据
返回,当日所有股票交易数据
成交时间、成交价格、价格变动，成交手、成交金额(元)，买卖类型

get_today_all,一次性获取最近一个日交易日所有股票的交易数据
返回，股票代码，名称，涨跌幅，现价，开盘价，最高价，最低价，最日收盘价，成交量，换手率，成交额，市盈率，市净率，总市值，流通市值

get_today_ticks,获取当日分笔明细数据
返回,当日所有股票交易数据(DataFrame)
成交时间、成交价格、价格变动，成交手、成交金额(元)，买卖类型

get_token,设置配置口令
get_zz500s,获取中证500成份股
返回，日期，股票代码，股票名称，权重

global_realtime,全球实时指数




91 guba_sina
92 inst_detail
93 inst_tops
94 internet
95 is_holiday
96 latest_content
97 lpr_data
98 lpr_ma_data
99 margin_detail
100 margin_offset
101 margin_target
102 margin_zsl
103 moneyflow_hsgt
104 month_boxoffice
105 new_cbonds
106 new_stocks
107 notice_content
108 os
109 pledged_detail
110 pro
111 pro_api
112 pro_bar
113 profit_data
114 profit_divis
115 quotes
116 realtime_boxoffice
117 reset_instrument
118 set_token
119 sh_margin_details
120 sh_margins
121 shibor_data
122 shibor_ma_data
123 shibor_quote_data
124 stock
125 stock_issuance
126 stock_pledged
127 sz_margin_details
128 sz_margins
129 tick
130 top10_holders
131 top_list
132 trade_cal
133 trader
134 util
135 xsg_data