#!/usr/bin/python3
"""ejercicio 3"""
import json
import requests


def export_json_2():
    """Export to JSON"""
    t = "https://jsonplaceholder.typicode.com/todos/"
    users = "https://jsonplaceholder.typicode.com/users/"
    response_todos = requests.get(t)
    response_users = requests.get(users)
    dic_t = response_todos.json()
    dic_u = response_users.json()

    dict_ = {}

    for count in dic_t:
        list_j = []
        dictionary = {'username': '', 'task': '', 'completed': None}
        title_ = count.get('title')
        completed_ = count.get('completed')
        username_ = count.get('username')
        dictionary.update(task=title_, completed=completed_)
        list_j.append(dictionary)
        x = count.get('id')
        dict_.update({x: list_j})

    with open("todo_all_employees.json", mode='w') as f:
        json.dump(dict_, f)


if __name__ == "__main__":
    export_json_2()
