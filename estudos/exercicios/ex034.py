# --------------AUMENTOS MULTIPLOS-------------- #
s = float(input('Digite o salário do funcionário: R$'))
if s > 1250.00:
    maior = s + (s * 10/100)
    print(f'Você ganhava R$ {s} passou a receber R$ {maior}')
else:
    menor = s + (s * 15/100)
    print(f'Você ganhava R$ {s} passou a receber R$ {menor}')