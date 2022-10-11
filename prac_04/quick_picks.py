"""
Emma Naumann
CP1404 Practical 4
"Quick Pick" Lottery Ticket Generator
"""

import random

MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6


def main():
    """Generates a number or random quick picks dependent on user input."""
    number_quick_picks = int(input("Number of quick picks: "))
    while number_quick_picks < 0:
        print("Invalid number of quick picks. Try again.")
        number_quick_picks = int(input("Number quick picks: "))
    display_quick_picks(number_quick_picks)


def display_quick_picks(number_quick_picks):
    """Display each random quick pick with formatting."""
    for i in range(number_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()
