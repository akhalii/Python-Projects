#Toolbox

#Bank System

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

#_______________________________________________________________________________

#Adding numbers
def add(a, b):
    return a + b

#Subtracting numbers
def subtract(a, b):
    return a - b

#Multiplying numbers
def multiply(a, b):
    return a * b

#Dividing numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

#Running all functions
def main():
    x = 10
    y = 5
    print(f"Addition: {add(x, y)}")
    print(f"Subtraction: {subtract(x, y)}")
    print(f"Multiply: {multiply(x, y)}")
    print(f"Divide: {divide(x, y)}")

#_______________________________________________________________________________

#Gets Employee Data
def get_employee_data():
    name = input("Enter name: ")
    hours_worked = float(input("Hours worked: "))
    hourly_wage = float(input("Hourly wage: "))

    return name, hours_worked, hourly_wage

#Calculates Payroll
def calculate_payroll(hours_worked, hourly_wage):
    if hours_worked > 40:
        overtime = ((hours_worked - 40) * 1.5) + 40

        total_pay = overtime * hourly_wage
        return total_pay
    elif hours_worked <= 40 and hours_worked > 0:
        total_pay = hours_worked * hourly_wage
        return total_pay

#Displays Pay
def display_employee_pay(name, total_pay):
    print(f"Name: {name}")
    print(f"Pay: {total_pay:,.2f}")

#Gets Order Data
def get_order_data():
    name = input("Enter name: ")
    order_total = float(input("How much was your order? "))

    return name, order_total

#Calculates Order Discount
def calculate_discount(order_total):
    if order_total <= 500:
        return order_total
    elif order_total > 500:
        discounted_amount = order_total * .9
        return discounted_amount

#Displays Order Summary
def display_order_summary(customer_name, original_total, discounted_total):
    print(f"Name: {customer_name}")
    print(f"Original order total: {original_total}")
    print(f"Discounted order total: {discounted_total}")

#Get Monthly Revenue and Expenses
def get_monthly_data():
    monthly_revenue = float(input("Monthly Revenue? "))
    monthly_expenses = float(input("Monthly Expenses? "))

    return monthly_revenue, monthly_expenses

#Calculates Net Profit or Net Loss
def calculate_profit_or_loss(revenue, expenses):
    profit = revenue - expenses

    return profit

#Displays Net Profit or Net Loss Summary
def display_profit_summary(profit):
    if profit < 0:
        difference = profit * -1
        
        print(f"Net Loss: {profit:,.2f}")
        print(f"Difference: {difference:,.2f}")
        
    elif profit > 0:
        print(f"Net Profit: {profit:,.2f}")
        print(f"Difference: {profit:,.2f}")

#Menu
def display_menu():
    print("1. Payroll Calculator")
    print("2. Customer Orders Processor")
    print("3. Monthly Profit Calculator")
    print("4. Exit")

    choice = int(input("Enter a number (1-4): "))

    return choice

#Processes Menu Choice
def process_menu_choice(choice):

    if choice == 1:
        print()
        name, hours_worked, hourly_wage = get_employee_data()
        total_pay = calculate_payroll(hours_worked, hourly_wage)

        print()
        display_employee_pay(name, total_pay)
            
    elif choice == 2:
        print()
        name, order_total = get_order_data()
        discounted_total = calculate_discount(order_total)

        print()
        display_order_summary(name, order_total, discounted_total)
    elif choice == 3:
        print()
        monthly_revenue, monthly_expenses = get_monthly_data()
        profit = calculate_profit_or_loss(monthly_revenue, monthly_expenses)

        print()
        display_profit_summary(profit)
    
#Main
def main():
    while True:
        print()
        choice = display_menu()
        process_menu_choice(choice)

        if choice == 4:
            break

if __name__ == "__main__":
    main()