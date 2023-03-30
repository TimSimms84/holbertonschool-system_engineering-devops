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


def get_todo():
    import requests
    from sys import argv
    id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(id)).json()

    toDo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(id)).json()

    completedTask = []

    for task in toDo:
        if task.get("completed") is True:
            completedTask.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(completedTask), len(toDo)))
    for task in completedTask:
        print("\t {}".format(task))


if __name__ == '__main__':
    get_todo()
