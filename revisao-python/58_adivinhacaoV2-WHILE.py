from random import randint

choice = int(input("Digite Um número de 0 a 10: ")) #Escolha
computer_choice = randint (0,10) #Escolha do computador
cont_choice = 1 #Contador de escolhas

while choice != computer_choice:
    cont_choice += 1
    if choice < computer_choice: #mais
        choice = int(input("Mais... tente novamente:  "))
    elif choice > computer_choice: #menos
        choice = int(input("Menos... tente novamente:  "))

print(f"Você ganhou com um total de {cont_choice} palpites")
