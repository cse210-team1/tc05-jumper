
import random


class Target:
    """A code template for a word that is being searched for. The responsibility of this 
    class of objects is to generate the word that will be searched for, take a character
    as a guess, and to return a Bool based on whether the guess was within the word. Also,
    a record of the already-guessed characters is kept track of and updated in both a list
    of single characters as well as a single string.
    
    Stereotype:
        Searchable item

    Attributes:
        possible_words (list): A list of possible words that get_rand_word chooses from.
        word (list): The chosen word, broken up into a list of the individual characters.
        self.guess (list): A list of correct guesses in the word and underscores representing blank spaces
        guess (str): A character passed in as a guess.
        filled_word (str): The self.guess list, condensed into a single string.
    """
    def __init__(self):
        """Initializes all variables.

        Args: 
            self (Target): An instance of Target.
            
        Returns:
            Nothing.
        """
        self.possible_words = self.load_word_file()
        self.word = []   # ex: ['B', 'a', 't']
        self.guess = []    # ex: ['_', 'a', '_']
        self.filled_word = ""   # ex: ['_a_']


    def load_word_file(self):
        """Opens a word file for randome word selection"""
        with open("game/words.txt") as word_file:
            inner_text = word_file.read().strip()
            text_lines = inner_text.split()
            words = []
            for line in text_lines:
                words.append(line)
            return words
            
    def get_rand_word(self):
        """Selects a random word from possible_words, breaks it into characters, and assigns it to word.
           Also assigns self.guess with the correct amount of underscores.

        Args: 
            self (Target): A single instance of Target.
            
        Returns:
            Nothing.
        """

        number = random.randint(0, len(self.possible_words) - 1)
        whole_word = self.possible_words[number]
        self.word = list(whole_word)
        for char in self.word:
            self.guess.append(' █ ')

    def check_guesses(self, guess):
        """Checks the guess against each letter in word, and if it matches any of them, returns True.

        Args: 
            self (Target): An instance of Target.
            guess (str): A single letter character.
            
        Returns:
            Bool: If the guess was correct or not.
        """
        guess_is_correct = False
        guess_letter = str.lower(guess)
        for char in self.word:
            if char == guess_letter:
                guess_is_correct = True
        return guess_is_correct

    def update_guess(self, guess):
        """Takes the guess and converts underscores into the guessed letter, in the places that
           letter goes in word.

        Args: 
            self (Target): An instance of Target.
            guess (str): A single letter character.
            
        Returns:
            filled_word (str): The self.guess list compressed into a string.
        """
        word_index = 0
        whole_word = ""
        for char in self.word:
            if char == guess:
                self.guess[word_index] = guess
            word_index += 1
        self.filled_word = whole_word.join(self.guess)
        return self.filled_word