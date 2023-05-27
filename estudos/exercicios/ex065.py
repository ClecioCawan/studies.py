#----Aula014----MAior e menor valor----------------------------------#
contador_resposta = 'S'

soma = quantidade_termos = media = maior_valor = menor_valor = 0

# todas as variaveis são iguais a 0

while contador_resposta in 'Ss':

    n = int(input('Digite um valor: '))
    soma += n
    quantidade_termos += 1

    if quantidade_termos == 1:
        maior_valor = menor_valor = n
    
    else:
        if n > maior_valor:
            maior_valor = n
        if n < menor_valor:
            menor_valor = n

    contador_resposta = str(input('Quer continuar?: [S / N]')).upper().strip()
media = soma / quantidade_termos
print(f'Você digitou {quantidade_termos} números e a media é {media}')
#-----------------------Fim----------------------------------------------------------------#