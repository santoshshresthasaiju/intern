def display_menu():
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Quit")


def addtask(tasks):
    task = input("Enter the task:")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def viewstasks(tasks):
    if not tasks:
        print("Not tasks added.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "pending"
            print(f"{i}. {task['task']} - {status}")

def markCompleted(tasks):
    viewstasks(tasks)
    index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            addtask(tasks)
        elif choice == "2":
            viewstasks(tasks)
        elif choice == "3":
            markCompleted(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
