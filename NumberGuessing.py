# Number Guessing Game using python library

#from math import *
from random import *

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

generatedNumber = randint( num1, num2)   # generates number between num1 and num2

guess = int(input("Number of Guesses : ")) # User enters the number to be guessed

count = 0  # count shows number of guesses

while count < guess :
    count = count +1
    guess = int(input("Number of Guesses : ")) # User enters the number to be guessed

    if generatedNumber == guess:
        print(f"Congratulation you guessed successfully {count} try and guessed number is {generatedNumber}")
        break  # if user  enters number which is matched then program will close

    elif generatedNumber < guess :
        print(f"You are closer to  ")
        continue

    elif generatedNumber > guess:
        print(f"You are going to far away ")
        continue
    else:
        break

print(f"Number is {generatedNumber} ")
print(f"You tried {count} and not guessed the number ")
print("Better luck next time ")