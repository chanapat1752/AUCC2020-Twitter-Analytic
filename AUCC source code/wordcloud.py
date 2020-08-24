import matplotlib.pyplot as plt # ใช้ในการแสดง Word Cloud 
from pythainlp.tokenize import word_tokenize # ใช้ในการตัดคำ
from wordcloud import WordCloud, STOPWORDS # ใช้ทำ Word Cloud 
import pymongo
from pymongo import MongoClient
import datetime as dt
import time


#In[]:
client = MongoClient('mongodb://localhost:27017/University')
db = client.University


#In[]:
def getWordClouds():
    FWORD = ["ขายตัว","นัดเยส","เย็ด","ไซค์ไลน์","กะหรี่","sideline","สาวเสียบ","ไซด์ไลน์","ขายหี","ขายบริการ","เงี่ยน","ชักว่าว","คอลว่าว","forsex","ควย","อีโรติก","เปิดซิง","สวิงกิ้ง","สวิงขอนแก่น","แตด","หี","เลสเบี้ยน","เกย์","ยสตน","น้ำแตก","คอลเสียว","มบูร","บูรพา","BUU","มอบู","บางแสน","ส่งต่อ","มือสอง","มช","มเชียงใหม่","ทีมมช","ม.เชียงใหม่","มหาวิทยาลัยเชียงใหม่"]
    o = ['during', "shouldn't", 'about', 'on', "what's", 'at', 'has', 'it', "they'll", 'each', 'herself', 'yourself', 'we', 'and', 'in', "they've", 'get', "how's", "you'll", "we're", 'other', 'had', 'few', 'against', 'themselves', 'out', 'am', 'they', 'as', 'when', 'how', 'both', "i've", 'his', 'you', 'a', 'all', 'being', 'itself', 'been', 'own', 'your', 'for', 'she', 'hers', 'up', 'to', 'not', 'any', 'down', "mustn't", 'off', 'why', 'who', "let's", 'most', "you'd", 'but', 'yourselves', "weren't", "she's", 'an', 'only', "he'll", "hadn't", "we've", "can't", "don't", 'my', 'again', 'once', 'myself', "he'd", 'cannot', 'between', 'very', "she'll", "aren't", "we'll", 'such', 'no', 'what', 'this', 'same', "i'm", 'ever', 'me', 'were', "shan't", 'himself', 'www', 'com', 'could', "that's", "who's", 'the', 'would', "haven't", "wasn't", "couldn't", 'however', 'since', "hasn't", 'else', 'further', "he's", 'ought', 'because', "she'd", 'while', 'whom', 'doing', "we'd", 'him', 'from', 'above', 'he', 'here', 'did', 'are', 'then', "i'd", 'until', "wouldn't", "doesn't", "isn't", 'is', 'those', "won't", 'some', 'also', 'into', 'ourselves', 'them', 'which', "when's", 'where', 'r', 'its', 'than', 'so', 'below', 'shall', 'like', 'http', 'otherwise', 'theirs', "where's", "they'd", 'do', 'there', 'with', "i'll", 'or', "here's", "why's", 'her', 'before', 'if', 
'can', 'of', 'our', 'ours', 'through', 'was', 'that', 'over', 'just', 'be', 'more', "didn't", 'by', "you've", 'having', "there's", "they're", "it's", 'their', 'under', 'should', "you're", 'nor', 'yours', 'too', 'have', 'after', 'k', 'these', 'i', 'does']
    text = ""
    k = 0
    allword = 0
    fcount = 0
    dataA = list(db.retweet_permin_data.find({'university':"Chiang Mai",'timeUpdate': {'$gte':dt.datetime(2019, 11, 3, 19, 0, 0, 0),'$lte':dt.datetime(2019, 11, 3, 23, 59, 0, 0)}}))
    for item in dataA:
        # num = item['retweet']['retweet_thismin']
        dataB = db.master_data.find_one({'id_str':item['id_str']})
        try:
            for i in dataB['hashtags']:
                for p in FWORD:
                    if p in i['text']: 
                        fcount +=1
                        i['text'] = ''
                        continue
                # for j in range(num):
                text += i['text']+" "+o[k]+" "
                k+=1
                if(k == 35):
                    k=0   
                allword+=1 
        except:
            next
        
    # for item in dataA:
    #     for i in item['hashtags']:
    #         for p in FWORD:
    #             if p in i['text']: 
    #                 fcount +=1
    #                 print(i['text'])
    #                 i['text'] = ''
    #                 continue
    #         text += i['text']+" "+o[k]+" "
    #         k+=1
    #         if(k == 35):
    #             k=0   
    #         # print(count)
    #         allword+=1 
                    
    # print(text)
    wordcloud = WordCloud(font_path='THSarabunNew.ttf', # path ที่ตั้ง Font
                      stopwords = list(STOPWORDS), # ลบคำที่ไม่ใช้ออก
                      background_color="white", # ตั้งค่าพืสี้นหลัง
                      regexp=r"[\u0E00-\u0E7Fa-zA-Z'0-9]+", # ป้องกัน bug วรรณยุกต์
                    
                      width=1920, height=1080,
                      collocations=False).generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    print(allword)
    print(fcount)
    plt.show()

    

getWordClouds()