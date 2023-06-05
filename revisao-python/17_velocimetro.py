velocidade = int(input("Velocidade do veículo na via (km/h): "))

if velocidade > 80:
    diferenca_velocidade = velocidade - 80
    multa = diferenca_velocidade * 5
    print(f"Você exedeu a velocidade permitida na via em {diferenca_velocidade} km/h \nVocê foi multado em R${multa}.")

else:
    print("Você está dento da velocidade permitida na via.")
