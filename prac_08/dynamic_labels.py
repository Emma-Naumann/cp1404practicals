"""
Dynamic Labels Do From Scratch Exercise
Emma Naumann
CP1404 Practical 8
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    """Kivy app containing basic dynamic widget creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Emma", "Chloe", "Bob", "Freddie"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from list and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicWidgetsApp().run()
