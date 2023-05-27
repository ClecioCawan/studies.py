#----Aula014------------- VARIOS VALORES V.1----------------------------------#
n = int(input('Digite um número: [para parar use 999] '))
n = contador = soma = 0

while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um número: [para parar use 999] '))
print(f'Você digitou {contador} números e a soma entre eles é {soma}.')   
#-----------------------------------FIM-------------------------------------------#