# Inheritance in python

class Person:
    def __init__(self, grade):
        self.grade = grade

    def display_info(self):
        print(f"grade is {self.grade}")


class Student(Person):
    def __init__(self, grade, name):
        super().__init__(grade)
        self.name = name

    def display_info(self):
        super().display_info()
        print(f"name is {self.name}")


st1 = Student("A", "Kali")
st1.display_info()


class Teacher:
    def __init__(self, name):
        self.name = name

    def syllabus(self):
        print(f"Teacher name {self.name}")


class Student(Teacher):
    def __init__(self, name, subject, StudentName):
        super().__init__(name)
        self.subject = subject
        self.StudentName = StudentName

    def syllabus(self):
        super().syllabus()
        print(f"Student name : {self.StudentName} learn {self.subject}")


st2 = Student("chand", "xyz", "kali")
st2.syllabus()


class Animal:
    def __init__(self,name) -> None:
        self.name = name
    
    def sound(self):
        print(f"{self.name} sound like : ")
    
class dog(Animal):
    def __init__(self,name,sound_type):
        super().__init__(name)
        self.sound_type = sound_type
    def sound(self):
        super().sound()
        print(f" dog sound is{self.sound_type}")

class cat(Animal):
    def __init__(self,name,soundbase):
        super().__init__(name)
        self.soundbase = soundbase
    
    def sound(self):
        super().sound()
        print(f" Soun type is {self.soundbase}")
    
animal1 = dog("Moti","bark")
animal1.sound()
