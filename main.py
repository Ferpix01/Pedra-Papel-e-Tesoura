import random

# Pega a escolha do usuário e armazena
def get_user_choice():
    print("Escolha: \n1 - Pedra \n2 - Papel \n3 - Tesoura")
    choice = input("O que tu quer: ")
    while choice not in ['1', '2', '3']:
        print("Opção inválida!")
        choice = input("O que tu quer: ")
    return choice

# Pega a escolha da máquina e armazena
def get_computer_choice():
    choices = ['Pedra', 'Papel', 'Tesoura']
    return random.choice(choices)

#Verifica o que foi escolhido e se venceu-empatou-perdeu
def get_result(user_choice, computer_choice):
    user_choice = get_choice_name(user_choice)
    print("Você jogou: " + user_choice)
    print("Computador jogou: " + computer_choice)
    if user_choice == computer_choice:
        return "Empate"
    elif ((user_choice == 'Pedra' and computer_choice == 'Tesoura') or
          (user_choice == 'Tesoura' and computer_choice == 'Papel') or
          (user_choice == 'Papel' and computer_choice == 'Pedra')):
        return "Você ganhou!"
    else:
        return "Computador ganhou!"

def get_choice_name(choice):
    choices = {
        '1': 'Pedra',
        '2': 'Papel',
        '3': 'Tesoura'
    }
    return choices[choice]

#Joga o jogo
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = get_result(user_choice, computer_choice)
    print(result)

#Script para repetição
while True:
    play_game()
    next_game = input("Mais um? (s/n): ")
    if next_game.lower() != 's':
        print("Perdedor XD")
        break
