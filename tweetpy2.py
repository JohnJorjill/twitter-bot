import tweepy
import time

# Here we set our tokens and create our api object which is the main object we will use

auth = tweepy.OAuthHandler('')
auth.set_access_token('')

api = tweepy.API(auth)
user = api.me()


def limit_handler(cursor):  # this function will do time.sleep(300) if there is tweepy.RateLimitError error which happenes when you abuse api
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)
    except StopIteration:
        print('done')


search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets): # tweepy.Cursor(api.search, search_string) will search all tweets with search_string and numberOfTweets
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepyError as e:
        print(e.reason)
    except StopIteration:
        break