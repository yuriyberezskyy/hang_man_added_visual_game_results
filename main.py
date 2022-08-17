#Step 4
import hangman_logo
import hangman_words
import random

stages = hangman_logo.stages
print(hangman_logo.logo)
print("YOU HAVE 6 LIVES")

end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    isChar = False
    for position in range(word_length):
        letter = chosen_word[position]

        
        if letter == guess:
            if display[position] != letter:
              display[position] = letter
            else:
              print("You already used this letter")
            isChar = True

    if isChar == False:
      print(stages.pop())
      print(f"You guessed a letter {guess}, it's not in the word. You lost 1 life out of {len(stages)}")
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    if not stages:
      end_of_game = True
      print("You lost")

