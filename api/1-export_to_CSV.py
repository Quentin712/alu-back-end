#!/usr/bin/python3
"""Saves the TODO list of an employee to a CSV file using a REST API."""
import csv
import requests
import sys


def export_to_csv(employee_id):
    """Writes every task of the employee into a file named USER_ID.csv."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos".format(base_url)

    user = requests.get(user_url).json()
    todos = requests.get(todos_url, params={"userId": employee_id}).json()

    username = user.get("username")

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(
            csv_file, quoting=csv.QUOTE_ALL, lineterminator="\n")
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        export_to_csv(int(sys.argv[1]))
