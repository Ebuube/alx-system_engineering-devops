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

    '''
    # Create data
    user_data = {}
    user_data[emp_id] = []
    for todo in todos:
        if todo.get('completed') is True:
            status = 'true'
        else:
            status = 'false'
            task = {"task": todo.get('title'), "completed": status,
                    "username": user.get('username')}
            user_data[emp_id].append()
    '''

    """
    Write information to a file
    """
    file_fmt = ".json"
    filename = emp_id + file_fmt
    with open(filename, 'w') as f:
        f.write('{{"{}": ['.format(emp_id))  # opening
        for todo in todos:
            if todo.get('completed') is True:
                status = 'true'
            else:
                status = 'false'
            msg = '{{"task": "{}", "completed": {}, "username": {}}}'.format(
                    todo.get('title'), status, user.get('username'))
            f.write(msg)
            if todo != todos[-1]:
                f.write(", ")
        f.write("]}")
