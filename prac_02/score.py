"""
CP1404 - Practical 2
Program to determine score status
"""
import random


def main():
    """Print the category of a user score and random score."""
    user_score = float(input("Enter score: "))
    while user_score < 0 or user_score > 100:
        print("Invalid score. Try again.")
        user_score = int(input("Enter score: "))
    user_score_message = determine_score_category(user_score)
    print(f"A score of {user_score} is {user_score_message}.")

    random_score = random.randint(0, 100)
    random_score_message = determine_score_category(random_score)
    print(f"A score of {random_score} is {random_score_message}.")


def determine_score_category(score):
    """Determine the category of a score."""
    if score < 50:
        message = "bad"
    elif score < 90:
        message = "passable"
    else:
        message = "excellent"
    return message


main()
