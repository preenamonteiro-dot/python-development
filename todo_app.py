import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    task_name = input("Enter task name: ")
    tasks = load_tasks()

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index}. {task['task']} - {status}")

def delete_task():
    tasks = load_tasks()
    view_tasks()

    try:
        task_no = int(input("Enter task number to delete: "))

        if task_no < 1 or task_no > len(tasks):
            print("Error: Task does not exist.")
        else:
            removed_task = tasks.pop(task_no - 1)
            save_tasks(tasks)
            print(f"Deleted task: {removed_task['task']}")

    except ValueError:
        print("Error: Please enter a valid number.")

def mark_completed():
    tasks = load_tasks()
    view_tasks()

    try:
        task_no = int(input("Enter task number to mark as completed: "))

        if task_no < 1 or task_no > len(tasks):
            print("Error: Task does not exist.")
        else:
            tasks[task_no - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")

    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    while True:
        print("\n===== TO-DO LIST APPLICATION =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Thank you for using To-Do List App!")
            break
        else:
            print("Invalid choice. Please try again.")

main()