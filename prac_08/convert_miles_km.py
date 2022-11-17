"""
CP1404 Practical
Kivy GUI program to convert miles to kilometres
Emma Naumann
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Emma Naumann'

MILES_TO_KM = 1.60934


class ConvertMilesToKilometresApp(App):
    """ConvertMilesToKilometres is a Kivy App for converting distance."""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation, output result to label widget."""
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """Handle increment by making input go up or down by 1."""
        value = self.get_valid_miles() + increment
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_valid_miles(self):
        """Get valid distance in miles from text input, return 0 if value error."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKilometresApp().run()
