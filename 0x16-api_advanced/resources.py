#!/usr/bin/python3
"""
This module contains function to get some information concerning subereddits
"""
import requests
count = 0


def dict_structure(dic=dict(), level=0, delim='\t'):
    """
    Print the structure of a dictionary
    """
    if (type(dic) != dict or type(level) != int) or type(delim) != str:
        print("Invalid type `dic`: {}".format(type(dic)))
        print("Invalid type `level`: {}".format(type(level)))
        print("Invalid type `delim`: {}".format(type(delim)))
        return

    for key, val in dic.items():
        tab = delim * level
        if 
        if type(val) == dict:
            dict_structure(val, level + 1)
        elif type(val) == list:
            list_structure(val, level + 1)
        elif type(val) == str:
            print("{}{}".format(tab, val[:20]))
        else:
            print("{}{}".format(tab, type(val)))


def list_structure(data=list(), level=0, delim='\t'):
    """
    Print the structure of a list
    """
    if (type(data) != list or type(level) != int) or type(delim) != str:
        print("Invalid type `data`: {}".format(type(data)))
        print("Invalid type `level`: {}".format(type(level)))
        print("Invalid type `delim`: {}".format(type(delim)))
        return

    for mem in data:
        tab = delim * level
        if type(mem) == list:
            list_structure(mem, level + 1)
        elif type(mem) == dict:
            dict_structure(mem)
        elif type(mem) == str:
            print("{}{}".format(tab, mem[:20]))
        else:
            print("{}{}".format(tab, type(mem)))


def recurse(subreddit, hot_list=[]):
    """
    Return a list containing the titles of all hot articles
    for a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    global after

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

    if len(hot_list) > 0:
        params['after'] = after
        print("Setting param[after] = {}".format(params.get('after')))

    print('number of posts: {}'.format(len(hot_list)))  # test

    response = requests.get(url, headers=headers,
                            allow_redirects=False, params=params)

    if response.status_code == 200:
        top_posts = response.json().get('data').get('children')

        print("Data structure")
        my_dict = {'it1': 'hello',
                    'it2': 'me',
                    'it3': {
                        'it3_it1': 'swap',
                        'it3_it2': 'val',
                        'it3_it3': 'dance',
                        },
                    'it4': 15,
                    'it5': 841}
        # dict_structure(my_dict)
        print("posts are {} in number".format(len(top_posts)))
        # list_structure(top_posts)
        dict_structure(top_posts[0])
    '''
        after = response.json().get('data').get('name')
        print("Count: {}".format(count))
        print("After: {}".format(after))
        if top_posts is not None:
            hot_list.append(top_posts)
        else:
            with open(filname, 'w') as fp:
                import json
                json.dump(hot_list, fp)
    else:
        print(None)

    return (recurse(subreddit, hot_list))
    '''
