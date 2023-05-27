from random import choice

a1 = input('Digite o nome do PRIMEIRO aluno:')
a2 = input('Digite o nome do SEGUNDO aluno:')
a3 = input('Digite o nome do TERCEIRO aluno:')
a4 = input('Digite o nome do QUARTO aluno:')
a5 = input('Digite o nome do QUINTO aluno:')
lista = [a1, a2, a3, a4, a5]
escolhido = choice(lista)
print(f'O aluno escolhido foi {escolhido}')