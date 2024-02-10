import input


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
                print("Tutorial")
                x += 1
            elif newInput.input == False:
                x += 1
            
            
    
    