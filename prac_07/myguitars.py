"""
Emma Naumann
CP1404 Practical 7 - Intermediate exercises
More guitars!
"""

import csv
from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Store guitar objects from a file in a list, then display their details."""
    guitars = []

    with open(FILENAME, "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            row[1] = int(row[1])  # safe to ignore type warning
            row[2] = float(row[2])  # safe to ignore type warning
            new_guitar = Guitar(row[0], row[1], row[2])
            new_guitar.year = int(new_guitar.year)
            guitars.append(new_guitar)
            print(f"{new_guitar.name} added.")

    display_guitars(guitars)
    add_guitars(guitars)

    with open(FILENAME, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def display_guitars(guitars):
    """Display formatted guitar details."""
    guitars.sort()
    print("These are the guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:30} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def add_guitars(guitars):
    """Add new user guitar to guitars list."""
    print("Now add your guitars to the list!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $ "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.")
        name = input("Name: ")


main()
