#!/usr/bin/python3

"""Export to JSON"""
import json
from sys import argv
import requests

if __name__ == '__main__':
    employee_id = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos" \
        .format(employee_id)

    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    user_name = user_response.get('username')

    todos_information = [
        dict(zip(["task", "completed", "username"],
                 [task["title"], task["completed"], user_name]))
        for task in todos_response]

    user_dict = {str(employee_id): todos_information}
    with open(str(employee_id) + '.json', "w") as file:
        file.write(json.dumps(user_dict))
