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




Health = RED("Health")
HP = RED("HP")
Strength = RED("Strength")
Elixir = MAGENTA("Elixir")
Shield = BLUE("Shield")


class item():
    def __init__(self, Name_I, Effect_I):
        self.Name_I = Name_I
        self.Effect_I = Effect_I

    def __str__(self):
        return f"{self.Name_I}:\n   {self.Effect_I}"
    

# Här skapas itemobjekt
item_1 = item(f"{Health} {Elixir}", f"Restores 30 {HP}")
item_2 = item(f"{Strength} {Elixir}", f"Increases {Strength} by 50")
item_3 = item(f"{Shield}", f"Increases max {HP} by 30")

# Här skapas en lista för spelarens item-inventory
item_inventory = []

