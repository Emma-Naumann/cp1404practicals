"""
Emma Naumann
CP1404 Practical 5
Hexadecimal colour codes in a dictionary
"""

NAME_TO_CODE = {"aliceblue": "#f0f8ff", "amaranth": "#e52b50", "amethyst": "#9966cc", "aqua": "#00ffff",
                "aquamarine4": "#458b74", "baby pink": "#f4c2c2", "bittersweet": "#fe6f5e", "black": "#000000",
                "blue2": "#0000ee", "boysenberry": "#873260"}
print(NAME_TO_CODE)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"The colour {colour_name} has hexadecimal code {NAME_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name. Try again.")
    colour_name = input("Enter colour name: ").lower()
