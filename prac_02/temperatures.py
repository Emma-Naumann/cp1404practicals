"""
CP1404 - Practical 2
Temperature conversion
"""

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"


def main():
    """Convert temperature between celsius and fahrenheit, until user quits."""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print_temperature_fahrenheit(fahrenheit)
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print_temperature_celsius(celsius)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def print_temperature_celsius(celsius):
    """Print converted temperature in celsius."""
    print(f"Result: {celsius:.2f} C")


def print_temperature_fahrenheit(fahrenheit):
    """Print converted temperature in fahrenheit."""
    print("Result: {:.2f} F".format(fahrenheit))


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


main()
