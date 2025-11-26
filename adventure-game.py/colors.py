from colorama import init, Fore, Style
init(autoreset=True)
# Här skapas funktioner för olika färger
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

# Här skapas färgade typer för ord  
Blade = CYAN("Blade")
Gun = YELLOW("Gun")

Health = RED("Health")
HP = RED("HP")
Strength = RED("Strength")
Elixir = MAGENTA("Elixir")
Sheild = BLUE("Sheild")
Level = GREEN("Level")