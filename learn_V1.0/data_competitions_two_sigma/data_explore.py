# -*- coding: utf-8 -*-

# =================================================
# @Time : 2018/12/1 20:39 
# @Author : zhoulinbin <zhoulinbin@jd.com>
# @File : data_explore.py
# @Desc : 数据读取，和统计分析，极值，比例分布，用户交叉情况

# =================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
import pickle as pk
import csv
import datetime
import lightgbm as lgb
from scipy import stats
from scipy.sparse import hstack, csr_matrix
from sklearn.model_selection import train_test_split
from wordcloud import WordCloud
from collections import Counter
# from nltk.corpus import stopwords
# stop = set(stopwords.words('english'))
# from nltk.util import ngrams
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report



import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls

#from xgboost import XGBClassifier
import lightgbm as lgb
from sklearn import model_selection
from sklearn.metrics import accuracy_score
import re
import time


def predict_pseudo_test():
    train_X_tr = pd.read_csv('D:/transaction_risk_competition/transaction_train_new.csv', header=None)
    train_y_op = pd.read_csv('D:/transaction_risk_competition/operation_train_new.csv', header=None)
    train_y = pd.read_csv('D:/transaction_risk_competition/tag_train_new.csv', header=None)

    # test_y_true= pd.read_csv('E:/DC_BIG_data/loan/test_target_true.csv',header = None)
    # lr_model = LogisticRegression(C=1.0, penalty='l2')
    # lr_model.fit(train_X, train_y)
    # # test_y_predict=lr_model.predict(test_X)
    # # print classification_report(test_y_true,test_y_predict)
    # predict_prob = lr_model.predict_proba(test_X)
    # result = pd.DataFrame(predict_prob)
    # result.to_csv("result_whole.csv")

if __name__=='__main__':
    #read_sample()
    #predict_pseudo_test()
    train_X_tr = pd.read_csv('D:/transaction_risk_competition/transaction_train_new.csv')
    #去掉'geo_code'列因为不好分
    # 看空值分布
    len_count = len(train_X_tr['UID'])
    for col in ['UID', 'day', 'time', 'trans_amt', 'bal', 'acc_id1', 'acc_id2', 'acc_id3', 'amt_src1', 'amt_src2',
                'trans_type2', 'trans_type1', 'market_code', 'market_type', 'merchant', 'code1', 'code2', 'channel',
                'device_code1', 'device_code2', 'device_code3', 'device1', 'device2', 'mac1', 'ip1', 'ip1_sub']:
        print('{0}'.format(col), '%.2f' % (train_X_tr[col].isnull().sum() / len_count))

    train_X_tr['merchant'].isnull().sum() / len(train_X_tr['UID'])  # code1,code2,device_code3缺少太多，删掉这些列

    train_X_tr = train_X_tr[
        ['UID', 'day', 'time', 'trans_amt', 'bal', 'acc_id1', 'acc_id2', 'acc_id3', 'amt_src1', 'amt_src2',
         'trans_type2', 'trans_type1', 'market_code', 'market_type', 'merchant', 'channel',
         'device_code1', 'device_code2', 'device1', 'device2', 'mac1', 'ip1', 'ip1_sub']]
    print(train_X_tr.head(10))
    # 显示所有列显示所有行
    pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    pd.set_option('max_colwidth', 100)



    # 选取做因子化factorize，把几个可枚举的字符串转为了数字，并返回一个（字符串，数字）的对应映射表方便检查
    ##amt_src1 交易资金来源类型，余额，花呗做因子化
    ##trans_type1	交易类型，消费，退款。。。14种
    ##trans_type2	线上线下 ，一定要因子化，只有4中，加上none,5种
    ##market_type	营销类型，只有2种，加上空值，三种，适合因子化factorize，把字符串转为了数字
    ##channel 平台，渠道没有空值，5种，，适合因子化
    ##########################################
    #1，对market_type
    values = {'market_type': 0}
    #先把market_type中的空值填充为0，在后续因子化
    train_X_tr.fillna(value=values, inplace=True)
    train_X_tr['market_type'], uniques = pd.factorize(train_X_tr['market_type'], sort=True)
    del uniques
    # 这里不对market_type做独热码处理，
    # 因为会把[uid,market_type]放在groupby中统计次数和 对应分组的金额
    # 若要对因子化后的market_type做哑变量独热码处理，
    #按如下处理，先单取market_type这一列get_dummies，再和去掉market_type列的原数据join可还原
    # columns = list(train_X_tr.columns)
    # columns.remove('market_type')
    # columns_del_market_type = columns
    # train_X_tr = pd.get_dummies(train_X_tr['market_type'], prefix='market_type').join(
    #     train_X_tr[columns_del_market_type])

    #2，对channel处理,
    values = {'channel': 0}
    train_X_tr.fillna(value=values, inplace=True)
    #channel本身是102，106，118，119，140的数字型，不用因子化了
    # 这里也不对channel做独热码处理,
    # 因为会把[uid,channel]放在groupby中统计次数和 对应分组的金额
    # 若要对因子化后的channel哑变量独热码处理，
    # 按如下处理，先单取market_type这一列get_dummies，再和去掉market_type列的原数据join可还原
    ###其实channel表中无空值的，
    # columns = list(train_X_tr.columns)
    # columns.remove('channel')
    # columns_del_channel = columns
    # train_X_tr = pd.get_dummies(train_X_tr['channel'], prefix='channel').join(train_X_tr[columns_del_channel])

    #3，对trans_type2，线上线下 ，一定要因子化，只有4中，加上none,5种
    # channel本身是102，103，104，105，数字浮点型，转为整型，并转空值为0就不用因子化了
    values = {'trans_type2': 0}#把空值填充为0，
    train_X_tr.fillna(value=values, inplace=True)
    train_X_tr.head(5)

    #4，对trans_type1，交易类型，消费，退款。。。 因为不是数字型，要因子化factorize为数值型
    #并用于后续的groupby ['uid','trans_type1']
    #加上把空值转为的0，一共15种，
    values = {'trans_type1': '0'}
    train_X_tr.fillna(value=values, inplace=True)


    train_X_tr['trans_type1'], uniques = pd.factorize(train_X_tr['trans_type1'], sort=True)
    del uniques

    # 这里也不对trans_type1做独热码处理,
    # 因为会把[uid,trans_type1]放在groupby中统计次数和 对应分组的金额
    # 若要对因子化后的trans_type1哑变量独热码处理，
    # 按如下处理，先单取trans_type1这一列get_dummies，再和去掉trans_type1列的原数据join可还原
    #columns = list(train_X_tr.columns)
    # columns.remove('trans_type1')
    # columns_del_trans_type1=columns
    # 最好还保留因子化后的trans_type1，放在后面的groupby字段里，同时get_dummies(train_X_tr['trans_type1']得到这笔交易是什么类型
    #train_X_tr = pd.get_dummies(train_X_tr['trans_type1'], prefix='trans_type1').join(train_X_tr[columns])
    train_X_tr.head(5)

    #5，amt_src1 交易资金来源类型，余额，花呗做因子化
    #总共有27中，因为分按分布分为10中比较合适
    #train_X_tr['amt_src1'].value_counts()#显示个数
    #train_X_tr['amt_src1'].value_counts(1)#加上1显示百分百
    #定义一个映射字典，
    # dict_map={'c5fc631370cabc0d':1,'155c9e1c32bd0fa2':2,
    #  '4d7831c6f695ab19': 3, 'f29829bc82459191': 4,
    #  '992d3ce08a4ca702': 5, 'a571c7fda8b7df37': 6,
    #  '9451ef3c5a0d6807': 7, 'acdbdb842ac20f1e': 8,
    #  'fd4d2d1006a95637': 9, '8c9987909b3e95a4': 10,
    #  '27c42480134c0d02':11, '8c9987909b3e95a4': 10,
    #  }#这种方式太麻烦了，更自动的方法是：
    a = train_X_tr['amt_src1'].value_counts().index.tolist()
    #['c5fc631370cabc0d', '155c9e1c32bd0fa2', '4d7831c6f695ab19', 'f29829bc82459191', '992d3ce08a4ca702', 'a571c7fda8b7df37',
    # '9451ef3c5a0d6807', 'acdbdb842ac20f1e', 'fd4d2d1006a95637', '8c9987909b3e95a4', '27c42480134c0d02', 'b3acdf321be07351',
    # '767001914a988cfb', 'b0a5496f0db7f70a', '8c753ae7afb60e61', '3045dd7701f3e263', '8576ce2e7ab65ac2', '0b747ef141d49c8c',
    #  '9a1fad6202fd1a24', 'd7de70fc65292e41', '79b1dd31895a6278', 'd4f7a3699ef02458', 'd46a2a9577fb52c3', '47b415a384665f45',
    #  '4ec06e4d12f8560d', '295eadbc19cddb04', '41c767468d03b4ac', 'f2500fa92c7e39b9']
    b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] + ([-1] * (len(a) - 11))
    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    #取计数为前11的amt_src1为012345678910，后面的全取为-1
    #然后，pandas值替换函数repalce
    train_X_tr['amt_src1'] = train_X_tr['amt_src1'].replace(a, b)
    train_X_tr['amt_src1'].head(10)
    #至此完成 amt_src1的交易资金来源类型，余额，花呗做因子化，后面做groupby[uid,amt_src1]


    ##开始构造特征：先不区分日期，也就是全日期
    #1，groupby uid 取计数count,次数
    train_X_tr_uid1_count = train_X_tr[
        ['acc_id1', 'acc_id2', 'acc_id3', 'amt_src1', 'amt_src2', 'trans_type2', 'trans_type1', 'market_code',
         'market_type', 'merchant', 'channel', 'device_code1', 'device_code2', 'device1', 'device2', 'mac1', 'ip1',
         'ip1_sub']].groupby(train_X_tr['UID']).count().add_suffix('_count').reset_index()
    # train_X_tr_uid1_count.head(5)

    #2，groupby uid，xx(因子量)取金额均值（最大，最小等等）
    train_X_tr_uid2_channel_bal = train_X_tr.groupby(['UID', 'channel'])['trans_bal'].agg(
        {'mean', 'max', 'min'}).add_prefix(
        'bal_channel_').unstack()
    train_X_tr_uid2_channel_bal.columns = [x[0] + "_" + str(x[1]) for x in train_X_tr_uid2_channel_bal.columns.ravel()]
    train_X_tr_uid2_channel_bal.reset_index(inplace=True)
    train_X_tr_uid2_channel_bal.fillna(0.0, inplace=True)
    print(train_X_tr_uid2_channel_bal.head(5))

    train_X_tr_uid2_market_type_bal = train_X_tr.groupby(['UID', 'market_type'])['trans_bal'].agg(
        {'mean', 'max', 'min'}).add_prefix(
        'bal_market_type_').unstack()
    train_X_tr_uid2_market_type_bal.columns = [x[0] + "_" + str(x[1]) for x in
                                               train_X_tr_uid2_market_type_bal.columns.ravel()]
    train_X_tr_uid2_market_type_bal.reset_index(inplace=True)
    train_X_tr_uid2_market_type_bal.fillna(0.0, inplace=True)
    print(train_X_tr_uid2_market_type_bal.head(5))

    train_X_tr_uid2_trans_type2_bal = train_X_tr.groupby(['UID', 'trans_type2'])['trans_bal'].agg(
        {'mean', 'max', 'min'}).add_prefix(
        'bal_trans_type2_').unstack()
    train_X_tr_uid2_trans_type2_bal.columns = [x[0] + "_" + str(x[1]) for x in
                                               train_X_tr_uid2_trans_type2_bal.columns.ravel()]
    train_X_tr_uid2_trans_type2_bal.reset_index(inplace=True)
    train_X_tr_uid2_trans_type2_bal.fillna(0.0, inplace=True)
    print(train_X_tr_uid2_trans_type2_bal.head(5))

    train_X_tr_uid2_trans_type1_bal = train_X_tr.groupby(['UID', 'trans_type1'])['trans_bal'].agg(
        {'mean', 'max', 'min'}).add_prefix(
        'bal_trans_type1_').unstack()
    train_X_tr_uid2_trans_type1_bal.columns = [x[0] + "_" + str(x[1]) for x in
                                               train_X_tr_uid2_trans_type1_bal.columns.ravel()]
    train_X_tr_uid2_trans_type1_bal.reset_index(inplace=True)
    train_X_tr_uid2_trans_type1_bal.fillna(0.0, inplace=True)
    print(train_X_tr_uid2_trans_type1_bal.head(5))

    train_X_tr_uid2_bal_src1_bal = train_X_tr.groupby(['UID', 'bal_src1'])['trans_bal'].agg(
        {'mean', 'max', 'min'}).add_prefix(
        'bal_bal_src1_').unstack()
    train_X_tr_uid2_bal_src1_bal.columns = [x[0] + "_" + str(x[1]) for x in
                                            train_X_tr_uid2_bal_src1_bal.columns.ravel()]
    train_X_tr_uid2_bal_src1_bal.reset_index(inplace=True)
    train_X_tr_uid2_bal_src1_bal.fillna(0.0, inplace=True)
    print(train_X_tr_uid2_bal_src1_bal.head(5))

    ####################
    train_X_tr_uid2_channel_bal = train_X_tr.groupby(['UID', 'channel'])['bal'].agg(
        {'mean', 'max', 'min'}).add_prefix(
        'bal_channel_').unstack()
    train_X_tr_uid2_channel_bal.columns = [x[0] + "_" + str(x[1]) for x in train_X_tr_uid2_channel_bal.columns.ravel()]
    train_X_tr_uid2_channel_bal.reset_index(inplace=True)
    train_X_tr_uid2_channel_bal.fillna(0.0, inplace=True)
    print(train_X_tr_uid2_channel_bal.head(5))

    train_X_tr_uid2_market_type_bal = train_X_tr.groupby(['UID', 'market_type'])['bal'].agg(
        {'mean', 'max', 'min'}).add_prefix(
        'bal_market_type_').unstack()
    train_X_tr_uid2_market_type_bal.columns = [x[0] + "_" + str(x[1]) for x in
                                               train_X_tr_uid2_market_type_bal.columns.ravel()]
    train_X_tr_uid2_market_type_bal.reset_index(inplace=True)
    train_X_tr_uid2_market_type_bal.fillna(0.0, inplace=True)
    print(train_X_tr_uid2_market_type_bal.head(5))

    train_X_tr_uid2_trans_type2_bal = train_X_tr.groupby(['UID', 'trans_type2'])['bal'].agg(
        {'mean', 'max', 'min'}).add_prefix(
        'bal_trans_type2_').unstack()
    train_X_tr_uid2_trans_type2_bal.columns = [x[0] + "_" + str(x[1]) for x in
                                               train_X_tr_uid2_trans_type2_bal.columns.ravel()]
    train_X_tr_uid2_trans_type2_bal.reset_index(inplace=True)
    train_X_tr_uid2_trans_type2_bal.fillna(0.0, inplace=True)
    print(train_X_tr_uid2_trans_type2_bal.head(5))

    train_X_tr_uid2_trans_type1_bal = train_X_tr.groupby(['UID', 'trans_type1'])['bal'].agg(
        {'mean', 'max', 'min'}).add_prefix(
        'bal_trans_type1_').unstack()
    train_X_tr_uid2_trans_type1_bal.columns = [x[0] + "_" + str(x[1]) for x in
                                               train_X_tr_uid2_trans_type1_bal.columns.ravel()]
    train_X_tr_uid2_trans_type1_bal.reset_index(inplace=True)
    train_X_tr_uid2_trans_type1_bal.fillna(0.0, inplace=True)
    print(train_X_tr_uid2_trans_type1_bal.head(5))

    train_X_tr_uid2_bal_src1_bal = train_X_tr.groupby(['UID', 'amt_src1'])['bal'].agg(
        {'mean', 'max', 'min'}).add_prefix(
        'amt_bal_src1_').unstack()
    train_X_tr_uid2_bal_src1_bal.columns = [x[0] + "_" + str(x[1]) for x in
                                            train_X_tr_uid2_bal_src1_bal.columns.ravel()]
    train_X_tr_uid2_bal_src1_bal.reset_index(inplace=True)
    train_X_tr_uid2_bal_src1_bal.fillna(0.0, inplace=True)
    print(train_X_tr_uid2_bal_src1_bal.head(5))

    #每个用户只看最近一半的记录
    train_X_tr_dt_mid = train_X_tr[['UID', 'day']].groupby(['UID']).mean().add_suffix("_mid").reset_index()
    train_X_tr = pd.merge(train_X_tr, train_X_tr_dt_mid, how='left', on='UID')
    train_X_tr.head(5)
    #再重新统计上面记录

    train_X_tr_uid1_day_count = train_X_tr[['day']].groupby(train_X_tr['UID']).count().add_suffix(
        '_count').reset_index()
    train_X_tr_uid1_day_count.head(100)
    ###这样不是分组内，去重统计， 如何分组内去重统计

    train_X_tr['day_time'] = train_X_tr.apply(lambda x: str(x['day']) + "_" + str(x['time']), axis=1)
    # train_X_tr.head(5)
    train_X_tr_uid1_day_time_count = train_X_tr[['day_time']].groupby(train_X_tr['UID']).count().add_suffix(
        '_count').reset_index()
    train_X_tr_uid1_day_time_count.head(100)

    ###这样不是分组内去重
    train_X_tr.loc[train_X_tr["UID"] == 10001]

    # train_X_tr.loc[train_X_tr["UID"] == 10001]
    # 需要先排序
    # train_X_tr['day'] = train_X_tr.groupby('UID')['day'].sort()
    train_X_tr.sort_values(by=['UID', 'day', 'time'], inplace=True)
    train_X_tr['day_shift'] = train_X_tr.groupby('UID')['day'].shift(-1)
    train_X_tr.head(15)







    train_X_tr.head(5)








