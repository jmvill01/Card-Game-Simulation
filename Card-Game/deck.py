from card import Card
import random

class Deck:
    Total_Cards = 52
    Num_Hearts = 13
    Num_Spades = 13
    Num_Diamonds = 13
    Num_Clubs = 13

    def initialize_cards(self):
        card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        card_types = ["Hearts", "Spades", "Diamonds", "Clubs"]
        Cards = []


        for j in card_types:
            for i, val in enumerate(card_values):
                card = Card(j, card_values[i])
                Cards.append(card)
        return Cards
    
    def shuffle(self, cards: list[Card]):
        random.shuffle(cards)
        return cards


