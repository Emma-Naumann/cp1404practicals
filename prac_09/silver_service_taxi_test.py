"""
CP1404 Practical 9
SilverServiceTaxi testing program
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    silver_service_taxi = SilverServiceTaxi(name="Fancy Taxi", fuel=150, fanciness=2)
    print(silver_service_taxi)
    silver_service_taxi.drive(distance=18)
    print(silver_service_taxi)
    print(f"{silver_service_taxi.get_fare()}")


main()
