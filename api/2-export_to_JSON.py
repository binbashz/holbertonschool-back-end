#!/usr/bin/python3
"""Gather user's todo from API."""
import json
import requests as r
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])  # Get user ID from command-line argument
    user_data = r.get(f'https://jsonplaceholder.typicode.com/users/{user_id}').json() 
    # Get user data from API
    todo_list = r.get('https://jsonplaceholder.typicode.com/todos').json() 
    # Get list of all todos from API
    user_tasks = []

    with open(f"{user_id}.json", "w") as file:
        for task in todo_list:
            if task["userId"] == user_id:
                user_tasks.append({
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user_data["username"]
                })

        json.dump({str(user_id): user_tasks}, file)
