# --------------------------- GRUPO DA MAIORIDADE ---------------------------- #
from datetime import date

atual = date.today().year
total_maiores = 0 # Contador de maiores 
total_menores = 0 # Contador de menores

for p in range (1, 6):
    ano_pessoa = int(input(f'Digite o ano do nascimento da {p} pessoa:'))
    idade_pessoa = atual - ano_pessoa

    if idade_pessoa >= 21:
        total_maiores += 1 # Contador de maiores 

    else:
        total_menores += 1 # Contador de menores

print(f'{total_maiores} são maiores de idade')
print(f'{total_menores} são menores de idade')
