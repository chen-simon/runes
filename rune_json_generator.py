# i = input("English text:")

eng = "abcdefghijklmnopqrstuvwxyz"
rune = "ᚫᛒᚳᛞᛖᚠᛡᚻᛁᛡᚴᛚᛗᚾᛟᛈᛩᚱᛋᛏᚢᚡᚹᛉᚣᛣ"

print('{')
for i, letter in enumerate(eng):
    print(f"    '{letter}': ('{rune[i]}', lambda x : 0),")
print('}')