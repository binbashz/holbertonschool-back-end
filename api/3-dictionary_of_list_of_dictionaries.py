#!/usr/bin/python3
"""Gather user's todo from API."""
import json
import requests as r

if __name__ == "__main__":
    user_data = r.get(f'https://jsonplaceholder.typicode.com/users').json()
    # Get user data from API
    todo_list = r.get('https://jsonplaceholder.typicode.com/todos').json() 
    # Get list of all todos from API
    user_tasks = []
    user_dict = {}  # Initialize a dictionary to store user tasks

    with open("todo_all_employees.json", "w") as file:
        for u in user_data:
            user_id = int(u["id"])
            user_tasks = []  # Reset the user_tasks list for each user
            for t in todo_list:
                if t["userId"] == user_id:
                    user_tasks.append({
                        "task": t["title"],
                        "completed": t["completed"],
                        "username": u["username"]
                    })
            user_dict[str(user_id)] = user_tasks 
            # Store user tasks in the dictionary

        json.dump(user_dict, file)  
        # Write the user tasks dictionary to the JSON file
