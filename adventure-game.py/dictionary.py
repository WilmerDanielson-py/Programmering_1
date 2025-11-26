
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



Goblin = f"{Fore.GREEN}\nGoblin{Style.RESET_ALL}: \nGoblins are small, green humanoid creatures known for their mischievous nature and cunning tactics.\nThey often travel in packs and can be found in forests and caves. \nDespite their size, goblins can be quite dangerous due to their agility and numbers. \nThese goblins have a weakness to both Blade and Gun type attacks.\n\n"
Zombie = f"{Fore.YELLOW}Zombie{Style.RESET_ALL}: \nZombies are reanimated corpses that move with a slow, shuffling gait.\nThey are driven by an insatiable hunger for human flesh and are often found in graveyards or abandoned areas.\nZombies are relentless and can infect others with their bite, turning them into more zombies.\nThese zombies have a weakness to Blade type attacks.\n\n"
Ravager = f"{Fore.MAGENTA}Ravager{Style.RESET_ALL}: \nRavagers are large, heavily armored beasts that serve as tanks in battle.\nThey possess immense strength and durability, making them formidable opponents.\nRavagers are often used by dark forces to break through enemy lines and cause chaos on the battlefield.\nThese ravagers have a weakness to Gun type attacks.\n\n"
Warlock = f"{Fore.BLUE}Warlock{Style.RESET_ALL}: \nWarlocks are powerful spellcasters who have made pacts with dark entities to gain their magical abilities.\nThey can cast devastating spells and summon otherworldly creatures to do their bidding.\nWarlocks are often feared for their ability to manipulate the forces of darkness and bend them to their will.\nThese warlocks have a weakness to Gun type attacks.\n\n"
Greger = f"{Fore.BLACK}Greger{Style.RESET_ALL}: \nGreger is a mysterious dark entity known for his cunning and manipulative nature.\nHe thrives in the shadows, using deception and trickery to achieve his goals.\nGreger is a master of dark magic and can summon powerful minions to do his bidding.\nThese Gregers have a weakness to Blade type attacks.\n\n"
Bellman = f"{Fore.RED}Bellman{Style.RESET_ALL}: \nBellman is a jester-like figure who uses humor and wit to disarm his opponents.\nHe is known for his unpredictable nature and ability to turn the tide of battle with his clever tricks.\nBellman often employs illusions and distractions to confuse his enemies and gain the upper hand.\nThese Bellmen have a weakness to Joke type attacks.\n\n"
Johannes_Thessen = f"{Fore.CYAN}Johannes Thessén{Style.RESET_ALL}: \nJohannes Thessén is a legendary coder known for his unparalleled programming skills.\nHe is said to possess the ability to manipulate code in ways that defy conventional logic.\nJohannes is often sought after by those in need of complex software solutions and innovative algorithms.\nThese Johannes Thesséns have a weakness to Sunlight type attacks.\n\n"
Physics_Entity = f"{Fore.GREEN}Physics Entity{Style.RESET_ALL}: \nThis entity represents a complex physics equation that governs fluid dynamics.\nIt embodies the principles of motion, pressure, and viscosity in fluid systems.\nThis physics entity is often studied by scientists and engineers to understand and predict fluid behavior in various applications.\nThese Physics Entities have a weakness to Nikodesmos type attacks.\n\n"
Dictionary = Goblin + Zombie + Ravager + Warlock + Greger + Bellman + Johannes_Thessen + Physics_Entity