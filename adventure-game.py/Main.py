# Här importeras alla nödvändiga moduler och klasser

from shop import *
from rooms import *
from attack import *
from colors import *
from bellman import *
from Johannes import *
from item_class import *
from dictionary import *
from entity_class import *
from weapon_class import *
from player_class import *
from typing_speed import *
from physics_enemy import *

# här deklareras variabeln my_shop som en instans av klassen shop.
my_shop = shop()

# Här skapas huvudfunktionen för spelet
def main():
    clear_terminal()
    print_slow("Student was a programming student who was most comfortable in front of the computer. Code was clear and logical, which suited him perfectly.\n")
    print_slow("Math and physics, however, were subjects student had difficulty with and didn't really get into. \n")
    print_slow("At school, student had a teacher named Johannes, who taught in a serious and structured way. ")
    print_slow("Johannes played an important role in the student's schooling, \nbut something always felt off... even if the subjects weren't always his favorites.\n")
    print_slow("Something that always bothered the student, however, were Bellman jokes. ")
    print_slow("He never understood why they were funny and often thought they took focus away from more important things. \n")
    print_slow("Instead, student used his energy for programming. ")
    print_slow("Through code, student found his way to express himself and develop.\n\n")
    print_slow("One day, however, everything changed. The student was on vacation and found himself in a mysterious dungeon on an abandoned island far far away from the school...\n\n")
    conti = True
    while conti == True:
        conti = input("Press Enter to continue...\n: ")
        if conti == "":
            conti = False
            clear_terminal()
        else:
            conti = True
            print(RED("Staying a bit longer..."))
# Här skapas spelaren
    player_name = input("\nWhat is your name, student?\n: ")
    Player_1 = Player(player_name, 150, 150, 1, 0, 20, 0)
    clear_terminal()
    print(GREEN("\nHi " + Player_1.Name_P + ", welcome to the dungeon!\n"))
    
    print_slow("Your objective is to defeat the boss at the end of the dungeon.\nThe dungeon is composed of many different rooms, trap rooms, monster rooms and loot rooms.\nYou will encounter various enemies along the way and collect more powerful weapons to help you on your journey.\n")
    print(f"\nYou start with a {Fore.BLACK}Common{Style.RESET_ALL} Dagger as your weapon.\n   The stats are:\n   {Fore.RED}Damage{Style.RESET_ALL}: 15\n   {Fore.BLUE}Attack Speed{Style.RESET_ALL}: 20\n   {Fore.GREEN}Range{Style.RESET_ALL}: 1.\n")
    print("You have " + str(Player_1.HP_P) + f" {HP} and are at {Level} " + str(Player_1.Level_P) + ". Good luck on your adventure!\n")
    
    
    alive = True
    room_encounter = 0
    miniboss_trigger = False
    boss_trigger = False
    
    # 30 rum innan slutbossen
    while room_encounter < 31 and alive:

        # Om du går in i ett nytt rum
        player_action = ta_player_action()
        room_encounter, alive, miniboss_trigger, boss_trigger = rooms(Player_1, weapon_inventory, item_inventory, player_action, room_encounter, alive, miniboss_trigger, boss_trigger) 

    # Här hanteras de andra valen i menyn
        if player_action == "s":
            print(Player_1)
            
        elif player_action == "w":
            print("\nYou have the following weapons at your disposal:\n")
            for weapon in weapon_inventory:
                print(f"{weapon}\n")
        
        elif player_action == "d":
            Dictionary()
            
        elif player_action == "i":
            item_inventory_display(Player_1, item_inventory)
        
        elif player_action == "e":
            print(f"\nWelcome to the {Fore.BLACK}black market{Style.RESET_ALL}! Here are the available items:\n")
            my_shop.show(Player_1.Gold_gain)
            while True:
                try:
                    choice = int(input("What do you want to buy? (Enter the item number)\n: ").strip())
                    if 0 <= choice <= 7:
                        break
                    else:
                        print(RED("Invalid choice! Please enter a number between 0 and 7.\n"))
                except ValueError:
                    print(RED("Invalid input! Please enter a number.\n"))
            Player_1.Gold_gain = my_shop.buy(choice, Player_1.Gold_gain)
            if choice != 0:
                print(f"\nYou now have {Player_1.Gold_gain} {Gold} left.")
        elif player_action == "q":
            print("\nThank you for playing! Goodbye!\n")
            alive = False
        
        
main()
print("The game has been terminated along with your save files.\n\n")