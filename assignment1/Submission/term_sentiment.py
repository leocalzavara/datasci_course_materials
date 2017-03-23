import sys
import json


def lines(fp):
    print str(len(fp.readlines()))

def make_sent_dict(sent_filename):
    afinnfile = open(sent_filename)
    scores = {}
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
    sent_dict = make_sent_dict(sys.argv[1])
    tweets = parse_tweet(sys.argv[2])
    term_sentiment = {}
    for tweet in tweets:
        words = tweet.split()
        tweet_score = sum([sent_dict[word] if sent_dict.has_key(word) else 0 for word in words])
        for word in words:
            if word not in sent_dict:
                sentiment = tweet_score / float(len(words))
                if word in term_sentiment:
                    term_sentiment[word] += sentiment
                else:
                    term_sentiment[word] = sentiment
    
    for term, sentiment in term_sentiment.items():
        print term + ' ' + str(sentiment)

if __name__ == '__main__':
    main()
