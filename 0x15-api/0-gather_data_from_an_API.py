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

    # completed tasks
    done_tasks = 0
    for todo in todos:
        if todo.get('completed') is True:
            done_tasks = done_tasks + 1

    """
    Show information regarding the user in question
    """
    # information
    print("Employee {} is done with tasks({}/{}):".format(
          user.get('name'), done_tasks, len(todos)))
    for todo in todos:
        if todo.get('completed') is True:
            print("\t {}".format(todo.get('title')))
