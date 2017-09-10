#!/usr/bin/python

import json, logging, sys, time
from StringIO import StringIO

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#ADD YOUR STUFF HERE!
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


class MyStreamListener(StreamListener):
    """ 
    A listener handles tweets that are received from the stream.
    """
    def on_data(self, dataStr):
        data = json.loads(dataStr)
        if "text" not in data:#"empty tweet? ignore
            return True
        print data["text"]
        output.write(data["text"].encode('utf-8')+'\n')
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":

    if len(sys.argv) == 2:
        topic = sys.argv[1]
    else:
        print "Usage: python listener.py <hashtag>"
        sys.exit(1)
    output_path = topic+'.txt'
    output = open(output_path,'a')

    listen = MyStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listen)
    stream.filter(track=[topic])

