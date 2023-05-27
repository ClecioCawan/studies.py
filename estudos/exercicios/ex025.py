# -------PROCURANDO STRING DENTRO DE OUTRA-------- #
n = str(input('Qual o seu nome completo?')).strip()
tf = 'silva' in n.lower()
print(f'O seu nome tem Silva? {tf}')
# --------------------FIM------------------------  #