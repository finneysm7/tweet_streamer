#!/usr/bin/env python3
import tweepy
import logging
import os
import pprint

consumer_token = os.environ['CONSUMER_TOKEN']
consumer_key = os.environ['CONSUMER_KEY']
access_token = os.environ['ACCESS_TOKEN']
access_key = os.environ['ACCESS_SECRET']
auth = tweepy.OAuthHandler(consumer_token, consumer_key)
auth.set_access_token(access_token, access_key)

api = tweepy.API(auth)
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

geoStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=geoStreamListener)
myStream.filter(track=['Donald Trump'], languages=['en'])

# try:
#     myStream = tweepy.Stream(auth = api.auth, listener=geoStreamListener())
#     myStream.filter(track=['python'], languages=['en'])
# except KeyboardInterrupt:
#     #User pressed ctrl+c or cmd+c -- get ready to exit the program
#     print("KeyboardInterrupt caught. Closing stream and exiting.")
#     myStream.disconnect()