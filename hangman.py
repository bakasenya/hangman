import random
from word_list import words


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = words
lives = 6
chosen_word = random.choice(word_list)
print(f"It is a {len(chosen_word)} word. Guess wisely.")

blank = ""



for position in range(len(chosen_word)):
    blank += "_"
print(blank)
game_over = False
correct_word = []

while not game_over:
    user_input = input("Guess a letter: ").lower()
    
    if user_input in correct_word:
        print(f"You have already guessed '{user_input}' letter, guess another!")
    
    display = ""
        
    for letter in chosen_word:
        if letter == user_input:
            display += letter
            correct_word.append(user_input)
        elif letter in correct_word:
            display += letter
        else:
            display += "_"
    print(display)
    
    
    if user_input not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left")
        if lives == 0:
            game_over = True
            print(f"It was {chosen_word}! You lose")
            
    if "_" not in display:
        game_over = True
        print("You Win!")
        
    print(stages[lives])


