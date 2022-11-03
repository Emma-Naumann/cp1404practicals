"""
Emma Naumann
CP1404 Practical 6 - Do from scratch exercises
Guitars! testing program
"""

from guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
other = Guitar("Another Guitar", 2013, 1000)


def run_tests():
    print(f"{guitar.name} get_age() - Expected 100. Got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected 9. Got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage()}")


run_tests()
