import random
from collections import Counter

# Suit symbols and card values
suit_symbols = {
    "hearts": "♥",
    "diamonds": "♦",
    "spades": "♠",
    "clubs": "♣"
}

values = {
    "ace": "A",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "jack": "J",
    "queen": "Q",
    "king": "K"
}

suits = list(suit_symbols.keys())
value_names = list(values.keys())
deck = [(value, suit) for suit in suits for value in value_names]

def print_card(value_display, suit_symbol):
    left = f"{value_display:<2}"
    right = f"{value_display:>2}"
    
    print("┌─────────────┐")
    print(f"│ {left}          │")
    print("│             │")
    print("│             │")
    print(f"│      {suit_symbol}      │")
    print("│             │")
    print("│             │")
    print(f"│          {right} │")
    print("└─────────────┘")

def print_card_back():
    print("┌─────────────┐")
    for _ in range(7):
        print("│  #########  │")
    print("└─────────────┘")

def black_jack():
    global deck  # <-- Added this line so deck is accessible and modifiable inside

    def calculate_hand_value(hand):
        """Calculate the blackjack value of a hand."""
        value = 0
        aces = 0
        for card_value, _ in hand:
            if card_value in ["jack", "queen", "king"]:
                value += 10
            elif card_value == "ace":
                aces += 1
                value += 11  # Count ace as 11 initially
            else:
                value += int(values[card_value])
        
        # Adjust for aces if value > 21
        while value > 21 and aces:
            value -= 10  # Count ace as 1 instead of 11
            aces -= 1
    
        return value

    def deal_initial_hands(deck):
        random.shuffle(deck)
        player_hand = []
        computer_hand = []
    
        player_hand.append(deck.pop())
        computer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        computer_hand.append(deck.pop())
    
        return player_hand, computer_hand, deck

    def print_hand(hand):
        for card_value, card_suit in hand:
            print_card(values[card_value], suit_symbols[card_suit])

    def show_computer_hand(computer_hand, hide_second_card=True):
        value1, suit1 = computer_hand[0]
        print_card(values[value1], suit_symbols[suit1])
    
        if hide_second_card:
            print_card_back()
        else:
            value2, suit2 = computer_hand[1]
            print_card(values[value2], suit_symbols[suit2])
     
    # Initial deal at start
    player_hand, computer_hand, deck = deal_initial_hands(deck)

    while True:
        print("\nPlayer's hand:")
        print_hand(player_hand)
        player_value = calculate_hand_value(player_hand)
        print(f"Player hand value: {player_value}")
        
        print("\nDealer's hand:")
        show_computer_hand(computer_hand, hide_second_card=True)
        
        if player_value == 21 and computer_hand == 21:
            print("Tie!")
            return
        
        # Player turn
        choice = input("Do you want to hit or stand? h/s: ").lower()
        if choice == 'h':
            player_hand.append(deck.pop())
            player_value = calculate_hand_value(player_hand)
            if player_value > 21:
                print("\nPlayer's hand:")
                print_hand(player_hand)
                print("Bust! You lose.")
                return
        elif choice == 's':
            break
        else:
            print("Invalid input, please enter 'h' or 's'.")
    
    # Dealer turn
    print("\nDealer's hand:")
    show_computer_hand(computer_hand, hide_second_card=False)
    dealer_value = calculate_hand_value(computer_hand)
    print(f"Dealer hand value: {dealer_value}")

    while dealer_value < 17:
        print("Dealer hits.")
        computer_hand.append(deck.pop())
        print_hand(computer_hand)
        dealer_value = calculate_hand_value(computer_hand)
        print(f"Dealer hand value: {dealer_value}")
        
        if dealer_value > 21:
            print("Dealer busts! You win!")
            return
    
    # Final comparison
    print("\nFinal hands:")
    print("Player's hand:")
    print_hand(player_hand)
    print(f"Player value: {player_value}")
    
    print("Dealer's hand:")
    print_hand(computer_hand)
    print(f"Dealer value: {dealer_value}")
    
    if dealer_value > player_value:
        print("Dealer wins!")
    elif dealer_value < player_value:
        print("You win!")
    else:
        print("It's a tie!")

def texas_holdem():
   
    global deck
   
    def hands():
        random.shuffle(deck)
        player_hand = []
        computer_hand = []
    
        player_hand.append(deck.pop())
        computer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        computer_hand.append(deck.pop())

        return player_hand, computer_hand, deck
    
    def comunity_Cards():
        deck.pop()
        flop = [deck.pop() for _ in range(3)]
        deck.pop()
        turn = deck.pop()
        deck.pop()
        river = deck.pop()
        return flop + [turn, river], + deck

    def print_hand(hand):
        for card_value, card_suit in hand:
            print_card(values[card_value], suit_symbols[card_suit])

    def show_computer_hand(computer_hand, hide_both_cards):
    
        if hide_both_cards:
            print_card_back()
            print_card_back()
        else:
            value1, suit1 = computer_hand[0]
            print_card(values[value1], suit_symbols[suit1])
            value2, suit2 = computer_hand[1]
            print_card(values[value2], suit_symbols[suit2])

    def card_value_rank(card_value):
        order = ['two', "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
        return order.index(card_value) + 2
    
print("Hello welcome to Flynn's casino here is a list of games we have")
print("Black Jack, Texas Hold'em")
playerChoice = input("What game would you like to play: ").lower()

if playerChoice == "black jack":
    black_jack()
elif playerChoice == "texas hold'em":
    texas_holdem()

