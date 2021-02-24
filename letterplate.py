from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import ObjectProperty, ListProperty, NumericProperty


class LetterPlate(Widget):
    plate_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.plate_texture = Image(source='letter_plate.png').texture
