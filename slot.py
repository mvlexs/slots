import random
from collections import Counter
from player import Player
import input
from result import Result

prizelist = ['🍒','🍑','🍋','💎','💲']
values = ['','','']

class Slot():
    roll1 = None
    roll2 = None
    roll3 = None
    prize = 0
    prizelist = ['🍒','🍑','🍋','💎','💲']
    values = values

    def __init__ (self, roll1, roll2, roll3, prize, prizelist, values):
        self.roll1 = roll1
        self.roll2 = roll2
        self.roll3 = roll3
        self.prize = prize
        self.prizelist = prizelist
        self.values = values

    def roll(self,player: Player):
        self.roll1 = random.choice(self.prizelist)
        self.roll2 = random.choice(self.prizelist)
        self.roll3 = random.choice(self.prizelist)
        self.values = [self.roll1,self.roll2,self.roll3]
        print(self.values)
        result = self.checkWin()
        prize = self.checkPrize(result)
        player.money += prize

        self.again()

    def checkWin(self) -> Result:
        #win_or_loss, winning_symbol, winning_count

        counts = Counter(self.values).most_common(1)[0]
        if counts [1] > 1:
            this_result = Result(
                True,
                counts[0],
                counts[1]
            )
            print("Congrats, you win!")
        elif "💲" in self.values:
            result = Result(True, "💲", 1)
            print("Congrats, you win!")
        elif "💎" in self.values:
            result = Result(True, "💎", 1)
            print("Congrats, you win!")
        else:
            print("You lose! :(")

        return result
    

    def checkPrize(self, result: Result) -> int:
        if result.win:
            match result.symbol:
                
                case '🍑':
                    return 5 * (result.count - 1)
                case '🍋':
                    return 10 * (result.count - 1)
                case '🍒':
                    return 25 * (result.count - 1)
                case '💎':
                    if result.count != 1:
                        return 50 * (result.count - 1)
                    else:
                        return 5
                case '💲':
                    if result.count != 1:
                        return 100 * (result.count - 1)
                    else:
                        return 10
                case _:
                    return 0

        return 0

    def again(self):
        x = 1
        newInput = input.Input(0)
        print("Do you want to play again?\ny/n")
        while x == 1:
            newInput.inputYN()
            if newInput.input == True:
                self.roll()
                x += 1
            elif newInput.input == False:
                exit()