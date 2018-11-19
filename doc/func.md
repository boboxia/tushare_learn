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


38 get_debtpaying_data
39 get_deposit_rate

40 get_fund_info
41 get_future_daily
42 get_gdp_contrib
43 get_gdp_for
44 get_gdp_pull
45 get_gdp_quarter
46 get_gdp_year
47 get_gem_classified
48 get_gold_and_foreign_reserves
49 get_growth_data
50 get_h_data
51 get_hist_data
52 get_hists
53 get_hs300s
54 get_index
55 get_industry_classified
56 get_instrument
57 get_intlfuture
58 get_k_data
59 get_latest_news
60 get_loan_rate
61 get_markets
62 get_money_supply
63 get_money_supply_bal
64 get_nav_close
65 get_nav_grading
66 get_nav_history
67 get_nav_open
68 get_notices
69 get_operation_data
70 get_ppi
71 get_profit_data
72 get_profit_statement
73 get_realtime_quotes
74 get_report_data
75 get_rrr
76 get_shfe_daily
77 get_shfe_vwap
78 get_sina_dd
79 get_sme_classified
80 get_st_classified
81 get_stock_basics
82 get_suspended
83 get_sz50s
84 get_terminated
85 get_tick_data
86 get_today_all
87 get_today_ticks
88 get_token
89 get_zz500s
90 global_realtime
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