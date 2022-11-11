alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

word = input("word to be encrypted: ")
key = int(input("Key to be used: "))

encrypted = word.upper()

for i in range(encrypted):
    if i - key < 0:
        i = len(alfabeto) - i
    encrypted[i] = alfabeto[alfabeto.find(encrypted[i]) - 1]

print(encrypted.lower())