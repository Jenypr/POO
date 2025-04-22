def maior(x, y):
    if x > y:
        return x
    else:
        return y

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

maior_numero = maior(n1, n2)
print("O maior número é:", maior_numero)