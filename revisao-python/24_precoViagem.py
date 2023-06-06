distancia = float(input("Digite a distância que você deseja percorrer, em KM : "))

if distancia <= 200:
    viagem_curta = distancia * 0.50
    print(f"Você percorreu {distancia} Km,\nO valor a pagar é de: R${viagem_curta}") 
else:
    viagem_longa = distancia * 0.45
    print(f"Você percorreu {distancia} Km, \nO valor a pagar é de: R${viagem_longa}")