from datetime import date

atual  = date.today().year
ano = int(input('Digite o ano do seu nascimento:'))
idade = (atual - ano)  

print(f'VOCÊ TEM {idade} ANOS!!!')

if idade < 9:
    print('CLASSIFICAÇÃO : MIRIM !!!')

elif idade > 9 and idade <= 15:
    print('CLASSIFICAÇÃO :INFANTIL !!!')

elif idade > 15 and idade <= 19:
    print('CLASSIFICAÇÃO : JUNIOR !!!') 

elif idade >= 19 and idade <= 25:
    print('CLASSIFICAÇÃO : SÊNIOR !!!')

elif idade > 25:
    print('CLASSIFICAÇÃO : MASTER !!!')
