def display_hangman(tries):

  stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
  return stages[tries]



def get_guess(guessed_letters,guessed_words):

  keep_guessing = True

  while keep_guessing == True:
    guess = input("Enter a letter or a word: ")

  # guessed a letter
    if len(guess) == 1:
      if guess in guessed_letters:
        print("you have already guessed that letter")
        keep_guessing = True
      else:
        keep_guessing = False

  #we guessed a word
    else:
      if guess in guessed_words:
        print("you have already guessed that word")
        keep_guessing =True
      else:
        keep_guessing = False
    
  return guess

def display_word_completion(word_completion):
  for letter in word_completion:
    print('',letter,'',end = '')

def game(word,tries):
  #setup
  keep_playing = True
  guessed_letters = []
  guessed_words= []
  word = word.lower()
  word_completion = '-'*len(word)
  


  while keep_playing == True:
    hangman_graphic = display_hangman(tries)
    print(hangman_graphic)
    display_word_completion(word_completion)
    print("\n")
    guess = get_guess(guessed_letters,guessed_words)


    guess= guess.lower()
    if len(guess) == 1:
      guessed_letters.append(guess)
      #if they guessed a correct letter
      if guess in word:
        word_indecies = []
        for i in range(len(word)):
          if guess == word[i]:
            word_indecies.append(i)
        
        temp_word_completion = ""
        for i in range(len(word_completion)):
          if i in word_indecies:
            temp_word_completion = temp_word_completion + word[i]
          else:
            temp_word_completion = temp_word_completion + word_completion[i]
        word_completion = temp_word_completion



      # if the letter isnt in the word
      else:
        print("was not in the word")
        tries = tries - 1
    
    # a problem for later
    else:
      guessed_words.append(guess)
      if guess == word:
        word_completion = word
        print(hangman_graphic)
        display_word_completion(word_completion)
        print("\n")
        print("YOU WIN")
      else:
        print("That was not the word")
        tries = tries - 1

    
#if you lose
    if tries <0:
      print("you lose")
      break
    
    if word_completion == word:
      print(hangman_graphic)
      display_word_completion(word_completion)
      print("YOU WIN")
      
      break




  



def main():
  print("WELCOME to hangman")
  game("Toronto",6)


main()