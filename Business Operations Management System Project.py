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
