import json
from datetime import datetime

available_commands = ["add", "list-all", "list-todo", "list-in-progress", "list-done", "update", "delete", "mark-in-progress", "mark-done", "exit"]

def add_task(inp, id):
    actual_input = inp[4:]
    task_id = id
    status = "todo"
    created_at = datetime.now()
    updated_at = datetime.now()
    with open("data.json", 'r+') as file:
        try:
            temp = json.load(file)  # Load JSON data
        except json.JSONDecodeError:
            # If file is empty or corrupted, initialize with empty structure
            temp = []
    
    # id - 0, desc - 1, status - 2, created at - 3, updated at - 4
    temp.append({"id":task_id, "description" : actual_input, "status": status, "created-at": created_at, "updated-at": updated_at})
    with open("data.json", 'w') as file:
        json.dump(temp, file, indent=4, default=str)  # Write the updated JSON back to the file
    
    print(f"Task added successfully! (ID: {task_id})\n")

def listAllTasks():
    with open("data.json", 'r') as file:
        try:
            temp = json.load(file)  # Load JSON data
        except json.JSONDecodeError:
            # If file is empty or corrupted, initialize with empty structure
            print("No tasks found!\n")
            return
        for task in temp:
            print(f"Task ID {task["id"]}")
            print(f"Name of the task {task["description"]}")
            print(f"Current status {task["status"]}")
            print(f"Created At {task["created-at"]}")
            print(f"Updated At {task["updated-at"]}\n")

def listTodo():
    with open("data.json", 'r') as file:
        try:
            temp = json.load(file)  # Load JSON data
        except json.JSONDecodeError:
            # If file is empty or corrupted, initialize with empty structure
            print("No tasks found!")
            return
        for task in temp:
            if task["status"] == "todo":
                print(f"Task ID {task["id"]}")
                print(f"Name of the task {task["description"]}")
                print(f"Current status {task["status"]}")
                print(f"Created At {task["created-at"]}")
                print(f"Updated At {task["updated-at"]}\n")

def listIP():
    with open("data.json", 'r') as file:
        try:
            temp = json.load(file)  # Load JSON data
        except json.JSONDecodeError:
            # If file is empty or corrupted, initialize with empty structure
            print("No tasks found!")
            return
        for task in temp:
            if task["status"] == "in-progress":
                print(f"Task ID {task["id"]}")
                print(f"Name of the task {task["description"]}")
                print(f"Current status {task["status"]}")
                print(f"Created At {task["created-at"]}")
                print(f"Updated At {task["updated-at"]}\n")

def listDone():
    with open("data.json", 'r') as file:
        try:
            temp = json.load(file)  # Load JSON data
        except json.JSONDecodeError:
            # If file is empty or corrupted, initialize with empty structure
            print("No tasks found!")
            return
        for task in temp:
            if task["status"] == "done":
                print(f"Task ID {task["id"]}")
                print(f"Name of the task {task["description"]}")
                print(f"Current status {task["status"]}")
                print(f"Created At {task["created-at"]}")
                print(f"Updated At {task["updated-at"]}\n")

task_found = False
def delete_tasks(inp):
    id = inp.split(' ')[1]
    with open("data.json", 'r') as file:
        try:
            temp = json.load(file)  # Load JSON data
        except json.JSONDecodeError:
            # If file is empty or corrupted, initialize with empty structure
            print("No tasks found!\n")
            return
    
        for pos, task in enumerate(temp):
            if task["id"] == int(id):
                deleted_task = temp.pop(pos)
                print(f"Task: {deleted_task["description"]} has been successfully deleted\n")
                task_found = True
                break
        if not task_found:
            print(f"Task with ID {id} not found!\n")
            return
    with open("data.json", 'w') as file:
        json.dump(temp, file, indent=4, default=str)  # Write the updated JSON back to the file
        
    print(f"Task updated successfully! (ID: {id})\n")

def update_tasks(inp):
    actual_input = inp[9:]
    id = inp.split(' ')[1]
    with open("data.json", 'r') as file:
        try:
            temp = json.load(file)  # Load JSON data
        except json.JSONDecodeError:
            # If file is empty or corrupted, initialize with empty structure
            print("No tasks found!\n")
            return
    
        for task in temp:
            if task["id"] == int(id):
                task["description"] = actual_input
                task["updated-at"] = datetime.now()
    with open("data.json", 'w') as file:
        json.dump(temp, file, indent=4, default=str)  # Write the updated JSON back to the file
        
    print(f"Task updated successfully! (ID: {id})\n")

def markInProgress(inp):
    strid = inp.split(' ')[1]
    intid = int(strid)
    with open("data.json", 'r') as file:
        try:
            temp = json.load(file)  # Load JSON data
        except json.JSONDecodeError:
            # If file is empty or corrupted, initialize with empty structure
            print("No tasks found!\n")
            return
    
        for task in temp:
            if task["id"] == intid:
                task["status"] = "in-progress"
                task["updated-at"] = datetime.now()
    with open("data.json", 'w') as file:
        json.dump(temp, file, indent=4, default=str)  # Write the updated JSON back to the file

    print(f'Task with id {intid} has been updated to in-progress\n')


def markDone(inp):
        strid = inp.split(' ')[1]
        intid = int(strid)
        with open("data.json", 'r') as file:
            try:
                temp = json.load(file)  # Load JSON data
            except json.JSONDecodeError:
                # If file is empty or corrupted, initialize with empty structure
                print("No tasks found!\n")
                return
    
            for task in temp:
                if task["id"] == intid:
                    task["status"] = "done"
                    task["updated-at"] = datetime.now()
        with open("data.json", 'w') as file:
            json.dump(temp, file, indent=4, default=str)  # Write the updated JSON back to the file

        print(f'Task with id {intid} has been updated to done\n')

def main():
    print("Welcome to the todo tasks cli.\n")
    print("Available commands: ")
    for command in available_commands:
        print(command)
    print("")
    empty_data = []
    with open("data.json", 'w') as file:
        json.dump(empty_data, file)
    task_id_counter = 0
    while True:
        user = input("task-cli ")
        action = user.split(' ')[0]
        if action.lower() == 'add':
            task_id_counter += 1
            add_task(user, task_id_counter)
        elif action.lower() == 'list-all':
            listAllTasks()
        elif action.lower() == 'list-todo':
            listTodo()
        elif action.lower() == 'list-in-progress':
            listIP()
        elif action.lower() == 'list-done':
            listDone()
        elif action.lower() == 'update':
            update_tasks(user)
        elif action.lower() == 'delete':
            delete_tasks(user)
        elif action.lower() == 'mark-in-progress':
            markInProgress(user)
        elif action.lower() == "mark-done":
            markDone(user)
        elif action.lower() == 'exit':
            print("Thank you for using the CLI")
            break
        else:
            print("Invalid input, please try again")

if __name__ == "__main__":
    main()