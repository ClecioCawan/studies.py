#-----------------MÉDIA V.2---------------------------------------------------------#
b1 = float(input('Digite a sua primeira nota:'))
b2 = float(input('Digite a sua segunda nota :'))
m = (b1 + b2) /2
print(f'Você tirou {b1} no primeiro e {b2} no segundo bimestre, a sua media foi {m}.')

if m >= 6.0:
    print('VOCÊ ESTA APROVADO!!!')

elif m <= 5.9 and m >= 5.0:
    print('VOCÊ VAI PRA RECUPERAÇÃO!!!')
elif m < 5.0:
    print('VOCÊ ESTA REPOVADO!!!')
#-----------------------------------FIM-----------------------------------------------#