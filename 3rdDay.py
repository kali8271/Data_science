# Access Modifiers 
# protected access modifiers using single underscore '_'
class Student:
    def __init__(self,name,roll,val):
        self._name = name
        self._roll = roll   # we can create protected access modifiers
        self._aval = val
    
    def _availibility(self):
        print(f"Availibility of Student is {self._aval}")

    def _record(self,score,dob,phone):
        self._score = score
        self._dob = dob
        self._phone = phone
        print(f"{self._score} {self._dob} {self._phone}")
    
class Node(Student):
    def __init__(self, name, roll, val):
        super().__init__(name, roll, val)
    
    def _scale(self):
        print("Scale is based on their score")
    
st1 = Node("abc",123,"present")
st1._availibility()
st1._record("outstanding",12,233455)
st1._scale()

 # creation of private access modifiers using double underscore '__'   
class Student:
    def __init__(self,name,roll,val):
        self.__name = name
        self.__roll = roll   # we can create private access modifiers
        self.__aval = val
    
    def _availibility(self):
        print(f"Availibility of Student is {self.__aval}")
        print(f"Name of Student {self.__name} and roll is {self.__roll}")
    def _record(self,score,dob,phone):
        self.__score = score
        self.__dob = dob
        self.__phone = phone
        print(f"Score : {self.__score} dob only day :  {self.__dob} Phone : {self.__phone}")
    
class Node(Student):
    def __init__(self, name, roll, val):
        super().__init__(name, roll, val)
    
    def _scale(self):
        print("Scale is based on their score")

st1 = Node("abc",123,"present")
st1.__availibility()
st1.__record("outstanding",12,233455)
st1.__scale()