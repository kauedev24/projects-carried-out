from art import vs, logo
from data import data
from random import choice
from os import system

USERS_INSTAGRAM = data


def more_followers(a, b):
    """Descobre quem tem mais seguidores."""
    if a > b:
        return 'a'
    else:
        return 'b'
    

def format_data(account):
    """Formata os dados para as saídas."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f'{account_name}, {account_descr}, from {account_country}.'


def play_game():
    """Inicia o jogo."""
    print(logo)

    game_over  = False
    score = 0
    while not game_over:
        # pegar 2 pessoas aleatoriamente 
        account_a = choice(USERS_INSTAGRAM)
        account_b = choice(USERS_INSTAGRAM)
        if account_a == account_b:
            account_b = choice(USERS_INSTAGRAM)
    
        print(f"\nYou're right! Current score: {score}.")

        formatted_a = format_data(account_a)
        formatted_b = format_data(account_b)
        print(f"Compare A: {formatted_a}")
        print(vs)
        print(f"Against B: {formatted_b}")
        
        right_answer = more_followers(account_a['follower_count'], account_b['follower_count'])
        
        user_choice = input('Who has more followers? Type "A" or "B" \n').lower()
        if user_choice == right_answer:
            score += 1
            system('clear')
            continue
        else:
            print(f"\nSorry, that's wrong. Final score: {score}.")
            game_over = True
        

while input('\nDo you want to play again? "Yes" or "No" \n').lower() == 'yes':
    system('clear')
    play_game()
