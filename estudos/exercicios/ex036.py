#---------APROVANDO IMPRESTIMO------------------------------#
valor = float(input('Digite o valor da casa : R$'))
salario = float(input('Digite o valor do seu salário : R$'))
anos = float(input('Quantos anos você vai pagar :'))
prestacao = valor / (anos * 12)
minimo = (salario * 30/100)
print(f'Para pagar uma casa de R$ {valor:.2f} em {anos}')
print(f'Você irá pagar R$ {prestacao:.2f} por mês!')
if prestacao <= minimo:
    print('EMPRESTIO CONSEDIDO')
else:
    print('EMPRESTIMO NEGADO')
#----------------------FIM---------------------------------#