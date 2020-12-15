import tweepy
import csv
import os
import snscrape.modules.twitter as sntwitter
import sys
sys.dont_write_bytecode = True

#ENV_VALUES
tag = os.environ["TAG"]
since_date = os.environ["FROM"]
until_date =  os.environ["UNTIL"]
tweet_count = os.environ["NUM"]

#Provide your own credentials here.
TWITTER_CLIENT_KEY = 'XXXXXXXXXXXXXXXXXX'
TWITTER_CLIENT_SECRET = 'XXXXXXXXXXXXXXXXXX'
TWITTER_CLIENT_ID_ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXX'
TWITTER_CLIENT_ID_ACCESS_TOKEN_SECRET = 'XXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(TWITTER_CLIENT_KEY, TWITTER_CLIENT_SECRET)
auth.set_access_token(TWITTER_CLIENT_ID_ACCESS_TOKEN, TWITTER_CLIENT_ID_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)

#pip install snscrape
csvFile = open('/root/src/csv_files/%s_from_%s_to_%s_%s_tweets.csv' %(tag, since_date, until_date, tweet_count), 'a')
csvWriter = csv.writer(csvFile)
maxTweets = int(tweet_count)  # the number of tweets you require
print('%s since:%s until:%s' % (tag, since_date, until_date))
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('%s' % tag +'since:%s until:%s' % (since_date, until_date)).get_items()) :
        if i > maxTweets :
            break
        csvWriter.writerow([tweet.date, tweet.username, tweet.content]) #If you need more information, just provide the attributes