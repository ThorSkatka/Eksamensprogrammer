import random

class Spillet:
    def __init__(self, player_count = 2, round_cap = 10, deck_count = 1):
        self.round = 1
        self.player_names = ['Hans', 'Bonk']
        self.player_count = player_count
        self.round_cap = round_cap
        self.deck_count = deck_count
        self.gen_deck()
    
    
    # TODO Generer deck
    def gen_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        card_stack = []
        
        for deck in range(self.deck_count):
            for i, suit in enumerate(suits):
                for card in range(2, 15):
                    card_stack.append([suit, card])
        
        return card_stack
    
    def players(self):
        players_at_table = []
        random.shuffle(self.player_names)
        
        for i, name in enumerate(self.player_names):
            players_at_table.append(name)
        
        return players_at_table

Spil = Spillet()
    # TODO Definer liste af spillere
    # TODO Vuder vinder af runden
    # TODO krig funktion
    # TODO Hold styr på nuværende runde
    # TODO Bordet som liste af aktiv kort
    # TODO Giv bordet til vinderen
    # TODO Dræb spiller
    # TODO Vurder vinderen

# ! Spiller
# TODO random name
# TODO hand as Deck
# TODO discard pile as Deck
# TODO Function to call deal from Deck
# TODO Function to say if dead or not