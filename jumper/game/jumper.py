class Jumper:

    """
    
    Stereotype:
        

    Attributes:
        
    """

    def __init__(self):
        self.lives = 0
        self.pic = ["  ___  \n", " /___\ \n", " \   / \n", "  \ /  \n",
                    "   0   \n", "  /|\ \n", "  / \  \n", "\n", "^^^^^^^\n"]
        self.pic_string = ""
        self.to_string()

    def remove_line(self):
        self.pic[self.lives] = "\n"
        if self.lives >= 3:
            self.pic[4] = "   X   \n"
        self.lives = self.lives + 1
        

    def to_string(self):
        self.pic 
        self.pic_string = ""
        for i in self.pic:
            self.pic_string += i
