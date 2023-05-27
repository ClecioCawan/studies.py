# Analisando TEXTOS

n = str(input('Digite o seu nome completo: ')).strip()
espacos = (n.count(' '))
primeiro = n.find(' ')
print('Analisando seu nome...')
print(f'Seu nome completo em maiusculas é {n.upper()}')
print(f'Seu nome completo em minusculas é {n.lower()}')
print(f'Seu nome tem ao todo {len(n) - espacos} letras')
print(f'Seu primeiro nome tem {primeiro} letras.')