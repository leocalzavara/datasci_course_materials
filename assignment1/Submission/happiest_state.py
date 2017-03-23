import sys
import string
import json


states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}


def make_sent_dict(sent_filename):
    afinnfile = open(sent_filename)
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary
    return scores


def parse_tweet(tweet_filename, sent_dict):
    tweetfile = open(tweet_filename)
    total = 0
    geo_info = { 'coordinates': 0, 'place': 0, 'user': 0 }
    state_score = { x: 0 for x in states } # init state_score as a copy of states but replacing all values with zero
    for line in tweetfile:
        tweet = json.loads(line)
        tweet_score = 0
        if tweet.has_key('text'):
            words = tweet['text'].encode('utf8').translate(None, '!"#$%&\()*+,-./:;<=>?@[\\]^_{|}~').split()
            tweet_score = sum([sent_dict[word] if sent_dict.has_key(word) else 0 for word in words])
        else:
            continue
        total += 1
        # if 'lang' in tweet and tweet['lang'] != 'en':
            # continue
        if 'coordinates' in tweet and tweet['coordinates']:
            geo_info['coordinates'] += 1
            # print tweet['coordinates']
            # todo: find state by coordinates
        elif 'place' in tweet and tweet['place'] and tweet['place']['country_code'] == 'US':
            geo_info['place'] += 1
            location_arr = tweet['place']['full_name'].encode('utf-8').split(',')
            state = get_state(location_arr)
            if state:
                state_score[state] += tweet_score
        elif 'user' in tweet and tweet['user'] and tweet['user']['location']:
            geo_info['user'] += 1
            location_arr = tweet['user']['location'].encode('utf-8').translate(None, '!"#$%&\()*+-./:;<=>?@[\\]^_{|}~').split(',')
            state = get_state(location_arr)
            if state:
                state_score[state] += tweet_score
    
    tweetfile.close()
    #print geo_info
    #print total
    
    return state_score


def get_state(location_arr):
    for location in location_arr:
        for code, name in states.items():
            if location == code or location == name:
                return code
    return None

def get_value(dict):
    return dict[1]

def main():
    sent_dict = make_sent_dict(sys.argv[1])
    state_scores = parse_tweet(sys.argv[2], sent_dict)
    sorted_scores = sorted(state_scores.items(), key=get_value, reverse=True)
    # for state in sorted_scores:
        # print state
    print sorted_scores[0][0]

if __name__ == '__main__':
    main()
