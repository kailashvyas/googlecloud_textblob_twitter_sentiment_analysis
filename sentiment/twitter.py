import os
import tweepy


class Twitter:

    def __init__(self):
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def get_tweets(self, text):
        tweets = []
        for item in self.api.search(q=text, count=100):
            tweets.append(item.text)
        return tweets
