from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from textblob import TextBlob

class Sentiment():

    def __init__(self):
        self.client = language.LanguageServiceClient()

    def get_google_sentiment(self, text):
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT,
            language="en")
        sentiment = self.client.analyze_sentiment(document=document).document_sentiment

        return sentiment

    def get_text_blob_sentiment(self, text):
        analysis = TextBlob(text)

        return analysis.sentiment

    def process_data(self, data):
        sentiment = []
        for item in data:
            sentiment.append({'text': item,
                              'google': self.get_google_sentiment(item),
                              'textblob': self.get_text_blob_sentiment(item)})

        return sentiment


    def get_google_sentiment_percentage(self, data):
        positive = 0
        negative = 0
        neutral = 0
        total = len(data)
        for item in data:
            if item['google'].score > 0:
                print("positive counter")
                positive=positive+1
            elif item['google'].score == 0:
                neutral=neutral+1
            else:
                negative=negative+1

        return {'positive': (positive/total)*100,
                'negative': (negative/total)*100,
                'neutral': (neutral/total)*100,
                'total': total}

    def get_text_blob_percentage(self, data):
        positive = 0
        negative = 0
        neutral = 0
        total = len(data)
        for item in data:
            if item['textblob'].polarity > 0:
                positive=positive+1
            elif item['textblob'].polarity == 0:
                neutral=neutral+1
            else:
                negative=negative+1

        return {'positive': (positive/total)*100,
                'negative': (negative/total)*100,
                'neutral': (neutral/total)*100,
                'total': total}
