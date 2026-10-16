import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

def create_task(tasks, name):
    return {
        "id": get_next_id(tasks),
        "task": name,
        "completed": False
    }

def add_task(tasks):
    name = input("Enter task: ").strip()

    if name == "":
        print("Task cannot be empty!")
        print()
        return

    task = create_task(tasks, name)
    tasks.append(task)

    print("Task added!")
    print()

def view_tasks(tasks):
    if not tasks:
        print("No tasks found")
        print()
        return
    
    for task in tasks:
        if task["completed"]:
            status = "✓"
        else:
            status = "✕"

        print(f"[{task['id']}] - {task['task']} - [{status}]")
    print()

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        print()
        return
    
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
    except ValueError:
        print("Invalid input. Please enter a number.")
        print()
        return

    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            tasks.pop(i)
            print("Task deleted!")
            print()
            return
    print("Task ID not found.")
    print()

def complete_task(tasks):
    if not tasks:
        print("No tasks to complete")
        print()
        return
    
    view_tasks(tasks)

    try:
        task_id = int(input("Enter task ID to mark completed: ").strip())
    except ValueError:
        print("Invalid input!")
        print()
        return

    for task in tasks:
        if task_id == task['id']:
            if task["completed"]:
                print("Task is already completed")
                print()
                return

            task["completed"] = True
            print("Task marked complete")
            print()
            return

    print("Task ID not found")
    print()
            

def edit_task(tasks):
    if not tasks:
        print("No tasks to edit")
        print()
        return
    
    view_tasks(tasks)

    try:
        task_id = int(input("Enter the task ID to edit: ").strip())
    except ValueError:
        print("Invalid input!")
        print()
        return
    
    new_name = input("Enter the new task name: ").strip()

    if new_name == "":
        print("New task name cannot be blank!")
        print()
        return

    for task in tasks:
        if task_id == task['id']:
            task["task"] = new_name
            print("Task updated!")
            print()
            return
    
    print("Task ID not found")
    print()

def search_tasks(tasks):

    if not tasks:
        print("No tasks available to search.")
        return
    
    found = False
    search = input("Enter the task to search: ").strip().lower()
    if search == "":
        print("Search cannot be empty!")
        return

    for task in tasks:
        if search in task["task"].strip().lower():
            status = "✓" if task["completed"] else "✕"
            print(f"[{task['id']}] - {task['task']} - [{status}]")
            found = True
    if not found:
        print("No matching tasks found!")

def filter_tasks(tasks):
    print("\n---Filter tasks---")
    print("1. Show all tasks")
    print("2. Show completed tasks")
    print("3. Show incomplete tasks")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        view_tasks(tasks)
    elif choice == "2":
        completed_tasks = [task for task in tasks if task["completed"]]
        view_tasks(completed_tasks)
    elif choice == "3":
        incomplete_tasks = [task for task in tasks if not task["completed"]]
        view_tasks(incomplete_tasks)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")


def show_menu():
    print("\n---Task Manager---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Edit task")
    print("5. Mark task as completed")
    print("6. Search task")
    print("7. Filter task")
    print("8. Exit")
    print()

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
            save_tasks(tasks)

        elif choice == "2":
            view_tasks(tasks)
        
        elif choice == "3":
            delete_task(tasks)
            save_tasks(tasks)
            
        elif choice == "4":
            edit_task(tasks)
            save_tasks(tasks)
        
        elif choice == "5":
            complete_task(tasks)
            save_tasks(tasks)
        
        elif choice == "6":
            search_tasks(tasks)

        elif choice == "7":
            filter_tasks(tasks)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
            print()


if __name__ == "__main__":
    main()