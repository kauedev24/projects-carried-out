import random, json
from logo import logo, stages

with open('words.json', 'r') as file:
    words = json.load(file)

random_word = random.choice(words)  # escolhendo a palavra

display = []
for i in range(len(random_word)):  # numero de espaços correspondente ao tamanho da palavra
    display.append("_")

print(logo)

START = True
STOP = False

life = 0
while START:  # iniciando o jogo
    letter_word = input('Guess a letter: ').lower()

    len_ = 0
    for letter in random_word:  # verificando se a letra existe na palavra
        if letter_word == letter:
            display[len_] = letter_word

        len_ += 1
    
    print(f'{display}\n')

    if "_" not in display:
        print(f'You Win, the word is "{random_word.capitalize()}".\n')
        START = STOP

    if letter_word not in random_word:  # contador de chances
        print(stages[life])
        life += 1
        
    if life == len(stages):
        print(f'You lose, the word was {random_word}\n')
        START = STOP      
