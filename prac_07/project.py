"""
Emma Naumann
CP1404 Practical 7
Do from scratch exercises - project management program

Class program
"""


class Project:
    """Project class for storing details of a project."""

    def __init__(self, name="", start_date=0, priority=0, cost=0, completion_percentage=0):
        """Initialise a Guitar."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation of a Project."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost}," \
               f"completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """Less than, used for sorting Projects by priority."""
        return self.priority < other.priority
