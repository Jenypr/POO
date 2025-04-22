frase = input('Digite uma frase: ')
i = 0
while frase[i] != ' ':
    i += 1
i += 1
while i < len(frase):
    print(frase[i], end='')
    i += 1