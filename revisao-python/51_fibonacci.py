numero = int(input("Quantos termos você quer mostrar: "))
termo_1 = 0 #sempre começa com esses 2 termos
termo_2 = 1
print(termo_1,"=>", termo_2, end=" => ") #mostrando os 2 primeiros termos (termos fixos)
for c in range (3 , numero + 1):#laço começando em 3 e indo até o número máximo de termos
    termo_3 = termo_2 + termo_1 #terceiro termo é a soma dos anteriores
    print(termo_3, end=" => ")
    termo_1 = termo_2 #recebendo novos valores conforme o laço continua.
    termo_2 = termo_3
print("Acabou")

