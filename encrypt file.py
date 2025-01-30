def encrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, 'r') as input_file:
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
        with open(input_name, 'r') as input_file:
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
