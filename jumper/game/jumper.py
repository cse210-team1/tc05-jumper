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
        self.lives = self.lives + 1

    def to_string(self):
        x = self.pic
        self.pic_string = ""
        for i in x:
            self.pic_string += i
