ano = int(input("Digite o ano recorrente: "))
bissexto = ano % 4 #Divisão por 4 , quando resto é zero.

if bissexto == 0:
    print(f"O ano {ano} é BISSEXTO ")
    
else:
    print(f"O ano {ano} NÃO é BISSEXTO ")