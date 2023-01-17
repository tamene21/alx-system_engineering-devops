#!/usr/bin/python3
"""Export to json info of https://jsonplaceholder.typicode.com"""

import csv
import json
import requests
import sys

if __name__ == "__main__":
    dict_user = {}
    array_users = []
    array_tasks = []

    page_user = "https://jsonplaceholder.typicode.com/users/"

    req_user = requests.get(page_user)

    page = ("https://jsonplaceholder.typicode.com/todos/")
    req = requests.get(page)
    for user in req_user.json():
        if user.get('id') not in array_users:
            values = []
            values.append(str(user.get('id')))
            values.append(str(user.get('username')))
            array_users.append(values)

    for user in array_users:
        page = (("https://jsonplaceholder.typicode.com/todos?\
userId={}".format(int(user[0]))))
        req = requests.get(page)
        for task in req.json():
            dict_task = {}
            dict_task['username'] = user[1]
            dict_task['task'] = task.get('title')
            dict_task['completed'] = task.get('completed')
            array_tasks.append(dict_task)
        dict_user[user[0]] = array_tasks
        array_tasks = []
    json_object = json.dumps(dict_user)

    with open("todo_all_employees.json", "w") as outfile:
        outfile.write(json_object)
