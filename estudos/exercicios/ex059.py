#-aula014---------------------MENU DE OPÇÕES(CALCULADORA)------------------#
from time import sleep

n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
opçao = 0

print('ESCOLHA DENTRE AS OPÇÕES SEGUINTES')
while opçao != 7:

    print('''
    =======================
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] DIVIDIR
    [ 4 ] POTÊNCIAR
    [ 5 ] SUBTRAIR
    [ 6 ] NOVOS NÚMEROS
    [ 7 ] SAIR DO PROGRAMA
    =======================
    ''')
    opçao = int(input('Digite a sua opção:'))

    if opçao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} e igual a {soma} ')
    elif opçao == 2:
        produto =  n1 * n2
        print(f'A produto entre {n1} e {n2} e igual a {produto} ')
    elif opçao == 3:
        dividisao = n1 / n2
        print(f'A Divisão entre {n1} e {n2} e igual a {dividisao} ')
    elif opçao == 4:
        potencia = n1 ** n2
        print(f'A potênciação entre {n1} e {n2} e igual a {potencia} ')
    elif opçao == 5:
        subtraçao = n1 - n2
        print(f'A subtração entre {n1} e {n2} e igual a {subtraçao} ')
    elif opçao == 6:
        print('INFORME OS NÚMEROS NOVAMENTE:')    
        n1 = int(input('Digite o primeiro número:'))
        n2 = int(input('digite o segundo número:'))
        
    elif opçao == 7:
        print('FINALIZANDO...')
    
    else:
        print('OPÇÃO INVÁLIDA... TENTE NOVAMENTE!')
    sleep(1.5)
print('Fim do programa... !!!VOLTE SEMPRE!!! :)')
#--------------------------------------FIM-------------------------------------------------------#