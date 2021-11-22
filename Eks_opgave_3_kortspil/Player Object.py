import random



# ! Defines what a deck is
class Deck:
    # * Make dummy deck with stack of cards 
    def __init__(self, deck=[]):
        self.deck = deck
        #self.size = size
        
    # * Shuffle a stack of cards
    def shuffle(self): 
        random.shuffle(self.deck)
        return self.deck

    # * Play and remove top card from deck
    def play(self):
        return self.deck.pop(0)
    
    def deal(self, amount):
        dealt_hand = self.deck[:amount]
        self.deck = self.deck[amount:]
        
        return dealt_hand
    
    # * Add cards won to deck
    def __add__(self, other):
        return self.deck + other.deck


# ! Defines what a player is
class Player:
    # * Initialize Player
    def __init__(self, name=''):
        self.name = name
        self.hand = Deck()
        self.discard = Deck()
    
    # * Deals x amount of cards from players hand
    def play_card(self):
        return self.hand.play()
    
    # * Vital status for given player
    def vital_status(self):
        # 0 for dead and 1 for living player
        if len(self.hand.deck) + len(self.discard.deck) == 0:
            return 0
        else:
            return 1
    
    # TODO random name
    # TODO hand as Deck
    # TODO discard pile as Deck
    # TODO Function to call deal from Deck
    # TODO Function to say if dead or not