from character import Character

dice = [5, 4, 3, 3, 2, 1]
for r in ['boar', 'weasel', 'goat', 'raccoon']:
    print(Character.generate_character([r], dice))
