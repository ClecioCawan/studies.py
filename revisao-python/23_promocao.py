nome = str(input("Digite o seu nome: "))
sexo = str(input("Digite o seu sexo (H / M): ")).strip().upper()
valor_compras = float(input("Digite o valor total das compras: "))

homens_desconto = valor_compras - (valor_compras * 5/100)
mulher_desconto = valor_compras - (valor_compras * 13/100)

if sexo == "H" : #Tem que colocar entre aspas uma string
    print(f"Olá {nome}, Você gastou R${valor_compras} e com o desconto fica de R${homens_desconto}")

if sexo == "M" :
    print(f"Olá {nome}, Você gastou R${valor_compras} e com desconto fica de R${mulher_desconto} ")
    

