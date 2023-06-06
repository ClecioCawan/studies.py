# EQUILÁTERO: a = b = c
# ISÓSCELES: (a = b != c) and (b != a = c) and (c != a = b)
# ESCALENO:  a != b != c 

a = float(input("Valor do segmento A: "))
b = float(input("Valor do segmento B: "))
c = float(input("Valor do segmento C: "))

if a < b + c and b < a + c and c < b + a:
    print("Pode formar um triângulo")

    if a == b == c: #equilátero
        print(f"Esse triângulo é EQUILÁTERO")

    elif a != b == c or b != c == a or c != a == b: #isóceles
        print("Esse triângulo é ISÓCELES") 

    elif a != b != c: #escaleno
        print("Esse triângulo é ESCALENO")

else:
    print("NÃO pode formar um triângulo")