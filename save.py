

def save(newPlayer):
    save_file = open("slots_save.txt","w")
    save_file.write(str(newPlayer.money))
    save_file.close()

def read_from_save(newPlayer):
    
    try:
        with open("slots_save.txt") as save_file:
            newPlayer.money = int(save_file.read())
            save_file.close()

    except:
        save_file = open("slots_save", "w")
        save_file.write(str(newPlayer.money))
        save_file.close()

    return newPlayer.money
