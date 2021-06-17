import random

class Target:
    def __init__(self):
        self.possible_words = ["Cat", "Bat", "Firetruck", "Playground", "Mouse"]
        self.word = []   # ex: ['B', 'a', 't']
        self.guess = []    # ex: ['_', '_', '_']
    def get_rand_word(self):
        number = random.randint(0, len(self.possible_words))
        whole_word = self.possible_words[number]
        self.word = list(whole_word)
    def check_guess(self):
        #self.word & self.guess
        pass
    def update_guess(self):
        #self.guess
        pass

