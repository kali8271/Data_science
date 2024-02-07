# To-do list using dictionary

to_do_list = {}  # creating empty dictionary

def add_task(task):
    to_do_list[task] = "incommplete"
    print(f"Task {task} added in to-do list")

def complete_task(task):
    if task in to_do_list:
        to_do_list[task] = "completed"
        print(f"Task {task} marked as completed")

def display_task():
    print("\n Print to_do list")
    for task,status in to_do_list.items():
        print(f"{task} is {status}")


add_task("Work is pending")
add_task("work completed")
display_task()
complete_task("Completed")
display_task()

# creating todo list using classes and object
class TodoList:
    def __init__(self,owner):
        self.owner = owner
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(task)

    def complete_task(self,task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task {task} is completed" )
        else:
            print("Task not found ")
        
    def display_task(self):
        print(f"The to-do task of {self.owner} : ")
        for task in self.tasks:
            print(task)

classExercise = TodoList("chand")
classExercise.add_task("do this work")
classExercise.add_task("I have to read")
classExercise.display_task()
