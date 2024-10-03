def register_participant():

    # Handle event registration logic

    registars = 0

    name = input("Enter a name: ").lower()
    role = input("Enter a role: ").lower()
    registars +=1
    print()
    check_guest_list(name)
    validate_role(role)
    print()

    while registars <= 100:
        again = input("Would you like to register more (yes/no)? ").lower()
        if again == "yes":
            print()
            name = input("Enter a name: ").lower()
            role = input("Enter a role: ").lower()
            print()
            check_guest_list(name)
            validate_role(role)
            registars +=1
            print()
        else:
            break    



def validate_role(role):

    # Validate the role and prompt for re-entry if invalid

    student = 0
    faculty = 0
    guest = 0

    if role == "student":
        print(f"Valid {role}")
        student += 1
        return student
    elif role == "faculty":
        print(f"Valid {role}")
        faculty += 1
        return faculty
    elif role == "guest":
        print(f"Valid {role}")
        guest += 1
        return guest
    else:
        print("Invalid role. Enter a valid role.")

 

def check_guest_list(name):

    # Check if the guest is on the allowed list

    guest_list = "kha"

    if name == guest_list:
        print("You can register.")
    else:
        print("You can't register.")

 
register_participant()
def manage_capacity():

    # Manage registrations and stop once capacity is reached

    if student/registar > .75:
        print("This event is student-heavy")
    elif faculty/registar > .5:
        print("Faculty are showing strong interest")
    elif guest > 10:
        print("Expect additional guest services")



def greet_participant(name):

    # Provide custom greetings based on the participant's name

    pass

 

def send_thank_you(name, role, registration_days):

    # Send thank-you message based on conditions

    pass

 

def collect_event_data():

    # Collect and analyze attendance data

    pass

 

def display_registration_stats(student_count, faculty_count, guest_count):

    # Display final registration statistics

    pass

 

def main():

    # Call methods and move data between them

    manage_capacity()

    # Other function calls go here

    pass

 

if __name__ == "__main__":

    main()
