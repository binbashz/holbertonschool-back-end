#!/usr/bin/python3
""" getting todo list of users from  api  """

import json
import requests


if __name__ == "__main__":
    """ getting todo list of users from an api  """
    res_User = requests.get('https://jsonplaceholder.typicode.com/users')
    is_response = res_User.json()
    resTask = requests.get('https://jsonplaceholder.typicode.com/todos')
    response_Task = resTask.json()

    json_file = "todo_all_employees.json"
    tasklist = []
    a_user = []
    all_users = []
    new_dict = {}
    for user in is_response:
        USER_ID = int(user["id"])
        tasklist = []
        for task in response_Task:
            if int(task["userId"]) == USER_ID:
                TASK_TITLE = task['title']
                TASK_COMPLETED_STATUS = task["completed"]
                USERNAME = user["username"]

                tasklist.append({
                    "username": USERNAME,
                    "task": TASK_TITLE,
                    "completed": TASK_COMPLETED_STATUS
                })
        new_dict[USER_ID] = tasklist
        with open(json_file, "w") as jfile:
            json.dump(new_dict, jfile)
