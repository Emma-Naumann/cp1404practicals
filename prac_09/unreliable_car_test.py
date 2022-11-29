from prac_09.unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar(name="Unreliable", fuel=100, reliability=10)
    reliable_car = UnreliableCar(name="Reliable", fuel=100, reliability=80)

    # do multiple tests
    for i in range(1, 11):
        print(unreliable_car)
        print(f"The unreliable car drove: {unreliable_car.drive(distance=i)}km")

        print(reliable_car)
        print(f"The reliable car drove: {reliable_car.drive(distance=i)}km")


main()
