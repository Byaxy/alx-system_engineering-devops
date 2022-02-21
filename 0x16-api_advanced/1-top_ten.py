#!/usr/bin/python3
''' Contains the number_of_subscribers function '''

import requests
import sys


def top_ten(subreddit):
    '''prints titles of the first 10 hot posts listed for a given subreddit'''
    headers = {'User-agent': 'hbnbtest'}
    url = 'https://www.reddit.com/r/'
    posts = requests.get(url + '{}/hot.json?limit=10'.format(
        sys.argv[1]), allow_redirects=False, headers=headers)

    if posts.status_code == 200:
        for post in posts.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
