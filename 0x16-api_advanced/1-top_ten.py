#!/usr/bin/python3
''' Contains the number_of_subscribers function '''

import requests
import sys


def number_of_subscribers(subreddit):
    '''gets the titles of the first 10 hot posts listed for a given subreddit'''
    headers = {'User-agent': 'hbnbtest'}
    posts = requests.get('https://www.reddit.com/r/{}/about.json?limit=10'.format(
        sys.argv[1]), allow_redirects=False, headers=headers)

    if posts.status_code == 200:
        for post in posts.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
