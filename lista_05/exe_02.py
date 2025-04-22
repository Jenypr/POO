def maior(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

maior_numero = maior(n1, n2, n3)

print("O maior número é:", maior_numero)