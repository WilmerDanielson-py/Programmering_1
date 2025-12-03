#combat system v2
import random as r
import math
from colorama import init, Fore, Style
init(autoreset=True)
from entity_class import *
from weapon_class import *
from colors import *
from item_class import *
from player_class import *
from dictionary import *
from shop import *
from typing_speed import *
from testfil import *

def dodge_attack():
    dodge_prob = r.randint(1, 5)
    if dogde_prob == 1:
        print(Fore.GREEN)("You dodged the attack! Im pround of you unlike your parents you looser\n")

    else:
        Player_1.HP_P = Player_1.HP_P - entity_n.STR_E
        print(f"You received {entity_n.STR_E} {Fore.RED}damage{Style.RESET_ALL} from the {entity_n.Name_E}!\nYour current {HP} is now {Player_1.HP_P}/{Player_1.MaxHP_P}.\n")

