# Importing Libraries
import datetime
with open("user.txt", "r") as user_file, open("tasks.txt", "r") as task_file:
    users = user_file.readlines()
    tasks = task_file.readlines()

# Load Users Function
def load_users():
    users = {}
    with open("user.txt", "r") as user_file:
        for line in user_file:
            username, password = line.strip().split(", ")
            users[username] = password
    return users

# Login Function
def login():
    users = load_users()
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in users and users[username] == password:
            print("Login successful!\n")
            return username
        else:
            print("Invalid username or password. Please try again.\n")

# Register User Function
def register_user():
    users = load_users()
    new_username = input("Enter new username: ")
    if new_username in users:
        print("Username already exists. Choose another.\n")
        return
    new_password = input("Enter new password: ")
    confirm_password = input("Confirm password: ")
    if new_password == confirm_password:
        with open("user.txt", "a") as user_file:
            user_file.write(f"{new_username}, {new_password}\n")
        print("User registered successfully!\n")
    else:
        print("Passwords do not match.\n")

# add task function
def add_task(logged_in_user):
    username = input("Enter username for the task: ")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (DD/MM/YYYY): ")
    assigned_date = datetime.date.today().strftime("%d/%m/%Y")
    completed = "No"

    with open("tasks.txt", "a") as tasks_file:
        tasks_file.write(f"{username}, {title}, {description}, {assigned_date}, {due_date}, {completed}\n")

    print("Task added successfully!\n")

# View all tasks
def view_all_tasks():
    with open("tasks.txt", "r") as tasks_file:
        tasks = tasks_file.readlines()
        if not tasks:
            print("\nNo tasks found.\n")
        else:
            for line in tasks:
                task = line.strip().split(", ")
                print(f"\nUser: {task[0]}\nTitle: {task[1]}\nDescription: {task[2]}"
                      f"\nAssigned Date: {task[3]}\nDue Date: {task[4]}\nCompleted: {task[5]}"
                      "\n" + "-" * 30)
                
# View tasks assigned to the logged-in user
def view_my_tasks(logged_in_user):
    """Displays only tasks assigned to the logged-in user."""
    with open("tasks.txt", "r") as file:
        tasks = [line.strip().split(", ") for line in file if line.strip().split(", ")[0] == logged_in_user]
        if not tasks:
            print("\nYou have no assigned tasks.\n")
        else:
            for task in tasks:
                print(f"\nTitle: {task[1]}\nDescription: {task[2]}"
                      f"\nAssigned Date: {task[3]}\nDue Date: {task[4]}"
                      f"\nCompleted: {task[5]}"
                      "\n" + "-" * 30)

# Display statistics for admin
def display_statistics():
    """Displays total number of users and tasks."""
    with open("tasks.txt", "r") as tasks_file:
        task_count = sum(1 for _ in tasks_file)
    with open("user.txt", "r") as user_file:
        user_count = sum(1 for _ in user_file)

    print("\n=== Statistics ===")
    print(f"Total Users: {user_count}")
    print(f"Total Tasks: {task_count}")
    print("==================\n")


# Main Execution Loop
logged_in_user = login()

while True:
    menu = input("""
r - register user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics (admin only)
e - exit
Choose an option: """).lower()

    if menu == 'r':
        if logged_in_user == 'admin':
            register_user()
        else:
            print("Only admin can register new users.\n")
    elif menu == 'a':
        add_task(logged_in_user)
    elif menu == 'va':
        view_all_tasks()
    elif menu == 'vm':
        view_my_tasks(logged_in_user)
    elif menu == 'ds':
        if logged_in_user == 'admin':
            display_statistics()
        else:
            print("Only admin can view statistics.\n")
    elif menu == 'e':
        print("Thank you.")
        break
    else:
        print("Wrong option, please try again.")
