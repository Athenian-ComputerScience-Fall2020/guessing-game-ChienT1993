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
a = user()
x = int(input("Enter a number where your range of guessing number will start: "))
y = int(input("Enter a number where your range of guessing number will end: "))
random_num= random.randint(x,y)

tries= 1

z = int(input("Enter how many guesses you want to do: "))
def user():
    user_input= int(input("Type your number here: "))
    return user_input


def guess():
 if a == random_num:
    print ("Congratulation, you have guess the correct number!")
    exit ()
 elif tries == z:
    print ("Game over, you are out of chances!")
    print ("The correct answer is " + str(random_num))
    exit ()
 elif a < random_num:
    print ("Your number is too low!")
    tries = tries + 1
    inp = user()
 elif a > 10:
    print ("Sorry, your number is out of range!")
    tries = tries + 1
    inp = user()
 elif a > random_num:
    print ("Your number is too high!")
    tries = tries + 1
    inp = user()

yes = 1
no = 2
try:
    again = input("Do you want to try again? (yes or no): ")
    if again == yes:
        user()
    elif again == no:
        print ("Thanks for spending your time on the game!")
except:
    print ("Sorry, please type yes or no")