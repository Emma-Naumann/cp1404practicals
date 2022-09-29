"""
Emma Naumann
CP1404 Practical 3
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid input. Try again!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Question Answers
# 1. A ValueError will occur when either numerator or denominator is a string.

# 2. A ZeroDivisionError occurs when denominator = 0.

# 3. Use an error-checking pattern for the denominator to ask for input until != 0.


