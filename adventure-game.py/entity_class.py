import random as r
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



Blade = CYAN("Blade")
Gun = YELLOW("Gun")
HP = RED("HP")
Strength = RED("Strength")

class entity():
    def __init__(self, Name_E, Element_E, HP_E, Weak_E, STR_E, AtkSpeed_E, MaxHP_E, LVL_E, Gold_drop):
        self.Name_E = Name_E
        self.STR_E = STR_E
        self.HP_E = HP_E
        self.Element_E = Element_E
        self.Weak_E = Weak_E
        self.AtkSpeed_E = AtkSpeed_E
        self.MaxHP_E = MaxHP_E
        self.LVL_E = LVL_E
        self.Gold_drop = Gold_drop
# Här skapas en strängrepresentation av fienden
    def __str__(self):
        return f"You have encountered a {self.Element_E} type {self.Name_E} meaning its weak to {self.Weak_E} type attacks.\nIts stats are:\n   {Strength}: {self.STR_E}\n   {HP}: {self.HP_E}\n   {Fore.BLUE}AtkSpeed{Style.RESET_ALL}: {self.AtkSpeed_E}\n"
    


# Här skapas fiender
# entity = entity("name","type","HP","weak","STR","Atkspeed","maxHP","Level_gain","Gold_drop")


entity_1 = entity("Goblin","Normal",150,Blade + " and " + Gun,5, 10, 150, 1, 20)
entity_2 = entity("Zombie","Undead",170,Blade,10, 12, 170, 1, 30)
entity_3 = entity("Skeleton","Undead",120,Blade,8, 14, 120, 1, 25)
entity_4 = entity("Ghoul","Undead",150,Gun,12, 13, 150, 1, 35)
entity_5 = entity("Wolf","Beast",130,Gun,11, 16, 130, 1, 30)


entity_15 = entity("Bandit Fighter","Human",720,Blade,16, 14, 720, 1, 55)
entity_16 = entity("Ghoul Brute","Undead",510,Blade,30, 12, 210, 1, 65)
entity_17 = entity("Dire Wolf","Beast",220,Gun,50, 15, 220, 1, 70)


entity_9 = entity("Elite Goblin","Monster",500,Gun,24, 14, 260, 1, 100)
entity_10 = entity("Undead Champion","Undead",670,Blade,28, 11, 300, 2, 140)
entity_11 = entity("Bandit Captain","Human",320,Gun,30, 13, 320, 2, 180)
entity_12= entity("Warlock","Berserker",70,Gun,49, 15, 70, 1, 40)
entity_13 = entity("Ravager","Tank",3000,Gun,3, 8, 1000, 2, 60)
entity_14 = entity("Greger","Dark",1337,Blade,24, 15, 1337, 2, 100)

entity_6 = entity("Bellman","Jester","inf","Joke",10, 1, "inf", 6, 300)

entity_7 = entity("Johannes Thessén","Coder",5000,"Sunlight",99, 20, 5000, 8, 400)

entity_8 = entity(" ρ * ( ∂u/∂t  +  (u · ∇)u )  =  -∇p  +  μ ∇²u  +  f","Physics",2500,"Nikodesmos",25, 18, 2500, 10, 250)

# Här skapas funktioner för att gruppera fiender i olika svårighetsgrader
def t1():
    return [entity_1, entity_2,  entity_3, entity_4, entity_5]
def t2():
    return [entity_15, entity_16, entity_17]
def t3():
    return [entity_9, entity_10, entity_11, entity_12, entity_13, entity_14]





all_enteties = [entity_1, entity_2,  entity_3, entity_4, entity_5, entity_9, entity_10, entity_11, entity_12, entity_13, entity_14, entity_15, entity_16, entity_17]
