from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.properties import ObjectProperty
from kivy.clock import Clock


class Game(Widget):
    def animate_hint_icon(self):
        pass

    def animate_y(self, *args):
        wid = ObjectProperty(None)
        anim = Animation(pos=(self.center_x - 65, self.center_y + 70))
        anim.start(wid)

class Main(App):
    def on_start(self):
        Clock.schedule_interval(Game.animate_y, 2)


Main().run()

