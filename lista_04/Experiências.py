n = int(input())
total_coelhos = 0
total_ratos = 0
total_sapos = 0

for i in range(n):
    quant, tipo = input().split()
    quant = int(quant)
    if tipo == 'C':
        total_coelhos += quant
    elif tipo == 'R':
        total_ratos += quant
    else:
        total_sapos += quant

total_cobaias = total_coelhos + total_ratos + total_sapos

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")

percentual_coelhos = (total_coelhos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_sapos = (total_sapos / total_cobaias) * 100

print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")