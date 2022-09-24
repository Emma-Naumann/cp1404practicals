"""
NAUMANN, Emma - Prac 02
Program asks user for a password, with error checking to repeat if the password doesn't meet a
minimum length set by a variable. The program should then print asterisks as long as the word.
"""


def main():
    minimum_length = int(input("Minimum character length: "))
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


def get_password(minimum_length):
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Invalid number of characters. Try again.")
        password = input("Password: ")
    return password


main()
