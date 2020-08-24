# In[ ]:
# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import datetime as dt
import time
#In[]:
client = MongoClient('mongodb://localhost:27017/University')
db = client.University
db.master_data.create_index([('id_str', pymongo.ASCENDING)], unique=True)
db.retweet_update_data.create_index([('id_str', pymongo.ASCENDING)], unique=True)

#In[]:
def addHours(time):
    formatT = dt.datetime.strptime(time, '%a %b %d %X +0000 %Y')
    now = formatT + dt.timedelta(hours=7)
    return now.strftime('%a %b %d %X +7 %Y')

#In[]:
def tweetSearchCleansing():
    masterData = []
    rawData = []
    retweetCountUpdate = []
    dataA = db.tweet_raw_data.find({"addData":"incomplete"})
    for item in dataA:
        try:
            strTime = addHours(item['data']['created_at'])
            db.master_data.insert_one(
                {
                    'university':item['university'],
                    'keyword':item['keyword'],
                    'id_str': item['id_str'],
                    'created_at': strTime,
                    'text':item['data']['full_text'],
                    'user_id':item['data']['user']['id_str'],
                    'user_name':item['data']['user']['name'],
                    'user_screen-name':item['data']['user']['screen_name'],
                    'user_followers':item['data']['user']['followers_count'],
                    'retweet_count':item['data']['retweet_count'],
                    'favorite_count':item['data']['favorite_count'],
                    'hashtags':item['data']['entities']['hashtags'],
                    'timeUpdate':dt.datetime.today()
                }
            )
            db.retweet_update_data.insert_one(
                {
                    'university':item['university'],
                    'id_str':item['id_str'],
                    'retweet_count':0,
                    'favorite_count':0,
                    'timeUpdate':dt.datetime.today()
                }
            ) 
            rawData.append((pymongo.UpdateOne(
                {
                    'id_str':item['id_str']
                },
                {
                    '$set': {
                        'addData':'complete'
                    }
                },upsert=True)))
        except pymongo.errors.DuplicateKeyError:
            masterData.append((pymongo.UpdateOne(
                {
                    'id_str':item['id_str']
                },
                {
                    '$set': {
                        'user_name':item['data']['user']['name'],
                        'user_screen-name':item['data']['user']['screen_name'],
                        'user_followers':item['data']['user']['followers_count'],
                        'retweet_count':item['data']['retweet_count'],
                        'favorite_count':item['data']['favorite_count'],
                        'timeUpdate':dt.datetime.today()
                    }
                },upsert=True)))
            idUpdate = db.retweet_update_data.find_one({'id_str':item['id_str']})
            masterId = db.master_data.find_one({'id_str':item['id_str']})
            retweet = item['data']['retweet_count'] - masterId['retweet_count']
            favourite = item['data']['favorite_count'] - masterId['favorite_count']
            retweetCountUpdate.append((pymongo.UpdateOne(
                {
                    'id_str':item['id_str']
                },
                {
                    '$set': {
                        'retweet_count':idUpdate['retweet_count']+retweet,
                        'favorite_count':idUpdate['favorite_count']+favourite,
                        'timeUpdate':dt.datetime.today()
                    }
                },upsert=True)))
            rawData.append((pymongo.UpdateOne(
                {
                    'id_str':item['id_str']
                },
                {
                    '$set': {
                        'addData':'complete'
                    }
                },upsert=True)))
    if(len(masterData)>0):
        db.master_data.bulk_write(masterData,ordered=False)
        db.retweet_update_data.bulk_write(retweetCountUpdate,ordered=False)
    if(len(rawData)>0):
        db.tweet_raw_data.bulk_write(rawData,ordered=False)

#In[]:
def tweetFilterCleansing():
    masterData = []
    rawData = []
    retweetCountUpdate = []
    dataA = db.tweetFilter_raw_data.find({"addData":"incomplete"})
    for item in dataA:
        try:
            if "extended_tweet" in item['data']:
                strTime = addHours(item['data']['created_at'])
                db.master_data.insert_one(
                    {
                        'university':item['university'],
                        'keyword':item['keyword'],
                        'id_str': item['id_str'],
                        'created_at': strTime,
                        'text':item['data']['extended_tweet']['full_text'],
                        'user_id':item['data']['user']['id_str'],
                        'user_name':item['data']['user']['name'],
                        'user_screen-name':item['data']['user']['screen_name'],
                        'user_followers':item['data']['user']['followers_count'],
                        'retweet_count':item['data']['retweet_count'],
                        'favorite_count':item['data']['favorite_count'],
                        'hashtags':item['data']['extended_tweet']['entities']['hashtags'],
                        'timeUpdate':dt.datetime.today()
                    }
                )
                db.retweet_update_data.insert_one(
                    {
                        'university':item['university'],
                        'id_str':item['id_str'],
                        'retweet_count':0,
                        'favorite_count':0,
                        'timeUpdate':dt.datetime.today()
                    }
                ) 
                print('create_to_master')
                rawData.append((pymongo.UpdateOne(
                    {
                        'id_str':item['id_str']
                    },
                    {
                        '$set': {
                            'addData':'complete'
                        }
                    },upsert=True)))
            else:
                strTime = addHours(item['data']['created_at'])
                db.master_data.insert_one(
                    {
                        'university':item['university'],
                        'keyword':item['keyword'],
                        'id_str': item['id_str'],
                        'created_at': strTime,
                        'text':item['data']['text'],
                        'user_id':item['data']['user']['id_str'],
                        'user_name':item['data']['user']['name'],
                        'user_screen-name':item['data']['user']['screen_name'],
                        'user_followers':item['data']['user']['followers_count'],
                        'retweet_count':item['data']['retweet_count'],
                        'favorite_count':item['data']['favorite_count'],
                        'hashtags':item['data']['entities']['hashtags'],
                        'timeUpdate':dt.datetime.today()
                    }
                )
                db.retweet_update_data.insert_one(
                    {
                        'university':item['university'],
                        'id_str':item['id_str'],
                        'retweet_count':0,
                        'favorite_count':0,
                        'timeUpdate':dt.datetime.today()
                    }
                )
                print('create_to_master')
                rawData.append((pymongo.UpdateOne(
                    {
                        'id_str':item['id_str']
                    },
                    {
                        '$set': {
                            'addData':'complete'
                        }
                    },upsert=True)))
        except pymongo.errors.DuplicateKeyError:
            masterData.append((pymongo.UpdateOne(
                {
                    'id_str':item['id_str']
                },
                {
                    '$set': {
                        'user_name':item['data']['user']['name'],
                        'user_screen-name':item['data']['user']['screen_name'],
                        'user_followers':item['data']['user']['followers_count'],
                        'retweet_count':item['data']['retweet_count'],
                        'favorite_count':item['data']['favorite_count'],
                        'timeUpdate':dt.datetime.today()
                    }
                },upsert=True)))
            idUpdate = db.retweet_update_data.find_one({'id_str':item['id_str']})
            masterId = db.master_data.find_one({'id_str':item['id_str']})
            retweet = item['data']['retweet_count'] - masterId['retweet_count']
            favourite = item['data']['favorite_count'] - masterId['favorite_count']
            retweetCountUpdate.append((pymongo.UpdateOne(
                {
                    'id_str':item['id_str']
                },
                {
                    '$set': {
                        'retweet_count':idUpdate['retweet_count']+retweet,
                        'favorite_count':idUpdate['favorite_count']+favourite,
                        'timeUpdate':dt.datetime.today()
                    }
                },upsert=True)))
            print('update_to_master')
            rawData.append((pymongo.UpdateOne(
                {
                    'id_str':item['id_str']
                },
                {
                    '$set': {
                        'addData':'complete'
                    }
                },upsert=True)))
    if(len(masterData)>0):
        db.master_data.bulk_write(masterData,ordered=False)
        db.retweet_update_data.bulk_write(retweetCountUpdate,ordered=False)
    if(len(rawData)>0):
        db.tweetFilter_raw_data.bulk_write(rawData,ordered=False)    

#In[]:
def retweetFilterCleansing():
    masterData = []
    rawData = []
    retweetCountUpdate = []
    dataA = db.retweet_raw_data.find({"addData":"incomplete"})
    for item in dataA:
        try:
            if "extended_tweet" in item['data']['retweeted_status']:
                strTime = addHours(item['data']['retweeted_status']['created_at'])
                db.master_data.insert_one(
                    {
                        'university':item['university'],
                        'keyword':item['keyword'],
                        'id_str': item['data']['retweeted_status']['id_str'],
                        'created_at': strTime,
                        'text':item['data']['retweeted_status']['extended_tweet']['full_text'],
                        'user_id':item['data']['retweeted_status']['user']['id_str'],
                        'user_name':item['data']['retweeted_status']['user']['name'],
                        'user_screen-name':item['data']['retweeted_status']['user']['screen_name'],
                        'user_followers':item['data']['retweeted_status']['user']['followers_count'],
                        'retweet_count':item['data']['retweeted_status']['retweet_count'],
                        'favorite_count':item['data']['retweeted_status']['favorite_count'],
                        'hashtags':item['data']['retweeted_status']['extended_tweet']['entities']['hashtags'],
                        'timeUpdate':dt.datetime.today()
                    }
                )
                db.retweet_update_data.insert_one(
                    {
                        'university':item['university'],
                        'id_str':item['data']['retweeted_status']['id_str'],
                        'retweet_count':0,
                        'favorite_count':0,
                        'timeUpdate':dt.datetime.today()
                    }
                ) 
                print('create_to_master')
                rawData.append((pymongo.UpdateOne(
                    {
                        'id_str':item['id_str']
                    },
                    {
                        '$set': {
                            'addData':'complete'
                        }
                    },upsert=True)))
            else:
                strTime = addHours(item['data']['retweeted_status']['created_at'])
                db.master_data.insert_one(
                    {
                        'university':item['university'],
                        'keyword':item['keyword'],
                        'id_str': item['data']['retweeted_status']['id_str'],
                        'created_at': strTime,
                        'text':item['data']['retweeted_status']['text'],
                        'user_id':item['data']['retweeted_status']['user']['id_str'],
                        'user_name':item['data']['retweeted_status']['user']['name'],
                        'user_screen-name':item['data']['retweeted_status']['user']['screen_name'],
                        'user_followers':item['data']['retweeted_status']['user']['followers_count'],
                        'retweet_count':item['data']['retweeted_status']['retweet_count'],
                        'favorite_count':item['data']['retweeted_status']['favorite_count'],
                        'hashtags':item['data']['retweeted_status']['entities']['hashtags'],
                        'timeUpdate':dt.datetime.today()
                    }
                )
                db.retweet_update_data.insert_one(
                    {
                        'university':item['university'],
                        'id_str':item['data']['retweeted_status']['id_str'],
                        'retweet_count':0,
                        'favorite_count':0,
                        'timeUpdate':dt.datetime.today()
                    }
                )
                print('create_to_master')
                rawData.append((pymongo.UpdateOne(
                    {
                        'id_str':item['id_str']
                    },
                    {
                        '$set': {
                            'addData':'complete'
                        }
                    },upsert=True)))
        except pymongo.errors.DuplicateKeyError:
            masterData.append((pymongo.UpdateOne(
                {
                    'id_str':item['data']['retweeted_status']['id_str']
                },
                {
                    '$set': {
                        'user_name':item['data']['retweeted_status']['user']['name'],
                        'user_screen-name':item['data']['retweeted_status']['user']['screen_name'],
                        'user_followers':item['data']['retweeted_status']['user']['followers_count'],
                        'retweet_count':item['data']['retweeted_status']['retweet_count'],
                        'favorite_count':item['data']['retweeted_status']['favorite_count'],
                        'timeUpdate':dt.datetime.today()
                    }
                },upsert=True)))
            idUpdate = db.retweet_update_data.find_one({'id_str':item['data']['retweeted_status']['id_str']})
            masterId = db.master_data.find_one({'id_str':item['data']['retweeted_status']['id_str']})
            retweet = item['data']['retweeted_status']['retweet_count'] - masterId['retweet_count']
            favourite = item['data']['retweeted_status']['favorite_count'] - masterId['favorite_count']
            retweetCountUpdate.append((pymongo.UpdateOne(
                {
                    'id_str':item['data']['retweeted_status']['id_str']
                },
                {
                    '$set': {
                        'retweet_count':idUpdate['retweet_count']+retweet,
                        'favorite_count':idUpdate['favorite_count']+favourite,
                        'timeUpdate':dt.datetime.today()
                    }
                },upsert=True)))
            print('update_to_master')
            rawData.append((pymongo.UpdateMany(
                {
                    'id_str':item['id_str']
                },
                {
                    '$set': {
                        'addData':'complete'
                    }
                },upsert=True)))
    if(len(masterData)>0):
        db.master_data.bulk_write(masterData,ordered=False)
        db.retweet_update_data.bulk_write(retweetCountUpdate,ordered=False)
    if(len(rawData)>0):
        db.retweet_raw_data.bulk_write(rawData,ordered=False)