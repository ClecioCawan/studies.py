horas_atividade = float(input("Digite o número de horas que você passou realizando atividade física por mês: "))

if horas_atividade <= 10: 
    pontos = horas_atividade * 2
    fatura = pontos * 0.05
    print(f"Você fez atividade física por {horas_atividade} horas.\nAcumulou {pontos} pontos.\nFaturou R${fatura}")

elif horas_atividade > 10 and horas_atividade <= 20:
    pontos = horas_atividade * 5
    fatura = pontos * 0.05
    print(f"Você fez atividade física por {horas_atividade} horas.\nAcumulou {pontos} pontos.\nFaturou R${fatura}")

elif horas_atividade > 20:
    pontos = horas_atividade * 10
    fatura = pontos * 0.05
    print(f"Você fez atividade física por {horas_atividade} horas.\nAcumulou {pontos} pontos.\nFaturou R${fatura}")


