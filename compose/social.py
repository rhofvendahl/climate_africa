#importing all dependencies
import numpy as np # tweepy dependency
import tweepy # easy to use except for videos

def twauth():
    # API Keys
    consumer_key='XXXXXXXXXXXXXXXXXXXXXXXXXX'
    consumer_secret_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    access_token_secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    # Authenticate Twitter API
    auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
    auth.set_access_token(access_token,access_token_secret)
    api=tweepy.API(auth)

    # return api handler
    return api

def tweet(api, status):
    api.update_status(status)

    # tweets with pictures
    # tweet_media = api.update_with_media(image_path, status)
    # api.update_status(tweet_media)