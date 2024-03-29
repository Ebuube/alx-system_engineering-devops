#!/usr/bin/python3
"""
This module contains function to get some information concerning subereddits
"""
import requests


def recurse(subreddit, hot_list=[], after=None, items=0):
    """
    Return a list containing the titles of all hot articles
    for a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    root = 'https://www.reddit.com/'
    end_point = '/r/{}/hot.json'.format(subreddit)
    url = str(root) + str(end_point)
    user_agent = """Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 \
Safari/537.36 Avast/118.0.0.0"""
    headers = {
            "User-Agent": user_agent
            }

    params = {}
    params['show'] = 'all'

    if items > 0:
        params['count'] = items
        params['after'] = after

    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)

    if response.status_code != 200:
        # Request error: may be due to invalid subreddit
        return None

    top_posts = response.json().get('data').get('children')
    after = response.json().get('data').get('after')
    # print("after: {}".format(after))    # test

    if top_posts is not None and len(top_posts) > 0:
        for post in top_posts:
            title = post.get('data').get('title')
            # print("title: {}".format(title))
            hot_list.append(title)

    if after is None:
        # No more posts
        if len(hot_list) > 0:
            return hot_list
        else:
            return 0

    items += len(top_posts)
    return recurse(subreddit, hot_list, after, items)
