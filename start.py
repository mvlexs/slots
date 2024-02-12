import player
import slot
import save

def start():
    newPlayer = player.Player(50)
    newSlot = slot.Slot(0,0,0,0,slot.prizelist,slot.values)
    newPlayer.money = 50
    newPlayer.money = save.read_from_save(newPlayer)
    print(newPlayer.money)
    newPlayer.tutorial()
    newSlot.roll(newPlayer)

    
    

    