import random
import os

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# functions:
#   generate collection- generate cards with random psa rating and price
def generate_cards():
    with open("Pokemon Collection.txt", "w") as file:
        file.write(f"Charizard,10,39999.99\n")
        file.write(f"Venusaur,9,1099.99\n")
        file.write(f"Blastoise,8,1199.99\n")
        file.write(f"Nidoking,7,135.00\n")
    print("Collection Generated!")

#   load collection
def load_array():
    collection = []
    with open("Pokemon Collection.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                card_name, psa, price = parts
                collection.append((card_name,int(psa),float(price)))
    return collection

def load_dict():
    collection = {}
    with open("Pokemon Collection.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                card_name, psa, price = parts
                collection[card_name] = {'psa': int(psa), 'price': float(price)}
    return collection

#   view collection- uses dictionary and displays cards alphabetically
def view_collection():
    collection = load_array()
    print("Collection:\n")
    for card_name,psa,price in sorted(collection):
        print(f"{card_name} | PSA: {psa} | Price: ${price:,.2f}")

#   add card- ask for name of card, psa rating, and price of card
def add_card():
    while True:
        card_name = input("Enter card name: ")
        if not card_name.isalpha():
            print("Invalid input. Enter a name.")
        else:
            break
    while True:
        try:
            psa_rating = int(input("Enter PSA rating: "))
            if 1 <= psa_rating <= 10:
                break
            else:
                print("Invalid input. Enter a rating between 1 and 10.")
        except ValueError:
            print("Enter a valid number.")
        except Exception as e:
            print(f"Error: '{e}'")
    while True:
        try:
            card_price = float(input("Enter card price: "))
            if card_price >= 0:
                break
            else:
                print("Invalid input. Enter a positive number.")
        except ValueError:
            print("Enter a number.")
        except Exception as e:
            print(f"Error: '{e}'")

    with open("Pokemon Collection.txt", "a") as file:
        file.write(f"{card_name},{psa_rating},{card_price:.2f}\n")
    print("\nCard added!\n")

#   delete card- delete card from collection
def delete_card():
    collection = load_dict()

    for x, (card_name, details) in enumerate(collection.items(), start= 1):
        print(f"{x}. {card_name} | PSA: {details['psa']} | Price: ${details['price']:,.2f}")

    while True:
        try:
            choice = int(input("\nEnter Choice: "))
            if choice <= 0:
                print("Invalid input. Enter a number greater than 0.")
            elif choice > len(collection):
                print("Enter a number within range.")
            else:
                break
        except ValueError:
            print("Enter a number.")
        except Exception as e:
            print(f"Error: '{e}'")

    deleted_card = list(collection.keys())[choice-1] # found on stackoverflow
    del collection[deleted_card]

    with open("Pokemon Collection.txt", "w") as file:
        for card_name, details in collection.items():
            file.write(f"{card_name},{details['psa']},{details['price']:.2f}\n")
    print("\nCard Deleted!")

#   change card price- change card price
def change_price():
    collection = load_dict()
    for x, (card_name, details) in enumerate(collection.items(), start= 1):
        print(f"{x}. {card_name} | PSA: {details['psa']} | Price: ${details['price']:,.2f}")

    while True:
        try:
            choice = int(input("\nEnter Choice: "))
            if choice <= 0:
                print("Invalid input. Enter a number greater than 0.")
            elif choice > len(collection):
                print("Enter a number within range.")
            else:
                break
        except ValueError:
            print("Enter a number.")
        except Exception as e:
            print(f"Error: '{e}'")

    card = list(collection.keys())[choice-1]

    while True:
        try:
            new_price = float(input("Enter new price: "))
            if new_price < 0:
                print("Invalid input. Enter a price greater than 0.")
            else:
                break
        except ValueError:
            print("Enter a number.")
        except Exception as e:
            print(f"Error: '{e}'")

    collection[card]['price'] = new_price

    with open("Pokemon Collection.txt", "w") as file:
        for card_name, details in collection.items():
            file.write(f"{card_name},{details['psa']},{details['price']:.2f}\n")
    print("\nCard Price Updated!")

#   sort collection: (by dictionary)
#       price
def sort_price():
    collection = load_dict()
    print("\nSort by:")
    print("1. Ascending")
    print("2. Descending")
    while True:
        try:
            choice = int(input("\nEnter Choice: "))
            if choice <= 0:
                print("Invalid input. Enter a number greater than 0.")
            elif choice > 2:
                print("Enter a number within range.")
            else:
                break
        except ValueError:
            print("Enter a number.")
        except Exception as e:
            print(f"Error: '{e}'")
    clear_screen()

    if choice == 1:
        sorted_price = {k: v for k, v in sorted(collection.items(), key=lambda item: item[1]['price'])}
        print("\nSorted Collection:")
        for card_name,details in sorted_price.items():
            print(f"{card_name} | PSA: {details['psa']} | Price: ${details['price']:,.2f}")
    if choice == 2:
        sorted_price = {k: v for k, v in sorted(collection.items(), key=lambda item: item[1]['price'], reverse = True)}
        print("\nSorted Collection:")
        for card_name,details in sorted_price.items():
            print(f"{card_name} | PSA: {details['psa']} | Price: ${details['price']:,.2f}")

#       psa rating
def sort_rating():
    collection = load_dict()
    print("\nSort by:")
    print("1. Ascending")
    print("2. Descending")
    while True:
        try:
            choice = int(input("\nEnter Choice: "))
            if choice <= 0:
                print("Invalid input. Enter a number greater than 0.")
            elif choice > 2:
                print("Enter a number within range.")
            else:
                break
        except ValueError:
            print("Enter a number.")
        except Exception as e:
            print(f"Error: '{e}'")
    clear_screen()

    if choice == 1:
        sorted_rating = {k: v for k, v in sorted(collection.items(), key=lambda item: item[1]['psa'])}
        print("\nSorted Collection:")
        for card_name,details in sorted_rating.items():
            print(f"{card_name} | PSA: {details['psa']} | Price: ${details['price']:,.2f}")
    if choice == 2:
        sorted_rating = {k: v for k, v in sorted(collection.items(), key=lambda item: item[1]['psa'], reverse = True)}
        print("\nSorted Collection:")
        for card_name,details in sorted_rating.items():
            print(f"{card_name} | PSA: {details['psa']} | Price: ${details['price']:,.2f}")

#   sort collection
def sort_collection():
    print("Sort by:")
    print("1. Price")
    print("2. PSA")
    while True:
        try:
            choice = int(input("\nEnter Choice: "))
            if choice <= 0:
                print("Invalid input. Enter a number greater than 0.")
            elif choice > 2:
                print("Enter a number within range.")
            else:
                break
        except ValueError:
            print("Enter a number.")
        except Exception as e:
            print(f"Error: '{e}'")

    if choice == 1:
        clear_screen()
        sort_price()
    if choice == 2:
        clear_screen()
        sort_rating()

#   most / least expensive card- calls most / least expensive card name, psa rating, and price (use array)
def most_least_expensive():
    collection = load_array()
    most_expensive = max(collection, key=lambda x: x[2])
    least_expensive = min(collection, key=lambda x: x[2])
    most_expensive_card_name = most_expensive[0]
    least_expensive_card_name = least_expensive[0]
    most_expensive_card_psa = most_expensive[1]
    least_expensive_card_psa = least_expensive[1]
    most_expensive_card_price = most_expensive[2]
    least_expensive_card_price = least_expensive[2]

    print(f"Most Expensive Card: {most_expensive_card_name} | {most_expensive_card_psa} | ${most_expensive_card_price:,.2f}")
    print(f"Least Expensive Card: {least_expensive_card_name} | {least_expensive_card_psa} | ${least_expensive_card_price:,.2f}")

#   calculate whole collection worth- total amount for whole collection (use array)
def calculate_collection():
    collection = load_array()

    print(f"Total Worth of Collection: ${sum(x[2] for x in collection):,.2f}")

# make menu to add card, view collection, change card rating, change price of card, most exp card,
# least exp card, sort cards and delete card
def menu():
    while True:
        print("1. Generate Collection")
        print("2. View Collection")
        print("3. Add Card")
        print("4. Delete Card")
        print("5. Change Card Price")
        print("6. Sort Collection")
        print("7. Most / Least Expensive Card")
        print("8. Calculate Collection")
        print("9. Quit Application")
        while True:
            try:
                choice = int(input("\nChoose option (1-9): "))
                if 1 > choice > 9:
                    print("Invalid choice.")
                else:
                    break
            except ValueError:
                print("Enter a number.")
            except Exception as e:
                print(f"Error: '{e}'")
        clear_screen()
        print()
        if choice == 1:
            generate_cards()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 2:
            view_collection()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 3:
            add_card()
            refresh = input("Press Enter to go back to main menu.")
            clear_screen()
        if choice == 4:
            delete_card()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 5:
            change_price()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 6:
            sort_collection()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 7:
            most_least_expensive()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 8:
            calculate_collection()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 9:
            print("Thank you for using this tool!")
            break

if __name__ == "__main__":
    menu()
