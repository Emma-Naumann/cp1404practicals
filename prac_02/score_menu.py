"""
Emma Naumann - Practical 2
Python program which follows the standard structure that uses a main and other functions.
"""


def main():
    """Print result or number of stars based on valid score."""
    score = get_valid_score()
    choice = input("Menu:\n(R)esult \n(S)tars \n(Q)uit \n> ").upper()
    while choice != "Q":
        if choice == "R":
            score_message = determine_score_category(score)
            print(f"A score of {score} is {score_message}.")
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        choice = input("Menu:\n(R)esult \n(S)tars \n(Q)uit \n> ").upper()
    print("Farewell")


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score. Try again.")
        score = int(input("Score: "))
    return score


def determine_score_category(score):
    """Determine the category of a valid score."""
    if score < 50:
        message = "bad"
    elif score < 90:
        message = "passable"
    else:
        message = "excellent"
    return message


def print_stars(score):
    """Print the score number of asterisks."""
    print('*' * score)


main()
