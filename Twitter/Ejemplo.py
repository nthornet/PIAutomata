import tweepy

ckey = "dvlMlZFX7927kEqaNEFaVg"
csecret = "OEBysw9gGRzrpsJyZCcvK2uytSPHVlgb021b1zlfUo"
atoken = "86863810-bxfssXDyzrzHuAWbStClTzDkVU6T4kjo6hNh8sLMJ"
asecret = "tw2cBjRzYZVNNrm84mo9GPj3JZqdEQ0EIhMyY0i7jp04N"

OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret,
    'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q=('"cuzco"'), since='2020-05-11', until='2020-05-12').items(5):
    t=1
    tweet.text

