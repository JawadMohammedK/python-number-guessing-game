# this is number guessing game
import random
print("Hi, this is python number guessing game,\n you have 7 chances to guess the number! lets start")
print("the computer will pick a number, you need to catch it!")

low = int(input("Enter the lowest number:"))
high = int(input("Enter the highest number:"))

number = random.randint(low,high)
chance = 7
attempts = 0
while attempts < chance:
    attempts += 1
    inputy = int(input(f"Please enter the number you want to guess, your number must between {low}, {high} "))

    if inputy == number:
        print("You did it ")
        break
    elif inputy > number:
          print("Wrong! You chose higher number! Please Try again")
    elif inputy < number:
        print("Wrong! You chose Lower, Try Again ")


    if attempts >= chance and inputy != number:
     print(f"Sorry You have consumed all the 7 attempts, the solution was: {number} ")




