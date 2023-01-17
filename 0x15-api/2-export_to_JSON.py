#!/usr/bin/python3
"""Export to json info of https://jsonplaceholder.typicode.com"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    employee_username = ''

    dict_user = {}
    array_tasks = []

    page_user = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])

    req_user = requests.get(page_user)
    employee_username = req_user.json()['username']

    page = ("https://jsonplaceholder.typicode.com/todos?userId={}".format
            (sys.argv[1]))
    req = requests.get(page)

    for task in req.json():
        dict_task = {}
        dict_task['task'] = task.get('title')
        dict_task['completed'] = task.get('completed')
        dict_task['username'] = employee_username
        array_tasks.append(dict_task)
    dict_user[str(sys.argv[1])] = array_tasks
    json_object = json.dumps(dict_user)

    with open("{}.json".format(sys.argv[1]), "w") as outfile:
        outfile.write(json_object)
