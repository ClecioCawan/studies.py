# ----------------------Analizador completo ------------------ #
soma_idade = 0
media_idade = 0
idade_homen_velho = 0
nome_velho = 0
total_mulhere_20 = 0
for c in range (1, 5):
    print(f'>>>>>>>>PESSOA {c}<<<<<<<<<<<<<<')
    nome = str(input('Digite o nome: ')).strip().upper()
    idade = int(input('Digite a idade '))
    sexo = str (input('Digite o sexo: [M / F]')).strip().upper()

    soma_idade += idade
    
    if c == 1 and sexo == 'M':
        idade_homen_velho = idade
        nome_velho = nome

    elif sexo == 'M' and idade > idade_homen_velho:
        idade_homen_velho = idade
        nome_velho = nome

    elif sexo == 'F' and idade < 20:
        total_mulhere_20 += 1

media_idade = soma_idade / 4

print(f'A media da idade de todas as pessoas {media_idade}')
print(f'O homen mais velho tem {idade_homen_velho} anos e se chama {nome_velho}')
print(f'AO todo tem {total_mulhere_20} mulheres menores de 20 anos')
