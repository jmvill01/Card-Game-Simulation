from card import Card
from deck import Deck
import numpy as np
import time
from decision_logic import call_play


def main():
    # Define a list to hold initial up-facing cards
    num_wins = 0
    num_losses = 0
    num_games = 100
    played_games = 0
    player_sets = []
    num_sets = 6
    chosen_set = None

    while played_games < num_games:    

        # Initialize the deck
        deck_init = Deck()
        deck = deck_init.initialize_cards()
        deck = deck_init.shuffle(deck)
        
        # Layout the number of sets of cards
        for i in range(num_sets):
            player_sets.append(deck[i])
            deck.pop(i) 

        # for i in player_sets:
            # print(i.getSuit())
            # print(i.getVal())
            # print("\n")

        # --------- Begin game ---------
        # Pick a set, call your play
        chosen_set = 0

        while chosen_set < num_sets and len(deck) > 0: 

            # Call your play
            call = call_play(player_sets[chosen_set].getVal())
            # player_sets[chosen_set].printCard()
            # print(call)

            # draw 1 card onto the chosen set of cards
            prev_card = player_sets[chosen_set]
            player_sets[chosen_set] = deck[0]
            deck.pop(0)
            # player_sets[chosen_set].printCard()

            # Check if set is still valid
            valid_set = None
            new_val = player_sets[chosen_set].getVal()

            if call == "Lesser":
                if new_val <= prev_card.getVal():
                    # print("Successful!")
                    valid_set = True
                else:
                    # print("Failure!")
                    valid_set = False
            else:
                if new_val >= prev_card.getVal():
                    # print("Successful!")
                    valid_set = True
                else:
                    # print("Failure!")
                    valid_set = False

            # print('\n')
            if not valid_set:
                chosen_set += 1

            # print(len(deck), " | ", chosen_set)
            # print('\n')

        if len(deck) == 0:
            # print("You won with: ", num_sets - chosen_set, " sets left!")
            num_wins += 1
        else:
            # print("You lost with: ", len(deck), " cards left in the deck!")
            num_losses += 1
        
        played_games += 1
    
    win_percentage = 100 * (num_wins / num_games)
    print("\nNumber of games: ", num_games, " | Number of Losses: ", num_losses)
    print("Total percentage of wins: ", win_percentage, "%")
    print("Total wins: ", num_wins)
    return

if __name__ == "__main__":
    main()
