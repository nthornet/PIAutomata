import os, shutil
from instaloader import Instaloader
from Image.GetImg.Instagram import engagement
import time

loader = Instaloader()
NUM_POSTS = 10


def get_hashtags_posts(query):
    posts = loader.get_hashtag_posts(query)
    users = {}
    postdata = []
    count = 0
    for post in posts:
        profile = post.owner_profile
        if profile.username not in users:
            summary = engagement.get_summary(profile)
            users[profile.username] = summary
            postdata.append(post)
            count += 1
            print('{}: {}'.format(count, profile.username))
            if count == NUM_POSTS:
                break
    return users, postdata


def get_topengagement(users):
    newdict = {}
    original = {}
    count = 0
    top3 = []
    top3orig = []
    for user in users:
        # recrea el diccionario pero con el engagement como key
        newdict[users[user]['engagement']] = user
        original[users[user]['engagement']] = count
        count += 1
    count = 0
    for key in sorted(newdict.keys(), reverse=True):  # ordena por key
        if count < 3:
            # escoge los 3 mas altos y los guarda en top3
            print("%s : %d " % (newdict[key], key))
            top3.append(newdict[key])
            top3orig.append(original[key])
            count += 1
        else:
            break
    return top3, top3orig


def multihash(hashtags, maxposts):
    mainhash = hashtags[0]
    secondaryhash = hashtags[1:]
    posts = loader.get_hashtag_posts(mainhash)
    users = {}
    postdata = []
    count = 0
    if maxposts > 0:
        for post in posts:
            for hash in secondaryhash:
                if hash in post.caption_hashtags:
                    profile = post.owner_profile
                    if profile.username not in users:
                        summary = engagement.get_summary(profile)
                        users[profile.username] = summary
                        postdata.append(post)
                        count += 1
                        print('{}: {}'.format(count, profile.username))
                        if count == NUM_POSTS:
                            break
            maxposts -= 1
    return users, postdata


def downloadtop3(tops, posts, query,location=None):
    count = 1
    for key in tops:
        loader.download_post(posts[key], '#' + query)
        t = time.strftime("%d_%m_%Y_%H")
        if location is None:
            shutil.move(os.path.join('#' + query), os.path.join(t, '#' + query, 'user' + str(count)))
        else:
            shutil.move(os.path.join('#' + query), location)
        count += 1


if __name__ == "__main__":
    hashtag = "cusco"
    users, posts = multihash(hashtags=['cusco', 'tourism'], maxposts=10)
    # users, posts = get_hashtags_posts(hashtag)
    top, original = get_topengagement(users)
    downloadtop3(original, posts, hashtag)

    print(users)
