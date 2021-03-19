#!/usr/bin/python3


import tweepy
import time, datetime


consumer_key = 'REDACTED'
consumer_secret = 'REDACTED'

key = 'REDACTED'
secret = 'REDACTED'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

def twitter_bot(hashtag, delay):
    while True:
        print(f"\n{datetime.datetime.now()}\n")

        for tweet in tweepy.Cursor(api.search, q=hashtag, rpp=200).items(200):
            try:
                tweet_id = dict(tweet._json)["id"]
                tweet_text = dict(tweet._json)["text"]

                print("id" + str(tweet_id))
                print("text: " + str(tweet_text))

                api.retweet(tweet_id)
                api.create_favorite(tweet_id)
                #store_last_seen(FILE_NAME, tweet_id)
        
            except tweepy.TweepError as error:
                print(error.reason)

        time.sleep(delay)


twitter_bot("$FTM", 60)
