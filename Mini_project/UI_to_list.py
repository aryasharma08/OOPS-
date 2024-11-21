import json
import streamlit as st # type: ignore

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


# Streamlit UI
st.title("📝 To-Do List App")

# Load tasks
tasks = load_tasks()


# Function to display tasks in a dropdown or list
def display_tasks():
    if not tasks:
        st.write("No tasks available!")
        return None
    else:
        options = [
            f"{i + 1}. {'✓' if task['completed'] else '✗'} {task['task']}"
            for i, task in enumerate(tasks)
        ]
        return st.selectbox("Select a task:", options,
                            index=0) if options else None


# Tabs for the to-do list
tabs = st.tabs(
    ["View Tasks", "Add Task", "Update Task", "Delete Task", "Mark Completed"])

# View tasks
with tabs[0]:
    st.subheader("📋 Tasks")
    if not tasks:
        st.write("No tasks to display!")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            st.write(f"{i}. [{status}] {task['task']}")

# Add a new task
with tabs[1]:
    st.subheader("➕ Add Task")
    new_task = st.text_input("Enter the task:")
    if st.button("Add Task"):
        if new_task.strip():
            tasks.append({"task": new_task, "completed": False})
            save_tasks(tasks)
            st.success("Task added successfully!")
            st.experimental_rerun()
        else:
            st.error("Task cannot be empty!")

# Update a task
with tabs[2]:
    st.subheader("✏️ Update Task")
    selected_task = display_tasks()
    if selected_task:
        task_index = int(selected_task.split(".")[0]) - 1
        updated_task = st.text_input("Enter the updated task:",
                                     value=tasks[task_index]["task"])
        if st.button("Update Task"):
            tasks[task_index]["task"] = updated_task
            save_tasks(tasks)
            st.success("Task updated successfully!")
            st.experimental_rerun()

# Delete a task
with tabs[3]:
    st.subheader("❌ Delete Task")
    selected_task = display_tasks()
    if selected_task:
        task_index = int(selected_task.split(".")[0]) - 1
        if st.button("Delete Task"):
            tasks.pop(task_index)
            save_tasks(tasks)
            st.success("Task deleted successfully!")
            st.experimental_rerun()

# Mark task as completed
with tabs[4]:
    st.subheader("✅ Mark Task as Completed")
    selected_task = display_tasks()
    if selected_task:
        task_index = int(selected_task.split(".")[0]) - 1
        if not tasks[task_index]["completed"] and st.button(
                "Mark as Completed"):
            tasks[task_index]["completed"] = True
            save_tasks(tasks)
            st.success("Task marked as completed!")
            st.experimental_rerun()
