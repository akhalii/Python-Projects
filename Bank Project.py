#Constants
MIN_BALANCE = 0.00
OVERDRAFT_FEE = 35.00

#Check balance
def check_balance(balance):
    print(f"\nBalance: ${balance:,.2f}\n")

#Deposits
def deposit():
    deposit_amount = float(input("\nHow much would you like to deposit? "))
    if deposit_amount < 0.00:
        print("That is not a valid amount!")
        return 0
    else:
        return deposit_amount

#Withdraws
def withdraw():
    withdraw_amount = float(input("\nHow much would you like to withdraw? "))
    if withdraw_amount < 0.00:
        print("That is not a valid amount!")
        return 0
    else:
        return withdraw_amount

#Quit
def exit_app():
    quit()

#Display Menu
def display_menu():
    min_balance = MIN_BALANCE
    overdraft_fee = OVERDRAFT_FEE
    balance = 0.00
    is_running = True

    while is_running:
        choice = int(input("1. Check Balance\n"
                           "2. Deposit\n"
                           "3. Withdraw\n"
                           "4. Quit\n"
                           "Enter an option (1-4): "))
        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            balance += deposit()
            print(f"\nBalance: ${balance:,.2f}\n")
        elif choice == 3:
            balance -= withdraw()
            if balance < min_balance:
                balance -= overdraft_fee
                print(f"\nYou occurred a $35 overdraft fee!\n"
                      f"Balance: ${balance:,.2f}\n")
            else:
                print(f"\nBalance: ${balance:,.2f}\n")
        elif choice == 4:
            exit_app()

display_menu()
