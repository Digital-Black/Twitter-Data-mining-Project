import re
import tweepy
import twitter_credentials
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

class MaxListener(tweepy.StreamListener):

    def on_data(self, data):
        sn = str(data.split('"screen_name":',1)[1])
        sn = sn.partition(',')[0]
        sn = re.split('"', ' ' + sn)
        snnew = ''.join(sn)
        text = str(data.split('"text":',1)[1])
        text = text.partition('"source":')[0]
        print(snnew[0:50], text[0:280])

# process_data retained for optional functionality
    def process_data(self, raw_data):
        return True

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

            # returning non-False reconnects the stream, with backoff.

# Create a Stream
class MaxStream():
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self):
        self.stream.filter(track=['place', 'words', 'and', 'sentences', 'between'
                                  'these', 'single', 'quotes',
                                  'to', 'scan',
                                  "for", 'instances', 'of', 'hate',
                                  'speech'])
        for tweet in stream.filter:
            tweet.text = tweet.text.encode('unicode-escape').decode('utf-8')
            tweet.user.name = tweet.user.name.encode('unicode-escape').decode('utf-8')
            print(tweet.user.name + ' ' + tweet.text + '\n')

if __name__ == '__main__':
    listener = MaxListener()

    auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

    stream = MaxStream(auth, listener)
    stream.start()
