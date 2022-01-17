# i = input("English text:")

eng = "abcdefghijklmnopqrstuvwxyz"
rune = "ᚪᛒᚳᛞᛖᚠᚷᚻᛁᛡkᛚᛗᚾᚩᛈqᚱᛋᛏᚢvᚹᛉᚣz"

print('{')
for i, letter in enumerate(eng):
    print(f"    '{letter}': '{rune[i]}',")
print('}')