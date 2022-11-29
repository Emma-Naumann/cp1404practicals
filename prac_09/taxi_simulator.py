"""
Taxi Simulator
"""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive \n>>> "


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2),
             SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    current_taxi = None
    total_fare = 0.00

    print("Let's drive!")
    menu_choice = input(MENU).lower()
    while menu_choice != "q":
        if menu_choice == "c":
            display_taxis("Taxis available:", taxis)
            current_taxi = get_valid_taxi(taxis)
        elif menu_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                distance_driven = current_taxi.drive(distance)
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
                total_fare += current_taxi.get_fare()
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_fare:.2f}")
        menu_choice = input(MENU).lower()
    print(f"Total trip cost: {total_fare:.2f}")
    display_taxis("Taxis are now:", taxis)


def get_valid_taxi(taxis):
    taxi_choice = int(input("Choose taxi: "))
    if taxi_choice < 0 or taxi_choice > (len(taxis) - 1):
        print(f"Invalid option, choice must be between 0 and {len(taxis) - 1}")
        return None
    return taxis[taxi_choice]


def display_taxis(message, taxis):
    print(message)
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi.__str__()}")


main()
