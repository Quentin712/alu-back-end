#!/usr/bin/python3
"""Saves the TODO lists of all employees to one JSON file using a REST API."""
import collections
import json
import requests


def export_all_to_json():
    """Writes the tasks of every employee into todo_all_employees.json."""
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    all_tasks = collections.OrderedDict()
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        key = str(user_id)
        all_tasks[key] = []
        for task in todos:
            if task.get("userId") == user_id:
                all_tasks[key].append(collections.OrderedDict([
                    ("username", username),
                    ("task", task.get("title")),
                    ("completed", task.get("completed"))]))

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_to_json()
