"""
CP1404 - Practical 1
Loops
"""

# odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# part a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# part b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# part c
number_stars = int(input("Number of stars: "))
for number in range(number_stars):
    print('*', end=' ')
print()

# part d
for number in range(1, number_stars + 1):
    print(number * '*')
print()
