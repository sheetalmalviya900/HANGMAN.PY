import string
from word import choose_word
from images import IMAGES

def ifValid(user_input):
  if len(user_input) != 1:
    return False

  if not user_input.isalpha():
    return False
  return True


def is_word_guessed(secret_word,letter_guessed):
   
  if secret_word==get_guessed_word(secret_word,letter_guessed):
    return True
  return False


def get_guessed_word(secret_word,letters_guessed):
  index=0
  guessed_word=""
  while(index<len(secret_word)):
        if secret_word[index] in letters_guessed:
              guessed_word+=secret_word[index]
        else:
              guessed_word+="_"
        index+=1
  return guessed_word



def get_available_letters(letters_guessed):
    
  import string
  letters_left=string.ascii_lowercase
  for i in letters_guessed:
    letters_left=letters_left.replace(i,"")
  return letters_left

def get_hint(secret_word,letters_guessed):
  import random
  letters_not_guessed=[]
  for i in secret_word:
    if i not in letters_guessed:
      if i not in letters_not_guessed:
        letters_not_guessed.append(i)
  return random.choice(letters_not_guessed)
                    
              

def hangman(secret_word):
      
  print ("Welcome to the game, Hangman.....!!")
  print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
  print ("\n")

  letters_guessed = []
  total_lives=remaining_lives = 8
  image_selection_list=[1,2,3,4,5,6,7,8]
  level=input("Enter the level in which you want to play""\n""a for easy""\n""b for mrdium""\n""c for hard""\n""Enter the level:-")
  if level=="b":
    total_lives=remaining_lives=6
    image_selection_list=[1,2,4,5,7,8]
  elif level=="c":
    total_lives=remaining_lives=4
    image_selection_list=[1,3,5,7]
  else:
    if level!="a":
          print("your choice is valid""\n""game is starting in easy level")
  
  while (remaining_lives>0):
    available_letters = get_available_letters(letters_guessed)
    print ("Available letters: " + available_letters)

    guess = input("Please guess a letter: ")
    letter = guess.lower()

    if letter=="hint":
      print("your hint for this secret word is ",get_hint(secret_word,letters_guessed))
    else:
      if (not ifValid(letter)):
        print("invalid input")
        continue

    if letter in secret_word:
      letters_guessed.append(letter)
      print(letters_guessed)
      print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
      print ("")

      if is_word_guessed(secret_word, letters_guessed) == True:
        print (" * * Congratulations, you won! * * ")
        print ("")
        break

    else:
      print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
      letters_guessed.append(letter)
      print(IMAGES[image_selection_list[total_lives-remaining_lives]])
      remaining_lives -= 1
      print ("Remaining Lives : ", (remaining_lives))
      print ("")
  else:
      print("sorry you lose the game, the word was -",secret_word)

secret_word=choose_word()
hangman(secret_word)
