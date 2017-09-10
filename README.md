# tweet-generator
Python 2 script that builds tweets using Markov Chains. Connects to the Twitter Firehose, learns which words follow which, then strings a valid tweet together. Refuses to use profanity, hyperlinks, or 141+ characters at a time.
Usage: python listener.py <subject>; sh run.sh <subject> <num of tweets>
If you want to do one step at a time:
Usage: python listener.py <subject>; python buildmarkov.py <subject>; python tweetbuilder.py <num of tweets>
