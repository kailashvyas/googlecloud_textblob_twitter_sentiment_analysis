import os
import tweepy


class Twitter:

    """ Searches and returns 100 tweets using tweepy library
    """

    def __init__(self):

        """ Initialize twitter api variables
            authenticate and initialize twitter
         """

        # Specify the twitter variables in environment
        consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
        consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
        access_token = os.getenv('TWITTER_TOKEN')
        access_token_secret = os.getenv('TWITTER_TOKEN_SECRET')

        # Authenticate twitter
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def get_tweets(self, text):

        """ Searxh twitter and return 100 tweets

        Args:
            text (string): text to search in twitter

        Returns:
            array: Returns array of tweets in text format
        """
        tweets = []
        for item in self.api.search(q=text, count=100):
            tweets.append(item.text)

        return tweets
