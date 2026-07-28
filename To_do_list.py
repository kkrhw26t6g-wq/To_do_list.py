def add_task(tasks):
    """Prompts the user for a task and adds it to the list."""
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print(f'Task added: "{task}"')
    else:
        print("Error: Task description cannot be empty.")


def view_tasks(tasks):
    """Displays all current tasks with 1-based numbering."""
    if not tasks:
        print("Your tasks list is empty.")
    else:
        print("Your Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def delete_task(tasks):
    """Deletes a task by its 1-based task number."""
    if not tasks:
        print("Your tasks list is empty. Nothing to delete.")
        return

    try:
        task_num = int(input("Enter task number to delete: "))
        # Check if index is within valid range (1 to len(tasks))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print("Error: Invalid task number.")
    except ValueError:
        print("Error: Please enter a valid number.")


def display_menu():
    """Prints the main menu options."""
    print("\n==================")
    print("  TO-DO LIST MENU  ")
    print("==================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
