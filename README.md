# Task-Manager
This Python code provides a secure and user-friendly task management system with the following features:

User Authentication: Secure login with username and password (hashed for enhanced security).
User Registration: Admin users can register new users.
Task Management: Create tasks, assign them to users, specify due dates, and track completion status (optional).
Task Viewing: Users can view all tasks (admin) or their assigned tasks.
Statistics: Admin users can view overall system statistics on users and tasks.
Requirements:

Python 3.x
Getting Started

Installation: Ensure you have Python 3 installed. You can download it from https://www.python.org/downloads/.
File Creation: Create two text files named user.txt and tasks.txt in the same directory as the Python script.
Running the Script

Save the code as a Python file (e.g., task_manager.py).
Open your terminal or command prompt and navigate to the directory where you saved the script.
Run the script using the command python task_manager.py.
Instructions

Upon launch, you'll be prompted to enter your username and password. If you haven't registered yet, the script will guide you through the registration process.
The script will present a menu with various options:
r: Register a new user (admin-only)
a: Add a new task
va: View all tasks (admin-only)
vm: View tasks assigned to you
s: Display statistics (admin-only)
e: Exit the program
Task Management

When adding a task, you'll be prompted to enter:

Username of the person assigned to the task (or b to go back, e to exit).
Task title
Task description
Due date (YYYY-MM-DD format)
Statistics

The admin user can view statistics on the total number of users and tasks.
