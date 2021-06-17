from game.target import Target 
from game.console import Console
from game.jumper import Jumper 

class Director:
    
    def __init__(self):
        """Class Constructor"""
        self._target = Target()
        self._jumper = Jumper()
        self._console = Console()
        
    def game_run(self):
        """ Starts the game and handles the game loop"""
        self._console.write("Welcome to Jumper!")
        self._console.write(self._jumper.pic_string)
        self._console.write(self._target.guess)
        while self.can_play():
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
        
    def get_inputs(self):
        """Gets the guess from the user through the console"""
        guess = self._console.read_char("Guess a letter: [a-z] ")
        if self._target.check_guess(guess):
            self._target.update_guess()
        else:
            self._jumper.remove_line()

        

    def do_outputs(self):
        self._console.write(self._target.guess)
        self._console.wrtie(self._jumper.pic_string)

    def do_updates(self):
        pass
    def can_play(self):
        if jumper.lives >= 4:
            return False
        else:
            return True
    