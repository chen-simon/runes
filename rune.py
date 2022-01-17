rune = {
    'a': 'ᚪ',
    'b': 'ᛒ',
    'c': 'ᚳ',
    'd': 'ᛞ',
    'e': 'ᛖ',
    'f': 'ᚠ',
    'g': 'ᚷ',
    'h': 'ᚻ',
    'i': 'ᛁ',
    'j': 'ᛡ',
    'k': 'K',
    'l': 'ᛚ',
    'm': 'ᛗ',
    'n': 'ᚾ',
    'o': 'ᚩ',
    'p': 'ᛈ',
    'q': 'Q',
    'r': 'ᚱ',
    's': 'ᛋ',
    't': 'ᛏ',
    'u': 'ᚢ',
    'v': 'V',
    'w': 'ᚹ',
    'x': 'ᛉ',
    'y': 'ᚣ',
    'z': 'Z',
}

while True:
    inp = input("\nEnter text: ")

    for char in inp:
        if char in rune:
            print(rune[char.lower()], end='')
        else:
            print(char, end='')
