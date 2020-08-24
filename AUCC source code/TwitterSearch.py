# In[ ]:
# -*- coding: utf-8 -*-
import io
from TwitterAPI import TwitterAPI
import pymongo
from pymongo import MongoClient
import json
import datetime as dt
import time
import DataCleansing
#In[]:
client = MongoClient('mongodb://localhost:27017/University')
db = client.University
db.tweet_raw_data.create_index([('id_str', pymongo.ASCENDING)], unique=True)

#In[]:
consumer_key = "ZFgaiN6GN1TQfmE5fGKsMtJYK"
consumer_secret = "4qiHeE4bPcWQdtcJ5XUIVFq5Hb5GW09o1fnXDhwLChaBGt5qK2"
access_token_key = "1174571429590777858-8oVMqrQLcUzkggCeP3sGHaiBkZxuTJ"
access_token_secret = "e37yn39mR58kNVdc0RmgRvmBCYgwwK1k6frMhBwH4zJrd"
api1 = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

consumer_key2 = "PxHnXHujfFzKUVELrBaRk7poC"
consumer_secret2 = "vtopnTljRn6QwfQoKjUFelOAZdFFctmQ0IjocQbVet8cXJWk0X"
access_token_key2 = "1174571429590777858-hLPCiJCDytrdPTgyWPOwQO1V2FemRy"
access_token_secret2 = "5nKeHhtPqvZ3LH0WWuShGcOIBGytOss2BP8ipsXxaYBuD"
api2 = TwitterAPI(consumer_key2, consumer_secret2, access_token_key2, access_token_secret2)

consumer_key3 = "FilOxKSUzoykAcI8pvQd4e0nm"
consumer_secret3 = "2wbTTsfaSKJzdeuUv51hJUlX4m7iGx8q07yJGVnh8gwejkzVLe"
access_token_key3 = "1174571429590777858-zcT0RKmB6VE9adrgMq1mTwlA8xjoPl"
access_token_secret3 = "glUu5nZ48S22GFghTpFBvpaHyVg3wNQk6ABEmtA5WgMjr"
api3 = TwitterAPI(consumer_key3, consumer_secret3, access_token_key3, access_token_secret3)

consumer_key4 = "VsqPrX2gQxSBgwPRnr77rEgUf"
consumer_secret4 = "AO1wsHN5NPSLq00GXNiaHw4nUpPsyYSzXYTBLNCxJVmLcXJOcm"
access_token_key4 = "1174555805883912192-dUjuCWOsE4J0oDFYIu7LM2m6hl2dKv"
access_token_secret4 ="kt3OxdERZx1LevWfAZ8zdzpMwboC2TwIfIhcPzrFPBz0M"
api4 = TwitterAPI(consumer_key4, consumer_secret4, access_token_key4, access_token_secret4)

consumer_key5 = "1DZZoYshAU76NnrAyxv2nBFkf"
consumer_secret5 = "cShrBwSlyxB5YrGbyldf74oseAxX1tvjyvLDnQEEa1vot8bTyC"
access_token_key5 = "1174571429590777858-gpviZByIHbRDWdenh8XHzTHJJvXlur"
access_token_secret5 = "Jc89VdWcjaN850f2mRMr66Bemcm9LBFJLUekoDpFutVV1"
api5 = TwitterAPI(consumer_key5, consumer_secret5, access_token_key5, access_token_secret5)

consumer_key6 = "dNoTLkMp1RJFSvCD63flyr7S5"
consumer_secret6 = "grZUcxmlXiqdTbDCVqV9fcd55UFpTGGrkT0qopuaeWwAAEib42"
access_token_key6 = "1174571429590777858-Nue9XDdChK9Khm5Pfj4vqQcQJn3eNV"
access_token_secret6 = "GCYvRPNrdBl906khjDK25GsoErWtG2RxEjNYiCf491vjM"
api6 = TwitterAPI(consumer_key6, consumer_secret6, access_token_key6, access_token_secret6)

consumer_key7 = "V8tvMQRSk75brnhok5GqUNp5q"
consumer_secret7 = "oUyCWXMRjUkIDigvafdn0V5JLbMZvDGxSmv7iOx5357KPodw6Q"
access_token_key7 = "1174571429590777858-ADf88tREEeL39q9honGGCTrvfrS4LA"
access_token_secret7 = "f2S456nyYHtZJ0Db0xjrnfGsOriD3HStZKpDt3E8ShCtx"
api7 = TwitterAPI(consumer_key7, consumer_secret7, access_token_key7, access_token_secret7)

consumer_key8 = "fb067HhGGhDIy7TeLf2FjAfOS"
consumer_secret8 = "Ed6qAy8RxPlXGwBxO2UslSnOVMGRsPM2Q9gLjJXiIzZey5Sb7W"
access_token_key8 = "1182253441508245504-VFLyOfKoaYcvT9EKSTlWvJGcv1HXzz"
access_token_secret8 = "4oL0xIFMkSCumZnda3C86QHdpdisbeHmGPjnoiPA4Wh6X"
api8 = TwitterAPI(consumer_key8, consumer_secret8, access_token_key8, access_token_secret8)

consumer_key9 = "wMHDuymaldeaE8GFJRwNxmfHw"
consumer_secret9 = "VkptLM7o90sjnfRSybO8UKBW6qxPKzjgAeETfcD6OmbovBTh06"
access_token_key9 = "1182253441508245504-8TQgOByXwYdrcMgoPTqzn2o3Styan6"
access_token_secret9 = "M4XDBjJag9xFa1s7nIZMygJbaw7JHlAnwrRTohOcUwiiE"
api9 = TwitterAPI(consumer_key9, consumer_secret9, access_token_key9, access_token_secret9)

consumer_key10 = "lQKA4hOMOcCx79lzPN6QpFesH"
consumer_secret10 = "15NyqtNOiPBVi4i5FQEegDtFRqsDaMYDEL2bqNuWruJXIrD4jG"
access_token_key10 = "1182253441508245504-mVxO9hDrtciHA5oyDR9AxeAmjCx6CT"
access_token_secret10 = "fWkqX3hX09PY2WFF2Ged4QJ9kv5aTfOjMf7ofimBsjZVK"
api10 = TwitterAPI(consumer_key10, consumer_secret10, access_token_key10, access_token_secret10)


#In[]:
allAPI=[api1,api2,api3,api4,api5,api6,api7,api8,api9,api10]
#allAPI=[api1,api2,api3,api4,api5]
# allAPI=[api6,api7,api8,api9,api10]

#In[]:
with io.open("keywordSearch.json",encoding="utf-8") as json_file:
    twData = json.load(json_file)

#In[]:
def getRawTwitter():
    rawData = []
    for i in range(10):
        try:
            t0 = time.time()
            for key, value in twData.items():
                for val in value:
                    kw = val +" -filter:retweets"
                    r = allAPI[i].request('search/tweets', {'q':kw,'lang':'th','tweet_mode':'extended','count':'100'})
                    for item in r:
                        try:
                            db.tweet_raw_data.insert_one(
                                {
                                    'university':key,
                                    'keyword':val,
                                    'id_str': item['id_str'],
                                    'data':item,
                                    'timeUpdate':dt.datetime.today(),
                                    'addData':'incomplete'
                                })
                        except pymongo.errors.DuplicateKeyError:
                            rawData.append((pymongo.UpdateOne(
                                {
                                    'id_str':item['id_str']
                                },
                                {
                                    '$set': {
                                        'data':item,
                                        'timeUpdate':dt.datetime.today(),
                                        'addData':'incomplete'
                                    }
                                },upsert=True)))
            if(len(rawData)>0):
                db.tweet_raw_data.bulk_write(rawData,ordered=False)
                rawData=[]
            DataCleansing.tweetSearchCleansing()
            t1 = time.time()
            print('API-',i+1,': %f'%(t1-t0))
        except:
            print('Next API')
            next

# In[ ]:
if __name__ == '__main__':
    while True:
        getRawTwitter()         
