import tweepy
import csv
import pandas as pd
import wget

####input your credentials here
consumer_key = "dvlMlZFX7927kEqaNEFaVg"
consumer_secret = "OEBysw9gGRzrpsJyZCcvK2uytSPHVlgb021b1zlfUo"
access_token = "86863810-bxfssXDyzrzHuAWbStClTzDkVU6T4kjo6hNh8sLMJ"
access_token_secret = "tw2cBjRzYZVNNrm84mo9GPj3JZqdEQ0EIhMyY0i7jp04N"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Open/Create a file to append data
csvFile = open('ua.csv', 'a')
# Use csv Writer
csvWriter = csv.writer(csvFile)
media_files = set()
puntaje = 0
lista = {}
for tweet in tweepy.Cursor(api.search, q="#cusco", count=10,
                           lang="en",
                           since="2017-04-03").items():

    media = tweet.entities.get('media', [])
    if (len(media) > 0):
        # print("favorite_count: " , tweet.favorite_count)
        # print("retweet_count: " , tweet.retweet_count)
        puntaje += tweet.favorite_count
        puntaje += tweet.retweet_count * 2
        lista[media[0]['media_url']] = puntaje
        puntaje = 0
        # print("--------------------------")
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

sorted_lista = sorted(lista.items(), key=lambda kv: kv[1], reverse=True)

i = 1
for img in sorted_lista:
    print("EL puntaje es: ", img[1])
    wget.download(img[0])
    if i == 3:
        break
    i += 1