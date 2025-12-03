from colorama import init, Fore, Style
init(autoreset=True)



def RED(text, color=Fore.RED):
    return f"{color}{text}{Style.RESET_ALL}"   
def GREEN(text, color=Fore.GREEN):
    return f"{color}{text}{Style.RESET_ALL}" 
def BLUE(text, color=Fore.BLUE):
    return f"{color}{text}{Style.RESET_ALL}" 
def YELLOW(text, color=Fore.YELLOW):
    return f"{color}{text}{Style.RESET_ALL}" 
def MAGENTA(text, color=Fore.MAGENTA):
    return f"{color}{text}{Style.RESET_ALL}" 
def CYAN(text, color=Fore.CYAN):
    return f"{color}{text}{Style.RESET_ALL}"  
def BLACK(text, color=Fore.BLACK):
    return f"{color}{text}{Style.RESET_ALL}"




HP = RED("HP")
Strength = RED("Strength")
Level = GREEN("Level")

class Player():
    def __init__(self, Name_P, HP_P, MaxHP_P, Level_P, STR_P, maxlevel_P, Gold_gain):
        self.Name_P = Name_P
        self.HP_P = HP_P
        self.MaxHP_P = MaxHP_P
        self.Level_P = Level_P
        self.STR_P = STR_P
        self.maxlevel_P = maxlevel_P
        self.Gold_gain = Gold_gain
# Här skapas en strängrepresentation av spelaren
    def __str__(self):
        return f"\nPlayer {Fore.GREEN}Name{Style.RESET_ALL}: {self.Name_P}\nPlayer {HP}: {self.HP_P}/{self.MaxHP_P}\nPlayer {Strength}: {self.STR_P}\nPlayer {Level}: {self.Level_P}\n"



Gold_gain = 0

