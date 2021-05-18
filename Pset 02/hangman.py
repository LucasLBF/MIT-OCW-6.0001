# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import sys

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

# end of helper code

# -----------------------------------


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guessed = True
    pieces_secret_word = [letter for letter in secret_word]
    for letter in pieces_secret_word:
        if letter not in letters_guessed:
            guessed = False
            break
    return guessed    
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    length = len(secret_word)
    dashes = '__ ' * length
    pieces_dashes = dashes.split()
    pieces_secret_word = [letter for letter in secret_word]
    i = 0
    for i in range(len(pieces_secret_word)):
        if pieces_secret_word[i] in letters_guessed:
            pieces_dashes[i] = pieces_secret_word[i]
    dashes = ' '.join(pieces_dashes)
    return dashes
    



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet_lst = []
    for item in string.ascii_lowercase:
        alphabet_lst.append(item)
    for letter in letters_guessed:
        if letter in alphabet_lst:
            alphabet_lst.remove(letter)
    available_letters = ''.join(alphabet_lst)        
    return available_letters
    
    

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
    tries = 6
    warnings = 3
    letters_guessed = []
    
    while True:
        
        if is_word_guessed(secret_word, letters_guessed):
            print('\o/ Congratulations! You guessed the word! \o/')
            print('Thanks for playing and see you next time! :D')
            print('')
            print('------------------------------------------')
            print('')
            sys.exit()
            
        if tries == 0:
            print('You ran out of guesses! :(')
            print('The word was %s. Better luck next time!' % secret_word)
            sys.exit()
        
        print('I am thinking of a %d letter word.' % len(secret_word))
        print('You have %d guesses left' % tries)
        print('List of avilable words: ',get_available_letters(letters_guessed))
        guess = input('> ')
        print('')
        print('------------------------------------------')
        print('')
        if str.isalpha(guess) == False or len(guess) > 1:
            warnings -= 1
            print('Oops! That is not a valid letter. You have %d warnings left' % warnings)
            print('')
            print('------------------------------------------')
            print('')
            if warnings == 0:
                print('You have ran out of warnings. Closing game.')
                sys.exit()
            continue
        
            
        elif guess not in letters_guessed:
            guess = guess.lower()
            letters_guessed.append(guess)
        
        else:
            print('You already guessed this letter!')
            print('')
            print('------------------------------------------')
            print('')
            continue
        pieces_secret_word = [letter for letter in secret_word]
        if guess in pieces_secret_word:
            print('Good guess: ',get_guessed_word(secret_word, letters_guessed))
            print('')
            print('------------------------------------------')
            print('')
            continue
        else:
            print('Oops! That letter is not in my word: ',get_guessed_word(secret_word, letters_guessed))
            tries -= 1
            print('')
            print('------------------------------------------')
            print('')
            continue
        
        
        
    



start = input('Press enter to start the game.')
if not len(start) < 1:
    print('Invalid input.')
    sys.exit()    
wordlist = load_words()
print('Loading word list from file...')
print('%d words loaded.' % len(wordlist))
print('')
print('========================================')
print('')
print('Welcome to the game Hangman!')
print('')
print('========================================')
print('')
secret_word = choose_word(wordlist)







# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
