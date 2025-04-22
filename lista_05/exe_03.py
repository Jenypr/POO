def iniciais(nome):
    nomes = nome.split()
    iniciais = ""
    for nome in nomes:
        iniciais += nome[0].upper()
    return iniciais

nome_completo = input("Digite seu nome completo: ")
iniciais_nome = iniciais(nome_completo)
print(f"As iniciais do seu nome são: {iniciais_nome}")