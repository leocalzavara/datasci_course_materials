import sys
import string
import json


def parse_tweet(tweet_filename):
    tweetfile = open(tweet_filename)
    hashtags = {}
    for line in tweetfile:
        tweet = json.loads(line)
        if 'lang' in tweet and tweet['lang'] != 'en':
            continue
        if 'entities' in tweet and 'hashtags' in tweet['entities'] and tweet['entities']['hashtags']:
            for hashtag in tweet['entities']['hashtags']:
                x = hashtag['text'].encode('utf-8')
                if x in hashtags:
                    hashtags[x] += 1
                else:
                    hashtags[x] = 1
    return hashtags

def get_value(dict):
    return dict[1]

def main():
    hashtags = parse_tweet(sys.argv[1])
    #print hashtags
    sorted_hashtags = sorted(hashtags.items(), key=get_value, reverse=True)
    for k, v in sorted_hashtags[0:10]:
        print k, v

if __name__ == '__main__':
    main()
