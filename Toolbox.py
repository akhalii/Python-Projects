# Toolbox
#_______________________________________________________________________________

# Enter Positive Number only
while True:
    try:
        choice = int(input("Prompt"))
        if choice <= 0:
            print("Enter a number greater than 0.")
        else:
            break
    except ValueError:
        print("Enter a number.")

# Bank System

# Constants
MIN_BALANCE = 0.00
OVERDRAFT_FEE = 35.00

# Check balance
def check_balance(balance):
    print(f"\nBalance: ${balance:,.2f}\n")

# Deposits
def deposit():
    deposit_amount = float(input("\nHow much would you like to deposit? "))
    if deposit_amount < 0.00:
        print("That is not a valid amount!")
        return 0
    else:
        return deposit_amount

# Withdraws
def withdraw():
    withdraw_amount = float(input("\nHow much would you like to withdraw? "))
    if withdraw_amount < 0.00:
        print("That is not a valid amount!")
        return 0
    else:
        return withdraw_amount

# Quit
def exit_app():
    quit()

# Display Menu
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

# basic math

# Adding numbers
def add(a, b):
    return a + b

# Subtracting numbers
def subtract(a, b):
    return a - b

# Multiplying numbers
def multiply(a, b):
    return a * b

# Dividing numbers
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# Running all functions
def display():
    x = 10
    y = 5
    print(f"Addition: {add(x, y)}")
    print(f"Subtraction: {subtract(x, y)}")
    print(f"Multiply: {multiply(x, y)}")
    print(f"Divide: {divide(x, y)}")

#_______________________________________________________________________________

# how to do menus

# Gets Employee Data
def get_employee_data():
    name = input("Enter name: ")
    hours_worked = float(input("Hours worked: "))
    hourly_wage = float(input("Hourly wage: "))

    return name, hours_worked, hourly_wage

# Calculates Payroll
def calculate_payroll(hours_worked, hourly_wage):
    if hours_worked > 40:
        overtime = ((hours_worked - 40) * 1.5) + 40

        total_pay = overtime * hourly_wage
        return total_pay
    elif hours_worked <= 40 and hours_worked > 0:
        total_pay = hours_worked * hourly_wage
        return total_pay

# Displays Pay
def display_employee_pay(name, total_pay):
    print(f"Name: {name}")
    print(f"Pay: {total_pay:,.2f}")

# Gets Order Data
def get_order_data():
    name = input("Enter name: ")
    order_total = float(input("How much was your order? "))

    return name, order_total

# Calculates Order Discount
def calculate_discount(order_total):
    if order_total <= 500:
        return order_total
    elif order_total > 500:
        discounted_amount = order_total * .9
        return discounted_amount

# Displays Order Summary
def display_order_summary(customer_name, original_total, discounted_total):
    print(f"Name: {customer_name}")
    print(f"Original order total: {original_total}")
    print(f"Discounted order total: {discounted_total}")

# Get Monthly Revenue and Expenses
def get_monthly_data():
    monthly_revenue = float(input("Monthly Revenue? "))
    monthly_expenses = float(input("Monthly Expenses? "))

    return monthly_revenue, monthly_expenses

# Calculates Net Profit or Net Loss
def calculate_profit_or_loss(revenue, expenses):
    profit = revenue - expenses

    return profit

# Displays Net Profit or Net Loss Summary
def display_profit_summary(profit):
    if profit < 0:
        difference = profit * -1
        
        print(f"Net Loss: {profit:,.2f}")
        print(f"Difference: {difference:,.2f}")
        
    elif profit > 0:
        print(f"Net Profit: {profit:,.2f}")
        print(f"Difference: {profit:,.2f}")

# Menu
def display_menu():
    print("1. Payroll Calculator")
    print("2. Customer Orders Processor")
    print("3. Monthly Profit Calculator")
    print("4. Exit")

    choice = int(input("Enter a number (1-4): "))

    return choice

# Processes Menu Choice
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
    
# Main
def show_code():
    while True:
        print()
        choice = display_menu()
        process_menu_choice(choice)

        if choice == 4:
            break

#_______________________________________________________________________________

# method return and catch

def multiply(a,b,c):
    return a*b, c #if returning 2
    
def sdjkafljewiof():
    multiple2, multiple3 = multiply(1,2,3) #catch 2
    
#_______________________________________________________________________________

# files

file = open("example.txt", "r") #open("file name", "r or w or a") (r = read, w = write, a = append)

file.close() # closes file

# write file
with open("example.txt", "w") as file:
    file.write("hello world\n")
    file.write("this is a test\n")

# appends (add text) file
with open("example.txt", "a") as file:
    file.write("fjdkslfjdsk")
    
# reads file (prints it)
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip()) # .strip() deletes blank lines

# error handle
except FileNotFoundError:
    print(f"Error: '{input_file}' not found.")
except Exception as e:
    print(f"An error occured: {e}")

#_______________________________________________________________________________

# arrays, tuples, and matrixes

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

list1[0] = 30 # changes position of item to another item
list1.append(10) # adds to array
list1.insert(0, "pizza") # inserts into the position in array
del list1[0] # deletes item in that position in array
list1.remove("pizza") # removes item from array
list1.pop(0) # pull item out of array

for x in list1:   # lists all items in array
    print(x)

# lists items in array
for x, items in enumerate(list1, start=1):
    print(x, items)

combined = list1 + list2 # adds two arrays
print(combined)

combined = (list1 * 3) # multiplies array by number
print(combined)

combined.reverse() # flips it array
print(combined)

combined.sort() # sorts array
print(combined)

squares = [x%2 for x in range(50)] # math function in array
print(squares)

my_tuple = (1,2,3) # tuple is a constant, but same commands as arrays
print (my_tuple[0])
print (my_tuple[-1])

array = [1,2,3]

matrix = [  # contains multiple arrays
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print (matrix[1][1]) # prints specific item in matrix

for array in matrix:    # makes a board
    for x in array:
        print(x, end=" ")
    print()

numbers = [10,20,30]

print(sum(numbers)) # sums up all items in array
print(min(numbers)) # prints smallest number
print(max(numbers)) # prints largest number
print(len(numbers)) # prints how many items in array

# x[1] is referring to second element
max(x[1] for x in list) # largest second element in tuple 
min(x[1] for x in list) # smallest second element in tuple
list.sort(key=lambda x: x[1], reverse = True) # sort tuple in descending order accorcing to second element

# adds items in .txt file into tuple and splits into two elements
list_of_students = []
with open("grades.txt", "r") as file:
    for line in file:
        parts = line.strip().split(': ')
        if len(parts) == 2:
            student, grade = parts
            list_of_students.append((student, int(grade)))

#_______________________________________________________________________________

# Clear screen
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#_______________________________________________________________________________

messy_string = "       Hello!          ,          World        "

print(messy_string)
print(messy_string.strip()) # strips blanks
print(messy_string.lstrip()) # strips blanks left of element
print(messy_string.rstrip()) # strips blanks right of element

first_name = "Kha"
last_name = "Nguyen"

full_name = first_name + " " + last_name
print(full_name)

print(full_name.lower()) # lower cases all characters
print(full_name.upper()) # CAPS all characters

password = "Secure123"

print(password.isalpha()) # checks if there is alphabets
print(password.isdigit()) # checks if there is digits
print(password.isalnum()) # checks if there is alphabets and digits
print(password.isupper()) # checks if there is upper case
print(password.islower()) # checks if there is lower case

phrase = "Python Programming"

print(phrase[:6]) # prints 6 letters to the right
print(phrase[7:]) # prints 7 letters to the left
print(phrase[:-11]) # prints 11 letters to the left

csv_data = "Python,Java,C++,Javascript"
languages = csv_data.split(",")
print(languages)

separator = ", "
print(separator.join(languages))

#_______________________________________________________________________________

# Dictionaries

phonebook = {'Chris': '555-1111',
             'Katie': '555-2222',
             'Joanne': '555-3333'}

print(phonebook['Chris']) # output: 555-1111

key = 'Unknown'
if key in phonebook:
    print(phonebook[key]) # read
else:
    print("Key not found.")

phonebook['Joe'] = '555-4444' # adds to dictionary if there is no key
phonebook['Chris']  = '555-9999' # changes second element
del phonebook['Katie'] # deletes all Katie
removed = phonebook.pop('Chris', 'Not Found')
print(removed) # pop

for key in phonebook: # lists all keys
    print(key)

for value in phonebook.values(): # lists all values
    print(value)

for key, value in phonebook.items(): # lists all keys and values in item
    print(f"{key}: {value}")

squares = {x: x**2 for x in range(5)}

for key, value in squares.items(): # math
    print(f"{key},{value}")

#_______________________________________________________________________________

# encrypt and decrypt file
def encrypt_file(input_file, output_file, shift):
    try:
        with open(file_name, 'r') as input_file:
            text = input_file.read()

        encrypted_text = ' '

        for char in text:
            encrypted_text += chr((ord(char) + shift) % 256)

        with open(output_file, 'w') as output_file:
            output_file.write(encrypted_text)

        print(f"File '{input_file}' successfully encrypted as '{output_file}'!")
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    input_file = input("Enter the name of file to encrypt: ")
    output_file = input("Enter name of output file: ")
    shift = int(input("Enter name of shifts (+ or -): "))

    encrypt_file(input_file, output_file, shift)

def decrypt_file(input_file, shift):
    try:
        with open(file_name, 'r') as input_file:
            encrypted_text = input_file.read()

        decrypted_text = ' '

        for char in encrypted_text:
            decrypted_text += chr((ord(char) - shift) % 256)

        print(f"Decrypted Message:")
        print(decrypted_text)
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    input_file = input("Enter the name of file to decrypt: ")
    shift = int(input("Enter number of shifts (+ or -): "))

    decrypt_file(input_file, shift)
