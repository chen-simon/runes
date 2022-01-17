import codecs

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

file_text = ''

for key in rune:
    file_text += f"{key}::\n    thorn := false\n    Send, {rune[key]}\n    Return\n\n"

with codecs.open("rune2.ahk", "w", "utf-8-sig") as f:
    f.write(file_text)
