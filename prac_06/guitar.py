"""
Emma Naumann
CP1404 Practical 6 - Do from scratch exercises
Guitars!

Estimated: 40 minutes (2:06 pm)
Actual: 40 minutes (2:46pm)
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing details of a guitar."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Calculate guitar age in years using CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage based on VINTAGE_AGE."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars by year."""
        return self.year < other.year
