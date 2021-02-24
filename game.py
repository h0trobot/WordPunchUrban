from random import randint, sample
from itertools import permutations
import concurrent.futures
import json


class Game:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.level_data = {
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
        self.DICTIONARY = []

        # extract words, i.e. dictionary keys from words_dictionary.json
        with open('words_dictionary.json') as json_file:
            j_d = json_file.read()

        data = json.loads(j_d)
        self.dictionary = list(dict.keys(data))

        # excerpt words of length, 2-8 characters from dictionary list for main dictionary, DICTIONARY

        def by_size(words, size):
            return [word for word in words if len(word) == size]

        for i in range(3, 7):
            dicty = by_size(self.dictionary, i)
            self.DICTIONARY.extend(dicty)

        self.alphabet = [
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                    'V', 'W', 'X', 'Y', 'Z'
        ]

        self.user_answer = []
        self.unscrambled_words = []
        self.answer_perms = permutations(self.user_answer)

        '''
        using a random word taken from DICTIONARY, generate a string for current level and find all valid words from 
        permutations of chosen word. for_loop() iterates through each letter of each permutation, adding the next
        character successively and searching for a match in DICTIONARY
        '''

        case_word = self.DICTIONARY[randint(0, 55532)]
        case_word_list = []
        for char in case_word:
            case_word_list.append(char)

        case_word_perms = permutations(case_word_list)
        perms_list = []
        for p in case_word_perms:
            perms_list.append(p)

        def for_loop(perm):
            for chr in range(len(perm)):
                chars = perm[:chr + 1]
                possible_word = ''.join(chars)
                if possible_word in self.dictionary and possible_word not in self.level_data['valid entries'] and len(possible_word) > 1:
                    self.level_data['valid entries'].append(possible_word)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(for_loop, perms_list)

        self.random_string_for_level = list(perms_list[0])
        self.level_data['random string for level'] = self.random_string_for_level
        self.number_of_letter_blocks = len(self.random_string_for_level)
        self.valid_entries = self.level_data['valid entries']

        if len(self.valid_entries) > 5:
            for i in range(0, self.level_data['required entries last index']):
                n = randint(0, len(self.valid_entries) - 1)
                self.level_data['required entries'].append(self.valid_entries[n])
        elif len(self.valid_entries) <= 5:
            for i in range(0, 3):
                n = randint(0, len(self.valid_entries) - 1)
                self.level_data['required entries'].append(self.valid_entries[n])

        main_word = max(self.valid_entries, key=len)

        if main_word not in self.level_data['required entries']:
            self.level_data['required entries'].append(main_word)

        required_entries = self.level_data['required entries']

        # append the lengths of each required entry to entry_lengths. Not sure what this is useful for for now however.
        for entry in range(len(required_entries)):
            self.level_data['entry lengths'].append(len(required_entries[entry]))

        self.level_data['entry lengths'] = sorted(self.level_data['entry lengths'])
