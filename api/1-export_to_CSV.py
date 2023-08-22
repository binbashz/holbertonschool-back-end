#!/usr/bin/python3
"""Gather user's todo from API."""
import requests as r
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])  # Get user ID from command-line argument
    user_data = r.get(f'https://jsonplaceholder.typicode.com/users/{user_id}').json() 
    # Get user data from API
    
    todo_list = r.get('https://jsonplaceholder.typicode.com/todos').json()
    # Get list of all todos from API
    
    username = user_data["username"] 
    # Extract username from user data

    with open(f"{user_id}.csv", "w") as file:
        for task in todo_list:
            completed = task['completed']
            title = task['title']
            if task['userId'] == user_id:
                file.write(f'"{user_id}","{username}","{completed}","{title}"\n')
  
