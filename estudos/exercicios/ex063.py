#-------Aula014---------SEQUENCA DE FIBONACCI--------------------#
n = int(input('Digite quantos termos voçê quer mostrar: '))
t1 = 0 # termo 1
t2 = 1 # termo 2

print('~'* 30)
print(f'{t1} =>{t2}', end='')
contador = 3

while contador <= n:
    t3 = t1 + t2 # termo 3
    print(f' => {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
print('=> Fim') 
#----------------------FIM--------------------------------------#