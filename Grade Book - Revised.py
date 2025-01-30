import random
import os

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def student_grades():
    grades = {}
    grades["Kha"] = f"{random.randint(0,100)}\n"

    with open("Grade Book.txt", "w") as file:
        for key,value in grades.items():
            file.write(f"{key},{value}")
    print("Grades Generated!")

def load_grades():
    grades = {}
    with open("Grade Book.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                key, value = parts
                grades[key] = value
    return grades

def display_grades():
    grades = load_grades()
    print("Grades:\n")
    for key,value in grades.items():
        print(f"{key}: {value}")

def new_grades():
    while True:
        student_name = input("Enter name: ")
        if not student_name.isalpha():
            print("Invalid input. Enter a name.")
        else:
            break
    while True:
        try:
            student_grade = int(input("Enter a grade: "))
            if 0 <= student_grade <= 100:
                break
            else:
                print("Enter a grade between 0 and 100.")
        except ValueError:
            print("Enter a number.")
        except Exception as e:
            print(f"Error: '{e}'")
    
    with open("Grade Book.txt", "a") as file:
        file.write(f"{student_name},{student_grade}\n")
    print("\nGrade entered successfully!\n")

def update_grades():
    grades = load_grades()

    for x, (student_name,student_grade) in enumerate(grades.items(), start= 1):
        print(f"{x}. {student_name}: {student_grade}")

    while True:
        try:
            choice = int(input("\nEnter Choice: "))
            if choice <= 0:
                print("Invalid input. Enter a number greater than 0.")
            elif choice > len(grades):
                print("Enter a number within range.")
            else:
                break
        except ValueError:
            print("Enter a number.")
        except Exception as e:
            print(f"Error: '{e}'")
    while True:
        try:
            new_grade = int(input("Enter new grade: "))
            if new_grade < 0:
                print("Invalid input. Enter a positive number.")
            elif new_grade > 100:
                print("Grade can't be more than 100.")
            else:
                break
        except ValueError:
            print("Enter a number.")
        except Exception as e:
            print(f"Error: '{e}'")

    grades[choice-1] = new_grade

    with open("Grade Book.txt", "w") as file:
        for student_name,student_grade in grades.items():
            file.write(f"{student_name},{student_grade}\n")

    print("\nGrade updated!")

def sort_grades():
    grades = load_grades()

    sorted_grades = {k: v for k, v in sorted(grades.items(), key=lambda item: item[1], reverse = True)}

    print("Sorted Grades:")
    for key,value in sorted_grades.items():
        print(f"{key}: {value}")

def highest_lowest_grades():
    grades = load_grades()
    
    print(f"Highest Grade: {max(grades, key = grades.get)} with {max(grades.values())}")
    print(f"Lowest Grade: {min(grades, key = grades.get)} with {min(grades.values())}")

def main_menu():
    while True:
        print()
        print("1. Initialize")
        print("2. View Grades")
        print("3. Add Grade")
        print("4. Update Grade")
        print("5. Sort Grades")
        print("6. Highest / Lowest Grades")
        print("7. Quit")
        print()

        while True:
            try:
                choice = int(input("Choose option (1-7): "))
                if choice < 1 or choice > 7:
                    print("Invalid choice.")
                else:
                    break
            except ValueError:
                print("Enter a number.")
            except Exception as e:
                print(f"Error: '{e}'")
            
        print()
        
        if choice == 1:
            student_grades()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 2:
            display_grades()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 3:
            new_grades()
            refresh = input("Press Enter to go back to main menu.")
            clear_screen()
        if choice == 4:
            update_grades()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 5:
            sort_grades()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 6:
            highest_lowest_grades()
            refresh = input("\nPress Enter to go back to main menu.")
            clear_screen()
        if choice == 7:
            print("Thank you for using this tool!")
            break
    
main_menu()
