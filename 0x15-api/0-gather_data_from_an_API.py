#!/usr/bin/python3
'''
get the data and print
'''

import requests
from sys import argv


if __name__ == '__main__':
    
    emp_id = argv[1]
    total_todos = 0
    done_todos = 0
    done_todos_titles = []

    res = requests.get(
                   'https://jsonplaceholder.typicode.com/users/' +
                   emp_id)
    emp_name = res.json().get('name', 'user name not found')

    res = requests.get(
                   'https://jsonplaceholder.typicode.com/users/' +
                   emp_id + '/todos')
    emp_todos = res.json()

    for todo in emp_todos:
        total_todos += 1
        if todo.get('completed') is True:
            done_todos += 1
            done_todos_titles.append(todo.get(
                                          'title',
                                          'no title found'
                                          ))

    print('Employee {} is done with tasks({}/{}):'.format(
                                                   EMPLOYEE_NAME,
                                                   NUMBER_OF_DONE_TASKS,
                                                   TOTAL_NUMBER_OF_TASKS
                                                   ))

    for title in done_todos_titles:
        print('\t ' + title)
