TASK_FILE = "tasks.txt"

def add_task(task):
    # Adds a new task to the task file
    # 'a' mode means append - new data will be added without erasing old data.
    with open(TASK_FILE, 'a') as file:
        # We add ",Pending" so that each new tasks start as pending
        file.write(task + ", Pending\n")
    print(f"Task '{task}' added successfully!")

def view_tasks():
    # Reads and displays all tasks from the file
    # Demonstrates reading using readlines().
    try:
        with open(TASK_FILE, 'r') as file:
            # readlines() returns a list of strings, each representing a line
            tasks = file.readlines()

            # If the file is empty, tasks list will be empty
            if len(tasks) == 0:
                print("No tasks found")
                return
            
            print("\nYour tasks")
            index = 1 # We will manually number the tasks
            for line in tasks:
                # strip() removes spaces and newline characters
                # 'Buy milk, Pending'.split(',')
                # Output: ["Buy milk", "Pending"]
                task, status = line.strip().split(",")
                print(str(index) + ". " + task + " - " + status)
                index += 1
    except FileNotFoundError:
        # This happens if the file doesn't exist yet
        print("Task file not found. Add a task first!")

def mark_task_completed(task_number):
    # Marks a specific task as completed.
    # Demonstrates:
    # - Reading all lines
    # - Modifying them
    # - Writing back using 'w' mode (overwrites file)
    try:
        with open(TASK_FILE, 'r') as file:
            tasks = file.readlines()

        # If the number entered is no valid
        if task_number < 1 or task_number > len(tasks):
            print("Invalid task!!")
            return
        
        # Convert the chosen line into task name and status
        task, status = tasks[task_number - 1].strip().split(",")
        # Replace with Completed
        tasks[task_number - 1] = task + ", Completed\n"

        # Write the updated list back to the file
        with open(TASK_FILE, 'w') as file:
            file.writelines(tasks)

        print(f"Task '{task}' marked as completed!")
    except FileNotFoundError:
        print("Task file not found. Add a task first!")

def task_statistics():
    # Shows statistics of tasks
    try:
        with open(TASK_FILE, 'r') as file:
            # Read all lines
            tasks = file.readlines()

            total_tasks = len(tasks)
            completed = 0
            for line in tasks:
                if "Completed" in line:
                    completed += 1
            pending = total_tasks - completed
        
        print("\n Task Statistics:")
        print("\tTotal Tasks:", total_tasks)
        print("\tCompleted:", completed)
        print("\tPending:", pending)
    except FileNotFoundError:
        print("Task file not found. Add a task first!")


# MAIN PROGRAM LOOP
while True:
    print("\n ==== TASK MANAGER ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. View Tasks Statistics")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task description: ")
        add_task(task_name)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        try:
            # Convert user input to an integer
            task_num = int(input("Enter task number to mark completed: "))
            mark_task_completed(task_num)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":
        task_statistics()

    elif choice == "5":
        print("Exiting Task Manager. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")