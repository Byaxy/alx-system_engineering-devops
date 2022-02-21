#!/usr/bin/python3
''' Contains the number_of_subscribers function '''

import requests
import sys


def number_of_subscribers(subreddit):
    '''gets num of subscribers of a subreddit'''
    headers = {'User-agent': 'hbnbtest'}
    subs = requests.get('https://www.reddit.com/r/{}/about.json'.format(
        sys.argv[1]), allow_redirects=False, headers=headers)

    if subs.status_code == 200:
        return (subs.json()['data']['subscribers'])
    else:
        return 0
