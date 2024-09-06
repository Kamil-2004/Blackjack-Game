logo = """

  __                                    
|/  | /           /     |           /   
|___|(  ___  ___ (        ___  ___ (    
|   )| |   )|    |___)  )|   )|    |___)
|__/ | |__/||__  | \   / |__/||__  | \  
                    __/          

"""
print(logo)

# Blackjack game

import random  

def deal_card():
    """Function to deal a random card"""
    return random.randint(2, 11)

def calculate_score(cards):
    """Function to calculate the total score from a list of cards"""
    score = sum(cards)
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def play_blackjack():
    """Function to play a game of Blackjack"""
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    print("User:", user_cards)
    print("Computer:", [computer_cards[0], "*"])

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    if user_score == 21:
        print("Blackjack! You win!")
        return

    while input("Do you want another card? Type 'yes' or 'no': ").lower() == "yes":
        user_cards.append(deal_card())
        print("User:", user_cards)
        user_score = calculate_score(user_cards)
        if user_score > 21:
            print("Bust! You lose!")
            return

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("User score:", user_score)
    print("Computer score:", computer_score)

    if user_score > 21:
        print("Bust! You lose!")
    elif computer_score > 21:
        print("Computer busts! You win!")
    elif user_score > computer_score:
        print("You win!")
    elif user_score < computer_score:
        print("You lose!")
    else:
        print("It's a draw!")

play_blackjack()