import os

TASK_FILE = "tasks.txt"


# ----------------------------
# Load tasks from file
# ----------------------------
def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    return tasks


# ----------------------------
# Save tasks to file
# ----------------------------
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# ----------------------------
# Add a new task
# ----------------------------
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


# ----------------------------
# View all tasks
# ----------------------------
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print("------------------\n")


# ----------------------------
# Remove a task
# ----------------------------
def remove_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        index = int(input("Enter task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")


# ----------------------------
# Main Menu Loop
# ----------------------------
def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
