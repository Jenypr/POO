n = 100
maior = 0
posicao = 0
for i in range(1, n + 1):
    valor = int(input())
    if valor > maior:
        maior = valor
        posicao = i
print(maior)
print(posicao)