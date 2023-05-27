from datetime import date
atual = date.today().year
ano = (int(input('Digite o ano do seu nascimento:')))
idade = atual - ano
print(f'Você nasceu em {ano} tem {idade} anos em {atual}')
if idade == 18:
    print('VOCÊ DEVE SE ALISTAR IMEDIATAMENTE!!!')
elif idade < 18:
    saldo = (18 - idade)
    ano1 = ( atual + saldo )
    print(f'FALTA {saldo} ANOS PARA O SEU ALISTAMENTO MILITAR!!!')
else:
    saldo = (idade - 18)
    ano1 = ( atual - saldo )
    print('O SEU ALISTAMENTO JA PASSOU!!!')
    print(f'VOCÊ DEVERIA TER SE ALISTADO EM {ano1}')