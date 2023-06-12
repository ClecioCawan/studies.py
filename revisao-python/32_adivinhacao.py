from random import randint

choice = int(input("O computador sorteou um número entre 1 e 5, qual foi ele: "))

computer_choice = randint(1, 5)
user_choice = choice

if user_choice == computer_choice:
    print("Você acertou")
elif user_choice != computer_choice:
    print(f"Você Errou, o número sorteado foi {computer_choice}")