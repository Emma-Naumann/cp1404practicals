"""
Emma Naumann
CP1404 Practical 3
Random Numbers
"""


# print(random.randint(5, 20))  # line 1
# 10
# 19
# 15
# The smallest: 5
# The largest: 20
# This is because randint is inclusive of endpoints


# print(random.randrange(3, 10, 2))  # line 2
# 7
# 3
# 7
# Smallest: 3
# Largest: 9
# This is because randrange is not inclusive of endpoint values
# Line 2 could NOT produce a 4 since it is in steps of 2


# print(random.uniform(2.5, 5.5))  # line 3
# 4.081339707464739
# 4.411321462618175
# 2.8927198542641888
# Smallest: 2.5
# Largest: 5.5 (largest number exclusive, but could be inclusive depending on rounding)


# produce a random number between 1 and 100 inclusive
import random
print(random.randint(1, 100))
