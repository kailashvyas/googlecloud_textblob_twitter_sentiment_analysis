##  Twitter Sentiment Analysis using google cloud library and text blob

This is a flask web app which compares sentiment analysis with google cloud and textblob


## Getting started

 * Install Python 3 https://www.python.org/downloads/
 * Create a twitter dev app https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app
    and set enviroment variables TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_TOKEN, TWITTER_TOKEN_SECRET
 * Create a google credentials and set environment variable GOOGLE_APPLICATION_CREDENTIALS. Also enable Cloud Natural Language API
      https://support.google.com/googleapi/answer/6158862
      https://cloud.google.com/natural-language/docs/quickstart#set_up_a_project
 * Run pip install requirements.txt. This should install dependencies flask, google cloud, tweepy and textblob
 * Run python run.py
 * Visit https://127.0.0.1:5000
 * Search with a keyword in search box. This should return 100 tweets and process each tweet for sentiment analysis. This is presented in charts



App is deployed to heroku https://salty-bastion-31857.herokuapp.com/sentiment-index