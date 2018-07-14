from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from textblob import TextBlob


class Sentiment():

    """ Sentiment class to analyze tweets
        Analyzes using google cloud language api and text blob library
    """

    def __init__(self):
        self.client = language.LanguageServiceClient()

    def get_google_sentiment(self, text):

        """ Get google sentiment

        Args:
            text (string): text to analyze sentiment. In this case we are passing tweet

        Returns:
            object: Returns object in this format { score: value1, magnitude: value2 }
        """

        # language en is passed as this was throwing error if it encounters a tweet with language other than en
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT,
            language="en")
        sentiment = self.client.analyze_sentiment(document=document).document_sentiment

        return sentiment

    def get_text_blob_sentiment(self, text):

        """ Get Textblob sentiment

        Args:
            text (string): text to analyze sentiment. In this case we are passing tweet

        Returns:
            object: Returns object in this format { polarity: value1, subjectivity: value2 }
        """
        analysis = TextBlob(text)

        return analysis.sentiment

    def process_data(self, data):

        """ Process tweets specified in array

         Args:
             data (array): tweets to analyze

         Returns:
             array: Returns sentiment in array
         """

        sentiment = []
        for item in data:
            sentiment.append({'text': item,
                              'google': self.get_google_sentiment(item),
                              'textblob': self.get_text_blob_sentiment(item)})

        return sentiment


    def get_google_sentiment_percentage(self, data):

        """ Calculate google sentiment percentage.
            Calculates positive, negative and neutral sentiment percentage

         Args:
             data (array): tweets to analyze

         Returns:
             dict: Returns dictionary in this format
                    {
                        positive: value1,
                        negative: value2,
                        neutral: value3,
                        total: value4
                    }
         """
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

        """ Calculate text blob sentiment percentage.
            Calculates positive, negative and neutral sentiment percentage

         Args:
             data (array): tweets to analyze

         Returns:
             dict: Returns dictionary in this format
                    {
                        positive: value1,
                        negative: value2,
                        neutral: value3,
                        total: value4
                    }
         """
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
