# -------------------- VALIDAÇÃO DE DADOS -------------------------------------------- #
sexo = str(input('Informe o seu sexo: [ M / F ]')).strip().upper() [0]

while sexo not in 'MF': # o (not in) siguinifica "não estiver entre...."
    sexo = str(input('Dados inválidos, POR FAVOR tente novamente:')).strip().upper() [0]

print(f'SEXO {sexo} registrado')