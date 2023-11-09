#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers to a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    root = 'https://www.reddit.com/'
    end_point = '/r/{}/about.json'.format(subreddit)
    url = str(root) + str(end_point)
    user_agent = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 \
Safari/537.36 Avast/118.0.0.0"""
    headers = {
            "User-Agent": user_agent
            }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        subscribers = response.json().get('data').get('subscribers')
        if subscribers is not None:
            return subscribers
    else:
        return 0
