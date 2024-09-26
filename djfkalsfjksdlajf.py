##def multiply_until_1000():
##    product = 0
##    while product < 1000:
##        try:
##            user_input = float(input("Enter a number: "))
##            product = user_input * 10
##            print (f"The product of {user_input} * 10 = {product}")
##        except ValueError:
##            print("Invalid input. Please enter a valid number.")
##
##def add_number():
##    while True:
##        try:
##            num1 = float(input("Enter a number: "))
##            num2 = float(input("Enter a number: "))
##            total = num1 + num2
##            print(f"The total of {num1} + {num2} = {total}")
##            again = input("Do you want to do more? (yes/no)\n").strip().lower()
##            if again != "yes":
##                break
##        except ValueError:
##            print("Invalid input. Please enter numbers.")
##
##def display_number():
##    for num in range(0,1001,10):
##        print(num, end=", ")
##
##def running_total():
##    total = 0
##    while True:
##        try:
##            num = float(input("Enter a number you want to add: "))
##            total += num
##            again = input("Do you want to enter more? (yes,no)\n")
##            if again != "yes":
##                print(f"Total: {total}")
##                break
##        except ValueError:
##            print("Invalid input. Please enter numbers.")
##
##def display_pattern():
##    for i in range(10):
##        for i in range(15):
##            print("#", end=" ")
##        print()
##
##def get_positive_non_input():
##    while True:
##        try:
##            user_input = float(input("Enter a positive non-zero number: "))
##            if user_input > 0:
##                return user_input
##            else:
##                print("Enter a number that is greater than 0.")
##        except ValueError:
##            print("Invalid input. Please enter numbers.")

def user_input():
    while True:
        try:
            days_collected = int(input("How many days have you been collecting bugs? "))
            if days_collected < 0:
                print("Please enter a postive number.")
            else:
                return days_collected

def collect_bugs(day_number):
    while True:
        try:
            bugs = int(input(f"Enter number of bugs collected on Day {day_number}: "))
            if bugs < 0:
                print("Please enter a non-negative.")
            else:
                return bugs
        except ValueError:
            print("Invalid input. Please enter numbers.")

def calculate_total_bugs():
    total = 0
    for day in range(1,6):
        bug_collected = collect_bugs(day)
        total += bug_collected
    return total

def main():
    print("Bug collecter program")
    total = calculate_total_bugs()
    print(f"Total bugs collected over five days: {total}")

main()
