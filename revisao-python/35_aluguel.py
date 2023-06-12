tipo_carro = str(input("O carro é popular ou luxo (P / L): ")).lower().strip()
dias_carro = int(input("Quantos dias o carro foi alugado: "))
km_carro = float(input("Quantos KM foi rodado com o carro "))

if tipo_carro == "p": #R$90
    print("Carro Popular")
    if km_carro <= 100:
        aluguel = (dias_carro * 90) + (km_carro * 0.20)
        print(f"Você percorreu {km_carro}km, por {dias_carro} dias.\nO seu aluguel é de R${aluguel} ")

    elif km_carro > 100:
        aluguel = (dias_carro * 90) + (km_carro * 0.10)
        print(f"Você percorreu {km_carro}km, por {dias_carro} dias.\nO seu alguel é de R${aluguel}")

if tipo_carro == "l": #R$150
    print("Carro de Luxo")
    if km_carro <= 200:
        aluguel_luxo = (dias_carro * 150) + (km_carro * 0.30)
        print(f"Você percorreu {km_carro}km, por {dias_carro} dias.\nO seu aluguel é de R${aluguel_luxo}")
    
    elif km_carro > 200:
        aluguel_luxo = (dias_carro * 150) + (km_carro * 0.25)
        print(f"Você percorreu {km_carro}km, por {dias_carro} dias.\nO seu aluguel é de R${aluguel_luxo}")

print("OBRIGADO POR USAR O PROGRAMA!!!")
