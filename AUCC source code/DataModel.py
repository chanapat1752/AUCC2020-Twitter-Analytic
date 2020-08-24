# In[ ]:
# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import datetime as dt
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

#In[]:
client = MongoClient('mongodb://localhost:27017/University')
db = client.University

def getLinearPerMinModelById() :
    t0 = time.time()
    dataA = db.retweet_permin_data.find({'id_str':"1189365083043819520",'timeUpdate': {'$lt':dt.datetime.today()}})
    y = []
    for item in dataA:
        y.append(item['retweet']['retweet_thismin'])
    t1 = time.time()
    t2 = t1-t0
    print(t2)
    y.pop()
    print(y)
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'TH SarabunPSK'
    plt.style.use('seaborn-whitegrid')
    plt.title('Retweetperminute')
    plt.ylabel('รีทวิต')
    plt.xlabel('เวลา/นาที')
    plt.ylim(-1, 20)
    plt.xlim(-1, 300)
    plt.yticks(np.arange(min(y), max(y)+1, 1.0))
    plt.plot(y,'c',linewidth=1)
    plt.show()

def getLinearPerMinModelByUni() :
    t0 = time.time()
    dataA = db.uni_count_permin_data.find({'university':"Kasetsart",'timeUpdate': {'$lt':dt.datetime.today()}})
    y = []
    for item in dataA:
        y.append(item['retweet']['retweet_thismin'])
    t1 = time.time()
    t2 = t1-t0
    print(t2)
    y.pop()
    print(y)
    plt.style.use('seaborn-whitegrid')
    plt.title('Retweetperminute')
    plt.ylabel('retweet')
    plt.xlabel('Time/minute')
    plt.plot(y,'c',linewidth=1)
    plt.show()

def getLinearCountModelByUni():
    plt.style.use('seaborn-whitegrid')
    plt.title('Retweet Count Every Minute')
    plt.ylabel('retweet')
    plt.xlabel('Time/minute')
    TRACK = ["Mahidol","Chula","Thammasat","Kasetsart","Chiang Mai","Khon Kaen","Srinakharinwirot","Mahasarakham","Burapha","Mae Fah Luang"]
    COLOR = ['#FF0000','#808080','orange','#00FF00','#00FFFF','#008080','#0000FF','#008000','#FF00FF','#800080',]
    y = []
    k = 0
    for i in range(10):
        state = 0
        # dataA = db.uni_count_permin_data.find({'university':TRACK[i],'timeUpdate': {'$gte':dt.datetime(2019, 11, 3, 00, 0, 0, 0),'$lte':dt.datetime.now()}})
        dataA = db.uni_count_permin_data.find({'university':TRACK[i],'timeUpdate': {'$gte':dt.datetime(2019, 11, 3, 13, 25, 0, 0),'$lte':dt.datetime(2019, 11, 10, 13, 24, 0, 0)}})
        for item in dataA:
            state += item['retweet']['retweet_thismin']
            y.append(state)
        print(TRACK[i]," retweet : ",state)
        plt.plot(y,COLOR[k],linewidth=1,label=TRACK[i])
        k+=1
        plt.legend()
        y =[]
    plt.show()

def getUni():
    dataA = db.master_data.find({'university':"Mae Fah Luang"})
    date =["Nov 03","Nov 04","Nov 05","Nov 06","Nov 07","Nov 08","Nov 09"]
    dateday = [0,0,0,0,0,0,0]
    temp = 0
    
    for item in dataA:
        for i in date:
            if(i in item['created_at']):
                dateday[temp] += 1
            temp+=1
        temp = 0
    for k in range(7):
        print(date[k]," : ",dateday[k])
            

        

#In[]:
# getLinearPerMinModelById()
# getLinearPerMinModelByUni()
getLinearCountModelByUni()
# getUni()

