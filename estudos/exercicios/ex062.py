#---aula014--------------------GERADOR DE PA V.3---------------------------------#
print('''
##########################
       GERADOR DE P.A (V.3)
##########################
''')

n_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))

termo = n_termo
contador = 1
total_termos = 0
mais_termos = 10

while mais_termos != 0:

    total_termos += mais_termos

    while contador <= total_termos:
        print(f'{termo} -> ', end='')
        termo += razao
        contador += 1
    print('pausa')
    mais_termos = int(input('QUANTOS termos voçê quer mostrar mais?: '))
print('FIM')
#--------------------------------------FIM---------------------------#