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