from random import shuffle
a1 = str(input('Digite o nome do PRIMEIRO aluno:')) 
a2 = str(input('Digite o nome do SEGUNDO aluno:'))
a3 = str(input('Digite o nome do TERCEIRO aluno:'))
a4 = str(input('Digite o nome do QUARTO aluno:'))
lista = [a1, a2 , a3 , a4]
shuffle( lista )
print(f'A ordem apresentada será:')
print(lista)