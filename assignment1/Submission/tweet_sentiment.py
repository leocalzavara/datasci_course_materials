import sys
import string
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def make_sent_dict(sent_filename):
    afinnfile = open(sent_filename)
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores

def parse_tweet(tweet_filename):
    tweetfile = open(tweet_filename)
    tweets = []
    for line in tweetfile:
        tweet = json.loads(line)
        if tweet.has_key('text'):
            tweets.append(tweet['text'].encode('utf8').translate(None, '!"#$%&\()*+,-./:;<=>?@[\\]^_{|}~'))
        else:
            tweets.append('')
    return tweets

def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    sent_dict = make_sent_dict(sys.argv[1])
    tweets = parse_tweet(sys.argv[2])
    for tweet in tweets:
        words = tweet.split()
        word_scores = map(lambda word: sent_dict[word] if sent_dict.has_key(word) else 0, words)
        print sum(word_scores)

if __name__ == '__main__':
    main()
