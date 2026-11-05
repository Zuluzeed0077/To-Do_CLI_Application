import json
import os
from datetime import datetime
from clear_terminals import clear_terminal

FILENAME = "tasks.json"

# file handling and data helpers
def load_tasks():
    """Reads tasks from tasks.json file. Returns empty list if file doesn't exist."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_tasks(tasks):
    """Saves the current list of tasks to tasks.json."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def get_next_id(tasks):
    """Finds the highest existing ID and adds 1."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

#  core task management functions
def add_task(tasks):
    """Adds a new task to the list."""
    print("\n--- ADD NEW TASK ---")
    
    # 1. Title Input Validation
    title = input("Enter task title: ").strip()
    while not title:
        print("Title cannot be empty!")
        title = input("Enter task title: ").strip()

    # 2. Priority Input Validation
    print("Select Priority: 1) Low  2) Medium  3) High")
    while True:
        p_choice = input("Choice (1-3): ").strip()
        if p_choice in ["1", "2", "3"]:
            break
        print("Invalid choice. Please select 1, 2, or 3.")

    # 3. Due Date Validation
    while True:
        due_date = input("Enter due date (YYYY-MM-DD): ").strip()
        if not due_date:
            print("invalid date format! enter a valid date in YYYY-MM-DD format.")
            continue
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format! Please enter a valid date in YYYY-MM-DD format.")

    new_task = {
        "id": get_next_id(tasks),
        "title": title,
        "priority": "Low" if p_choice == "1" else "Medium" if p_choice == "2" else "High",
        "due_date": due_date,
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")

def view_tasks(tasks, show_completed=False):
    """Displays tasks filtered by completion status."""
    status_text = "COMPLETED" if show_completed else "PENDING"
    filtered = [t for t in tasks if t["completed"] == show_completed]

    print(f"\n--- {status_text} TASKS ({len(filtered)}) ---")
    if not filtered:
        print("No tasks found.")
        return

    print(f"{'ID':<4} | {'Title':<20} | {'Priority':<8} | {'Due Date':<12}")
    print("-" * 50)
    for t in filtered:
        print(f"{t['id']:<4} | {t['title']:<20} | {t['priority']:<8} | {t['due_date']:<12}")

def mark_completed(tasks):
    """Marks a selected task as done."""
    view_tasks(tasks, show_completed=False)
    try:
        task_id = int(input("\nEnter Task ID to mark completed: "))
        for t in tasks:
            if t["id"] == task_id:
                t["completed"] = True
                save_tasks(tasks)
                print(f"Task #{task_id} marked as completed!")
                return
        print("Task ID not found.")
    except ValueError:
        print("Please enter a valid number.")

def edit_task(tasks):
    """Edits title, priority, or due date of an existing task."""
    if not tasks:
        print("No tasks available to edit.")
        return
    
    print(f"{'ID':<4} | {'Title':<20} | {'Priority':<8} | {'Due Date':<12}")
    print("-" * 50)
    for t in tasks:
        print(f"{t['id']:<4} | {t['title']:<20} | {t['priority']:<8} | {t['due_date']:<12}")
    try:
        task_id = int(input("\nEnter Task ID to edit: "))
        task = next((t for t in tasks if t["id"] == task_id), None)
        
        if not task:
            print("Task ID not found.")
            return

        print(f"\nEditing Task #{task['id']}: {task['title']}")
        
        new_title = input(f"New Title (press Enter to keep '{task['title']}'): ").strip()
        if new_title:
            task["title"] = new_title
        while True:
            new_p = input(f"New Priority Low/Medium/High (press Enter to keep '{task['priority']}'): ").strip().capitalize()
            if new_p in ["Low", "Medium", "High"]:
                task["priority"] = new_p
            elif new_p == "":
                break
            else:
                print("Invalid priority. Please enter Low, Medium, or High.")
                continue
            break
        while True:
            new_d = input(f"New Due Date YYYY-MM-DD (press Enter to keep '{task['due_date']}'): ").strip()
            if new_d == "":
                break

            try:
                task["due_date"] = datetime.strptime(new_d, "%Y-%m-%d").strftime("%Y-%m-%d")
                break
            except ValueError:
                    print("Invalid date format. Please enter a valid date in YYYY-MM-DD format.")

        save_tasks(tasks)
        print("Task updated successfully!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Removes a task by ID."""
    if not tasks:
        print("No tasks available to delete.")
        return
    
    print(f"{'ID':<4} | {'Title':<20} | {'Priority':<8} | {'Due Date':<12}")
    print("-" * 50)
    for t in tasks:
        print(f"{t['id']:<4} | {t['title']:<20} | {t['priority']:<8} | {t['due_date']:<12}")
    try:
        task_id = int(input("\nEnter Task ID to delete: "))
        for i, t in enumerate(tasks):
            if t["id"] == task_id:
                del tasks[i]
                save_tasks(tasks)
                print(f"Task #{task_id} deleted successfully.")
                return
        print("Task ID not found.")
    except ValueError:
        print("Please enter a valid number.")

#  main application loop (the menu)
def main():
    clear_terminal()
    tasks = load_tasks()

    while True:
        print("\n==========================")
        print("     TASK MANAGER MENU    ")
        print("==========================")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. View Pending Tasks    ")
        print("4. Mark Task as Completed")
        print("5. View Completed Tasks")
        print("6. Delete Task")
        print("7. Exit")

        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            edit_task(tasks)
        elif choice == "3":
            view_tasks(tasks, show_completed=False)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            view_tasks(tasks, show_completed=True)
        elif choice == "6":
            delete_task(tasks)
        elif choice == "7":
            print("Goodbye! Your tasks are saved in tasks.json.")
            break
        else:
            print("Invalid option! Please pick a number from 1 to 7.")

if __name__ == "__main__":
    main()