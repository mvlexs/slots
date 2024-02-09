import player
import slot

def start():
    newPlayer = player.Player(10)
    newSlot = slot.Slot(0,0,0,0,slot.prizelist,slot.values)
    newPlayer.tutorial()
    newSlot.roll()
    