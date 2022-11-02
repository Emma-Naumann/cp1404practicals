"""
Emma Naumann
CP1404 Practical 6
Intermediate Exercises - Programming Language

Estimated: 40 minutes (12:22pm)
Actual: 25 minutes (12:47pm)
"""


class ProgrammingLanguage:
    """Store information about programming languages."""

    def __init__(self, name, typing, reflection, year):
        """Create a ProgrammingLanguage from the given parameters."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    # needs no parameters since information stored in object
    def is_dynamic(self):
        """Determine if programming language is dynamically typed."""
        return self.typing == "Dynamic"
