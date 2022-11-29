from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.50

    def __init__(self, fanciness: float, **kwargs):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(**kwargs)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation of SilverServiceTaxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()
