largura = float(input("Digite a largura do terreno, em metros: "))
comprimento = float(input("Digite o comprimento do terreno, em metros: "))
area = largura * comprimento

if area < 100:
    print(f"Esse é um TERRENO POPULAR, com {area :.1f} m²")

elif area >= 100 and area <= 500:
    print(f"Esse é um TERRENO MASTER, com {area :.1f} m²")

elif area > 500:
    print(f"Esse é um TERRENO VIP, com {area :.1f} m²")

