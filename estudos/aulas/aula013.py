# o ultimo numero nao conta

print('''for conte in range (1, 6):
    print('olá, mundo')
print('Caboçe')''')

# para conta pra traz

print('''for conte in range (6, 0, -1):
    print(conte)
print('olá, mundo')''')

# para conta de 2 em 2
print('''for conte in range(0, 9, 2):
    print(conte)
print('caboçe')''')

# contador
print('''n = int(input('DIGITE UM NUMERO:')
for conte in range (0, n + 1):
    print(conte)''')

# contador pulando...
print('''i = int(input('INICIO:')
f = int(input('FINAL:'))
p = int(input('PULOS:'))
for conte in range(i, f + 1, p ):
    print(conte)
print('FIM')''')

# somatorio com (for)
s = 0
for conte in range (0, 4):
    n = int(input('DIGITE UM NUMERO:'))
    s = s + n
print(f'A soma desses valores é {s}')