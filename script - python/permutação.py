#------------------------CALCULADORA DE PERMUTAÇÃO ------------------------------------------ #
# simples   == Pn = n! ---> sendo (n) o numero de elementos
# repetição == P(n/a) = n! / a! --> sendo (n) o numero de elemmentos, e (a) o úmero de repetções
from math import factorial

n_elementos = int(input('Digite o total de elementos (letras) da palavra: '))
repeticao = input('Existe repetções? [ S ] [ N ] ').upper().strip()

p_simples = factorial (n_elementos)
# p_repeticao = p_simples / factorial(n_repetidos)

if repeticao == 'S':
    n_repetidos = int(input('Quantas são: '))
    
    p_repeticao = p_simples / factorial(n_repetidos)

    print(f'Voçê Fez uma Permutação com Repetição, o resultado é {p_repeticao} ')

else:
    print(f'Voçê fez uma Permutação Simples, o resultado é {p_simples}')
# -----------------------------------FIM--------------------------------------------------------- #