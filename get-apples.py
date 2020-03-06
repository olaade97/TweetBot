

# theapplesbot

import tweepy as tp
import time
import os

# credentials to login to twitter api
consumer_key = 'HsrqPqzuXKH51ugMZTBwHEcGo'
consumer_secret = 'HHMjADbQ3U3SijWRKDOVNL0CVKlo3tBmKLpA2VBqFQFltsuUXW'
access_token = '1212588645221191680-cgrYJUtPTJsxZfBnCtBnTvw4Mpa0CO'
access_secret = 'Q6eKhFQFPUR4O2b5ymJ5rTij1zWxxnmUZ3stqk0OzsYJT'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('apples')

# iterates over pictures in models folder
for apples_image in os.listdir('.'):
    api.update_with_media(apples_image)
    time.sleep(30)
