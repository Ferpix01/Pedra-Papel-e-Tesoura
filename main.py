import random

# Vai tomar no cu piranhaaaaaa

def get_user_choice():
    print("Escolha: \n1 - Pedra \n2 - Papel \n3 - Tesoura\n4 - Mão de Deus")
    choice = input("O que tu quer: ")
    while choice not in ['1', '2', '3', '4']:
        print("Opção inválida filho da puta!")
        choice = input("O que tu quer: ")
    return choice

def get_computer_choice():
    choices = ['Pedra', 'Papel', 'Tesoura', 'Mão de Deus']
    return random.choice(choices)

def get_result(user_choice, computer_choice):
    user_choice = get_choice_name(user_choice)
    print("Você jogou: " + user_choice)
    print("Computador jogou: " + computer_choice)
    if user_choice == computer_choice:
        return "Empate"
    elif ((user_choice == 'Pedra' and computer_choice == 'Tesoura') or
          (user_choice == 'Tesoura' and computer_choice == 'Papel') or
          (user_choice == 'Mão de Deus' and computer_choice == 'Papel', 'Tesoura', 'Pedra') or
          (user_choice == 'Papel' and computer_choice == 'Pedra')):
        return "Você ganhou!"
    else:
        return "Computador ganhou!"

def get_choice_name(choice):
    choices = {
        '1': 'Pedra',
        '2': 'Papel',
        '3': 'Tesoura',
        '4': 'Mão de Deus'
    }
    return choices[choice]

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = get_result(user_choice, computer_choice)
    print(result)

while True:
    play_game()
    next_game = input("Mais um? (s/n): ")
    if next_game.lower() != 's':
        print("Perdedor filho da puta do caralho hein")
        break