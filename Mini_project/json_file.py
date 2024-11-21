#json a file format compatible on diffrent platforms
import json 

# File to store tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from the file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. [{status}] {task['task']}")

# Main menu function
def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
       

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":  # View tasks
            display_tasks(tasks)

        elif choice == "2":  # Add a task
            task_name = input("Enter the task: ")
            tasks.append({"task": task_name, "completed": False})
            save_tasks(tasks)
            print("Task added successfully!")

        elif choice == "3":  # Update a task
            display_tasks(tasks)
            try:
                index = int(input("Enter the task number to update: ")) - 1
                if 0 <= index < len(tasks):
                    new_task = input("Enter the updated task: ")
                    tasks[index]["task"] = new_task
                    save_tasks(tasks)
                    print("Task updated successfully!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "4":  # Delete a task
            display_tasks(tasks)
            try:
                index = int(input("Enter the task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    save_tasks(tasks)
                    print("Task deleted successfully!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "5":  # Mark task as completed
            display_tasks(tasks)
            try:
                index = int(input("Task completed: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index]["completed"] = True
                    save_tasks(tasks)
                    print("Task marked as completed!")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number!")



        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
