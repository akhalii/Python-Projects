class Toolbox:
    # \n = new line
    # \t = tab

    # f-strings
    def f_strings():
        money = 123,123.123
        {money:.2f} # rounding precision
        {money:,} # comma separator
        {money:,.2f} # comma separator with precision
        {money:%} # percentage
        {money:.0%} # percentage with precision
        {money:e} # scientific notation
        {money:E} # scientific notation, uppercase
        {money:.2e} # scientific notation with precision
        {money:d} # integer (the book also lists D, but Python rejects it)
        {money:,d} # integer with commas
        {money:10} # field width
        {money:<10} # left-align
        {money:>10} # right-align
        {money:^10} # center-align

    def testing_methods():
        word = "    hi    "
        word.isalnum()
        word.isalpha()
        word.isdigit()
        word.islower()
        word.isspace()
        word.isupper()
    def mod_methods():
        word = "    hi    "
        word.lower()
        word.upper()
        word.lstrip()
        word.lstrip(" ")
        word.rstrip()
        word.rstrip(" ")
        word.strip()
        word.strip(" ")

    # positive number only error handling
    def pos_num():
        while True:
            try:
                choice = int(input("Prompt"))
                if choice <= 0:
                    print("Enter a number greater than 0.")
                else:
                    break
            except ValueError:
                print("Enter a number.")
    
    # input output error handling
    def io_error():
        while True:
            try:
                choice = int(input("Prompt"))
                if choice <= 0:
                    print("Enter a number greater than 0.")
                else:
                    break
            except IOError:
                print("Input/Output Error.")
            except ValueError:
                print("Enter a number.")
    
    # zero division error handling
    def zero_division():
        while True:
            try:
                x = 5/0
                break
            except ZeroDivisionError:
                print("Can't divide by 0.")

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

    # method return and catch

    def multiply(a,b,c):
        return a*b, c #if returning 2

    def sdjkafljewiof():
        multiple2, multiple3 = multiply(1,2,3) #catch 2

    # files

    def write_file():
        with open("example.txt", "w") as file:
            file.write("hello world\n")
            file.write("this is a test\n")

    def append_file():
        with open("example.txt", "a") as file:
            file.write("fjdkslfjdsk")

    def read_file():
        with open("example.txt", "r") as file:
            for line in file:
                print(line.strip()) # .strip() deletes blank lines

    def file_error_handle():
        except FileNotFoundError:
            print(f"Error: '{input_file}' not found.")
        except Exception as e:
            print(f"An error occured: {e}")

    # import os first
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

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

    def encrypt():
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

    def decrypt():
        input_file = input("Enter the name of file to decrypt: ")
        shift = int(input("Enter number of shifts (+ or -): "))

        decrypt_file(input_file, shift)

    def lists():
        # lists, arrays, tuples, and matrixes

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
    
    def dictionaries():
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