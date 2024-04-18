#!/usr/bin/python3
"""Script using API and module requests"""


import json
import requests


def fetch_and_export_all_tasks():
    """json all user all tasks"""

    # URL to retrieve all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    # Fetch all users
    users_response = requests.get(users_url)
    users = users_response.json()

    all_tasks = {}

    # Iterate through each user and retrieve their tasks
    for user in users:
        user_id = user['id']
        username = user['username']

        # URL for the current user's tasks
        todos_url = f"https://jsonplaceholder.typicode.com/\
todos?userId={user_id}"
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        # Store the tasks in the required format
        all_tasks[user_id] = [
            {"username": username, "task": todo['title'],
             "completed": todo['completed']}
            for todo in todos
        ]

    # Write the data into a JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks, f)


if __name__ == "__main__":
    fetch_and_export_all_tasks()
