from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, ListProperty
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.config import Config
from random import randint, sample
from letterplate import LetterPlate
from kivy.graphics import Color, Ellipse, Line
from game import Game

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')


game = Game()


class Return:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    def game(self):
        return game


print(game.valid_entries)
print(game.random_string_for_level)
print(game.level_data['required entries'])
print(game.number_of_letter_blocks)


class LetterBlock0(Widget):                                                                  # letter block classes
    letter_block_texture0 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.letter_block_texture0 = Image(source=game.random_string_for_level[0] + '.png').texture

    # defining touch interactions
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            game.user_answer.append(game.random_string_for_level[0])
            game.level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(game.user_answer).lower() in game.valid_entries:
                if ''.join(game.user_answer) not in game.unscrambled_words:
                    print('correct entry: ' + ''.join(game.user_answer))
                    game.unscrambled_words.append(''.join(game.user_answer))
                game.user_answer.clear()
            elif ''.join(game.user_answer).lower() not in game.valid_entries and len(game.user_answer) > 0:
                print('incorrect')
                game.user_answer.clear()


class LetterBlock1(Widget):
    letter_block_texture1 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.letter_block_texture1 = Image(source=game.random_string_for_level[1] + '.png').texture

    # defining touch interactions
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            game.user_answer.append(game.random_string_for_level[1])
            game.level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(game.user_answer).lower() in game.valid_entries:
                if ''.join(game.user_answer) not in game.unscrambled_words:
                    print('correct entry: ' + ''.join(game.user_answer))
                    game.unscrambled_words.append(''.join(game.user_answer))
                game.user_answer.clear()
            elif ''.join(game.user_answer).lower() not in game.valid_entries and len(game.user_answer) > 0:
                print('incorrect')
                game.user_answer.clear()


class LetterBlock2(Widget):
    letter_block_texture2 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 3:
            self.letter_block_texture2 = Image(source=game.random_string_for_level[2] + '.png').texture

    # defining touch interactions
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            game.user_answer.append(game.random_string_for_level[2])
            game.level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(game.user_answer).lower() in game.valid_entries:
                if ''.join(game.user_answer) not in game.unscrambled_words:
                    print('correct entry: ' + ''.join(game.user_answer))
                    game.unscrambled_words.append(''.join(game.user_answer))
                game.user_answer.clear()
            elif ''.join(game.user_answer).lower() not in game.valid_entries and len(game.user_answer) > 0:
                print('incorrect')
                game.user_answer.clear()


class LetterBlock3(Widget):
    letter_block_texture3 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 4:
            self.letter_block_texture3 = Image(source=game.random_string_for_level[3] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            game.user_answer.append(game.random_string_for_level[3])
            game.level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(game.user_answer).lower() in game.valid_entries:
                if ''.join(game.user_answer) not in game.unscrambled_words:
                    print('correct entry: ' + ''.join(game.user_answer))
                    game.unscrambled_words.append(''.join(game.user_answer))
                game.user_answer.clear()
            elif ''.join(game.user_answer).lower() not in game.valid_entries and len(game.user_answer) > 0:
                print('incorrect')
                game.user_answer.clear()


class LetterBlock4(Widget):
    letter_block_texture4 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 5:
            self.letter_block_texture4 = Image(source=game.random_string_for_level[4] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            game.user_answer.append(game.random_string_for_level[4])
            game.level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(game.user_answer).lower() in game.valid_entries:
                if ''.join(game.user_answer) not in game.unscrambled_words:
                    print('correct entry: ' + ''.join(game.user_answer))
                    game.unscrambled_words.append(''.join(game.user_answer))
                game.user_answer.clear()
            elif ''.join(game.user_answer).lower() not in game.valid_entries and len(game.user_answer) > 0:
                print('incorrect')
                game.user_answer.clear()


class LetterBlock5(Widget):
    letter_block_texture5 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 6:
            self.letter_block_texture5 = Image(source=game.random_string_for_level[5] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            game.user_answer.append(game.random_string_for_level[5])
            game.level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(game.user_answer).lower() in game.valid_entries:
                if ''.join(game.user_answer) not in game.unscrambled_words:
                    print('correct entry: ' + ''.join(game.user_answer))
                    game.unscrambled_words.append(''.join(game.user_answer))
                game.user_answer.clear()
            elif ''.join(game.user_answer).lower() not in game.valid_entries and len(game.user_answer) > 0:
                print('incorrect')
                game.user_answer.clear()


class LetterBlock6(Widget):
    letter_block_texture6 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 7:
            self.letter_block_texture6 = Image(source=game.random_string_for_level[6] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            game.user_answer.append(game.random_string_for_level[6])
            game.level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(game.user_answer).lower() in game.valid_entries:
                if ''.join(game.user_answer) not in game.unscrambled_words:
                    print('correct entry: ' + ''.join(game.user_answer))
                    game.unscrambled_words.append(''.join(game.user_answer))
                game.user_answer.clear()
            elif ''.join(game.user_answer).lower() not in game.valid_entries and len(game.user_answer) > 0:
                print('incorrect')
                game.user_answer.clear()


class LetterBlock7(Widget):
    letter_block_texture7 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 8:
            self.letter_block_texture7 = Image(source=game.random_string_for_level[7] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            game.user_answer.append(game.random_string_for_level[7])
            game.level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(game.user_answer).lower() in game.valid_entries:
                if ''.join(game.user_answer) not in game.unscrambled_words:
                    print('correct entry: ' + ''.join(game.user_answer))
                    game.unscrambled_words.append(''.join(game.user_answer))
                game.user_answer.clear()
            elif ''.join(game.user_answer).lower() not in game.valid_entries and len(game.user_answer) > 0:
                print('incorrect')
                game.user_answer.clear()


class LetterBlock8(Widget):
    letter_block_texture8 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 9:
            self.letter_block_texture8 = Image(source=game.random_string_for_level[8] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            game.user_answer.append(game.random_string_for_level[8])
            game.level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(game.user_answer).lower() in game.valid_entries:
                if ''.join(game.user_answer) not in game.unscrambled_words:
                    print('correct entry: ' + ''.join(game.user_answer))
                    game.unscrambled_words.append(''.join(game.user_answer))
                game.user_answer.clear()
            elif ''.join(game.user_answer).lower() not in game.valid_entries and len(game.user_answer) > 0:
                print('incorrect')
                game.user_answer.clear()


class LetterBlock9(Widget):
    letter_block_texture9 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks == 10:
            self.letter_block_texture9 = Image(source=game.random_string_for_level[9] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            game.user_answer.append(game.random_string_for_level[9])
            game.level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(game.user_answer).lower() in game.valid_entries:
                if ''.join(game.user_answer) not in game.unscrambled_words:
                    print('correct entry: ' + ''.join(game.user_answer))
                    game.unscrambled_words.append(''.join(game.user_answer))
                game.user_answer.clear()
            elif ''.join(game.user_answer).lower() not in game.valid_entries and len(game.user_answer) > 0:
                print('incorrect')
                game.user_answer.clear()


class VirtualLetter0(Widget):                                                                   # virtual letter classes
    virtual_letter_texture_0 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.virtual_letter_texture_0 = Image(source=game.random_string_for_level[0]+'_yellow.png').texture


class VirtualLetter1(Widget):
    virtual_letter_texture_1 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.virtual_letter_texture_1 = Image(source=game.random_string_for_level[1]+'_yellow.png').texture


class VirtualLetter2(Widget):
    virtual_letter_texture_2 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 3:
            self.virtual_letter_texture_2 = Image(source=game.random_string_for_level[2]+'_yellow.png').texture


class VirtualLetter3(Widget):
    virtual_letter_texture_3 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 4:
            self.virtual_letter_texture_3 = Image(source=game.random_string_for_level[3]+'_yellow.png').texture


class VirtualLetter4(Widget):
    virtual_letter_texture_4 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 5:
            self.virtual_letter_texture_4 = Image(source=game.random_string_for_level[4]+'_yellow.png').texture


class VirtualLetter5(Widget):
    virtual_letter_texture_5 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 6:
            self.virtual_letter_texture_5 = Image(source=game.random_string_for_level[5]+'_yellow.png').texture


class VirtualLetter6(Widget):
    virtual_letter_texture_6 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 7:
            self.virtual_letter_texture_6 = Image(source=game.random_string_for_level[6]+'_yellow.png').texture


class VirtualLetter7(Widget):
    virtual_letter_texture_7 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 8:
            self.virtual_letter_texture_7 = Image(source=game.random_string_for_level[7]+'_yellow.png').texture


class VirtualLetter8(Widget):
    virtual_letter_texture_8 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 9:
            self.virtual_letter_texture_8 = Image(source=game.random_string_for_level[8]+'_yellow.png').texture


class VirtualLetter9(Widget):
    virtual_letter_texture_9 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if game.number_of_letter_blocks >= 10:
            self.virtual_letter_texture_9 = Image(source=game.random_string_for_level[9]+'_yellow.png').texture


class RightWidgetPlate(Widget):                                                                   # widget_plate widgets
    right_widget_plate_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.right_widget_plate_texture = Image(source='widget_plate_right.png').texture


class LeftWidgetPlate(Widget):
    left_widget_plate_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.left_widget_plate_texture = Image(source='widget_plate_left.png').texture


class Coin(Widget):                                                                                 # coin widget
    coin_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.coin_texture = Image(source='coin.png').texture


class ShuffleButton(Widget):                                                                        # shuffle button
    shuffle_button_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shuffle_button_texture = Image(source='shuffle.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.size = self.width + 5, self.height + 5
            game.level_data['user touch'] = touch.pos

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.size = self.width - 5, self.height - 5


class Base(Widget):                                                                                 # blue base widget
    base_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.base_texture = Image(source='base.png').texture


class Tablet(Widget):                                                                               # tablet widget
    tablet_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tablet_texture = Image(source='tablet.png').texture


class Background(Widget):                                                                           # background widget
    background_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_texture = Image(source='bg.png').texture


class WPUrbanApp(App):                                                                                   # main process

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

    def build(self):
        pass

    def tablet_entrance(self, widget, *args):
        entrance_animation = Animation(pos_hint={'center_x': .5, 'top': .945}, duration=1/2)
        entrance_animation.start(widget)

    def shuffle_letters(self, *args):
        letter_block_0 = self.root.ids.letter_0
        letter_block_1 = self.root.ids.letter_1
        letter_block_2 = self.root.ids.letter_2
        letter_block_3 = self.root.ids.letter_3
        letter_block_4 = self.root.ids.letter_4
        letter_block_5 = self.root.ids.letter_5
        letter_block_6 = self.root.ids.letter_6
        letter_block_7 = self.root.ids.letter_7
        letter_block_8 = self.root.ids.letter_8
        letter_block_9 = self.root.ids.letter_9
        if 15 <= game.level_data['user touch'][0] <= 55 and 207 <= game.level_data['user touch'][1] <= 241:

            if game.number_of_letter_blocks == 3:
                pos = sample(range(3), 3)
                shuffle_0 = Animation(pos=game.level_data['block positions 3'][pos[0]], duration=1/3)
                shuffle_1 = Animation(pos=game.level_data['block positions 3'][pos[1]], duration=1/3)
                shuffle_2 = Animation(pos=game.level_data['block positions 3'][pos[2]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(letter_block_2)

            if game.number_of_letter_blocks == 4:
                pos = sample(range(4), 4)
                shuffle_0 = Animation(pos=game.level_data['block positions 4'][pos[0]], duration=1/3)
                shuffle_2 = Animation(pos=game.level_data['block positions 4'][pos[2]], duration=1/3)
                shuffle_1 = Animation(pos=game.level_data['block positions 4'][pos[1]], duration=1/3)
                shuffle_3 = Animation(pos=game.level_data['block positions 4'][pos[3]], duration=1/3)
                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(letter_block_2), \
                    shuffle_3.start(letter_block_3)

            if game.number_of_letter_blocks == 5:
                pos = sample(range(5), 5)
                shuffle_0 = Animation(pos=game.level_data['block positions 5'][pos[0]], duration=1 / 3)
                shuffle_1 = Animation(pos=game.level_data['block positions 5'][pos[1]], duration=1 / 3)
                shuffle_2 = Animation(pos=game.level_data['block positions 5'][pos[2]], duration=1 / 3)
                shuffle_3 = Animation(pos=game.level_data['block positions 5'][pos[3]], duration=1 / 3)
                shuffle_4 = Animation(pos=game.level_data['block positions 5'][pos[4]], duration=1 / 3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4)

            if game.number_of_letter_blocks == 6:
                pos = sample(range(6), 6)
                shuffle_0, shuffle_1, shuffle_2, shuffle_3, shuffle_4, shuffle_5 = \
                    Animation(pos=game.level_data['block positions 6'][pos[0]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 6'][pos[1]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 6'][pos[2]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 6'][pos[3]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 6'][pos[4]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 6'][pos[5]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4),\
                    shuffle_5.start(letter_block_5)

            if game.number_of_letter_blocks == 7:
                pos = sample(range(7), 7)
                shuffle_0, shuffle_1, shuffle_2, shuffle_3, shuffle_4, shuffle_5, shuffle_6 = \
                    Animation(pos=game.level_data['block positions 7'][pos[0]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 7'][pos[1]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 7'][pos[2]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 7'][pos[3]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 7'][pos[4]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 7'][pos[5]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 7'][pos[6]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4),\
                    shuffle_5.start(letter_block_5), shuffle_6.start(letter_block_6)

            if game.number_of_letter_blocks == 8:
                pos = sample(range(8), 8)
                shuffle_0, shuffle_1, shuffle_2, shuffle_3, shuffle_4, shuffle_5, shuffle_6, shuffle_7 = \
                    Animation(pos=game.level_data['block positions 8'][pos[0]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 8'][pos[1]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 8'][pos[2]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 8'][pos[3]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 8'][pos[4]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 8'][pos[5]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 8'][pos[6]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 8'][pos[7]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4),\
                    shuffle_5.start(letter_block_5), shuffle_6.start(letter_block_6), shuffle_7.start(letter_block_7)

            if game.number_of_letter_blocks == 9:
                pos = sample(range(9), 9)
                shuffle_0, shuffle_1, shuffle_2, shuffle_3, shuffle_4, shuffle_5, shuffle_6, shuffle_7, shuffle_8 = \
                    Animation(pos=game.level_data['block positions 9'][pos[0]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 9'][pos[1]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 9'][pos[2]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 9'][pos[3]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 9'][pos[4]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 9'][pos[5]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 9'][pos[6]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 9'][pos[7]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 9'][pos[8]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4),\
                    shuffle_5.start(letter_block_5), shuffle_6.start(letter_block_6), shuffle_7.start(letter_block_7), shuffle_8.start(letter_block_8)

            if game.number_of_letter_blocks == 10:
                pos = sample(range(10), 10)
                shuffle_0, shuffle_1, shuffle_2, shuffle_3, shuffle_4, shuffle_5, shuffle_6, shuffle_7, shuffle_8, shuffle_9 = \
                    Animation(pos=game.level_data['block positions 10'][pos[0]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 10'][pos[1]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 10'][pos[2]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 10'][pos[3]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 10'][pos[4]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 10'][pos[5]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 10'][pos[6]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 10'][pos[7]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 10'][pos[8]], duration=1/3), \
                    Animation(pos=game.level_data['block positions 10'][pos[9]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4), \
                shuffle_5.start(letter_block_5), shuffle_6.start(letter_block_6), shuffle_7.start(letter_block_7), shuffle_8.start(letter_block_8), shuffle_9.start(letter_block_9)
            game.level_data['user touch'] = (0, 0)

    def letter_block_entrance(self, *args):
        letter_block_0 = self.root.ids.letter_0
        letter_block_1 = self.root.ids.letter_1
        letter_block_2 = self.root.ids.letter_2
        letter_block_3 = self.root.ids.letter_3
        letter_block_4 = self.root.ids.letter_4
        letter_block_5 = self.root.ids.letter_5
        letter_block_6 = self.root.ids.letter_6
        letter_block_7 = self.root.ids.letter_7
        letter_block_8 = self.root.ids.letter_8
        letter_block_9 = self.root.ids.letter_9

        self.tablet_entrance(self.root.ids.tablet)
        if game.number_of_letter_blocks == 3:
            letter_block_0.pos = game.level_data['block positions 3'][0]
            letter_block_1.pos = game.level_data['block positions 3'][1]
            letter_block_2.pos = game.level_data['block positions 3'][2]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)

        if game.number_of_letter_blocks == 4:
            letter_block_0.pos = game.level_data['block positions 4'][0]
            letter_block_1.pos = game.level_data['block positions 4'][1]
            letter_block_2.pos = game.level_data['block positions 4'][2]
            letter_block_3.pos = game.level_data['block positions 4'][3]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)

        if game.number_of_letter_blocks == 5:
            letter_block_0.pos = game.level_data['block positions 5'][0]
            letter_block_1.pos = game.level_data['block positions 5'][1]
            letter_block_2.pos = game.level_data['block positions 5'][2]
            letter_block_3.pos = game.level_data['block positions 5'][3]
            letter_block_4.pos = game.level_data['block positions 5'][4]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)
            entrance_animation.start(letter_block_4)

        if game.number_of_letter_blocks == 6:
            letter_block_0.pos = game.level_data['block positions 6'][0]
            letter_block_1.pos = game.level_data['block positions 6'][1]
            letter_block_2.pos = game.level_data['block positions 6'][2]
            letter_block_3.pos = game.level_data['block positions 6'][3]
            letter_block_4.pos = game.level_data['block positions 6'][4]
            letter_block_5.pos = game.level_data['block positions 6'][5]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)
            entrance_animation.start(letter_block_4)
            entrance_animation.start(letter_block_5)

        if game.number_of_letter_blocks == 7:
            letter_block_0.pos = game.level_data['block positions 7'][0]
            letter_block_1.pos = game.level_data['block positions 7'][1]
            letter_block_2.pos = game.level_data['block positions 7'][2]
            letter_block_3.pos = game.level_data['block positions 7'][3]
            letter_block_4.pos = game.level_data['block positions 7'][4]
            letter_block_5.pos = game.level_data['block positions 7'][5]
            letter_block_6.pos = game.level_data['block positions 7'][6]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)
            entrance_animation.start(letter_block_4)
            entrance_animation.start(letter_block_5)
            entrance_animation.start(letter_block_6)

        if game.number_of_letter_blocks == 8:
            letter_block_0.pos = game.level_data['block positions 8'][0]
            letter_block_1.pos = game.level_data['block positions 8'][1]
            letter_block_2.pos = game.level_data['block positions 8'][2]
            letter_block_3.pos = game.level_data['block positions 8'][3]
            letter_block_4.pos = game.level_data['block positions 8'][4]
            letter_block_5.pos = game.level_data['block positions 8'][5]
            letter_block_6.pos = game.level_data['block positions 8'][6]
            letter_block_7.pos = game.level_data['block positions 8'][7]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)
            entrance_animation.start(letter_block_4)
            entrance_animation.start(letter_block_5)
            entrance_animation.start(letter_block_6)
            entrance_animation.start(letter_block_7)

        if game.number_of_letter_blocks == 9:
            letter_block_0.pos = game.level_data['block positions 9'][0]
            letter_block_1.pos = game.level_data['block positions 9'][1]
            letter_block_2.pos = game.level_data['block positions 9'][2]
            letter_block_3.pos = game.level_data['block positions 9'][3]
            letter_block_4.pos = game.level_data['block positions 9'][4]
            letter_block_5.pos = game.level_data['block positions 9'][5]
            letter_block_6.pos = game.level_data['block positions 9'][6]
            letter_block_7.pos = game.level_data['block positions 9'][7]
            letter_block_8.pos = game.level_data['block positions 9'][8]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)
            entrance_animation.start(letter_block_4)
            entrance_animation.start(letter_block_5)
            entrance_animation.start(letter_block_6)
            entrance_animation.start(letter_block_7)
            entrance_animation.start(letter_block_8)

        if game.number_of_letter_blocks == 10:
            letter_block_0.pos = game.level_data['block positions 10'][0]
            letter_block_1.pos = game.level_data['block positions 10'][1]
            letter_block_2.pos = game.level_data['block positions 10'][2]
            letter_block_3.pos = game.level_data['block positions 10'][3]
            letter_block_4.pos = game.level_data['block positions 10'][4]
            letter_block_5.pos = game.level_data['block positions 10'][5]
            letter_block_6.pos = game.level_data['block positions 10'][6]
            letter_block_7.pos = game.level_data['block positions 10'][7]
            letter_block_8.pos = game.level_data['block positions 10'][8]
            letter_block_9.pos = game.level_data['block positions 10'][9]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)
            entrance_animation.start(letter_block_4)
            entrance_animation.start(letter_block_5)
            entrance_animation.start(letter_block_6)
            entrance_animation.start(letter_block_7)
            entrance_animation.start(letter_block_8)
            entrance_animation.start(letter_block_9)

    def letter_plate_entrance(self, *args):

        plates = []
        
        if len(game.level_data['entry lengths']) == 3:
            current_plate_pos_y = 610
            if game.level_data['entry lengths'][0] == 2:
                current_plate_pos_x = 83
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 3:
                current_plate_pos_x = 51
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 4:
                current_plate_pos_x = 20
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 5:
                current_plate_pos_x = -5
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 6:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

            current_plate_pos_y = 520
            if game.level_data['entry lengths'][1] == 2:
                current_plate_pos_x = 83
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 3:
                current_plate_pos_x = 51
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 4:
                current_plate_pos_x = 20
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 5:
                current_plate_pos_x = -5
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 6:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

            current_plate_pos_y = 430
            if game.level_data['entry lengths'][2] == 2:
                current_plate_pos_x = 83
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 3:
                current_plate_pos_x = 36
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 4:
                current_plate_pos_x = 20
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 5:
                current_plate_pos_x = -5
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 6:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

        elif len(game.level_data['entry lengths']) == 4:
            current_plate_pos_y = 610
            if game.level_data['entry lengths'][0] == 2:
                current_plate_pos_x = 83
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 3:
                current_plate_pos_x = 51
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 4:
                current_plate_pos_x = 20
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 5:
                current_plate_pos_x = -5
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 6:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

            current_plate_pos_y = 540
            if game.level_data['entry lengths'][1] == 2:
                current_plate_pos_x = 83
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 3:
                current_plate_pos_x = 51
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 4:
                current_plate_pos_x = 20
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 5:
                current_plate_pos_x = -5
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 6:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

            current_plate_pos_y = 470
            if game.level_data['entry lengths'][2] == 2:
                current_plate_pos_x = 83
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 3:
                current_plate_pos_x = 51
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 4:
                current_plate_pos_x = 20
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 5:
                current_plate_pos_x = -5
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 6:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

            current_plate_pos_y = 400
            if game.level_data['entry lengths'][3] == 2:
                current_plate_pos_x = 83
                for i in range(game.level_data['entry lengths'][3]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][3] == 3:
                current_plate_pos_x = 51
                for i in range(game.level_data['entry lengths'][3]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][3] == 4:
                current_plate_pos_x = 20
                for i in range(game.level_data['entry lengths'][3]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][3] == 5:
                current_plate_pos_x = -5
                for i in range(game.level_data['entry lengths'][3]):
                    plate = LetterPlate()
                    plate.size = 50, 50
                    plate.pos = current_plate_pos_x + 55, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][3] == 6:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][3]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

        elif len(game.level_data['entry lengths']) == 5:
            current_plate_pos_y = 610
            if game.level_data['entry lengths'][0] == 2:
                current_plate_pos_x = 93
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 3:
                current_plate_pos_x = 61
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 4:
                current_plate_pos_x = 30
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 5:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][0] == 6:
                current_plate_pos_x = 0
                for i in range(game.level_data['entry lengths'][0]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

            current_plate_pos_y = 555
            if game.level_data['entry lengths'][1] == 2:
                current_plate_pos_x = 93
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 3:
                current_plate_pos_x = 61
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 4:
                current_plate_pos_x = 30
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 5:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][1]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][1] == 6:
                current_plate_pos_x = 0
                for i in range(game.level_data['entry lengths'][4]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

            current_plate_pos_y = 500

            if game.level_data['entry lengths'][2] == 2:
                current_plate_pos_x = 93
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 3:
                current_plate_pos_x = 61
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 4:
                current_plate_pos_x = 30
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 5:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][2] == 6:
                current_plate_pos_x = 0
                for i in range(game.level_data['entry lengths'][2]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

            current_plate_pos_y = 445

            if game.level_data['entry lengths'][3] == 2:
                current_plate_pos_x = 93
                for i in range(game.level_data['entry lengths'][3]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][3] == 3:
                current_plate_pos_x = 61
                for i in range(game.level_data['entry lengths'][3]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][3] == 4:
                current_plate_pos_x = 30
                for i in range(game.level_data['entry lengths'][3]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][3] == 5:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][3]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][3] == 6:
                current_plate_pos_x = 0
                for i in range(game.level_data['entry lengths'][3]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

            current_plate_pos_y = 390

            if game.level_data['entry lengths'][4] == 2:
                current_plate_pos_x = 93
                for i in range(game.level_data['entry lengths'][4]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][4] == 3:
                current_plate_pos_x = 61
                for i in range(game.level_data['entry lengths'][4]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][4] == 4:
                current_plate_pos_x = 30
                for i in range(game.level_data['entry lengths'][4]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][4] == 5:
                current_plate_pos_x = 5
                for i in range(game.level_data['entry lengths'][4]):
                    plate = LetterPlate()
                    plate.size = 45, 45
                    plate.pos = current_plate_pos_x + 50, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)
            elif game.level_data['entry lengths'][4] == 6:
                current_plate_pos_x = 0
                for i in range(game.level_data['entry lengths'][4]):
                    plate = LetterPlate()
                    plate.size = 40, 40
                    plate.pos = current_plate_pos_x + 45, current_plate_pos_y
                    current_plate_pos_x = plate.pos[0]
                    plates.append(plate)
                    self.root.add_widget(plate)

            plates.clear()

    def on_start(self):
        self.letter_block_entrance()
        self.letter_plate_entrance()
        Clock.schedule_interval(self.shuffle_letters, 1/2)


WPUrbanApp().run()
