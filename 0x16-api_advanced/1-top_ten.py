#!/usr/bin/python3
"""
This module contains function to get some information concerning subereddits
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts
    if invalid `subreddit`, `None` is printed.
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    MAX_POSTS = 10
    root = 'https://www.reddit.com/'
    end_point = '/r/{}/hot.json'.format(subreddit)
    url = str(root) + str(end_point)
    user_agent = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 \
Safari/537.36 Avast/118.0.0.0"""
    headers = {
            "User-Agent": user_agent
            }

    params = {'limit': MAX_POSTS}
    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)

    if response.status_code == 200:
        count = 0
        top_posts = response.json().get('data').get('children')
        if top_posts is not None:
            for post in top_posts:
                if count >= MAX_POSTS:
                    break
                else:
                    count += 1

                print(post.get('data').get('title'))
    else:
        print(None)
