#!/usr/bin/python3
"""
Fetch and export user data in JSON format
"""
from requests import get
from sys import argv
import json


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <emp_id>".format(argv[0]))
        exit(1)

    emp_id = str(argv[1])
    api = 'https://jsonplaceholder.typicode.com'
    delim = '/'

    # user
    url = api + delim + 'users' + delim + str(emp_id)
    user = get(url).json()

    # todos for this user
    url = api + delim + 'users' + delim + emp_id + delim + 'todos'
    todos = get(url).json()

    # Create data
    user_data = {}
    user_data[emp_id] = []
    for todo in todos:
        task = {}
        task['task'] = todo.get('title')
        task['completed'] = todo.get('completed')
        task['username'] = user.get('username')
        user_data[emp_id].append(task)

    """
    Write information to a file
    """
    file_fmt = ".json"
    filename = emp_id + file_fmt
    with open(filename, 'w') as user_file:
        json.dump(user_data, user_file)
