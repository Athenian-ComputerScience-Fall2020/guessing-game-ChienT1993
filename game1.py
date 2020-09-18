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

tries = 1

def user():
    user_input= int(input("Type your number here: "))
    return user_input

inp1 = user()

if inp1 == random_num:
    print ("Congratulation, you have guess the correct number!")
    exit ()
elif inp1 < random_num:
    print ("Your number is too low!")
    tries = tries + 1
    inp2 = user()
elif inp1 > 10:
    print ("Sorry, your number is out of range!")
    tries = tries + 1
    inp2 = user()
elif inp1 > random_num:
    print ("Your number is too high!")
    tries = tries + 1
    inp2 = user()

if inp2 == random_num:
    print ("Congratulation, you have guess the correct number!")
    exit ()
elif inp2 < random_num:
    print ("Your number is too low!")
    tries = tries + 1
    inp3 = user()
elif inp2 > 10:
    print ("Sorry, your number is out of range!")
    tries = tries + 1
    inp3 = user()
elif inp2 > random_num:
    print ("Your number is too high!")
    tries = tries + 1
    inp3 = user()

if inp3 == random_num:
    print ("Congratulation, you have guess the correct number!")
    exit ()
elif inp3 < random_num:
    print ("Your number is too low!")
    tries = tries + 1
    inp4 = user()
elif inp3 > 10:
    print ("Sorry, your number is out of range!")
    tries = tries + 1
    inp4 = user()
elif inp3 > random_num:
    print ("Your number is too high!")
    tries = tries + 1
    inp4 = user()

if inp4 == random_num:
    print ("Congratulation, you have guess the correct number!")
    exit ()
elif inp4 < random_num:
    print ("Your number is too low!")
    tries = tries + 1
    inp5 = user()
elif inp4 > 10:
    print ("Sorry, your number is out of range!")
    tries = tries + 1
    inp5 = user()
elif inp4 > random_num:
    print ("Your number is too high!")
    tries = tries + 1
    inp5 = user()

if tries == 5:
    print ("Game over, you are out of chances!")
    print ("The correct answer is " + str(random_num))