# --------AULA 09 ---- manipulando textos------
frase = 'curso em video'
print(frase[3:15:2])

# print('''hojeeu comi pão com ovo,
# no café, e depois , no almoço, comi arroz
# e feijão com bife acebolado''')

frase1 = 'Curso em Video Python'
print(frase.upper().count('O'))

frase2 = 'curso em video python'
print(len(frase.strip()))

frase02 = 'curso em video python'
print('curso' in frase02)

frase3 = 'curso em video python'
print(frase.replace('curso', 'Android'))

frase4 = 'curso en video python'
frase5 = frase.replace('video' , 'Android')
print(frase5)

frase6 = 'curso em video'
dividido = frase.split()
print(dividido[0][3])

# -------------FIM DA AULA09-------------