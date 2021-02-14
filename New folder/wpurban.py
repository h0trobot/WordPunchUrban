from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, ListProperty
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.config import Config
from random import randint, sample
from itertools import permutations
import concurrent.futures
from kivy.graphics import Color, Ellipse, Line

import json

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '740')

level_data = {
    'random string for level': [],
    'valid entries': [],
    'required entries': [],
    'entry lengths': [],
    'required entries last index': randint(3, 4),
    'user touch': (0, 0),
    'block positions 3': [(77, 190), (232, 190), (155, 70)],
    'block positions 4': [(70, 150), (235, 150), (153, 70), (153, 230)],
    'block positions 5': [(71, 165), (236, 165), (104, 70), (154, 230), (204, 70)],
    'block positions 6': [(79, 204), (244, 174), (64, 114), (172, 234), (234, 79), (137, 49)],
    'block positions 7': [(68, 215), (240, 200), (50, 127), (158, 245), (248, 110), (90, 50), (183, 42)],
    'block positions 8': [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    'block positions 9': [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
    'block positions 10': [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
}


# extract words, i.e. dictionary keys from words_dictionary.json
with open('words_dictionary.json') as json_file:
    j_d = json_file.read()

data = json.loads(j_d)
dictionary = list(dict.keys(data))

# excerpt words of length, 2-8 characters from dictionary list for main dictionary, DICTIONARY


def by_size(words, size):
    return [word for word in words if len(word) == size]


DICTIONARY = []

for i in range(3, 7):
    dicty = by_size(dictionary, i)
    DICTIONARY.extend(dicty)

alphabet = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z'
]

user_answer = []
unscrambled_words = []
answer_perms = permutations(user_answer)

'''
using a random word taken from DICTIONARY, generate a string for current level and find all valid words from 
permutations of chosen word. for_loop() iterates through each letter of each permutation, adding the next
character successively and searching for a match in DICTIONARY
'''


def for_loop(perm):
    for chr in range(len(perm)):
        chars = perm[:chr + 1]
        possible_word = ''.join(chars)
        if possible_word in dictionary and possible_word not in level_data['valid entries'] and len(possible_word) > 1:
            level_data['valid entries'].append(possible_word)


case_word = DICTIONARY[randint(0, 55533)]
case_word_list = []
for char in case_word:
    case_word_list.append(char)

case_word_perms = permutations(case_word_list)
perms_list = []
for p in case_word_perms:
    perms_list.append(p)

random_string_for_level = list(perms_list[0])
level_data['random string for level'] = random_string_for_level
number_of_letter_blocks = len(random_string_for_level)
valid_entries = level_data['valid entries']

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(for_loop, perms_list)

if len(valid_entries) > 5:
    for i in range(0, level_data['required entries last index']):
        n = randint(0, len(valid_entries) - 1)
        level_data['required entries'].append(valid_entries[n])
elif len(valid_entries) <= 5:
    for i in range(0, 3):
        n = randint(0, len(valid_entries) - 1)
        level_data['required entries'].append(valid_entries[n])

main_word = max(valid_entries, key=len)

if main_word not in level_data['required entries']:
    level_data['required entries'].append(main_word)

required_entries = level_data['required entries']

# append the lengths of each required entry to entry_lengths. Not sure what this is useful for for now however.
for entry in range(len(required_entries)):
    level_data['entry lengths'].append(len(required_entries[entry]))

entry_lengths = sorted(level_data['entry lengths'])
print(valid_entries)
print(random_string_for_level)
print(number_of_letter_blocks)
print(required_entries)
print(entry_lengths)


class LetterBlock0(Widget):                                                                  # letter block classes
    letter_block_texture0 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.letter_block_texture0 = Image(source=random_string_for_level[0] + '.png').texture

    # defining touch interactions
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            user_answer.append(random_string_for_level[0])
            level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(user_answer).lower() in valid_entries:
                if ''.join(user_answer) not in unscrambled_words:
                    print('correct entry: ' + ''.join(user_answer))
                    unscrambled_words.append(''.join(user_answer))
                user_answer.clear()
            elif ''.join(user_answer).lower() not in valid_entries and len(user_answer) > 0:
                print('incorrect')
                user_answer.clear()


class LetterBlock1(Widget):
    letter_block_texture1 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.letter_block_texture1 = Image(source=random_string_for_level[1] + '.png').texture

    # defining touch interactions
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            user_answer.append(random_string_for_level[1])
            level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(user_answer).lower() in valid_entries:
                if ''.join(user_answer) not in unscrambled_words:
                    print('correct entry: ' + ''.join(user_answer))
                    unscrambled_words.append(''.join(user_answer))
                user_answer.clear()
            elif ''.join(user_answer).lower() not in valid_entries and len(user_answer) > 0:
                print('incorrect')
                user_answer.clear()


class LetterBlock2(Widget):
    letter_block_texture2 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 3:
            self.letter_block_texture2 = Image(source=random_string_for_level[2] + '.png').texture

    # defining touch interactions
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            user_answer.append(random_string_for_level[2])
            level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(user_answer).lower() in valid_entries:
                if ''.join(user_answer) not in unscrambled_words:
                    print('correct entry: ' + ''.join(user_answer))
                    unscrambled_words.append(''.join(user_answer))
                user_answer.clear()
            elif ''.join(user_answer).lower() not in valid_entries and len(user_answer) > 0:
                print('incorrect')
                user_answer.clear()


class LetterBlock3(Widget):
    letter_block_texture3 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 4:
            self.letter_block_texture3 = Image(source=random_string_for_level[3] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            user_answer.append(random_string_for_level[3])
            level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(user_answer).lower() in valid_entries:
                if ''.join(user_answer) not in unscrambled_words:
                    print('correct entry: ' + ''.join(user_answer))
                    unscrambled_words.append(''.join(user_answer))
                user_answer.clear()
            elif ''.join(user_answer).lower() not in valid_entries and len(user_answer) > 0:
                print('incorrect')
                user_answer.clear()


class LetterBlock4(Widget):
    letter_block_texture4 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 5:
            self.letter_block_texture4 = Image(source=random_string_for_level[4] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            user_answer.append(random_string_for_level[4])
            level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(user_answer).lower() in valid_entries:
                if ''.join(user_answer) not in unscrambled_words:
                    print('correct entry: ' + ''.join(user_answer))
                    unscrambled_words.append(''.join(user_answer))
                user_answer.clear()
            elif ''.join(user_answer).lower() not in valid_entries and len(user_answer) > 0:
                print('incorrect')
                user_answer.clear()


class LetterBlock5(Widget):
    letter_block_texture5 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 6:
            self.letter_block_texture5 = Image(source=random_string_for_level[5] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            user_answer.append(random_string_for_level[5])
            level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(user_answer).lower() in valid_entries:
                if ''.join(user_answer) not in unscrambled_words:
                    print('correct entry: ' + ''.join(user_answer))
                    unscrambled_words.append(''.join(user_answer))
                user_answer.clear()
            elif ''.join(user_answer).lower() not in valid_entries and len(user_answer) > 0:
                print('incorrect')
                user_answer.clear()


class LetterBlock6(Widget):
    letter_block_texture6 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 7:
            self.letter_block_texture6 = Image(source=random_string_for_level[6] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            user_answer.append(random_string_for_level[6])
            level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(user_answer).lower() in valid_entries:
                if ''.join(user_answer) not in unscrambled_words:
                    print('correct entry: ' + ''.join(user_answer))
                    unscrambled_words.append(''.join(user_answer))
                user_answer.clear()
            elif ''.join(user_answer).lower() not in valid_entries and len(user_answer) > 0:
                print('incorrect')
                user_answer.clear()


class LetterBlock7(Widget):
    letter_block_texture7 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 8:
            self.letter_block_texture7 = Image(source=random_string_for_level[7] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            user_answer.append(random_string_for_level[7])
            level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(user_answer).lower() in valid_entries:
                if ''.join(user_answer) not in unscrambled_words:
                    print('correct entry: ' + ''.join(user_answer))
                    unscrambled_words.append(''.join(user_answer))
                user_answer.clear()
            elif ''.join(user_answer).lower() not in valid_entries and len(user_answer) > 0:
                print('incorrect')
                user_answer.clear()


class LetterBlock8(Widget):
    letter_block_texture8 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 9:
            self.letter_block_texture8 = Image(source=random_string_for_level[8] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            user_answer.append(random_string_for_level[8])
            level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(user_answer).lower() in valid_entries:
                if ''.join(user_answer) not in unscrambled_words:
                    print('correct entry: ' + ''.join(user_answer))
                    unscrambled_words.append(''.join(user_answer))
                user_answer.clear()
            elif ''.join(user_answer).lower() not in valid_entries and len(user_answer) > 0:
                print('incorrect')
                user_answer.clear()


class LetterBlock9(Widget):
    letter_block_texture9 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks == 10:
            self.letter_block_texture9 = Image(source=random_string_for_level[9] + '.png').texture

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and self.height == 50:
            self.size = self.width + 3, self.height + 3
            self.opacity = .7

            user_answer.append(random_string_for_level[9])
            level_data['user touch'] = touch.pos

    def on_touch_move(self, touch):
        self.on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.height >= 53:
            self.size = self.width - 3, self.height - 3
            self.opacity = 1

            if ''.join(user_answer).lower() in valid_entries:
                if ''.join(user_answer) not in unscrambled_words:
                    print('correct entry: ' + ''.join(user_answer))
                    unscrambled_words.append(''.join(user_answer))
                user_answer.clear()
            elif ''.join(user_answer).lower() not in valid_entries and len(user_answer) > 0:
                print('incorrect')
                user_answer.clear()


class VirtualLetter0(Widget):                                                                   # virtual letter classes
    virtual_letter_texture_0 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.virtual_letter_texture_0 = Image(source=random_string_for_level[0]+'_yellow.png').texture


class VirtualLetter1(Widget):
    virtual_letter_texture_1 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.virtual_letter_texture_1 = Image(source=random_string_for_level[1]+'_yellow.png').texture


class VirtualLetter2(Widget):
    virtual_letter_texture_2 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 3:
            self.virtual_letter_texture_2 = Image(source=random_string_for_level[2]+'_yellow.png').texture


class VirtualLetter3(Widget):
    virtual_letter_texture_3 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 4:
            self.virtual_letter_texture_3 = Image(source=random_string_for_level[3]+'_yellow.png').texture


class VirtualLetter4(Widget):
    virtual_letter_texture_4 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 5:
            self.virtual_letter_texture_4 = Image(source=random_string_for_level[4]+'_yellow.png').texture


class VirtualLetter5(Widget):
    virtual_letter_texture_5 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 6:
            self.virtual_letter_texture_5 = Image(source=random_string_for_level[5]+'_yellow.png').texture


class VirtualLetter6(Widget):
    virtual_letter_texture_6 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 7:
            self.virtual_letter_texture_6 = Image(source=random_string_for_level[6]+'_yellow.png').texture


class VirtualLetter7(Widget):
    virtual_letter_texture_7 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 8:
            self.virtual_letter_texture_7 = Image(source=random_string_for_level[7]+'_yellow.png').texture


class VirtualLetter8(Widget):
    virtual_letter_texture_8 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 9:
            self.virtual_letter_texture_8 = Image(source=random_string_for_level[8]+'_yellow.png').texture


class VirtualLetter9(Widget):
    virtual_letter_texture_9 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if number_of_letter_blocks >= 10:
            self.virtual_letter_texture_9 = Image(source=random_string_for_level[9]+'_yellow.png').texture


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
            level_data['user touch'] = touch.pos

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.size = self.width - 5, self.height - 5


class LetterPlate(Widget):                                                                          # letter plate
    letter_plate_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.letter_plate_texture = Image(source='letter_plate.png').texture


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
        if 15 <= level_data['user touch'][0] <= 55 and 207 <= level_data['user touch'][1] <= 241:

            if number_of_letter_blocks == 3:
                pos = sample(range(3), 3)
                shuffle_0 = Animation(pos=level_data['block positions 3'][pos[0]], duration=1/3)
                shuffle_1 = Animation(pos=level_data['block positions 3'][pos[1]], duration=1/3)
                shuffle_2 = Animation(pos=level_data['block positions 3'][pos[2]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(letter_block_2)

            if number_of_letter_blocks == 4:
                pos = sample(range(4), 4)
                shuffle_0 = Animation(pos=level_data['block positions 4'][pos[0]], duration=1/3)
                shuffle_1 = Animation(pos=level_data['block positions 4'][pos[1]], duration=1/3)
                shuffle_2 = Animation(pos=level_data['block positions 4'][pos[2]], duration=1/3)
                shuffle_3 = Animation(pos=level_data['block positions 4'][pos[3]], duration=1/3)
                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(letter_block_2), \
                    shuffle_3.start(letter_block_3)

            if number_of_letter_blocks == 5:
                pos = sample(range(5), 5)
                shuffle_0 = Animation(pos=level_data['block positions 5'][pos[0]], duration=1 / 3)
                shuffle_1 = Animation(pos=level_data['block positions 5'][pos[1]], duration=1 / 3)
                shuffle_2 = Animation(pos=level_data['block positions 5'][pos[2]], duration=1 / 3)
                shuffle_3 = Animation(pos=level_data['block positions 5'][pos[3]], duration=1 / 3)
                shuffle_4 = Animation(pos=level_data['block positions 5'][pos[4]], duration=1 / 3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4)

            if number_of_letter_blocks == 6:
                pos = sample(range(6), 6)
                shuffle_0, shuffle_1, shuffle_2, shuffle_3, shuffle_4, shuffle_5 = \
                    Animation(pos=level_data['block positions 6'][pos[0]], duration=1/3), \
                    Animation(pos=level_data['block positions 6'][pos[1]], duration=1/3), \
                    Animation(pos=level_data['block positions 6'][pos[2]], duration=1/3), \
                    Animation(pos=level_data['block positions 6'][pos[3]], duration=1/3), \
                    Animation(pos=level_data['block positions 6'][pos[4]], duration=1/3), \
                    Animation(pos=level_data['block positions 6'][pos[5]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4),\
                    shuffle_5.start(letter_block_5)

            if number_of_letter_blocks == 7:
                pos = sample(range(7), 7)
                shuffle_0, shuffle_1, shuffle_2, shuffle_3, shuffle_4, shuffle_5, shuffle_6 = \
                    Animation(pos=level_data['block positions 7'][pos[0]], duration=1/3), \
                    Animation(pos=level_data['block positions 7'][pos[1]], duration=1/3), \
                    Animation(pos=level_data['block positions 7'][pos[2]], duration=1/3), \
                    Animation(pos=level_data['block positions 7'][pos[3]], duration=1/3), \
                    Animation(pos=level_data['block positions 7'][pos[4]], duration=1/3), \
                    Animation(pos=level_data['block positions 7'][pos[5]], duration=1/3), \
                    Animation(pos=level_data['block positions 7'][pos[6]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4),\
                    shuffle_5.start(letter_block_5), shuffle_6.start(letter_block_6)

            if number_of_letter_blocks == 8:
                pos = sample(range(8), 8)
                shuffle_0, shuffle_1, shuffle_2, shuffle_3, shuffle_4, shuffle_5, shuffle_6, shuffle_7 = \
                    Animation(pos=level_data['block positions 8'][pos[0]], duration=1/3), \
                    Animation(pos=level_data['block positions 8'][pos[1]], duration=1/3), \
                    Animation(pos=level_data['block positions 8'][pos[2]], duration=1/3), \
                    Animation(pos=level_data['block positions 8'][pos[3]], duration=1/3), \
                    Animation(pos=level_data['block positions 8'][pos[4]], duration=1/3), \
                    Animation(pos=level_data['block positions 8'][pos[5]], duration=1/3), \
                    Animation(pos=level_data['block positions 8'][pos[6]], duration=1/3), \
                    Animation(pos=level_data['block positions 8'][pos[7]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4),\
                    shuffle_5.start(letter_block_5), shuffle_6.start(letter_block_6), shuffle_7.start(letter_block_7)

            if number_of_letter_blocks == 9:
                pos = sample(range(9), 9)
                shuffle_0, shuffle_1, shuffle_2, shuffle_3, shuffle_4, shuffle_5, shuffle_6, shuffle_7, shuffle_8 = \
                    Animation(pos=level_data['block positions 9'][pos[0]], duration=1/3), \
                    Animation(pos=level_data['block positions 9'][pos[1]], duration=1/3), \
                    Animation(pos=level_data['block positions 9'][pos[2]], duration=1/3), \
                    Animation(pos=level_data['block positions 9'][pos[3]], duration=1/3), \
                    Animation(pos=level_data['block positions 9'][pos[4]], duration=1/3), \
                    Animation(pos=level_data['block positions 9'][pos[5]], duration=1/3), \
                    Animation(pos=level_data['block positions 9'][pos[6]], duration=1/3), \
                    Animation(pos=level_data['block positions 9'][pos[7]], duration=1/3), \
                    Animation(pos=level_data['block positions 9'][pos[8]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4),\
                    shuffle_5.start(letter_block_5), shuffle_6.start(letter_block_6), shuffle_7.start(letter_block_7), shuffle_8.start(letter_block_8)

            if number_of_letter_blocks == 10:
                pos = sample(range(10), 10)
                shuffle_0, shuffle_1, shuffle_2, shuffle_3, shuffle_4, shuffle_5, shuffle_6, shuffle_7, shuffle_8, shuffle_9 = \
                    Animation(pos=level_data['block positions 10'][pos[0]], duration=1/3), \
                    Animation(pos=level_data['block positions 10'][pos[1]], duration=1/3), \
                    Animation(pos=level_data['block positions 10'][pos[2]], duration=1/3), \
                    Animation(pos=level_data['block positions 10'][pos[3]], duration=1/3), \
                    Animation(pos=level_data['block positions 10'][pos[4]], duration=1/3), \
                    Animation(pos=level_data['block positions 10'][pos[5]], duration=1/3), \
                    Animation(pos=level_data['block positions 10'][pos[6]], duration=1/3), \
                    Animation(pos=level_data['block positions 10'][pos[7]], duration=1/3), \
                    Animation(pos=level_data['block positions 10'][pos[8]], duration=1/3), \
                    Animation(pos=level_data['block positions 10'][pos[9]], duration=1/3)

                shuffle_0.start(letter_block_0), shuffle_1.start(letter_block_1), shuffle_2.start(
                    letter_block_2), shuffle_3.start(letter_block_3), shuffle_4.start(letter_block_4), \
                shuffle_5.start(letter_block_5), shuffle_6.start(letter_block_6), shuffle_7.start(letter_block_7), shuffle_8.start(letter_block_8), shuffle_9.start(letter_block_9)
            level_data['user touch'] = (0, 0)

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
        if number_of_letter_blocks == 3:
            letter_block_0.pos = level_data['block positions 3'][0]
            letter_block_1.pos = level_data['block positions 3'][1]
            letter_block_2.pos = level_data['block positions 3'][2]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)

        if number_of_letter_blocks == 4:
            letter_block_0.pos = level_data['block positions 4'][0]
            letter_block_1.pos = level_data['block positions 4'][1]
            letter_block_2.pos = level_data['block positions 4'][2]
            letter_block_3.pos = level_data['block positions 4'][3]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)

        if number_of_letter_blocks == 5:
            letter_block_0.pos = level_data['block positions 5'][0]
            letter_block_1.pos = level_data['block positions 5'][1]
            letter_block_2.pos = level_data['block positions 5'][2]
            letter_block_3.pos = level_data['block positions 5'][3]
            letter_block_4.pos = level_data['block positions 5'][4]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)
            entrance_animation.start(letter_block_4)

        if number_of_letter_blocks == 6:
            letter_block_0.pos = level_data['block positions 6'][0]
            letter_block_1.pos = level_data['block positions 6'][1]
            letter_block_2.pos = level_data['block positions 6'][2]
            letter_block_3.pos = level_data['block positions 6'][3]
            letter_block_4.pos = level_data['block positions 6'][4]
            letter_block_5.pos = level_data['block positions 6'][5]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)
            entrance_animation.start(letter_block_4)
            entrance_animation.start(letter_block_5)

        if number_of_letter_blocks == 7:
            letter_block_0.pos = level_data['block positions 7'][0]
            letter_block_1.pos = level_data['block positions 7'][1]
            letter_block_2.pos = level_data['block positions 7'][2]
            letter_block_3.pos = level_data['block positions 7'][3]
            letter_block_4.pos = level_data['block positions 7'][4]
            letter_block_5.pos = level_data['block positions 7'][5]
            letter_block_6.pos = level_data['block positions 7'][6]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)
            entrance_animation.start(letter_block_4)
            entrance_animation.start(letter_block_5)
            entrance_animation.start(letter_block_6)

        if number_of_letter_blocks == 8:
            letter_block_0.pos = level_data['block positions 8'][0]
            letter_block_1.pos = level_data['block positions 8'][1]
            letter_block_2.pos = level_data['block positions 8'][2]
            letter_block_3.pos = level_data['block positions 8'][3]
            letter_block_4.pos = level_data['block positions 8'][4]
            letter_block_5.pos = level_data['block positions 8'][5]
            letter_block_6.pos = level_data['block positions 8'][6]
            letter_block_7.pos = level_data['block positions 8'][7]

            entrance_animation = Animation(size=(50, 50), duration=1 / 2)
            entrance_animation.start(letter_block_0)
            entrance_animation.start(letter_block_1)
            entrance_animation.start(letter_block_2)
            entrance_animation.start(letter_block_3)
            entrance_animation.start(letter_block_4)
            entrance_animation.start(letter_block_5)
            entrance_animation.start(letter_block_6)
            entrance_animation.start(letter_block_7)

        if number_of_letter_blocks == 9:
            letter_block_0.pos = level_data['block positions 9'][0]
            letter_block_1.pos = level_data['block positions 9'][1]
            letter_block_2.pos = level_data['block positions 9'][2]
            letter_block_3.pos = level_data['block positions 9'][3]
            letter_block_4.pos = level_data['block positions 9'][4]
            letter_block_5.pos = level_data['block positions 9'][5]
            letter_block_6.pos = level_data['block positions 9'][6]
            letter_block_7.pos = level_data['block positions 9'][7]
            letter_block_8.pos = level_data['block positions 9'][8]

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

        if number_of_letter_blocks == 10:
            letter_block_0.pos = level_data['block positions 10'][0]
            letter_block_1.pos = level_data['block positions 10'][1]
            letter_block_2.pos = level_data['block positions 10'][2]
            letter_block_3.pos = level_data['block positions 10'][3]
            letter_block_4.pos = level_data['block positions 10'][4]
            letter_block_5.pos = level_data['block positions 10'][5]
            letter_block_6.pos = level_data['block positions 10'][6]
            letter_block_7.pos = level_data['block positions 10'][7]
            letter_block_8.pos = level_data['block positions 10'][8]
            letter_block_9.pos = level_data['block positions 10'][9]

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
        plate_0 = self.root.ids.plate_0
        plate_1 = self.root.ids.plate_1
        plate_2 = self.root.ids.plate_2
        plate_3 = self.root.ids.plate_3
        plate_4 = self.root.ids.plate_4
        plate_5 = self.root.ids.plate_5
        plate_6 = self.root.ids.plate_6
        plate_7 = self.root.ids.plate_7
        plate_8 = self.root.ids.plate_8
        plate_9 = self.root.ids.plate_9
        plate_10 = self.root.ids.plate_10
        plate_11 = self.root.ids.plate_11
        plate_12 = self.root.ids.plate_12
        plate_13 = self.root.ids.plate_13
        plate_14 = self.root.ids.plate_14
        plate_15 = self.root.ids.plate_15
        plate_16 = self.root.ids.plate_16
        plate_17 = self.root.ids.plate_17
        plate_18 = self.root.ids.plate_18
        plate_19 = self.root.ids.plate_19
        plate_20 = self.root.ids.plate_20
        plate_21 = self.root.ids.plate_21
        plate_22 = self.root.ids.plate_22
        plate_23 = self.root.ids.plate_23
        plate_24 = self.root.ids.plate_24
        plate_25 = self.root.ids.plate_25
        plate_26 = self.root.ids.plate_26
        plate_27 = self.root.ids.plate_27
        plate_28 = self.root.ids.plate_28
        plate_29 = self.root.ids.plate_29

        if len(entry_lengths) == 3:
            if entry_lengths[0] == 2:
                plate_0.pos, plate_0.size = (128, 610), (50, 50)
                plate_1.pos, plate_1.size = (188, 610), (50, 50)
            if entry_lengths[0] == 3:
                plate_0.pos, plate_0.size = (96, 610), (50, 50)
                plate_1.pos, plate_1.size = (156, 610), (50, 50)
                plate_2.pos, plate_2.size = (216, 610), (50, 50)
            if entry_lengths[0] == 4:
                plate_0.pos, plate_0.size = (65, 610), (50, 50)
                plate_1.pos, plate_1.size = (125, 610), (50, 50)
                plate_2.pos, plate_2.size = (185, 610), (50, 50)
                plate_3.pos, plate_3.size = (245, 610), (50, 50)
            if entry_lengths[0] == 5:
                plate_0.pos, plate_0.size = (45, 610), (50, 50)
                plate_1.pos, plate_1.size = (100, 610), (50, 50)
                plate_2.pos, plate_2.size = (155, 610), (50, 50)
                plate_3.pos, plate_3.size = (210, 610), (50, 50)
                plate_4.pos, plate_4.size = (265, 610), (50, 50)
            if entry_lengths[0] == 6:
                plate_0.pos, plate_0.size = (100, 610), (40, 40)
                plate_1.pos, plate_1.size = (140, 610), (40, 40)
                plate_2.pos, plate_2.size = (180, 610), (40, 40)
                plate_3.pos, plate_3.size = (220, 610), (40, 40)
                plate_4.pos, plate_4.size = (260, 610), (40, 40)
                plate_5.pos, plate_5.size = (300, 610), (40, 40)
            if entry_lengths[1] == 2:
                plate_6.pos, plate_6.size = (128, 520), (50, 50)
                plate_7.pos, plate_7.size = (188, 520), (50, 50)
            if entry_lengths[1] == 3:
                plate_6.pos, plate_6.size = (96, 520), (50, 50)
                plate_7.pos, plate_7.size = (156, 520), (50, 50)
                plate_8.pos, plate_8.size = (216, 520), (50, 50)
            if entry_lengths[1] == 4:
                plate_6.pos, plate_6.size = (65, 520), (50, 50)
                plate_7.pos, plate_7.size = (125, 520), (50, 50)
                plate_8.pos, plate_8.size = (185, 520), (50, 50)
                plate_9.pos, plate_9.size = (245, 520), (50, 50)
            if entry_lengths[1] == 5:
                plate_6.pos, plate_6.size = (45, 520), (50, 50)
                plate_7.pos, plate_7.size = (100, 520), (50, 50)
                plate_8.pos, plate_8.size = (155, 520), (50, 50)
                plate_9.pos, plate_9.size = (210, 520), (50, 50)
                plate_10.pos, plate_10.size = (265, 520), (50, 50)
            if entry_lengths[1] == 6:
                plate_6.pos, plate_6.size = (100, 520), (40, 40)
                plate_7.pos, plate_7.size = (140, 520), (40, 40)
                plate_8.pos, plate_8.size = (180, 520), (40, 40)
                plate_9.pos, plate_9.size = (220, 520), (40, 40)
                plate_10.pos, plate_10.size = (260, 520), (40, 40)
                plate_11.pos, plate_11.size = (300, 520), (40, 40)
            if entry_lengths[2] == 2:
                plate_12.pos, plate_12.size = (128, 450), (50, 50)
                plate_13.pos, plate_13.size = (188, 450), (50, 50)
            if entry_lengths[2] == 3:
                plate_12.pos, plate_12.size = (96, 450), (50, 50)
                plate_13.pos, plate_13.size = (156, 450), (50, 50)
                plate_14.pos, plate_14.size = (216, 450), (50, 50)
            if entry_lengths[2] == 4:
                plate_12.pos, plate_12.size = (65, 450), (50, 50)
                plate_13.pos, plate_13.size = (125, 450), (50, 50)
                plate_14.pos, plate_14.size = (185, 450), (50, 50)
                plate_15.pos, plate_15.size = (245, 450), (50, 50)
            if entry_lengths[2] == 5:
                plate_12.pos, plate_12.size = (45, 450), (50, 50)
                plate_13.pos, plate_13.size = (100, 450), (50, 50)
                plate_14.pos, plate_14.size = (155, 450), (50, 50)
                plate_15.pos, plate_15.size = (210, 450), (50, 50)
                plate_16.pos, plate_16.size = (265, 450), (50, 50)
            if entry_lengths[2] == 6:
                plate_12.pos, plate_12.size = (50, 450), (40, 40)
                plate_13.pos, plate_13.size = (110, 450), (40, 40)
                plate_14.pos, plate_14.size = (170, 450), (40, 40)
                plate_15.pos, plate_15.size = (230, 450), (40, 40)
                plate_16.pos, plate_16.size = (290, 450), (40, 40)
                plate_17.pos, plate_17.size = (350, 450), (40, 40)

        if len(entry_lengths) == 4:
            if entry_lengths[0] == 2:
                plate_0.pos, plate_0.size = (128, 610), (50, 50)
                plate_1.pos, plate_1.size = (188, 610), (50, 50)
            if entry_lengths[0] == 3:
                plate_0.pos, plate_0.size = (96, 610), (50, 50)
                plate_1.pos, plate_1.size = (156, 610), (50, 50)
                plate_2.pos, plate_2.size = (216, 610), (50, 50)
            if entry_lengths[0] == 4:
                plate_0.pos, plate_0.size = (65, 610), (50, 50)
                plate_1.pos, plate_1.size = (125, 610), (50, 50)
                plate_2.pos, plate_2.size = (185, 610), (50, 50)
                plate_3.pos, plate_3.size = (245, 610), (50, 50)
            if entry_lengths[0] == 5:
                plate_0.pos, plate_0.size = (45, 610), (50, 50)
                plate_1.pos, plate_1.size = (100, 610), (50, 50)
                plate_2.pos, plate_2.size = (155, 610), (50, 50)
                plate_3.pos, plate_3.size = (210, 610), (50, 50)
                plate_4.pos, plate_4.size = (265, 610), (50, 50)
            if entry_lengths[0] == 6:
                plate_0.pos, plate_0.size = (100, 610), (40, 40)
                plate_1.pos, plate_1.size = (140, 610), (40, 40)
                plate_2.pos, plate_2.size = (180, 610), (40, 40)
                plate_3.pos, plate_3.size = (220, 610), (40, 40)
                plate_4.pos, plate_4.size = (260, 610), (40, 40)
                plate_5.pos, plate_5.size = (300, 610), (40, 40)
            if entry_lengths[1] == 2:
                plate_6.pos, plate_6.size = (128, 540), (50, 50)
                plate_7.pos, plate_7.size = (188, 540), (50, 50)
            if entry_lengths[1] == 3:
                plate_6.pos, plate_6.size = (96, 540), (50, 50)
                plate_7.pos, plate_7.size = (156, 540), (50, 50)
                plate_8.pos, plate_8.size = (216, 540), (50, 50)
            if entry_lengths[1] == 4:
                plate_6.pos, plate_6.size = (65, 540), (50, 50)
                plate_7.pos, plate_7.size = (125, 540), (50, 50)
                plate_8.pos, plate_8.size = (185, 540), (50, 50)
                plate_9.pos, plate_9.size = (245, 540), (50, 50)
            if entry_lengths[1] == 5:
                plate_6.pos, plate_6.size = (45, 540), (50, 50)
                plate_7.pos, plate_7.size = (100, 540), (50, 50)
                plate_8.pos, plate_8.size = (155, 540), (50, 50)
                plate_9.pos, plate_9.size = (210, 540), (50, 50)
                plate_10.pos, plate_10.size = (265, 540), (50, 50)
            if entry_lengths[1] == 6:
                plate_6.pos, plate_6.size = (100, 550), (40, 40)
                plate_7.pos, plate_7.size = (140, 550), (40, 40)
                plate_8.pos, plate_8.size = (180, 550), (40, 40)
                plate_9.pos, plate_9.size = (220, 550), (40, 40)
                plate_10.pos, plate_10.size = (260, 550), (40, 40)
                plate_11.pos, plate_11.size = (300, 550), (40, 40)
            if entry_lengths[2] == 2:
                plate_12.pos, plate_12.size = (128, 470), (50, 50)
                plate_13.pos, plate_13.size = (188, 470), (50, 50)
            if entry_lengths[2] == 3:
                plate_12.pos, plate_12.size = (96, 470), (50, 50)
                plate_13.pos, plate_13.size = (156, 470), (50, 50)
                plate_14.pos, plate_14.size = (216, 470), (50, 50)
            if entry_lengths[2] == 4:
                plate_12.pos, plate_12.size = (65, 470), (50, 50)
                plate_13.pos, plate_13.size = (125, 470), (50, 50)
                plate_14.pos, plate_14.size = (185, 470), (50, 50)
                plate_15.pos, plate_15.size = (245, 470), (50, 50)
            if entry_lengths[2] == 5:
                plate_12.pos, plate_12.size = (45, 470), (50, 50)
                plate_13.pos, plate_13.size = (100, 470), (50, 50)
                plate_14.pos, plate_14.size = (155, 470), (50, 50)
                plate_15.pos, plate_15.size = (210, 470), (50, 50)
                plate_16.pos, plate_16.size = (265, 470), (50, 50)
            if entry_lengths[2] == 6:
                plate_12.pos, plate_12.size = (50, 480), (40, 40)
                plate_13.pos, plate_13.size = (110, 480), (40, 40)
                plate_14.pos, plate_14.size = (170, 480), (40, 40)
                plate_15.pos, plate_15.size = (230, 480), (40, 40)
                plate_16.pos, plate_16.size = (290, 480), (40, 40)
                plate_17.pos, plate_17.size = (350, 480), (40, 40)
            if entry_lengths[3] == 2:
                plate_18.pos, plate_18.size = (128, 400), (50, 50)
                plate_19.pos, plate_19.size = (188, 400), (50, 50)
            if entry_lengths[3] == 3:
                plate_18.pos, plate_18.size = (96, 400), (50, 50)
                plate_19.pos, plate_19.size = (156, 400), (50, 50)
                plate_20.pos, plate_20.size = (216, 400), (50, 50)
            if entry_lengths[3] == 4:
                plate_18.pos, plate_18.size = (65, 400), (50, 50)
                plate_19.pos, plate_19.size = (125, 400), (50, 50)
                plate_20.pos, plate_20.size = (185, 400), (50, 50)
                plate_21.pos, plate_21.size = (245, 400), (50, 50)
            if entry_lengths[3] == 5:
                plate_18.pos, plate_18.size = (45, 400), (50, 50)
                plate_19.pos, plate_19.size = (100, 400), (50, 50)
                plate_20.pos, plate_20.size = (155, 400), (50, 50)
                plate_21.pos, plate_21.size = (210, 400), (50, 50)
                plate_22.pos, plate_22.size = (265, 400), (50, 50)
            if entry_lengths[3] == 6:
                plate_18.pos, plate_18.size = (50, 410), (40, 40)
                plate_19.pos, plate_19.size = (95, 410), (40, 40)
                plate_20.pos, plate_20.size = (140, 410), (40, 40)
                plate_21.pos, plate_21.size = (185, 410), (40, 40)
                plate_22.pos, plate_22.size = (230, 410), (40, 40)
                plate_23.pos, plate_23.size = (275, 410), (40, 40)
'''
        if len(entry_lengths) == 5:
            if entry_lengths[0] == 2:
                plate_0.pos, plate_0.size = (128, 610), (40, 40)
                plate_1.pos, plate_1.size = (188, 610), (40, 40)
            if entry_lengths[0] == 3:
                plate_0.pos, plate_0.size = (96, 610), (40, 40)
                plate_1.pos, plate_1.size = (156, 610), (40, 40)
                plate_2.pos, plate_2.size = (216, 610), (40, 40)
            if entry_lengths[0] == 4:
                plate_0.pos, plate_0.size = (65, 610), (40, 40)
                plate_1.pos, plate_1.size = (125, 610), (40, 40)
                plate_2.pos, plate_2.size = (185, 610), (40, 40)
                plate_3.pos, plate_3.size = (245, 610), (40, 40)
            if entry_lengths[0] == 5:
                plate_0.pos, plate_0.size = (45, 610), (40, 40)
                plate_1.pos, plate_1.size = (100, 610), (40, 40)
                plate_2.pos, plate_2.size = (155, 610), (40, 40)
                plate_3.pos, plate_3.size = (210, 610), (40, 40)
                plate_4.pos, plate_4.size = (265, 610), (40, 40)
            if entry_lengths[0] == 6:
                plate_0.pos, plate_0.size = (100, 610), (40, 40)
                plate_1.pos, plate_1.size = (140, 610), (40, 40)
                plate_2.pos, plate_2.size = (180, 610), (40, 40)
                plate_3.pos, plate_3.size = (220, 610), (40, 40)
                plate_4.pos, plate_4.size = (260, 610), (40, 40)
                plate_5.pos, plate_5.size = (300, 610), (40, 40)
            if entry_lengths[1] == 2:
                plate_6.pos, plate_6.size = (128, 540), (40, 40)
                plate_7.pos, plate_7.size = (188, 540), (40, 40)
            if entry_lengths[1] == 3:
                plate_6.pos, plate_6.size = (96, 540), (40, 40)
                plate_7.pos, plate_7.size = (156, 540), (40, 40)
                plate_8.pos, plate_8.size = (216, 540), (40, 40)
            if entry_lengths[1] == 4:
                plate_6.pos, plate_6.size = (65, 540), (40, 40)
                plate_7.pos, plate_7.size = (125, 540), (40, 40)
                plate_8.pos, plate_8.size = (185, 540), (40, 40)
                plate_9.pos, plate_9.size = (245, 540), (40, 40)
            if entry_lengths[1] == 5:
                plate_6.pos, plate_6.size = (45, 540), (40, 40)
                plate_7.pos, plate_7.size = (100, 540), (40, 40)
                plate_8.pos, plate_8.size = (155, 540), (40, 40)
                plate_9.pos, plate_9.size = (210, 540), (40, 40)
                plate_10.pos, plate_10.size = (265, 540), (40, 40)
            if entry_lengths[1] == 6:
                plate_6.pos, plate_6.size = (100, 550), (40, 40)
                plate_7.pos, plate_7.size = (140, 550), (40, 40)
                plate_8.pos, plate_8.size = (180, 550), (40, 40)
                plate_9.pos, plate_9.size = (220, 550), (40, 40)
                plate_10.pos, plate_10.size = (260, 550), (40, 40)
                plate_11.pos, plate_11.size = (300, 550), (40, 40)
            if entry_lengths[2] == 2:
                plate_12.pos, plate_12.size = (128, 470), (40, 40)
                plate_13.pos, plate_13.size = (188, 470), (40, 40)
            if entry_lengths[2] == 3:
                plate_12.pos, plate_12.size = (96, 470), (40, 40)
                plate_13.pos, plate_13.size = (156, 470), (40, 40)
                plate_14.pos, plate_14.size = (216, 470), (40, 40)
            if entry_lengths[2] == 4:
                plate_12.pos, plate_12.size = (65, 470), (40, 40)
                plate_13.pos, plate_13.size = (125, 470), (40, 40)
                plate_14.pos, plate_14.size = (185, 470), (40, 40)
                plate_15.pos, plate_15.size = (245, 470), (40, 40)
            if entry_lengths[2] == 5:
                plate_12.pos, plate_12.size = (45, 470), (40, 40)
                plate_13.pos, plate_13.size = (100, 470), (40, 40)
                plate_14.pos, plate_14.size = (155, 470), (40, 40)
                plate_15.pos, plate_15.size = (210, 470), (40, 40)
                plate_16.pos, plate_16.size = (265, 470), (40, 40)
            if entry_lengths[2] == 6:
                plate_12.pos, plate_12.size = (50, 480), (40, 40)
                plate_13.pos, plate_13.size = (110, 480), (40, 40)
                plate_14.pos, plate_14.size = (170, 480), (40, 40)
                plate_15.pos, plate_15.size = (230, 480), (40, 40)
                plate_16.pos, plate_16.size = (290, 480), (40, 40)
                plate_17.pos, plate_17.size = (350, 480), (40, 40)
            if entry_lengths[3] == 2:
                plate_18.pos, plate_18.size = (128, 400), (40, 40)
                plate_19.pos, plate_19.size = (188, 400), (40, 40)
            if entry_lengths[3] == 3:
                plate_18.pos, plate_18.size = (96, 400), (40, 40)
                plate_19.pos, plate_19.size = (156, 400), (40, 40)
                plate_20.pos, plate_20.size = (216, 400), (40, 40)
            if entry_lengths[3] == 4:
                plate_18.pos, plate_18.size = (65, 400), (40, 40)
                plate_19.pos, plate_19.size = (125, 400), (40, 40)
                plate_20.pos, plate_20.size = (185, 400), (40, 40)
                plate_21.pos, plate_21.size = (245, 400), (40, 40)
            if entry_lengths[3] == 5:
                plate_18.pos, plate_18.size = (45, 400), (40, 40)
                plate_19.pos, plate_19.size = (100, 400), (40, 40)
                plate_20.pos, plate_20.size = (155, 400), (40, 40)
                plate_21.pos, plate_21.size = (210, 400), (40, 40)
                plate_22.pos, plate_22.size = (265, 400), (40, 40)
            if entry_lengths[3] == 6:
                plate_18.pos, plate_18.size = (50, 410), (40, 40)
                plate_19.pos, plate_19.size = (95, 410), (40, 40)
                plate_20.pos, plate_20.size = (140, 410), (40, 40)
                plate_21.pos, plate_21.size = (185, 410), (40, 40)
                plate_22.pos, plate_22.size = (230, 410), (40, 40)
                plate_23.pos, plate_23.size = (275, 410), (40, 40)
            if entry_lengths[4] == 3:
                plate_24.pos, plate_24.size = (96, 400), (40, 40)
                plate_25.pos, plate_25.size = (156, 400), (40, 40)
                plate_26.pos, plate_26.size = (216, 400), (40, 40)
            if entry_lengths[4] == 4:
                plate_24.pos, plate_24.size = (65, 400), (40, 40)
                plate_25.pos, plate_25.size = (125, 400), (40, 40)
                plate_26.pos, plate_26.size = (185, 400), (40, 40)
                plate_27pos, plate_27.size = (245, 400), (40, 40)
            if entry_lengths[4] == 5:
                plate_24.pos, plate_24.size = (45, 400), (40, 40)
                plate_25.pos, plate_25.size = (100, 400), (40, 40)
                plate_26.pos, plate_26.size = (155, 400), (40, 40)
                plate_27.pos, plate_27.size = (210, 400), (40, 40)
                plate_28.pos, plate_28.size = (265, 400), (40, 40)
            if entry_lengths[4] == 6:
                plate_24.pos, plate_24.size = (50, 410), (40, 40)
                plate_25.pos, plate_25.size = (95, 410), (40, 40)
                plate_26.pos, plate_26.size = (140, 410), (40, 40)
                plate_27.pos, plate_27.size = (185, 410), (40, 40)
                plate_28.pos, plate_28.size = (230, 410), (40, 40)
                plate_29.pos, plate_29.size = (275, 410), (40, 40)
'''
    def on_start(self):
        self.letter_block_entrance()
        self.letter_plate_entrance()
        Clock.schedule_interval(self.shuffle_letters, 1/2)


WPUrbanApp().run()
