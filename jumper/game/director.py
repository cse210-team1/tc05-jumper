from game.target import Target 
from game.console import Console
from game.jumper import Jumper 

class Director:
    """Core of the progran.  This class is resonable for coordinating the classes
    so they work together.  It orginzes output and send it to the user, and gathers inputs.
    
    Stereotype:
        Coordinater
    
    Atributes:
        _target (Target object): Holds info about the word to be guessed
        _jumper (Jumper object): Holds info about the jumper, like how many lives are left
        _console (Console object): Maneges inputs and outputs.
    """
    
    
    def __init__(self):
        """Class Constructor"""
        self._target = Target()
        self._jumper = Jumper()
        self._console = Console()


    def start_game(self):
        """ Starts the game and handles the game loop"""
        self._target.get_rand_word()
        self._console.write("Welcome to Jumper!")
        self._console.write(self._jumper.pic_string)
        self._target.update_guess("")
        self._console.write(self._target.filled_word)
        while self.can_play():
            self.get_inputs()
            self.do_outputs()


    def get_inputs(self):
        """Gets the guess from the user through the console"""
        guess = self._console.read_char("Guess a letter: [a-z] ")
        if not self._target.check_guesses(guess):
            self._jumper.remove_line()
        self._target.update_guess(guess)



    def do_outputs(self):
        """Passes the outputs (the list of guesses and picture) to the console which displays
        it to the user"""
        

        self._jumper.to_string()
        self._console.write(self._jumper.pic_string)
        self._console.write(self._target.filled_word)


    def can_play(self):
        
        if self._target.word == self._target.guess:
            self._console.write("You Win!")
            return False
        
        elif self._jumper.lives >= 4:
            self._console.write("You Lose!")
            return False
        else:
            return True
    