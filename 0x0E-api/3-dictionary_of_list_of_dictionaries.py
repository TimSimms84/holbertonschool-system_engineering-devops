#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
 information about his/her TO DO list progress.
 must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
The script must display on the standard output the
employee TO DO list progress in this exact format:
First line: Employee EMPLOYEE_NAME is done
with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of
completed and non-completed tasks
Second and N next lines display the title of completed
tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""


def get_json():
    import csv
    import json
    import requests
    from sys import argv
    id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id)).json()
    toDo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id)).json()
    user = requests.get("https://jsonplaceholder.typicode.com/users").json()
    toDo = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    """
    prints to screen how many task the employee has done and what task
    """
    completedTask = []
    for task in toDo:
        if task.get("completed") is True:
            completedTask.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completedTask), len(toDo)))
    for task in completedTask:
        print("\t {}".format(task))

    """
    exports completed task to a csv file
    """
    with open("{}.csv".format(id), "w", newline="") as csvFile:
        writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for task in toDo:
            writer.writerow([int(id), user.get("username"),
                            task.get("completed"), task.get("title")])
    """exports all task as json"""
    jsonTask = []
    for task in toDo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = user.get("username")
        jsonTask.append(task_dict)
    json_dict = {}
    json_dict[id] = jsonTask
    with open("{}.json".format(id), "w") as file:
        json.dump(json_dict, file)


def save_all():
    """
    Records all tasks from all employees in JSON
    """
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    toDo = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    diction = {}
    usernames = {}
    for user in users:
        uid = user.get("id")
        diction[uid] = []
        usernames[uid] = user.get("username")
    for task in toDo:
        taskd = {}
        uid = task.get("userId")
        taskd["username"] = usernames.get(uid)
        taskd["task"] = task.get("title")
        taskd["completed"] = task.get("completed")
        diction.get(uid).append(taskd)

    with open("todo_all_employees.json", "w") as file:
        json.dump(diction, file)


if __name__ == '__main__':
    import csv
    import json
    import requests
    from sys import argv
    try:
        get_json()
    except Exception:
        save_all()
