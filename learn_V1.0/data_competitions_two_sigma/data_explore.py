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
    print(train_X_tr.head(10))





