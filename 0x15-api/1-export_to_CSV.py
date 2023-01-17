#!/usr/bin/python3
"""Export to CSV info of https://jsonplaceholder.typicode.com"""

import csv
import requests
import sys

if __name__ == "__main__":
    employee_username = ''

    page_user = "https://jsonplaceholder.typicode.com/users/{}".format(
        sys.argv[1])

    req_user = requests.get(page_user)
    employee_username = req_user.json()['username']

    page = ("https://jsonplaceholder.typicode.com/todos?userId={}".format
            (sys.argv[1]))
    req = requests.get(page)

    with open("{}.csv".format(sys.argv[1]), mode='w') as employee_file:
        employee_writer = csv.writer(
            employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

        for task in req.json():
            id = task.get('userId')
            status = task.get('completed')
            title = task.get('title')
            employee_writer.writerow([id, employee_username,
                                      status, title])
