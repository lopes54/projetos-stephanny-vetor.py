def calcular_faturamento(vetor):
    # Calcula o menor valor de faturamento
    menor_valor = min(vetor)
    # Calcula o maior valor de faturamento
    maior_valor = max(vetor)
    # Calcula a média mensal
    media_mensal = sum(vetor) / len(vetor)
    # Calcula o número de dias em que o faturamento diário foi superior à média mensal
    dias_acima_media = len([valor for valor in vetor if valor > media_mensal])
    
    return menor_valor, maior_valor, dias_acima_media

# Exemplo de uso do programa com um vetor de faturamento diário
faturamento_diario = [1000, 1500, 800, 1200, 1700, 900, 1100, 1300, 1400, 1600, 1800, 2000]
menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

print("Menor valor de faturamento: R$", menor)
print("Maior valor de faturamento: R$", maior)
print("Dias com faturamento acima da média mensal: ", dias_acima_media)
