"""
NAUMANN, Emma - Prac 02
Program asks user for a password, with error checking to repeat if the password doesn't meet a
minimum length set by a variable. The program should then print asterisks as long as the word.
"""

minimum_length = int(input("Minimum character length: "))
password = input("Password: ")
while len(password) < minimum_length:
    print("Invalid number of characters. Try again.")
    password = input("Password: ")
print('*' * len(password))
