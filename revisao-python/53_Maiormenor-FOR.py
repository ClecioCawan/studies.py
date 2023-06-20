maior_peso = 0
menor_peso = 0

for c in range (1, 6):
    peso_pessoa = float(input(f"Digite o peso da {c}° Pessoa: "))
    if c == 1:#validando o primeiro termo como maior_peso e menor_peso
        #passar as 2 variaveis para dentro do laço
        maior_peso = peso_pessoa
        menor_peso = peso_pessoa

    else: #verificando os outros termos
        if peso_pessoa > maior_peso:
            maior_peso = peso_pessoa

        if peso_pessoa < menor_peso:
            menor_peso = peso_pessoa

print(f"O MAIOR peso lido foi o de {maior_peso}\nO MENOR peso lido foi o de {menor_peso}")


