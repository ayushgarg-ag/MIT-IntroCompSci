# Problem Set 2, hangman.py
# Name: Ayush Garg
# Time spent: 2 hours

# Hangman Game
# -----------------------------------
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
      if letter not in letters_guessed:
        return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    current = ""
    for letter in secret_word:
      if letter in letters_guessed:
        current += letter
      else:
        current += "_ "
    return current


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    str = ""
    for letter in string.ascii_lowercase:
      if letter not in letters_guessed:
        str += letter
    return str


def num_unique_letters(secret_word):
  '''
  secret_word: string, the word the user is guessing
  returns: int, number of unique letters in a string
  '''
  str = ""
  for i in secret_word:
    if (i not in str):
      str += i
  return len(str)


def is_valid(user_letter, letters_guessed):
  '''
  user_letter: string, the letter the user guessed
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: boolean, whether the user_letter is a number and if it has been guessed before
  '''
  if (user_letter.isalpha() == False or user_letter in letters_guessed):
    return False
  return True


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings = 3
    guessed_letters = []
    number_guesses = 6

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " +
          str(len(secret_word)) + " letters long.", end='\n')
    print("You have " + str(warnings) + " warnings left.")
    print("--------------------------")

    while (number_guesses > 0 and is_word_guessed(secret_word, guessed_letters) == False):
      print("You have " + str(number_guesses) + " guesses left.")
      print("Available letters: ", get_available_letters(guessed_letters))
      user_letter = input("Please guess a letter: ").lower()

      if (is_valid(user_letter, guessed_letters) == False):
        if (warnings == 0):
          number_guesses -= 1
          print("You have no warnings left, so you lose one guess.")
        else:
          if (user_letter.isalpha() == False):
            warnings -= 1
            print("Oops! That is not a valid letter. You have " +
                  str(warnings) + " warnings left.")
          else:
            warnings -= 1
            print("Oops! You have already guessed that letter. You have " +
                  str(warnings) + " warnings left.")
      else:
        if (user_letter in secret_word):
          print("Yay! That letter is in my word: ", end="")
        else:
          print("Oops! That letter is not in my word: ", end="")
          if (user_letter in "aeiou"):
            number_guesses -= 2
            print("You lost two guesses for guessing a vowel wrong.")
          else:
            number_guesses -= 1

      guessed_letters.append(user_letter)
      result = get_guessed_word(secret_word, guessed_letters)
      print(result)
      if (is_word_guessed(secret_word, guessed_letters)):
        print("Congratulations you win!")
        print("Your total score for this game is: " +
              str(number_guesses*num_unique_letters(secret_word)))
      print("--------------------------")

    if(number_guesses == 0):
      print("Sorry, you ran out of guesses. The word was: ", secret_word)

# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    letters_in_other = other_word.split()
    my_word = my_word.replace(" ", "")
    is_same = True
    if (len(my_word) != len(other_word)):
      return False
    for i in range(len(my_word)):
      if (my_word[i] != "_"):
        if (my_word[i] != other_word[i]):
          return False
      else:
        if (other_word[i] in my_word):
          return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    str = ""
    for word in wordlist:
      if (match_with_gaps(my_word, word)):
        str += word + " "

    if (str == ""):
        return "No matches found"
    return str


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings = 3
    guessed_letters = []
    number_guesses = 6

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " +
          str(len(secret_word)) + " letters long.", end='\n')
    print("You have " + str(warnings) + " warnings left.")
    print("--------------------------")

    while (number_guesses > 0 and is_word_guessed(secret_word, guessed_letters) == False):
      print("You have " + str(number_guesses) + " guesses left.")
      print("Available letters: ", get_available_letters(guessed_letters))
      user_letter = input("Please guess a letter: ").lower()

      if (is_valid(user_letter, guessed_letters) == False and user_letter != "*"):
        if (warnings == 0):
          number_guesses -= 1
          print("You have no warnings left, so you lose one guess.")
        else:
          if (user_letter.isalpha() == False):
            warnings -= 1
            print("Oops! That is not a valid letter. You have " +
                  str(warnings) + " warnings left.")
          else:
            warnings -= 1
            print("Oops! You have already guessed that letter. You have " +
                  str(warnings) + " warnings left.")
      else:
        guessed_letters.append(user_letter)
        result = get_guessed_word(secret_word, guessed_letters)
        if (user_letter == "*"):
          print("Possible word matches are: ")
          print(show_possible_matches(result))
        elif (user_letter in secret_word):
          print("Yay! That letter is in my word: ", end="")
        else:
          print("Oops! That letter is not in my word: ", end="")
          if (user_letter in "aeiou"):
            number_guesses -= 2
            print("You lost two guesses for guessing a vowel wrong.")
          else:
            number_guesses -= 1

      print(result)
      if (is_word_guessed(secret_word, guessed_letters)):
        print("Congratulations you win!")
        print("Your total score for this game is: " +
              str(number_guesses*num_unique_letters(secret_word)))
      print("--------------------------")

    if(number_guesses == 0):
      print("Sorry, you ran out of guesses. The word was: ", secret_word)


if __name__ == "__main__":
    # Normal Hangman
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############
    # Hangman with hints
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)