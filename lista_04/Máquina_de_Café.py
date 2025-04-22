a1 = int(input())
a2 = int(input())
a3 = int(input())

tempo_andar1 = 2 * a2 + 4 * a3
tempo_andar2 = 2 * a1 + 2 * a3
tempo_andar3 = 4 * a1 + 2 * a2

tempo_minimo = min(tempo_andar1, tempo_andar2, tempo_andar3)

print(tempo_minimo)