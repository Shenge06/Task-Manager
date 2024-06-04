import datetime

# Initialize an empty dictionary to store user data
user_data = {}

# Load existing user data from a file into the dictionary
with open('user.txt', 'r') as user_file:
    for line in user_file:
        # Split each line into username and password and store in the user_data dictionary
        username, password = line.strip().split(', ')
        user_data[username] = password

while True:
    # Ask the user to enter their username and password
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    # Check if the entered username exists and the password is correct
    if username_input in user_data and password_input == user_data[username_input]:
        print("Login successful! Welcome, " + username_input + "!")
        break
    else:
        print("Invalid username or password. Please try again.")

while True:
    # Present a menu to the user and convert the user input to lowercase
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - display statistics
e - exit
: ''').lower()

    if menu == 'r':
        # User registration
        if username_input == 'admin':  # Additional condition to restrict registration to admin
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm your password: ")

            # Check if passwords match and the username is not already registered
            if new_password == confirm_password:
                if new_username not in user_data:
                    user_data[new_username] = new_password
                    with open('user.txt', 'a') as user_file:
                        user_file.write("{}, {}\n".format(new_username, new_password))  # Use comma and space
                    print("Registration successful!")
                else:
                    print("Username already exists. Registration failed.")
            else:
                print("Passwords do not match. Registration failed.")
        else:
            print("Only admin can register new users.")

    elif menu == 'a':
        # Adding a task
        task_username = input("Enter the username of the person the task is assigned to (type 'b' to go back, 'e' to exit): ")

        if task_username.lower() == 'b':
            break  # Go back to the main menu
        elif task_username.lower() == 'e':
            print('Goodbye!!!')
            exit()  # Exit the program

        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        task_due_date = input("Enter the due date of the task (YYYY-MM-DD): ")

        # Get the current date using the datetime module
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")

        # Store task data in tasks.txt file with correct formatting
        with open('tasks.txt', 'a') as task_file:
            task_file.write("{}, {}, {}, {}, {}, {}\n".format(task_username, task_title, task_description, task_due_date, current_date, "No"))

        print("Task added successfully!")

    elif menu == 'va':
        # Viewing all tasks
        with open('tasks.txt', 'r') as task_file:
            tasks = task_file.readlines()
            if tasks:
                for task in tasks:
                    task_info = task.strip().split(', ')
                    # Display task details
                    print("\nAssigned to:", task_info[0])
                    print("Title:", task_info[1])
                    print("Description:", task_info[2])
                    print("Due Date:", task_info[3])
                    print("Date Created:", task_info[4])
                    print("Status:", task_info[5])
            else:
                print("No tasks found.")

    elif menu == 'vm':
        # Viewing tasks for the logged-in user
        if username_input in user_data:
            with open('tasks.txt', 'r') as task_file:
                tasks = task_file.readlines()
                if tasks:
                    for task in tasks:
                        task_info = task.strip().split(', ')
                        if task_info[0] == username_input:
                            # Display task details for the logged-in user
                            print("\nAssigned to:", task_info[0])
                            print("Title:", task_info[1])
                            print("Description:", task_info[2])
                            print("Due Date:", task_info[3])
                            print("Date Created:", task_info[4])
                            print("Status:", task_info[5])
                else:
                    print("No tasks found for this user.")
        else:
            print("You are not authorized to view tasks.")

    elif menu == 's':
        # Display statistics - Only allow admin to view statistics
        if username_input == 'admin':
            # Read all tasks from tasks.txt file into a list
            with open('tasks.txt', 'r') as task_file:
                tasks = task_file.readlines()

            total_users = len(user_data)
            # Calculate total tasks
            total_tasks = len(tasks)
            print(f"Total number of users: {total_users}")
            print(f"Total number of tasks: {total_tasks}")
        else:
            print("Only admin can view statistics.")

    elif menu == 'e':
        # Exit the program
        print('Goodbye!!!')
        exit()

    else:
        # Invalid input
        print("You have entered an invalid input. Please try again.")






