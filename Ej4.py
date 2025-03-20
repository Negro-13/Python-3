print('Ingrese una plabra para saber si es un palindromo:')
word = input()
index = len(word) -1
wordiv = list(word)
word2div = []
while index >= 0:
    word2div.append(wordiv[index])
    index -= 1
word2 = ''.join(word2div)

if word.lower() == word2.lower():
    print(f'Tu palabra si es un pálindromo: {word.lower()} = {word2.lower()}')
else:
    print(f'La palabra {word} no es un palindromo')
