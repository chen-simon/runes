import codecs

def default(state):
    return ('', 0, '')

def g(state):
    if state == 'in':
        return ('', 2, 'ᛝ')
    elif state == 'ou':
        return ('oug', 0, '')
    else:
        return ('', 0, '')

def h(state):
    if state == 't':
        return ('', 0, 'ᚦ')
    elif state == 'oug':
        return ('', 0, 'ᛟ')
    else:
        return ('', 0, '') 

def i(state):
    return (2, 0, '') 

def n(state):
    return (3, 0, '') if state == 2 else (0, 0, '')

def o(state):
    return ('o', 0, '')

def t(state):
    return ('t', 0, 'ᛏ')

rune = {
    'a': ('ᚫ', default),
    'b': ('ᛒ', default),
    'c': ('ᚳ', default),
    'd': ('ᛞ', default),
    'e': ('ᛖ', default),
    'f': ('ᚠ', default),
    'g': ('ᚷ', g),
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
    'state': ('ᛉ', default),
    'y': ('ᚣ', default),
    'z': ('ᛣ', default),
    '.': ('᛫', default),
    ',': (',', default),
    ' ': (' ', default),
    '!': ('!', default),
    '?': ('?', default),
}

ignore = {"'", "-"}

raw_testatet = ''
with codecs.open('input.tstatet', 'r', 'utf-8-sig') as f:
    raw_testatet = f.read()

parsed, state = '', 0
for char in raw_testatet:
    l_char = char.lower()
    if l_char in rune:
        parsed += rune[l_char][0]
        updates = rune[l_char][1](state)

        state = updates[0]  # Update state
        if updates[1] != 0:
            parsed = parsed[:-updates[1]]   # Remove state characters
        parsed += updates[2]  # Add state character

    elif l_char not in ignore:
        parsed += char

with codecs.open('output.tstatet', 'w', 'utf-8-sig') as f:
    f.write(parsed)
