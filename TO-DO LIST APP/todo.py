class Task:
    def _init_(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description, "Not Started")
        self.tasks.append(task)
        print("Task added successfully.")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            print("Title:", task.title)
            print("Description:", task.description)
            print("Status:", task.status)
            print()

    def save_tasks(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.title},{task.description},{task.status}\n")
        print("Tasks saved successfully.")

    def load_tasks(self, filename):
        self.tasks = []
        try:
            with open(filename, "r") as file:
                for line in file:
                    title, description, status = line.strip().split(",")
                    task = Task(title, description, status)
                    self.tasks.append(task)
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("File not found.")

def main():
    todo_list = ToDoList()

    while True:
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == "2":
            title = input("Enter the title of the task to delete: ")
            todo_list.delete_task(title)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            filename = input("Enter the filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == "5":
            filename = input("Enter the filename to load tasks: ")
            todo_list.load_tasks(filename)
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
