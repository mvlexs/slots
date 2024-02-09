class Input():
    input = None
    
    def __init__(self,input):
        self.input
    

    def inputYN(self):
        x = input()
        if x.lower() in ['yes','y']:
            self.input = True
            return self.input
        elif x.lower() in ['no','n']:
            self.input = False
            return self.input
        else:
            print("Unrecognized input, please try again!")
            self.inputYN() 