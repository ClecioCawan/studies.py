# ----------------CUSTTO DA VIAGEM--------------------------- #
d = float(input('Digite a distância da sua viagem:'))
p = d * 0.50
l = d * 0.45
if d > 200:
    print(f'O preço da sua passagem de {d}Km vale R${p:.2f}')
else:
    print(f'O preço da sua passagem de {d}Km vale R${l:.2f}')
# ---------------------FIM----------------------------------- #