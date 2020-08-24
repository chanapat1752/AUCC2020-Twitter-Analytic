# In[ ]:
# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import datetime as dt
import time

#In[]:
client = MongoClient('mongodb://localhost:27017/University')
db = client.University

#In[]:
def getRetweetPerMinute():
    dataA = db.retweet_update_data.find()
    thistime = dt.datetime.today()
    for item in dataA:
        db.retweet_state_data.insert_one(
            {
                'university':item['university'],
                'id_str':item['id_str'],
                'retweet_count':item['retweet_count'],
                'favorite_count':item['favorite_count'],
                'timeUpdate':thistime
            }
        )
    dataB = db.retweet_state_data.aggregate([
            { "$group": {
                "_id": "$id_str",
                "retweetNow": { 
                    "$sum": { 
                        "$cond": [
                            { "$gte": [ "$timeUpdate", dt.datetime.today() - dt.timedelta(seconds=30) ] },
                            "$retweet_count", 
                            0
                        ]
                    }
                },
                "retweetPrevious": { 
                    "$sum": { 
                        "$cond": [
                            { "$lte": [ "$timeUpdate", dt.datetime.today() - dt.timedelta(seconds=30)] },
                            "$retweet_count", 
                            0
                        ]
                    }
                },
                "favouriteNow": { 
                    "$sum": { 
                        "$cond": [
                            { "$gte": [ "$timeUpdate", dt.datetime.today() - dt.timedelta(seconds=30) ] },
                            "$favorite_count", 
                            0
                        ]
                    }
                },
                "favouritePrevious": { 
                    "$sum": { 
                        "$cond": [
                            { "$lte": [ "$timeUpdate", dt.datetime.today() - dt.timedelta(seconds=30)] },
                            "$favorite_count", 
                            0
                        ]
                    }
                }
            }},
            { "$project": {
                "retweetInThisMin": { "$subtract": [ "$retweetNow", "$retweetPrevious" ] },
                "favouriteInThisMin": { "$subtract": [ "$favouriteNow", "$favouritePrevious" ] }
            }}
        ])
    dataC = db.retweet_state_data.aggregate([
            { "$group": {
                "_id": "$university",
                "retweetNow": { 
                    "$sum": { 
                        "$cond": [
                            { "$gte": [ "$timeUpdate", dt.datetime.today() - dt.timedelta(seconds=30) ] },
                            "$retweet_count", 
                            0
                        ]
                    }
                },
                "retweetPrevious": { 
                    "$sum": { 
                        "$cond": [
                            { "$lte": [ "$timeUpdate", dt.datetime.today() - dt.timedelta(seconds=30)] },
                            "$retweet_count", 
                            0
                        ]
                    }
                },
                "favouriteNow": { 
                    "$sum": { 
                        "$cond": [
                            { "$gte": [ "$timeUpdate", dt.datetime.today() - dt.timedelta(seconds=30) ] },
                            "$favorite_count", 
                            0
                        ]
                    }
                },
                "favouritePrevious": { 
                    "$sum": { 
                        "$cond": [
                            { "$lte": [ "$timeUpdate", dt.datetime.today() - dt.timedelta(seconds=30)] },
                            "$favorite_count", 
                            0
                        ]
                    }
                }
            }},
            { "$project": {
                "retweetInThisMin": { "$subtract": [ "$retweetNow", "$retweetPrevious" ] },
                "favouriteInThisMin": { "$subtract": [ "$favouriteNow", "$favouritePrevious" ] }
            }}
        ])
    deleteRetweetPerMin()
    for item in dataB:
        k = db.retweet_state_data.find_one({'id_str':item['_id']})
        db.retweet_permin_data.insert_one(
                {
                'university':k['university'],
                'id_str':item['_id'],
                'retweet':
                    {
                        'retweet_thismin':item['retweetInThisMin'],
                    },
                'favourite':
                    {
                        'favorite_thismin':item['favouriteInThisMin'],
                    },
                'timeUpdate':thistime
                }
            )
    for item in dataC:
        db.uni_count_permin_data.insert_one(
            {
            'university':item['_id'],
            'retweet':
                    {
                        'retweet_thismin':item['retweetInThisMin'],
                    },
                'favourite':
                    {
                        'favorite_thismin':item['favouriteInThisMin'],
                    },
                'timeUpdate':thistime
            }
        ) 
def deleteRetweetPerMin():
    db.retweet_state_data.delete_many({'timeUpdate':{'$lt':dt.datetime.today() - dt.timedelta(seconds=30)}})

# In[ ]:
if __name__ == '__main__':
    while True:
        curr_datetime = dt.datetime.now()
        curr_sec = curr_datetime.second
        if(curr_sec == 0):
                t0 = time.time()
                getRetweetPerMinute()
                t1 = time.time()
                t2 = t1-t0
                print(t2)