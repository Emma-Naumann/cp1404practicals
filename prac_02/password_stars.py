"""
NAUMANN, Emma - Prac 02

Password check program

Program asks user for a password, with error checking to repeat if the password doesn't meet a
minimum length set by a variable. The program should then print asterisks as long as the word.
"""


def main():
    """Print a length of asterisks to match a valid password length."""
    minimum_length = int(input("Minimum character length: "))
    password = get_password(minimum_length)
    print_asterisks(password)


def print_asterisks(password):
    """Print the password length of asterisks."""
    print('*' * len(password))


def get_password(minimum_length):
    """Get a valid password."""
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Invalid number of characters. Try again.")
        password = input("Password: ")
    return password


main()
