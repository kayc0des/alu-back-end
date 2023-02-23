#!/usr/bin/python3

import json
import request

def get_employee_task(employee_id):

    url = "https://jsonplaceholder.typicode.com/users/{}"\
        .format(employee_id)
    
    user_info = requests.request('GET', url).json()

    employee_username = user_info["username"]
    todo = "https://jsonplaceholder.typicode.com/users/
