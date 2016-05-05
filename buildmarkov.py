import pickle
import time,sys
def build_dict(topic):
    input_path = topic+'.txt'
    tweets = open(input_path,'r')
    markov = {'\n':[]}
    
    for tweet in tweets:
        tweet = [word.lower() for word in tweet.split()]
    
        #Remove bad stuff
        for word in tweet:
            if word[:4] == 'http':
                tweet.remove(word)
            if word[0] == '@':
                tweet.remove(word)

        #don't process empty tweets
        if len(tweet)==0:
            continue

        for i in range(len(tweet)):
            if i == 0:
                markov['\n'].append(tweet[0])
            
            if tweet[i] not in markov:
                markov[tweet[i]] = []
            try:
                markov[tweet[i]].append(tweet[i+1])
                
            except IndexError:
                markov[tweet[i]].append('\n')
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

