

def save(newPlayer):
    save_file = open("slots_save.txt","w")
    save_file.write(str(newPlayer.money))
    save_file.close()

def read_from_save(newPlayer):
    
    try:
        with open("slots_save.txt") as money_placeholder:
            newPlayer.money = int(money_placeholder.read())
    except:
        save_file = open("slots_save", "w")
        save_file.write(str(newPlayer.money))



    return newPlayer.money
