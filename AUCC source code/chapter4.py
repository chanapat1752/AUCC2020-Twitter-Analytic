# libraries
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import pymongo
from pymongo import MongoClient
import datetime as dt
from datetime import datetime
from wordcloud import WordCloud


client = MongoClient('mongodb://localhost:27017/University')
db = client.University

def chart():
    plt.figure()
    dataA = list(db.uni_count_permin_data.find({'university':"Mahidol",'timeUpdate': {'$gte':dt.datetime(2019, 10, 29, 22, 17, 0, 0),'$lte':dt.datetime(2019, 10, 30, 22, 16, 0, 0)}}))
    dataB = list(db.uni_count_permin_data.find({'university':"Thammasat",'timeUpdate': {'$gte':dt.datetime(2019, 10, 29, 22, 17, 0, 0),'$lte':dt.datetime(2019, 10, 30, 22, 16, 0, 0)}}))
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
    trends =[]
    for item in dataB:
        count+=1
        state+=item['retweet']['retweet_thismin']
        if(count%10==0):
            trends.append(state)
            state = 0
    plt.suptitle('Mahidol')
    plt.subplot(2,3,1)
    plt.plot(graph1,linewidth=1.5,color="c")
    plt.title('Cumulative Frequency', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,2)
    plt.plot(x,graph2,linewidth=1.5,color="rosybrown")
    plt.title('Frequency(every10minute)', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,3)
    plt.plot(x,graph2,linestyle='none', marker='o', color="orange", alpha=0.5)
    plt.title('Scatterplot Frequency(every10minute)', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,4)
    bars = ('22.00', '02.00', '06.00', '10.00', '14.00','18.00')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height)
    plt.xticks(y_pos, bars)
    plt.title('Bar Frequency', fontsize=10, color='black', style='italic')
    plt.subplot(2,3,5)
    plt.plot(x,graph2,linestyle='none', marker='o', color="orange", alpha=0.5)
    plt.plot(x,trends,linestyle='none', marker='o', color="c", alpha=0.5)
    plt.title('University vs retweet trends', fontsize=10, color='black', style='italic')
    plt.show()


def totalFrequency():
    plt.style.use('seaborn-whitegrid')
    TRACK = ["Burapha"]
    COLOR = ["c"]
    # TRACK = ["Mahidol","Chula","Thammasat","Kasetsart","Chiang Mai","Khon Kaen","Srinakharinwirot","Mahasarakham","Burapha","Mae Fah Luang"]
    # COLOR = ['#FF0000','#808080','#FFFF00','#00FF00','#00FFFF','#008080','#0000FF','#008000','#FF00FF','#800080',]
    i = 0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'TH SarabunPSK'
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    for uni in TRACK:
        count = 0
        state = 0
        xbar = []
        ybar = []
        dataA = list(db.uni_count_permin_data.find({'university':uni,'timeUpdate': {'$gte':dt.datetime(2019, 11, 3, 20, 41, 0, 0),'$lte':dt.datetime(2019, 11, 3, 21, 41, 0, 0)}}))
        for item in dataA:
            count+=1
            state+=item['retweet']['retweet_thismin']
            xbar.append(count)
            ybar.append(state)
            # state = 0
            # if(count%10==0):
            #     xbar.append(count)
            #     ybar.append(state)
            #     state=0
        i+=1
        plt.subplot(3,4,i)
        plt.plot(xbar,ybar,linewidth=1.5,color=COLOR[i-1],label=uni)
        # plt.title(uni, fontsize=10, color='black', style='italic')

    plt.ylabel('จำนวนรีทวิต',fontsize=15)
    plt.xlabel('เวลา/นาที',fontsize=15)
    plt.tick_params(labelsize=14)
    # plt.legend(loc="upper left")
    plt.show()
xbar = []
ybar = []
def totalSlope():
    plt.style.use('seaborn-whitegrid')
    TRACK = ["Chula"]
    COLOR = ["#FF0000"]
    # COLOR = ["#008000"]
    # TRACK = ["Mahidol","Chula","Thammasat","Kasetsart","Chiang Mai","Khon Kaen","Srinakharinwirot","Mahasarakham","Burapha","Mae Fah Luang"]
    # COLOR = ['#FF0000','#808080','#FFFF00','#00FF00','#00FFFF','#008080','#0000FF','#008000','#FF00FF','#800080',]
    i = 0
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'TH SarabunPSK'
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    for uni in TRACK:
        count = 0
        state = []
        statesum = 0
        dataA = list(db.uni_count_permin_data.find({'university':uni,'timeUpdate': {'$gte':dt.datetime(2019, 11, 7, 10, 18, 0, 0),'$lte':dt.datetime(2019, 11,7, 11, 18, 0, 0)}}))
        for item in dataA:
            statesum += item['retweet']['retweet_thismin']
            state.append(statesum)
            # state.append(item['retweet']['retweet_thismin'])
            count+=1
            if(count>1):
                slope = (state[count-1] - state[count-2])
                xbar.append(count)
                ybar.append(slope)
            else:
                slope = (state[count-1] - 0)
                xbar.append(count)
                ybar.append(slope)
        i+=1
        plt.subplot(3,4,i)
        plt.plot(xbar,ybar,linewidth=1.2,color=COLOR[i-1])
    
    plt.ylabel('ความชัน',fontsize=15)
    plt.xlabel('เวลา/นาที',fontsize=15)
    plt.tick_params(labelsize=14)
    
    plt.show()

def windowSideMean():
    slopeMean = []
    mean = 0
    count = 0
    j = 0
    while True:
        for i in range(5):
            mean +=abs(ybar[count+i])
        slopeMean.append(mean/5)
        print(count+1,'-',count+5,'=',slopeMean[j])
        j+=1
        mean = 0
        count+=2
        if(count==56):
            break

def windowSideDiff():
    slopeDiff = []
    diffMax = 0
    diffMin = 0
    count = 0
    j = 0
    while True:
        for i in range(5):
            if(i == 0):
                diffMax = ybar[count+i]
                diffMin = ybar[count+i]
            if(ybar[count+i]>diffMax):
                diffMax = ybar[count+i]
            if(ybar[count+i]<diffMin):
                diffMin = ybar[count+i]
        slopeDiff.append(diffMax-diffMin)
        print(count+1,'-',count+5,'=',slopeDiff[j])
        j+=1
        count+=2
        if(count==56):
            break

def taotong() :
    k = 0
    i = 0
    dataA = db.master_data.find({'university':'Burapha'})
    for item in dataA:
        if("เทาทอง" in item['text']):
            k+=item['retweet_count']
        i+=1
    print(k)

# chart()
# totalSlope()
# windowSideMean()
# windowSideDiff()
# totalFrequency()
taotong()