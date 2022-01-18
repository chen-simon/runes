import codecs

def default(x):
    return (0, 0, '')

def t(x):
    return (1, 0, '') 

def h(x):
    return (0, 2, 'ᚦ') if x == 1 else (0, 0, '')

def i(x):
    return (2, 0, '') 

def n(x):
    return (3, 0, '') if x == 2 else (0, 0, '')

def g(x):
    return (0, 3, 'ᛝ') if x == 3 else (0, 0, '')

rune = {
    'a': ('ᚫ', default),
    'b': ('ᛒ', default),
    'c': ('ᚳ', default),
    'd': ('ᛞ', default),
    'e': ('ᛖ', default),
    'f': ('ᚠ', default),
    'g': ('ᛡ', g),
    'h': ('ᚻ', h),
    'i': ('ᛁ', i),
    'j': ('ᛡ', default),
    'k': ('ᚴ', default),
    'l': ('ᛚ', default),
    'm': ('ᛗ', default),
    'n': ('ᚾ', n),
    'o': ('ᛟ', default),
    'p': ('ᛈ', default),
    'q': ('ᛩ', default),
    'r': ('ᚱ', default),
    's': ('ᛋ', default),
    't': ('ᛏ', t),
    'u': ('ᚢ', default),
    'v': ('ᚡ', default),
    'w': ('ᚹ', default),
    'x': ('ᛉ', default),
    'y': ('ᚣ', default),
    'z': ('ᛣ', default),
    '.': ('᛫', default),
}

raw_text = ''
with codecs.open('input.txt', 'r', 'utf-8-sig') as f:
    raw_text = f.read()

parsed, state = '', 0
for char in raw_text:
    if char in rune:
        parsed += rune[char][0]
        updates = rune[char][1](state)

        state = updates[0]  # Update state
        if updates[1] != 0:
            parsed = parsed[:-updates[1]]   # Remove state characters
        parsed += updates[2]  # Add state character

    else:
        parsed += char

with codecs.open('output.txt', 'w', 'utf-8-sig') as f:
    f.write(parsed)
