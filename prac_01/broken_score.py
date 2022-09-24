"""
CP1404 - Practical 1
Broken program to determine score status
"""


score = float(input("Enter score: "))
while score < 0 or score > 100:
    print("Invalid score. Try again.")
    score = int(input("Enter score: "))
if score < 50:
    message = "bad"
elif score < 90:
    message = "passable"
else:
    message = "excellent"
print(f"A score of {score} is {message}.")
