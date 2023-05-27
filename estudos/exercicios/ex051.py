# ---------------------------PROGRESSÃO ARITIMÉTRICA--------------------- #
print('-=' * 15)
print('   10 TERMOS DE UM P.A')
print('-=' * 15)

primeiro = int(input('Digite o primeiro termo: '))

razão = int(input('Qual é a razão da P.A: '))

decimo_termo = primeiro + (10 - 1) * razão # Formula para cacular o enesimo termo de uma P.A

for c in range (primeiro, decimo_termo, razão):
    print(c, end = ' - ')
    
print('ACABOU')