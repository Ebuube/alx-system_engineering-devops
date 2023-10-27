#!/usr/bin/python3
"""
Create record of all tasks from all employees
"""
from requests import get
from sys import argv
import json


if __name__ == "__main__":

    api = 'https://jsonplaceholder.typicode.com'
    delim = '/'

    # user
    url = api + delim + 'users'
    users = get(url).json()

    # todos for this user
    url = api + delim + 'todos'
    todos = get(url).json()

    # Create data
    user_data = {}
    for user in users:
        details = []
        for todo in todos:
            task = {}
            task['task'] = todo.get('title')
            task['completed'] = todo.get('completed')
            task['username'] = user.get('username')
            details.append(task)
        user_data[user.get('id')] = details

    """
    Write information to a file
    """
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as user_file:
        json.dump(user_data, user_file)
