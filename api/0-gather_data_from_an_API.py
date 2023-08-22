#!/usr/bin/python3
"""Gather user's todo from API."""
import requests as r
import sys

if __name__ == "__main__":
    # Get user ID from command-line argument
    user_id = int(sys.argv[1])

    # Get user data from API
    user_data = r.get(f'https://jsonplaceholder.typicode.com/users/{user_id}').json()

    # Get list of all todos from API
    todo_list = r.get('https://jsonplaceholder.typicode.com/todos').json()

    # Extract user's name from user data
    user_name = user_data["name"]

    # Calculate total tasks by dividing the length of todo list by 10
    total_tasks = int(len(todo_list) / 10)

    # Initialize counter for completed tasks
    completed_tasks = 0

    # Initialize list to store titles of finished tasks
    finished_tasks = []

    # Iterate through each task in the todo list
    for task in todo_list:
        # Check if task belongs to the user and is completed
        if task["userId"] == user_id and task["completed"]:
            # Add the title of completed task to the finished tasks list
            finished_tasks.append(task["title"])

            # Increment the counter of completed tasks
            completed_tasks += 1

    # Print a summary of the user's progress and list of completed tasks
    print(f"Employee {user_name} is done with tasks({completed_tasks}/{total_tasks}):")
    # Print each completed task title
    [print(f"\t {t}") for t in finished_tasks]
    
    
