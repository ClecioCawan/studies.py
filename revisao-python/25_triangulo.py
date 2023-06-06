a = float(input("Digite o comprimento do segmento A: "))
b = float(input("Digite o comprimento do segmento B: "))
c = float(input("Digite o comprimento do segmento C: "))

if a < b + c and b < a + c and c < b + a:#cada segmento é menor que a soma dos outros 2
    print("Pode formar um triângulo")

else:
    print("NÃO pode formar um triângulo")

