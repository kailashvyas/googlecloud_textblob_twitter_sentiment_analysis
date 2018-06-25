from app import app
from sentiment import twitter, sentiment
from flask import render_template, url_for, request


@app.route('/')
@app.route('/index')
def index():

    return render_template('home.html')


@app.route('/tweets')
def tweets():
    t = twitter.Twitter()
    search = request.args.get('search')
    data = t.get_tweets(search)
    s = sentiment.Sentiment()
    data = s.process_data(data)
    google_sentiment_percentage = s.get_google_sentiment_percentage(data)
    text_blob_percentage = s.get_text_blob_percentage(data)

    return render_template('tweets.html',
                           data=data,
                           google_sentiment_percentage=google_sentiment_percentage,
                           text_blob_percentage=text_blob_percentage)
