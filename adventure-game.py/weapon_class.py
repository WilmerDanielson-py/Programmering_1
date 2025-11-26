import random as r

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




Blade = CYAN("Blade")
Gun = YELLOW("Gun")


class weapon():
    def __init__(self, Rarity_W, Name_W, Type_W, Dmg_W, AtkSpeed_W, Range_W, Hits_W):
        self.Dmg_W = Dmg_W
        self.Range_W = Range_W
        self.AtkSpeed_W = AtkSpeed_W
        self.Type_W = Type_W
        self.Name_W = Name_W
        self.Rarity_W = Rarity_W
        self.Hits_W = Hits_W
        
# Här skapas en strängrepresentation av vapnet
    def __str__(self):
        return f"\n{self.Name_W}\nThis {self.Rarity_W} {self.Name_W} is a {self.Type_W} type weapon.\n   Stats are:\n   Damage: {self.Dmg_W}\n   AtkSpeed: {self.AtkSpeed_W}\n   Range: {self.Range_W} "

# Här skapas vapenobjekt
# weapon = weapon("rarity", "name","type","dmg","Atkspeed","range","max hits")
weapon_1 = weapon(BLACK("Common"), "Dagger", Blade, 15, 20, 1, 1)
weapon_2 = weapon(GREEN("Uncommon"), "Rapier", Blade, 45, 10, 20, 1)
weapon_3 = weapon(BLUE("Rare"), "Zweihander", Blade, 60, 8, 25, 3)
weapon_4 = weapon(BLUE("Rare"), "Shorre", Gun, 50, 7, 30, 5)
weapon_5 = weapon(MAGENTA("Epic"), "Ak 5", Gun, 7, 25, 100, 25)
weapon_6 = weapon(YELLOW("Legendary"), "Golden Scar", Gun, 10, 30, 150, 20)
weapon_7 = weapon(RED("Mythic"), "Musket", Gun, 2000, 1, 200, 1)

# Här skapas antal träffar för varje vapen

weapon_3.Hits_W = r.randint(0, 3)

weapon_4.Hits_W = r.randint(0, 5)

weapon_5.Hits_W = r.randint(0, 25)

weapon_6.Hits_W = r.randint(0, 20)


# Här skapas en lista för spelarens vapen-inventory
weapon_inventory = [weapon_1]