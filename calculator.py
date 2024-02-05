# Simple Calculator 

'''num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second Number : "))

print("Enter Characters for operations that you have to performed : ")
print(" for add : + \n", "for Substaction : - \n", "for multiplication : * \n","for divison :  / \n", "for modulus : %\n")
ch = (input("Enter your Choice : "))
if(ch == '+'):
    print(f"Sum of first number {num1} and second number {num2} is : ", (num1+num2))
elif(ch == '-'):
    print(f"Substraction of first number {num1} and second number {num2} is : ",(num1-num2))
elif(ch == '*'):
    print(f"Multiplication of first number {num1} and second number {num2} is : ",(num1 * num2))
elif(ch == '/'):
    print(f"Divison of first number {num1} and second number {num2} is : ",(num1/num2))
else:
    print(f"Modulus of first number{num1} and second number {num2} is : ",(num1 % num2))'''



#Simple Calculator using functions

def sum(x,y):
    return x+y

def substraction(x,y):
    return x-y

def multiply(x ,y):
    return x*y

def divison(x,y):
    return x/y

def modulus(x,y):
    return x%y


num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second Number : "))

print("Enter Characters for operations that you have to performed : ")
print(" for add : + \n", "for Substaction : - \n", "for multiplication : * \n","for divison :  / \n", "for modulus : %\n")
ch = (input("Enter your Choice : "))
if(ch == '+'):
    print(f"Sum of first number {num1} and second number {num2} is : ", sum(num1,num2))
elif(ch == '-'):
    print(f"Substraction of first number {num1} and second number {num2} is : ",substraction(num1,num2))
elif(ch == '*'):
    print(f"Multiplication of first number {num1} and second number {num2} is : ",multiply(num1,num2))
elif(ch == '/'):
    print(f"Divison of first number {num1} and second number {num2} is : ",divison(num1,num2))
else:
    print(f"Modulus of first number{num1} and second number {num2} is : ",modulus(num1,num2))