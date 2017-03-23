import sys
import json


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
    tweets = parse_tweet(sys.argv[1])
    total_words = 0
    term_count = {}
    for tweet in tweets:
        words = tweet.split()
        total_words += len(words)
        for word in words:
            if word in term_count:
                term_count[word] += 1
            else:
                term_count[word] = 1
    
    for term, count in term_count.items():
        print term + ' ' + str(count/float(total_words))

if __name__ == '__main__':
    main()
