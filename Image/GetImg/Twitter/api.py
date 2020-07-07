import tweepy
import csv
import pandas as pd
import wget

####input your credentials here
consumer_key = "dvlMlZFX7927kEqaNEFaVg"
consumer_secret = "OEBysw9gGRzrpsJyZCcvK2uytSPHVlgb021b1zlfUo"
access_token = "86863810-bxfssXDyzrzHuAWbStClTzDkVU6T4kjo6hNh8sLMJ"
access_token_secret = "tw2cBjRzYZVNNrm84mo9GPj3JZqdEQ0EIhMyY0i7jp04N"


def dowloadImagesbyHastag(Hashtag): 
    print(Hashtag)
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    media_files = set()
    puntaje = 0
    lista = {}

    for tweet in tweepy.Cursor(api.search, q=Hashtag, count=10,
                            lang="en",
                            since="2017-04-03").items(100):
        
        media = tweet.entities.get('media', [])
        
        if (len(media) > 0):
            puntaje += tweet.favorite_count
            puntaje += tweet.retweet_count * 2
            lista[media[0]['media_url']] = puntaje
            puntaje = 0
        print("CP")
    sorted_lista = sorted(lista.items(), key=lambda kv: kv[1], reverse=True)

    #Get Best Images
    i = 1
    for img in sorted_lista:
        wget.download(img[0],out="../TestImg/")
        if i == 2:
            break
        i += 1

def getInputHastags():
    NumHashTags = int(input("Ingrese el numero de Hastags: "))
    Hashtags = ""
    for i in range(0,NumHashTags):
        temp = input("Ingrese Hastag: ")   
        Hashtags = Hashtags + temp
    return Hashtags


if __name__ == "__main__": 
    hashtag = getInputHastags()
    dowloadImagesbyHastag(hashtag)