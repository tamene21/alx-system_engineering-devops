#!/usr/bin/python3
"""Returns information about a employee with a given ID"""
import requests
from sys import argv


if __name__ == "__main__":
    employee = ''
    task_complete = 0
    array_task_complete = []
    tasks = 0
    page = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])

    req = requests.get(page)
    employee = req.json()['name']

    page = ("https://jsonplaceholder.typicode.com/todos?userId={}".format
            (argv[1]))
    req = requests.get(page)
    for task in req.json():
        tasks += 1
        if task.get('completed') is True:
            task_complete += 1
            array_task_complete.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".format(employee,
                                                          task_complete,
                                                          tasks))
    for task in array_task_complete:
        print("\t", task)
