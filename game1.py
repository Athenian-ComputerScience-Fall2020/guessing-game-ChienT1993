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

x = int(input("Enter a number where your range of guessing number will start: "))
y = int(input("Enter a number where your range of guessing number will end: "))
random_num= random.randint(x,y)

tries= 1

z = int(input("Enter how many guesses you want to do: "))
def user():
    user_input= int(input("Type your number here: "))
    return user_input

def guess(tries, inp):
    if inp == random_num:
        print ("Congratulation, you have guess the correct number!")
        exit ()
    elif inp > y and inp < x:
        print ("Sorry, your number is out of range!")
        tries = tries + 1
        inp = user()
    elif inp < random_num:
        print ("Your number is too low!")
        tries = tries + 1
        inp = user()
    elif inp > random_num:
        print ("Your number is too high!")
        tries = tries + 1
        inp = user()
    if tries == z:
        print ("Game over, you are out of chances!")
        print ("The correct answer is " + str(random_num))
        exit ()
    return (tries, inp)

inp= user()
for a in range (2, z+1):
    output = guess (tries, inp)
    tries = output [0]
    inp = output [1]

again = input("Do you want to play again?(yes/no): ")

if again == "yes":
    inp= user()
elif again == "no":
    print ("Thanks for playing the game!")