from textblob import TextBlob
import tweepy as tw

consumer_token = 'Your Consumer Token' //From developer.twitter.com
consumer_secret = 'Your Consumer Secret'
key='Your access key'
secret= 'Your access token'
auth = tw.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(key, secret)
api = tw.API(auth)
public_tweets = api.search('BREXIT')
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    b=analysis.sentences
    print("""
""",b,analysis.sentiment,"""
""")
