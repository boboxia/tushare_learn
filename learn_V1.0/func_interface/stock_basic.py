# -*- coding: utf-8 -*-

# =================================================
# @Time : 2018/11/14 22:15 
# @Author : zhoulinbin <zhoulinbin@jd.com> 
# @Site :  
# @File : stock_basic.py 
# @Software: PyCharm
# @Object: PyCharm
# @Desc :沪深股，基础数据之股票列表
# @Tip :
# =================================================
from pyecharts import Kline
import tushare as ts
import pandas as pd
import numpy as np
import datetime
def learn_stock_basic(pro):
    pro = ts.pro_api()







if __name__ == "__main__":

    pro=ts.pro_api('ef97d7049d0b35b46a15dd10b6d973ea4d998f07d565e8b1b7c1decd')

    #data=pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    #print data
    ts.set_token('ef97d7049d0b35b46a15dd10b6d973ea4d998f07d565e8b1b7c1decd')
    data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    #data=ts.get_stock_basics('2018-11-15')

    #print  data
    #print(dir(ts))


    # pro = ts.pro_api()
    # df1 = pro.daily(ts_code='000938.SZ', start_date='20150401', end_date='20180930')
    # df = df1.sort_values(by=['trade_date'])
    # df.reset_index(level=0, inplace=True)
    # df.drop(['index'], axis=1, inplace=True)
    # print(df)
    # df.to_csv("aaa.csv")
    # date = df.trade_date.tolist()
    # data = []
    # for idx in df.index:
    #     row = [df.iloc[idx]['open'], df.iloc[idx]['close'], df.iloc[idx]['low'], df.iloc[idx]['high']]
    #     data.append(row)
    # kline = Kline("K 线图示例")
    # kline.add(
    #     "日K",
    #     date,
    #     data,
    #     mark_point=["max"],
    #     is_datazoom_show=True,
    # )
    # kline.render()
