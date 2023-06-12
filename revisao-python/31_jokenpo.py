# PEDRA ===> TESOURA /// PAPEL
# PAPEL ==> PEDRA /// TESOURA
# TESOURA ==> PAPEL /// PEDRA

import random 

escolha = int(input("Selecione pedra (1), papel (2) ou tesoura (3): "))

computer_choice = random.randint(1, 3)
user_choice = escolha 

if user_choice == 1 and computer_choice == 2:
    print("você escolheu PEDRA.\nO computador PAPEL\nComputador ganhou")
elif user_choice == 1 and computer_choice == 3:
    print("Você escolheu PEDRA.\nO computador TESOURA\nVocê ganhou")
elif user_choice == 2 and computer_choice == 1:
    print("Você escolheu PAPEL.\nO computador PEDRA\nVocê ganhou")
elif user_choice == 2 and computer_choice == 3:
    print("Você escolheu PAPEL\nO computador TESOURA\nComputador ganhou")
elif user_choice == 3 and computer_choice == 1:
    print("Você escolheu TESOURA.\nO computador PEDRA\nComputador ganhou")
elif user_choice == 3 and computer_choice == 2:
    print("Você escolheu TESOURA.\nO computador PAPEL\nVocê ganhou")
if user_choice == computer_choice:
    print("Empate")
