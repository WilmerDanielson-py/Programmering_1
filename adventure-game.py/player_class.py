import math
from colors import *


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


class Player():
    def __init__(self, Name_P, HP_P, MaxHP_P, Level_P, STR_P, maxlevel_P, Gold_gain):
        self.Name_P = Name_P
        self.HP_P = HP_P
        self.MaxHP_P = MaxHP_P
        self.Level_P = Level_P
        self.STR_P = STR_P
        self.maxlevel_P = maxlevel_P
        self.Gold_gain = Gold_gain
        
    def increase_hp(self, amount):
        self.HP_P = min(self.HP_P + amount, self.MaxHP_P)
        

    def __str__(self):
        return f"\nStudent {Fore.GREEN}Name{Style.RESET_ALL}: {self.Name_P}\nStudent {HP}: {self.HP_P}/{self.MaxHP_P}\nStudent {Strength}: {self.STR_P}\nStudent {Level}: {math.floor(self.Level_P)}\n"

def level_up(self, enemy):
    self.Level_P += enemy.LVL_E
    rounded = math.floor(self.Level_P)
    print(f"You have gained {enemy.LVL_E} {Level}(s)")
    print(f"You are at {Level} {rounded}\n")
    self.Gold_gain = self.Gold_gain + enemy.Gold_drop
    print(f"You gained {enemy.Gold_drop} {Gold}!")
    print(f"You have {self.Gold_gain} {Gold}\n")


def increase_stat(self, enemy):
    while True:

        choice_stat = input(f"You leveled up {enemy.LVL_E} time(s)! Choose a stat to increase {enemy.LVL_E} time(s):\n1. Max {HP} (+5)\n2. {Strength} (+5):\n: ").strip()

        if choice_stat == "1":
            self.MaxHP_P += 5 * enemy.LVL_E
            self.increase_hp(15)
            print(f"Your Max HP increased to {self.MaxHP_P} and your current Max {HP} is now {self.MaxHP_P}.\n")
            
            hp_change = self.MaxHP_P - self.HP_P
            if hp_change > 0 and hp_change <= 15:
                self.increase_hp(hp_change)
                print(f"You also gained {hp_change} {HP}, your current {HP} is now {self.HP_P}/{self.MaxHP_P}.\n")
            else:
                print(f"You gained 15 {HP}, your current {HP} is now {self.HP_P}/{self.MaxHP_P}.\n")
            break
        elif choice_stat == "2":
            self.STR_P += 5 * enemy.LVL_E
            self.increase_hp(15)
            print(f"Your {Strength} has increased by 5 points and your current {Strength} is now {self.STR_P}.\n")
            print(f"You also gained 15 {HP}, your current {HP} is now {self.HP_P}.\n")
            break
        else:
            print("Invalid choice! Please enter '1' or '2'.")

Gold_gain = 0
