import input
import time


class Player():
    money = 10

    def __init__(self, money):
        self.money = money

    def tutorial(self):
        x = 1
        newInput = input.Input(0)
        print("Do you want an explanation before you play?")
        while x == 1:
            newInput.inputYN()
            if newInput.input == True:
                print("Welcome to mvlexs's 💲LOT💲!")
                time.sleep(1.5)
                print("The game is simple, you start with 50$, you pay 5$ for a spin, hope for the best and just have fun.")
                time.sleep(1.5)
                print("No worries, if you go broke, you can borrow some of my $, but remember to pay me back ;)")
                time.sleep(1.5)
                x += 1
            elif newInput.input == False:
                x += 1
        while x == 2:
            print("Alright then, let's play!") 
            time.sleep(1.5)
            x += 1

            
    
    