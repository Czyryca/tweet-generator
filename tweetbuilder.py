import pickle
from collections import Counter
import random
import sys

MAX_TWEET_SIZE = 140 
MAX_ATTEMPTS = 10
markov = {}


def buildtweet():
    return tweetbuilder(0,'\n')

'''
Recursively generates a tweet based on the last word added to the sentence.
To use, call the bootstrap buildtweet()
'''

def tweetbuilder(current_length,last_word):
#print 'entering tweetbuilder... len:'+str(current_length)+' last:'+last_word
    if last_word == '\n' and current_length>0:
        return ''
    iter = MAX_ATTEMPTS
    next_word = ''
    
    while next_word == '':
        possibilities = markov[last_word]
        next_word = possibilities[random.randint(0,len(possibilities)-1)]
        if len(next_word) + current_length > MAX_TWEET_SIZE: #140 is default
            if iter <= 0:
                return ''
            next_word = ''
            iter -= 1

    return ' '+next_word+tweetbuilder(current_length+len(next_word),next_word)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        num_tweets = int(sys.argv[1])
    else:
        num_tweets = 10
    input = open('output.pickle','r')
    markov = pickle.load(input)
    for i in range(num_tweets):
        print buildtweet()







