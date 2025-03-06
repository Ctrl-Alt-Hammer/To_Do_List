import json

file_name = "todo_list.json"


def load_task():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks,file)
    except:
        print ("Failed to save.")

def create_task(tasks):
    description = input("Enter task description: ").strip()
    if description:
       tasks["tasks"].append({"description": description, "completed": False})
       save_tasks(tasks)
       print("Task added successfully.")
    else:
        print("Task description cannot be empty.")

def view_tasks(tasks):
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List: ")
        for idx, task in enumerate(task_list):
            status = "Complete" if task["completed"] else "Incomplete"
            print(f"{idx + 1}. {task['description']} | {status}")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks["tasks"][task_number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")

def main():
   tasks = load_task()


   while True:
       print("\n To-Do List Manager")
       print("1. View Tasks")
       print("2. Add Task")
       print("3. Mark Task Complete")
       print("4. Exit")

       choice = input("Enter choice: ").strip()

       if choice == "1":
            view_tasks(tasks)
       elif choice == "2":
            create_task(tasks)
       elif choice == "3":
            mark_task_complete(tasks)
       elif choice == "4":
            save_tasks("GoodBye!")
            break
       else:
            print("Invalid choice. Please try again.")

main()