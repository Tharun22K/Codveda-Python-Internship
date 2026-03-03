import json

FILENAME = "tasks.json"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)

def view_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        status = "Done" if t["done"] else "Pending"
        print(f"{i+1}. {t['task']} - {status}")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
    else:
        print("Invalid task number")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    else:
        print("Invalid task number")

while True:
    print("\n1.Add 2.View 3.Mark Done 4.Delete 5.Exit")
    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        num = int(input("Task number: ")) - 1
        mark_done(num)
    elif choice == "4":
        num = int(input("Task number: ")) - 1
        delete_task(num)
    elif choice == "5":
        break
    else:
        print("Invalid choice")
