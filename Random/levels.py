'''
t, g, i, f, y = 'T', 'G', 'I', 'F', 'Y'
valid_entry = {
    'tgif': 'meaning1', 'gif': 'meaning2', 'fig': 'meaning3', 'fit': 'meaning4', 'gift': 'meaning5', 'it': 'meaning6',
    'if': 'meaning7', 'fyi':'menaing8'
}
user_input = str(input('Enter word: '))

user_input = user_input.lower()
if user_input in valid_entry:
    print(valid_entry.get(user_input))

else:
    print('Invalid Entry')
'''

letters = {}
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']
for letter in alphabet:
    lett_template = ('Alphabets_2/Letter_Blocks_01_Set_4_{}_64x64.png')
    i = 0
    letters[letter[i]] = lett_template.format(letter[i])
    i += 1
print(letters)

