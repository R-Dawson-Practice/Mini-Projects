## This could be improved by using a dict or struct for the password structure
## Instead of the while, maybe use recursion
## Create default password length if password_decission = 0

import sys
import random
import string
def password_generator(password_structure):
    letters = random.choices(string.ascii_letters, k=password_structure[0])
    symbols = random.choices("!@#$%^&*()-_=+[]{};:,.?/\\", k=password_structure[1])
    numbers = random.choices(string.digits, k=password_structure[2])
    password = letters + symbols + numbers
    random.shuffle(password)
    return "".join(password)

def password_decision():
    while(True):
        try:
            letter = input("How many letters in your password ").strip()
            symbols = input("How many symbols in your password ").strip()
            numbers = input("How many numbers in your password ").strip()
            letters_num = int(letter)
            symbols_num = int(symbols)
            numbers_num = int(numbers)
            if letters_num > 0 and symbols_num > 0 and numbers_num > 0:
                return [letters_num, symbols_num, numbers_num]
        except ValueError:
            print("Enter a number")
        except (KeyboardInterrupt, EOFError):
            print("\nEnd of program")
            sys.exit(0)

def display_password(password):
    password_string = ""
    for i in password:
        password_string += i
    print(password_string)
def main():
    password_structure = password_decision()
    password = password_generator(password_structure)
    display_password(password)
if __name__ == "__main__":
    main()