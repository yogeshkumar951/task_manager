import requests
import sys


"""Task CLI Commands

List Tasks:
    python task_cli.py list

Add Task:
    python task_cli.py add "Task title" priority

Delete Task:
    python task_cli.py delete task_id
"""

BASE_URL = "http://127.0.0.1:8000/api/tasks/"


def list_tasks():

    response = requests.get(BASE_URL)
    print('response: ddddddd', response)

    tasks = response.json()

    print("-" * 50)
    print(f"{'ID':<5} {'Title':<30} {'Status':<10}")
    print("-" * 50)

    # Table Rows
    for task in tasks:
        print(f"{task['id']:<5} {task['title']:<30} {task['status']:<10}")

    print("-" * 50)


def create_task(title, priority):

    data = {
        "title": title,
        "priority": priority
    }

    response = requests.post(BASE_URL, json=data)

    print(response.json())


def delete_task(task_id):

    requests.delete(BASE_URL + str(task_id) + "/")

    print("Task deleted")
    
    
def update_task(task_id, title, priority):

    data = {
        "title": title,
        "priority": priority
    }

    response = requests.patch(BASE_URL + str(task_id) + "/", json=data)

    print(response.json())


if __name__ == "__main__":

    command = sys.argv[1]

    if command == "list":
        list_tasks()

    elif command == "create":

        title = sys.argv[2]
        priority = sys.argv[3]

        create_task(title, priority)

    elif command == "delete":

        task_id = sys.argv[2]

        delete_task(task_id)
        
    elif command == "update":

        task_id = sys.argv[2]
        title = sys.argv[3]
        priority = sys.argv[4]

        update_task(task_id, title, priority)
        
    
        
        