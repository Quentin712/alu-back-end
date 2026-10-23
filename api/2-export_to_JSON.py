#!/usr/bin/python3
"""Saves the TODO list of an employee to a JSON file using a REST API."""
import collections
import json
import requests
import sys


def export_to_json(employee_id):
    """Writes every task of the employee into a file named USER_ID.json."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos".format(base_url)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url, params={"userId": employee_id}).json()

    username = user.get("username")

    tasks = []
    for task in todos:
        tasks.append(collections.OrderedDict([
            ("task", task.get("title")),
            ("completed", task.get("completed")),
            ("username", username)]))

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({str(employee_id): tasks}, json_file)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_json(int(sys.argv[1]))
