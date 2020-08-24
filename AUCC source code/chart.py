# libraries
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
import matplotlib
import matplotlib.dates as mdates
import pandas as pd
import numpy as np
import seaborn as sns
import pymongo
from pymongo import MongoClient
import datetime as dt
from datetime import datetime
from wordcloud import WordCloud

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'Comic Sans MS'
date = datetime.strptime('2017-05-04',"%Y-%m-%d")
print(date)
date = date.replace(minute=00, hour=0, second=00, year=2019, month=11, day=4)
print(date)
time = [date + dt.timedelta(minutes=i) for i in range(4320)]
date2 = datetime.strptime('2017-05-04',"%Y-%m-%d")
print(date)
date2 = date.replace(minute=00, hour=0, second=00, year=2019, month=11, day=4)
print(date)
time2 = [date + dt.timedelta(minutes=i) for i in range(0, 4320, 10)]
client = MongoClient('mongodb://localhost:27017/University')
db = client.University

df = sns.load_dataset('iris')

def graphScatterplot():
    TRACK = ["Mahidol","Chula","Thammasat","Kasetsart","Chiang Mai","Khon Kaen","Srinakharinwirot","Mahasarakham","Burapha","Mae Fah Luang"]
    COLOR = ['rosybrown','darksalmon','#FFFF00','#00FF00','#00FFFF','#008080','#0000FF','#008000','#FF00FF','#800080',]
    # initialize a figure
    plt.figure()
    plt.title("test")
    for u in range(10):
        dataA = db.uni_count_permin_data.find({'university':TRACK[u],'timeUpdate': {'$lt':dt.datetime.today()}})
        x = []
        y = []
        state = 0
        i = 0
        for item in dataA:
            state+=item['retweet']['retweet_thismin']
            i+=1
            if(i%10==0):
                x.append(i)
                y.append(state)
                state=0
        plt.subplot(3,4,u+1)
        plt.plot(y,linewidth=1,color=COLOR[u])
        plt.title(TRACK[u], fontsize=8, color='grey', loc='left', style='italic')
    # Add a title:
    plt.show()
    

def chart():
    university ="Burapha"
    plt.figure()
    dataA = list(db.retweet_permin_data.find({'id_str':"1191006873232633856",'timeUpdate': {'$gte':dt.datetime(2019, 11, 4, 0, 1, 0, 0),'$lte':dt.datetime(2019, 11, 6, 0, 0, 0, 0)}}))
    dataB = list(db.uni_count_permin_data.find({'university':university,'timeUpdate': {'$gte':dt.datetime(2019, 11, 4, 0, 1, 0, 0),'$lte':dt.datetime(2019, 11, 6, 0, 0, 0, 0)}}))
    x = []
    xx =[]
    xy= []
    count = 0
    graph1 = []
    graph2 = []
    graph3_1 = []
    graph3_2 = []
    state = 0
    state2 = 0
    for item in dataA:
        count+=1
        state+=item['retweet']['retweet_thismin']
        state2+=item['retweet']['retweet_thismin']
        if(count%30==0):
            x.append(count)
            graph2.append(state2)
            if(count<=1440):
                xx.append(count)
                graph3_1.append(state2)
            else:
                xy.append(count-1440)
                graph3_2.append(state2)
            state2=0
        graph1.append(state)
    print(count)
    count = 0
    state = 0
    height = []
    for item in dataA:
        count+=1
        state+=item['retweet']['retweet_thismin']
        if(count%480==0):
            height.append(state)
            state=0
    count = 0
    state = 0
    trends =[]
    for item in dataB:
        count+=1
        state+=item['retweet']['retweet_thismin']
        if(count%30==0):
            trends.append(state)
            state = 0
    print(count)
    plt.suptitle(university+' Most Tweet Trend 2days')
    plt.subplot(2,3,1)
    plt.plot(graph1,linewidth=1.5,color="c")
    plt.title('Cumulative Frequency', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,2)
    plt.plot(x,graph2,linewidth=1.5,color="rosybrown")
    plt.title('Frequency(every30minute)', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,3)
    sns.regplot(x, graph2)
    plt.title('Scatterplot with regression', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,4)
    bars = ('4/11 00', '4/11 08', '4/11 16', '5/11 00', '5/11 08','5/11 16')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.title('Bar Frequency', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,5)
    plt.plot(xx,graph3_1,linestyle='none', marker='o', color="orange", alpha=0.5,label="day1")
    plt.plot(xy,graph3_2,linestyle='none', marker='o', color="c", alpha=0.5,label="day2")
    plt.legend(loc='upper right')
    plt.title('Day1 vs Day2', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,6)
    plt.fill_between( x, trends, color="skyblue", alpha=0.4,label=university)
    plt.fill_between( x, graph2, color="red", alpha=0.4,label="Tweet Trend")
    plt.legend(loc='upper right')
    plt.title('University vs Tweet trend', fontsize=10, color='black', style='italic')
    plt.show()

def chartUni():
    university ="Mae Fah Luang"
    plt.figure()
    dataA = list(db.uni_count_permin_data.find({'university':university,'timeUpdate': {'$gte':dt.datetime(2019, 11, 4, 0, 1, 0, 0),'$lte':dt.datetime(2019, 11, 5, 0, 0, 0, 0)}}))
    dataB = list(db.master_data.find({'university':university,'timeUpdate': {'$gte':dt.datetime(2019, 11, 4, 0, 1, 0, 0)}}))
    x = []
    count = 0
    graph1 = []
    graph2 = []
    state = 0
    state2 = 0
    for item in dataA:
        count+=1
        state+=item['retweet']['retweet_thismin']
        state2+=item['retweet']['retweet_thismin']
        if(count%10==0):
            x.append(count)
            graph2.append(state2)
            state2=0
        graph1.append(state)
    print(count)
    count = 0
    state = 0
    height = []
    for item in dataA:
        count+=1
        state+=item['retweet']['retweet_thismin']
        if(count%240==0):
            height.append(state)
            state=0
    count = 0
    state = 0
    statefav = 0
    twtrwtfav = []
    for item in dataB:
        count+=1
    twtrwtfav.append(count)
    for item in dataA:
        state += item['retweet']['retweet_thismin']
        statefav += item['favourite']['favorite_thismin']
    twtrwtfav.append(state)
    twtrwtfav.append(statefav)

    print(count)
    plt.suptitle(university+' 4/11/2019 - 5/11/2019')
    plt.subplot(2,3,1)
    plt.plot(graph1,linewidth=1.5,color="c")
    plt.title('Cumulative Frequency', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,2)
    plt.plot(x,graph2,linewidth=1.5,color="rosybrown")
    plt.title('Frequency(every10minute)', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,3)
    bar1 = ('tweets','retweets','favourite')
    ybar1 = np.arange(len(bar1))
    plt.bar(ybar1,twtrwtfav,color=('c', 'skyblue', 'rosybrown'))
    plt.xticks(ybar1,bar1)
    plt.title('tweet retweet favorite count', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,4)
    bars = ('4/11 00', '4/11 04', '4/11 08', '5/11 12', '5/11 16','5/11 20')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.title('Bar Frequency', fontsize=10, color='black', style='italic')
    plt.show()

def chartalluni():
    TRACK = ["Mahidol","Chula","Thammasat","Kasetsart","Chiang Mai","Khon Kaen","Srinakharinwirot","Mahasarakham","Burapha","Mae Fah Luang"]
    COLOR = ['#FF0000','#808080','orange','#00FF00','#00FFFF','#008080','#0000FF','#008000','#FF00FF','#800080',]
    y=[]
    plt.figure()
    plt.style.use('seaborn-whitegrid')
    k=0
    for i in range(10):
        state = 0
        dataA = db.uni_count_permin_data.find({'university':TRACK[i],'timeUpdate': {'$gte':dt.datetime(2019, 11, 4, 0, 0, 0, 0),'$lte':dt.datetime(2019, 11, 7, 0, 2, 0, 0)}})
        for item in dataA:
            state += item['retweet']['retweet_thismin']
            y.append(state)
        plt.subplot(3,4,i+1)
        plt.plot(time,y,linewidth=1.5,color=COLOR[i])
        # xfmt = mdates.DateFormatter('%d-%m-%y %H:%M')
        plt.xticks(fontsize=8,rotation=45, ha='right')
        plt.title(TRACK[i], fontsize=12, color='black', style='italic')
        k+=1
        print(len(y))
        y =[]
    plt.suptitle('Cumulative Frequency all university between 4/11/2019 - 7/11/2019')
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    plt.show()

def chartalluni2():
    TRACK = ["Mahidol","Chula","Thammasat","Kasetsart","Chiang Mai","Khon Kaen","Srinakharinwirot","Mahasarakham","Burapha","Mae Fah Luang"]
    COLOR = ['#FF0000','#808080','orange','#00FF00','#00FFFF','#008080','#0000FF','#008000','#FF00FF','#800080',]
    
    plt.figure()
    plt.style.use('seaborn-whitegrid')
    k=0
    x = []
    count = 0
    graph2 = []
    state2 = 0
    for i in range(10):
        dataA = db.uni_count_permin_data.find({'university':TRACK[i],'timeUpdate': {'$gte':dt.datetime(2019, 11, 4, 0, 0, 0, 0),'$lte':dt.datetime(2019, 11, 7, 0, 2, 0, 0)}})
        for item in dataA:
            count+=1
            state2+=item['retweet']['retweet_thismin']
            if(count%10==0):
                x.append(count)
                graph2.append(state2)
                state2=0
            k+=1
            print(k)        
        plt.subplot(3,4,i+1)
        plt.plot(time2,graph2,linewidth=1.5,color=COLOR[i])
        graph2 = []
        plt.xticks(fontsize=8,rotation=45, ha='right')
        plt.title(TRACK[i], fontsize=12, color='black', style='italic')
        k+=1
        x=[]
        
    plt.suptitle('Frequency every10minute all University between 4/11/2019 - 7/11/2019')
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.5)
    plt.show()


# chart()
# chartUni()
chartalluni()