# ax² + bx + c = 0
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
delta = (b ** 2) - 4 * (a*c) #b² - 4*a*c

if delta < 0:

    print(f"O valor de delta é {delta}, portanto não existe!")

else:
    print(f"O valor de delta é {delta}.")


