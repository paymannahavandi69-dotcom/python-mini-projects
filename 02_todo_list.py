class Task:
    def __init__(self, title):
        self.title = title
        self.done = False
    
    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.title}"

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        print(f"Task '{title}' added!")
    
    def show_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks yet!")
        else:
            for i in range(len(self.tasks)):
                print(f"{i + 1}. {self.tasks[i]}")
    
    def remove_task(self, index):
        if index < 1 or index > len(self.tasks):
            print("Invalid task number!")
        else:
            removed = self.tasks.pop(index - 1)
            print(f"Task '{removed.title}' removed!")
    
    def mark_done(self, index):
        if index < 1 or index > len(self.tasks):
            print("Invalid task number!")
        else:
            self.tasks[index - 1].done = True
            print(f"Task '{self.tasks[index - 1].title}' marked as done!")
    
    def save_to_file(self, filename):
        file = open(filename, "w")
        for task in self.tasks:
            file.write(f"{task.title}|{task.done}\n")
        file.close()
        print("Tasks saved!")
    
    def load_from_file(self, filename):
        try:
            file = open(filename, "r")
            lines = file.readlines()
            file.close()
            self.tasks = []
            for line in lines:
                parts = line.strip().split("|")
                task = Task(parts[0])
                task.done = parts[1] == "True"
                self.tasks.append(task)
            print("Tasks loaded!")
        except FileNotFoundError:
            print("No saved file found!")
    
    def __len__(self):
        return len(self.tasks)
    
    def __str__(self):
        return f"TodoList: {len(self.tasks)} tasks"

todo = TodoList()

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Mark as Done")
    print("5. Save to File")
    print("6. Load from File")
    print("q. Quit")
    
    choice = input("Choose: ")
    
    if choice == "q":
        print("Goodbye!")
        break
    
    if choice == "1":
        title = input("Task title: ")
        todo.add_task(title)
    elif choice == "2":
        todo.show_tasks()
    elif choice == "3":
        todo.show_tasks()
        try:
            index = int(input("Task number to remove: "))
            todo.remove_task(index)
        except ValueError:
            print("Please enter a number!")
    elif choice == "4":
        todo.show_tasks()
        try:
            index = int(input("Task number to mark done: "))
            todo.mark_done(index)
        except ValueError:
            print("Please enter a number!")
    elif choice == "5":
        todo.save_to_file("tasks.txt")
    elif choice == "6":
        todo.load_from_file("tasks.txt")
    else:
        print("Invalid choice!")