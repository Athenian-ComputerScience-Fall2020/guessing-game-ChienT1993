#Collaborators: https://code-maven.com/number-guessing-in-python
'''
Use this file to write an "open" version of the game (no test code or defined format). This will be translated into a testable program later. Use the reponse statements provided to make that transition easier.

"Your number is too high."
"Your number is too low."
"Your number is out of range."
"I'm sorry you are giving up!"
"I'm sorry, you are out of guesses."

'''
import random

random_num= random.randint(0,10)

tries = 0

def user():
    user_input= int(input("Type your number here: "))
    return user_input

if user() == random_num:
    print ("Congratulation, you have guess the correct number!")
elif user() < random_num:
    print ("Your number is too low!")
    tries = tries + 1
elif user() > random_num:
    print ("Your number is too high!")
    tries = tries + 1
elif user() > 10:
    print ("Sorry, your number is out of range!")
    tries = tries + 1

if tries == 5:
    print ("Game over, the number you are looking for is: " + random_num)
elif tries > 0:
    print (user())