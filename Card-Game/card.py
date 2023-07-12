class Card:
    def __init__(self, suit, value):
        self.suit  = suit
        self.value = value
    
    def setVal(self, val):
        self.value = val

    def setSuit(self, suit: str):
        self.suit = suit

    def getVal(self):
        return self.value
    
    def getSuit(self):
        return self.suit
    
    def printCard(self):
        print(self.suit, " | ", self.value)
        return