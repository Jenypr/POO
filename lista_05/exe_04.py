def aprovado(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 60:
        return True
    else:
        return False

nota1 = float(input("Digite a nota do primeiro bimestre: "))
nota2 = float(input("Digite a nota do segundo bimestre: "))

if aprovado(nota1, nota2):
    print("Aprovado!")
else:
    print("Em prova final!")