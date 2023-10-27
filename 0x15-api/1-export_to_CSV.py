#!/usr/bin/python3
"""
Fetch and display an employee detail by employee id
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <emp_id>".format(argv[0]))
        exit(1)

    emp_id = argv[1]
    api = 'https://jsonplaceholder.typicode.com'
    delim = '/'

    # user
    url = api + delim + 'users' + delim + str(emp_id)
    user = get(url).json()

    # todos for this user
    url = api + delim + 'users' + delim + emp_id + delim + 'todos'
    todos = get(url).json()

    """
    Write information to a file
    """
    filename = str(user.get('id')) + '.csv'
    with open(filename, 'w') as f:
        for todo in todos:
            msg = '"{}","{}","{}","{}"\n'.format(
                    user.get('id'), user.get('username'),
                    todo.get('completed'), todo.get('title'))
            f.write(msg)
