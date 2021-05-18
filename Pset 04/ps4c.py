# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
wordlist = load_words(WORDLIST_FILENAME)

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = wordlist
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        enc_dict = {}
        i = 0
        for char in string.ascii_uppercase:
            if char in VOWELS_UPPER:
                enc_dict[char] = vowels_permutation[i].upper()
                i += 1
            else:
                enc_dict[char] = char
                
        i = 0
        for char in string.ascii_lowercase:
            if char in VOWELS_LOWER:
                enc_dict[char] = vowels_permutation[i]
                i += 1
            else:
                enc_dict[char] = char
                
        return enc_dict        
        
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        enc_message = ''
        for char in self.message_text:
            if char == ' ' or char in string.punctuation:
                enc_message += char
            elif str.isnumeric(char):
                enc_message += char
            else:
                enc_message += transpose_dict[char]
        return enc_message        
       
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self,text)
        
    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        msg_lst = []
        perms_lst = get_permutations('aeiou')
        for p in perms_lst:
            enc_dict = self.build_transpose_dict(p)
            msg = self.apply_transpose(enc_dict)
            valid = 0
            for word in msg.split():
                if is_word(self.valid_words, word):
                    valid += 1
            if valid == 0:
                continue
            else:
                msg_lst.append((valid,p,msg))
                
        msg_lst.sort(reverse = True)
        permutation = msg_lst[0][1]
        dec_msg = msg_lst[0][2]
        
        return (permutation,dec_msg)
        # get a list of all vowel permutations
        # build a transpose dictionary w/ each permutation
        # iterate every character in the message
        # create a new string and count the valid words in it
        # append (valid words,permutation,new string) to a list
        # sort list in descending order
        # permutation =  list[0][1]
        # decrypted string = list[0][2]
        # return (permutation,decrypted string)
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    print('-------------------------------------------------------------------')
    print('-------------------------------------------------------------------')
    message = SubMessage('Jack Florey is a mythical character.')
    permutation = 'eaoiu'
    enc_dict = message.build_transpose_dict(permutation)
    print('Original message:',message.get_message_text(),'Permutation:',permutation)
    print('Expected encryption: Jeck Fliray os e mythocel cherectar.')
    print('Actual encryption:',message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print('Decrypted message:',enc_message.decrypt_message())
    
    print('-------------------------------------------------------------------')
    print('-------------------------------------------------------------------')
    message = SubMessage('I scream, you scream, we all scream for ice cream.')
    permutation = 'uoiea'
    enc_dict = message.build_transpose_dict(permutation)
    print('Original message:',message.get_message_text(),'Permutation:',permutation)
    print('Expected encryption: I scroum, yea scroum, wo ull scroum fer ico croum.')
    print('Actual encryption:',message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print('Decrypted message:',enc_message.decrypt_message())