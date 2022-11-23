from prac_09.musician import Musician


class Band(Musician):
    """Band class."""

    def __init__(self, band_name="", **kwargs):
        """Initialise a Band."""
        super().__init__(**kwargs)
        self.band_name = band_name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.band_name} ({[musician for musician in self.musicians]})"

    def __repr__(self):
        """Return a string representation of a Musician, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their first (or no) instrument."""
        for musician in self.musicians:
            super().play()

