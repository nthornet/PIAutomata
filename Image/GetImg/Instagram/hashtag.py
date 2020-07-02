loader = Instaloader()
NUM_POSTS = 10

def get_hashtags_posts(query):
    posts = loader.get_hashtag_posts(query)
    users = {}
    count = 0
    for post in posts:
        profile = post.owner_profile
        if profile.username not in users:
            summary = engagement.get_summary(profile)
            users[profile.username] = summary
            count += 1
            print('{}: {}'.format(count, profile.username))
            if count == NUM_POSTS:
                break
    return users