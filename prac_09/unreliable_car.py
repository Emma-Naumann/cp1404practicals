from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""
    def __init__(self, reliability, **kwargs):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Generate a random number between 0 and 100, and drive the car if number is less than reliability."""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
