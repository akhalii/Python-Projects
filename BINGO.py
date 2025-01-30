import random
import os
import time

#ask for how many players

def total_players():
    while True:
        try:
            players = int(input("How many players? "))
            if players <= 0:
                print("Enter more than 0 players.")
            else:
                break
        except ValueError:
            print("Enter a number.")
    return players

#ask how much to deposit

def deposit(players):
    player_balance = {}

    print()
    for player in range(1, players + 1):
        while True:
            try:
                deposit = float(input(f"Player {player}, how much would you like to deposit? "))        
                if deposit <= 0:
                    print("Deposit has to be more than $0.")
                else:
                    player_balance[player] = deposit
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    return player_balance

#show player's balance

def balance(player_balance):
    for player, player_balance in player_balance.items():
        print(f"Player {player} balance: ${player_balance:,.2f}")

#betting

def bet(players, player_balance):
    betting_pool = 0

    for player in range(1, players + 1):
        while True:
            try:
                bets = float(input(f"Player {player}, how much would you like to bet? "))
            
                if bets <= 0:
                    print("Enter a positive betting amount.")
                elif bets > player_balance[player]:
                    print("Insufficient funds.")
                else:
                    player_balance[player] -= bets
                    betting_pool += bets
                    break
            except ValueError:
                print("Enter a number.")
    return betting_pool, bets

#generate cards

def generate_cards(players):
    card_number = 1
    cards = []

    for i in range(players):
        print()
        print(f"       Card {card_number}")

        card = []


        for x in range(5):
            row = []
            for y in range(5):
                row.append(random.randint(1, 99))
            card.append(row)

        
        card[2][2] = "X"


        for row in card:
            formatted_row = " | ".join(f"{num:>2}" if num != "X" else f"{num:>2}" for num in row)
            print(f"| {formatted_row} |")

        card_number += 1
        cards.append(card)

    return cards

#draw numbers

def draw_numbers():
    print()
    ball_number = random.randint(1, 99)
    print(f"Number drawn: {ball_number}")
    return ball_number

#check card and replace drawn number with 'X'

def check_and_replace(cards, ball_number):
    for card in cards:
        for x in range(5):
            for y in range(5):
                if card[x][y] == ball_number:
                    card[x][y] = "X"

#check to see if a card has won

def check_winner(card,):

    
    for row in card:
        if all(num == "X" for num in row):
            return True

    
    for col in range(5):
        if all(card[row][col] == "X" for row in range(5)):
            return True

    
    if all(card[i][i] == "X" for i in range(5)):
        return True
    if all(card[i][4-i] == "X" for i in range(5)):
        return True

    return False

#clears screen

def clear_screen():
    # Clear the screen based on the operating system
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux or macOS
        
#main


def main():
    players = total_players()
    player_balance = deposit(players)

    print()
    balance(player_balance)

    while True:
        print()
        betting_pool, bets = bet(players, player_balance)

        cards = generate_cards(players)

    
        winner_declared = False
        while not winner_declared:
            time.sleep(0.1)
            clear_screen()
            
            print()
            ball_number = draw_numbers()
            print()
            check_and_replace(cards, ball_number)

            clear_screen()

            for i, card in enumerate(cards):
                print(f"       Card {i + 1}")
                for row in card:
                    formatted_row = " | ".join(f"{num:>2}" if num != "X" else f"{num:>2}" for num in row)
                    print(f"| {formatted_row} |")
                print()
        
        
            for i, card in enumerate(cards):
                if check_winner(card):
                    print(f"BINGO! Card {i + 1} won ${betting_pool:,.2f}!")
                    player_balance[i + 1] += betting_pool
                    winner_declared = True
                    break

        print()
        again = input("Would you like to play again [Yes or Press Enter to Exit]? ").lower()

        print()
        balance(player_balance)

        if again != "yes":
            print()
            print("Thank you for playing BINGO!")
            break

if __name__ == "__main__":
    main()
