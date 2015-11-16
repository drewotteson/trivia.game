import random
import time
from jdict import *


#print (categorylist) 

class Gamestart(object):
    def __init__(self):
        print("")
        print("Welcome to Jeopardy!")
        print("")
        name=(input("Enter your name! "))
        print("Hello " + name + "!")
        print("")
        self.name=name
        self.bank=0
        self.categorychoice=0
        self.question=0

    def choosecategory(self):

        choice = str(input('| History | Sports | Art & Literature | Popular Culture | ''Choose a category! ')).lower()

        if choice == "h":
            print("History it is.")
            self.categorychoice = history
            
        if choice == "s":
            print("Sports it is.")
            self.categorychoice = sports 

        if choice == "a":
            print("Art & Literature it is.")
            self.categorychoice = artliterature

        if choice == "p":
            print("Popular Culture it is.")
            self.categorychoice = popculture

        else:
            print("Please enter the first letter of the category you would like.")

    def choosequestionvalue(self):

        choice = int(input('| 200 | 400 | 600 | 1000 | ''The higher the value, the harder the question.  Choose a value! '))

        if choice == 200:
            print("for 200")
            question = self.categorychoice
            print(question['200'])
            self.question=question['200']

        elif choice == 400:
            print("for 400")
            question = self.categorychoice
            print(question['400'])
            self.question=question['400']

        elif choice == 600:
            print("for 600")
            question = self.categorychoice
            print(question['600'])
            self.question=question['600']


        elif choice == 1000:
            print("for 1000")
            question = self.categorychoice
            print(question['1000'])
            self.question=question['1000']

        else:
            print("Please enter the number value that you would like a question from")

  


game=Gamestart()
game.choosecategory()
game.choosequestionvalue()

