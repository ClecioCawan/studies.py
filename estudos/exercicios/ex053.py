# ----------------- DETECTOR DE PALÍNDROMO ------------------ #
frase = input("Qual a frase? ").strip().upper() # para tira os espaços e colocar em maiúsculo
palavra = frase.strip() # para gerar um lista
juntar = ''.join(palavra) # para juntar sem espaços antes nem depois nem entre.
inverso = '' 

for c in range (len(juntar) - 1, - 1, - 1):
    inverso += juntar [c] # fazer a inversão da frase

print(f'O inverso de {juntar} é {inverso}')

if inverso == juntar:
    print('ISSO E UM PALÍNDROMO!') 

else:
    print('ISSO NÃO E UM PALÍNDROMO!')