from flask import Flask
import pymongo
import twint
import datetime
import pandas as pd
import pandas as pd
import requests
from requests_oauthlib import OAuth1
import time


import nest_asyncio
nest_asyncio.apply()

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["twitter"]
mycol = mydb["data"]
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def get_intervals(date_from,date_to):
    i=date_from
    j=i+datetime.timedelta(days=3)
    lst=[]
    while True:
        if(j>=date_to):
            lst.append((i,date_to))
            break
        else:
            lst.append((i,j))
            i=i+datetime.timedelta(days=3)
            j=j+datetime.timedelta(days=3)
            continue
    return lst

def get_user_tweets_3days(usr,date_from,date_to):
    c = twint.Config()
    c.Pandas =True
    c.Username=usr
    #c.Retweets = True
    c.Since = date_from
    c.Until = date_to
    twint.run.Search(c)
    print(usr,date_from,date_to)
    return twint.storage.panda.Tweets_df

def get_user_tweets(link,date_from=(datetime.date.today()-datetime.timedelta(days=7)).strftime('%Y-%m-%d'),date_to=datetime.date.today().strftime('%Y-%m-%d')):
    df=pd.DataFrame()
    usr=link.split('/')[-1]
    lst= get_intervals(datetime.datetime.strptime(date_from,'%Y-%m-%d'),datetime.datetime.strptime(date_to,'%Y-%m-%d'))
    for l in lst:
        df=df.append(get_user_tweets_3days(usr,l[0].strftime('%Y-%m-%d'),l[1].strftime('%Y-%m-%d')),ignore_index=True)
    return df
    
@app.route("/get")
def get():
    df=get_user_tweets('https://twitter.com/laurenarankin','2022-07-05','2022-07-19') 
    df.to_csv('laurenaracdnkin_tweets.csv')
    print(df)
    return "<p>ok</p>"