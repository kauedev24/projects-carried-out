from random import randint
from os import system
from art import LOGO


def easy():
    attemps = 10
    return attemps


def hard():
    attemps = 5
    return attemps


def low_or_high(answer, guess):
    if guess > answer:
        return'Too high.'
    elif guess < answer:
        return 'Too low.'
    else:
        return f'You got it! The answer was {answer}.'

answer = randint(1, 100)

def play_game():
    print(LOGO)
    print("\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    print(f'Ei o número é {answer}')
    difficulty = input('Chose a difficulty. Type "easy" or "hard": ')

    if difficulty == 'easy':
        choice = easy()
    elif difficulty == 'hard':
        choice = hard()

    guess = 0
    while guess != answer:
        if choice == 0:
            print("\nYou've run out of guesses, you lose.")
            break

        print('Guess again.')
        print(f'\nYou have {choice} attemps remaining to guess the number')

        guess = int(input('Make a guess: '))

        user_input = low_or_high(answer, guess)
        print(user_input)

        choice -= 1
    

        
while input('\nDo you want to play again? "Yes" or "No" \n').lower() == 'yes':
    system('clear')
    play_game()
