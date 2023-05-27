#------PRIMEIRA E ÚLTIMA OCORRÊNCIA DE UMA STRING---- #
f = str(input('Digite uma frase:')).strip().upper()
c = f.count('A')
p = f.find('A') +1
u = f.rfind('A') +1
print(f'A letra A aparece {c} vezes ma frase.')
print(f'A primeira letra A aparece na posição {p}.')
print(f'A última letra A pareceu na posição {u} ')
# -------------------FIM----------------------------- #   