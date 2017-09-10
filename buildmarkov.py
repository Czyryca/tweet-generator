import pickle
import time,sys

def build_dict(topic):
    input_path = topic+'.txt'
    tweets = open(input_path,'r')
    markov = {'\n':[]}
    blacklist = open("blacklist.txt",'r')
    
    for tweet in tweets:
        tweet = [word.lower() for word in tweet.split()]
    
        #Remove bad stuff
        for word in tweet:
            if word[:4] == 'http':
                tweet.remove(word)
            if word[0] == '@':
                tweet.remove(word)
            if word in blacklist:
                tweet.remove(word)

        #don't process empty tweets
        if len(tweet)==0:
            continue

        for i in range(len(tweet)):
            if i == 0: #word is the first in the tweet
                markov['\n'].append(tweet[0]) #\n used as placeholder for start
            
            if tweet[i] not in markov: #first use of word, add to keys
                markov[tweet[i]] = []


            try: #add word to list
                markov[tweet[i]].append(tweet[i+1])              
            except IndexError: #word at end of tweet
                markov[tweet[i]].append('\n')#mark this word as ending the tweet
    return markov
                

if __name__ == '__main__':
    if len(sys.argv) == 2:
        topic = sys.argv[1]
    else:
        print "Usage: python buildmarkov.py <input topic [no .txt]>"
        sys.exit(1)
    finished_markov = build_dict(topic)
    output = open('output.pickle','w')
    pickle.dump(finished_markov,output)

