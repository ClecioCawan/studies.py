#----aula014----------GERADOR DE PA V2---------------------#
print('''
##########################
       GERADOR DE P.A (V.2)
##########################
''')

n_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
termo = n_termo
contador = 1

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1

print('FIM')
#--------------------------------------FIM---------------------------#