# oops in python 
class bank:
    def __init__(self,acountnumber,accountholdername,balance):
        self.AccountNumber = acountnumber
        self.name = accountholdername
        self.balance = balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdrawl(self,amount):
        self.balance -= amount

    def check(self):
        print(f"{self.name} and deposited amount is {self.balance}")
    
bob = bank(1234,"chand",4000)
bob.deposit(300)
bob.check()


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

class car:

    def __init__(self,brand,model,color):
        self.brand = brand
        self.color = color
        self.model = model 

    def Driving(self):
        print(f"Car is Driving")
    def StartEngine(self):
        print(f"Start engine")
    def chessyNumber(self):
        print(f"34exer56")

car1 = car("BMW","Diesel","red")
car1.Driving()
car1.StartEngine()
car1.chessyNumber()

