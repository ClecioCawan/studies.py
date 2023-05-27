#--------------------GERENCIADOR DE PAGAMENTOS---------------------------------------------------- #
import colorama
from colorama import Fore
from colorama import Style

colorama.init()

print(Fore. RED + Style.BRIGHT + '{:=^40}'.format(' LOJAS AMERICANAS' ) + Style.RESET_ALL)

preço = float(input('Digite o preço das compras:'))
print(Fore.BLUE + Style.BRIGHT + '''FORMAS DE PAGAMENTO

[ 1 ] Á VISTA dinheiro ou cheque!
[ 2 ] Á VISTA cartão!
[ 3 ] 2X no cartão!
[ 4 ] 3X OU MAIS no cartão!''' + Style.RESET_ALL )
opçao = int(input('QUAL A OPÇÃO? :'))

if opçao == 1:
    desconto = preço - (preço * 10 / 100)
    print(f'A SUA COMPRA DE R$ {preço:.2f} VAI TE CUSTAR R$ {desconto:.2f} COM 10% DE DESCONTO!!!')
    print('!!!OBRIGADO PELA PREFERÊNCIA!!!')

elif opçao == 2:
    desconto1 = preço - (preço * 5 / 100)
    print(f'A SUA COMPRA DE R$ {preço:.2f} VAI TE CUSTAR R$ {desconto1:.2f} COM 10% DE DESCONTO!!!')
    print('!!!OBRIGADO PELA PREFERÊNCIA!!!')

elif opçao == 3:
    v2 = (preço / 2)
    print(f'SUA COMPRA FOI PARCELADA EM 2x DE R$ {v2:.2f}')
    print('!!!OBRIGADO PELA PREFERÊNCIA!!!')

elif opçao == 4:
    parcela = int(input('QUANTAS PARCELAS? :'))
    p1 = preço / parcela
    juro = preço + (preço * 20 / 100)
    print(f'SUA COMPRA FOI PARCELADA EM {parcela}x DE R$ {p1}')
    print(f'SUA COMPRA DE {preço} VAI CUSTAR COM 20% DE JUROS R$ {juro} NO FINAL')
#--------------------FIM--------------------------------------------------------------------------- #