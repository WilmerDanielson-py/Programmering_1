# Här importeras random för att kunna använda slumpgeneratorer
import random as r
# Här impoerteras matte för att använda vissa mattematiska funktioner
import math
# Här importeras nödvändiga bibliotek
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

# Här skapas huvudfunktionen för spelet
def main():

# Här skapas spelaren
    player_name = input("\nWhat is your name brave one?\n: ")
    Player_1 = Player(player_name, 150, 150, 1, 0, 20, 0)
    print(GREEN("\nHi " + Player_1.Name_P + ", welcome to the dungeon!\n"))
    print("Your objective is to defeat the boss at the end of the dungeon.\nThe dungeon is composed of many different rooms, trap rooms, monster rooms and loot rooms.\nYou will encounter various enemies along the way and collect more powerful weapons to help you on your journey.")
    print(f"\nYou start with a {Fore.BLACK}Common{Style.RESET_ALL} Dagger as your weapon.\n   The stats are:\n   {Fore.RED}Damage{Style.RESET_ALL}: 15\n   {Fore.BLUE}Attack Speed{Style.RESET_ALL}: 20\n   {Fore.GREEN}Range{Style.RESET_ALL}: 1.\n")
    print("You have " + str(Player_1.HP_P) + f" {HP} and are at {Level} " + str(Player_1.Level_P) + ". Good luck on your adventure!\n")
    
# temporär dodge test ememojs ingen aning hur länge den komemr vara kvar eller om det ens funkar
    def dodge_attac():
        dogde_prob = r.randint(1, 100)
        if dogde_prob <= 20: #20% chans
            return True
        else:
           return False

    # Här skapas en räknare för antal rum spelaren har gått igenom, om spelaren når rum 30 så möter den bossen, även vilkoren för att spelet ska fortsätta
    alive = True
    room_encounter = 0 
    while room_encounter < 30 and alive:

    # Här skapas en meny för spelaren att välja vad den vill göra
        player_action = input(CYAN("\nWhat do you wish to do? \n   Enter to a new room? (m)\n   Enter the market? (e)\n   View your stats? (s)\n   View the dictionary? (d)\n   View your weapon inventory? (w)\n   View your item inventory? (i)\n   Exit the game? (q)\n: ")).lower()
        stats = [Player_1.HP_P, Player_1.MaxHP_P, Player_1.STR_P ]
    # Här hanteras spelarens val
        if player_action == "m":
            door = input("\nYou see three doors in front of you, do you wish to enter \n   The left door (l), \n   The middle door (m), \n   The right door (r)?\n: ").lower()

            print(f"\nYou chose the {door} door...\n")
            if door == "l" or door == "m" or door == "r":
                encounter = r.randint(1,2)
                if encounter == 1:

                        entity_n = r.choice(all_enteties)
                        print((entity_n))
                        
                        action = input("Do you wish to attack (a), or do you wish to escape (e)?\n: ").lower()
                        if action == "a":
                            
                            if weapon_inventory:
                                print("Your weapons:")
                                for _weapon in weapon_inventory:
                                    print(f"{_weapon}\n")
                            weapon_choice = input("What weapon do you wish to use?\n: ").strip().lower()

                        # hittar det valda vapnet med hjälp av namnet och listan över vapen i inventory
                            
                            chosen_weapon = None
                            for _weapon in weapon_inventory:
                                if _weapon.Name_W.lower() == weapon_choice:
                                    chosen_weapon = _weapon
                                    break
                            if chosen_weapon is None:
                                print(RED("You don't have that weapon. Using your first weapon instead.\n"))
                                chosen_weapon = weapon_inventory[0]
                            
                            if chosen_weapon.AtkSpeed_W > entity_n.AtkSpeed_E:
                                print(f"You have chosen to attack with the {chosen_weapon.Name_W}.\n")
                                if chosen_weapon.Hits_W == 0:
                                    print(f"You missed!\n")
                                    if dodge_attac() == True:
                                        print(Fore.GREEN("You dodged the attack!\n"))
                                        print(f"You took no damage from the {entity_n.Name_E}!\n")
                                
                                    else:
                                        Player_1.HP_P = Player_1.HP_P - entity_n.STR_E
                                        print(f"You received {entity_n.STR_E} {Fore.RED}damage{Style.RESET_ALL} from the {entity_n.Name_E}!\nYour current {HP} is now {Player_1.HP_P}/{Player_1.MaxHP_P}.\n")
                                hits_this_turn = r.randint(1, chosen_weapon.Hits_W)
                                dmg_chosen_weapon = chosen_weapon.Dmg_W * hits_this_turn
                                total_dmg = Player_1.STR_P + dmg_chosen_weapon
                                entity_n.HP_E = entity_n.HP_E - total_dmg
                                print(f"You dealt a total of {total_dmg} {Fore.RED}damage{Style.RESET_ALL} with {hits_this_turn} hit(s) to the {entity_n.Name_E}!\nIts current {HP} is now {entity_n.HP_E}.\n")
                            elif chosen_weapon.AtkSpeed_W <= entity_n.AtkSpeed_E:
                                print("\nToo slow!\n")
                                print(f"The {entity_n.Name_E} is faster!\n")
                                Player_1.HP_P = Player_1.HP_P - entity_n.STR_E
                                print(f"You received {entity_n.STR_E} {Fore.RED}damage{Style.RESET_ALL} from the {entity_n.Name_E}!\nYour current {HP} is now {Player_1.HP_P}/{Player_1.MaxHP_P}.\n")
                            while entity_n.HP_E > 0 and Player_1.HP_P > 0:
                                hits_this_turn = r.randint(1, chosen_weapon.Hits_W)
                                dmg_chosen_weapon = chosen_weapon.Dmg_W * hits_this_turn
                                total_dmg = Player_1.STR_P + dmg_chosen_weapon


                                your_turn = input("Do you wish to continue your attack? (y/n)\n: ").lower()
                                if your_turn == "y":


                                    entity_n.HP_E = entity_n.HP_E - total_dmg
                                    print(f"You dealt a total of {total_dmg} {Fore.RED}damage{Style.RESET_ALL} with {hits_this_turn} hit(s) to the {entity_n.Name_E}!\nIts current {HP} is now {entity_n.HP_E}.\n")
                                    if entity_n.HP_E <= 0:
                                        Player_1.Level_P = Player_1.Level_P + entity_n.LVL_E
                                        rounded = math.floor(Player_1.Level_P)
                                        print(f"You have gained {entity_n.LVL_E} levels.")
                                        print(f"You have now reached level {rounded}.\n")
                                        Player_1.Gold_gain = Player_1.Gold_gain + entity_n.Gold_drop
                                        print(f"You have gained {entity_n.Gold_drop} gold from defeating the {entity_n.Name_E}.")
                                        print(f"You now have {Player_1.Gold_gain} gold in your fanny-pack")
                                        room_encounter += 1
                                        break
                                    Player_1.HP_P = Player_1.HP_P - entity_n.STR_E
                                    print(f"You received {entity_n.STR_E} {Fore.RED}damage{Style.RESET_ALL} from the {entity_n.Name_E}!\nYour current {HP} is now {Player_1.HP_P}/{Player_1.MaxHP_P}.\n")
                                    if Player_1.HP_P <= 0:
                                        alive = False
                                        print(RED("You have been defeated by the " + entity_n.Name_E + ". Game Over!\n"))
                                        break

                                elif your_turn == "n":
                                    escape_ = r.randint(1,2)
                                    if escape_ == 1:
                                        print(GREEN("\nYou escaped successfully!\n"))
                                        room_encounter += 1
                                        break
                                    else:
                                        print(RED(f"\nYou failed to escape, but the {entity_n} got one last hit on you.\n"))
                                        Player_1.HP_P = Player_1.HP_P - 20
                                        print(f"You received 20 {Fore.RED}damage{Style.RESET_ALL} from the {entity_n.Name_E}!\nYour current {HP} is now {Player_1.HP_P}/{Player_1.MaxHP_P}.\n")
                                        room_encounter += 1
                                    break

                        elif action == "e":
                            escape = r.randint(1,3) 
                            if escape == 1:
                                print(GREEN("\nYou got scared by the monster and fled.\n"))
                                room_encounter += 1
                                
                            elif escape == 2 or escape == 3:
                                print(RED("\nYou got so scared by the monster you couldn´t move, now prepare for battle!\n"))

                                if weapon_inventory:
                                    print("Your weapons:")
                                for _weapon in weapon_inventory:
                                    print(f"{_weapon}\n")
                            weapon_choice = input("What weapon do you wish to use?\n: ").strip().lower()

                        # hittar det valda vapnet med hjälp av namnet och listan över vapen i inventory
                        
                            chosen_weapon = None
                            for _weapon in weapon_inventory:
                                if _weapon.Name_W.lower() == weapon_choice:
                                    chosen_weapon = _weapon
                                    break
                            if chosen_weapon is None:
                                print(RED("You don't have that weapon. Using your first weapon instead.\n"))
                                chosen_weapon = weapon_inventory[0]
                                
                            if chosen_weapon.AtkSpeed_W > entity_n.AtkSpeed_E:
                                print(f"You have chosen to attack with the {chosen_weapon.Name_W}.\n")
                                if chosen_weapon.Hits_W == 0:
                                    print(f"You missed!\n")
                                    Player_1.HP_P = Player_1.HP_P - entity_n.STR_E
                                    print(f"You received {entity_n.STR_E} {Fore.RED}damage{Style.RESET_ALL} from the {entity_n.Name_E}!\nYour current {HP} is now {Player_1.HP_P}/{Player_1.MaxHP_P}.\n")
                                dmg_chosen_weapon = chosen_weapon.Dmg_W * chosen_weapon.Hits_W
                                total_dmg = Player_1.STR_P + dmg_chosen_weapon
                                entity_n.HP_E = entity_n.HP_E - total_dmg
                                print(f"You dealt a total of {total_dmg} {Fore.RED}damage{Style.RESET_ALL} with {chosen_weapon.Hits_W} hit(s) to the {entity_n.Name_E}!\nIts current {HP} is now {entity_n.HP_E}.\n")
                            elif chosen_weapon.AtkSpeed_W <= entity_n.AtkSpeed_E:
                                print("\nToo slow!\n")
                                print(f"The {entity_n.Name_E} is faster!\n")
                                Player_1.HP_P = Player_1.HP_P - entity_n.STR_E
                                print(f"You received {entity_n.STR_E} {Fore.RED}damage{Style.RESET_ALL} from the {entity_n.Name_E}!\nYour current {HP} is now {Player_1.HP_P}/{Player_1.MaxHP_P}.\n")
                            while entity_n.HP_E > 0 and Player_1.HP_P > 0:
                                dmg_chosen_weapon = chosen_weapon.Dmg_W * chosen_weapon.Hits_W
                                total_dmg = Player_1.STR_P + dmg_chosen_weapon


                                your_turn = input("Do you wish to attack? (y/n)\n: ").lower()
                                if your_turn == "y":


                                    entity_n.HP_E = entity_n.HP_E - total_dmg
                                    print(f"You dealt a total of {total_dmg} {Fore.RED}damage{Style.RESET_ALL} with {chosen_weapon.Hits_W} hit(s) to the {entity_n.Name_E}!\nIts current {HP} is now {entity_n.HP_E}.\n")
                                    if entity_n.HP_E <= 0:
                                        Player_1.Level_P = Player_1.Level_P + entity_n.LVL_E
                                        rounded = math.floor(Player_1.Level_P)
                                        print(f"You have gained {entity_n.LVL_E} levels.")
                                        print(f"You have now reached level {rounded}.\n")
                                        Player_1.Gold_gain = Player_1.Gold_gain + entity_n.Gold_drop
                                        print(f"You have gained {entity_n.Gold_drop} gold from defeating the {entity_n.Name_E}.")
                                        print(f"You now have {Player_1.Gold_gain} gold in your fanny-pack")
                                        break
                                    Player_1.HP_P = Player_1.HP_P - entity_n.STR_E
                                    print(f"You received {entity_n.STR_E} {Fore.RED}damage{Style.RESET_ALL} from the {entity_n.Name_E}!\nYour current {HP} is now {Player_1.HP_P}/{Player_1.MaxHP_P}.\n")
                                    if Player_1.HP_P <= 0:
                                        alive = False
                                        print(RED("You have been defeated by the " + entity_n.Name_E + ". Game Over!\n"))
                                        break

                                elif your_turn == "n":
                                    escape_ = r.randint(1,2)
                                    if escape_ == 1:
                                        print(GREEN("\nYou escaped successfully!\n"))
                                        room_encounter += 1
                                        break
                                    else:
                                        print(RED("\nYou escaped, but the " + entity_n.Name_E + " got one last hit on you.\n"))
                                        Player_1.HP_P = Player_1.HP_P - 20
                                        print(f"You received 20 {Fore.RED}damage{Style.RESET_ALL} from the {entity_n.Name_E}!\nYour current {HP} is now {Player_1.HP_P}/{Player_1.MaxHP_P}.\n")
                                        room_encounter += 1
                                    break

                
                            print(f"You have now entered {room_encounter} room(s).\n")
            # Här hanteras loot rooms, trap rooms och tomma rum
                else:
                    loot_room = r.randint(1,2)
                    if loot_room == 1:
                        print(YELLOW("\nYou have found a loot room!\n"))
                        weapon_chest = r.randint(1,2)
                        
                        if weapon_chest == 1:
                            print("There seems to be a weapon chest here!\n")
                            new_weapon = r.choice([weapon_2, weapon_3, weapon_4, weapon_5, weapon_6, weapon_7])
                            print(f"Wow, you found a {new_weapon.Rarity_W} {new_weapon.Name_W}!\n")
                            print(f"{new_weapon}\n")
                            Player_1.Level_P = Player_1.Level_P + 0.5
                            rounded = math.floor(Player_1.Level_P)
                            print(f"You have gained 0.5 levels.\n")
                            print(f"You have now reached level {rounded}.")
                            weapon_inventory.append(new_weapon)
                        else:
                            
                        # Härhanteras användandet av ett item när inventory är fullt
                            if len(item_inventory) == 5:
                                print(RED("Your item inventory is full!\n"))
                                if item_inventory:
                                    print("Your items:")
                                    for item in item_inventory:
                                        print(f"{item}")
                                else:
                                    print("Your item inventory is empty.")
                                full_inv = input("You must use (u) an item before picking up a new one.\n: ").lower()
                                if full_inv == "u":
                                    for item in item_inventory:
                                        print(item)
                                    use_item = input("Which item do you wish to use? (HP, STR, SH) \n: ").lower()
                                    if use_item == "hp":
                                        Player_1.HP_P = Player_1.HP_P + 30
                                    elif use_item == "str":
                                        Player_1.STR_P = Player_1.STR_P + 50
                                    elif use_item == "sh":
                                        Player_1.MaxHP_P = Player_1.MaxHP_P + 30
                                        
                                
                        # Här hanteras items när item_inventory inte är fullt
                            else:
                                print("There seems to be an item chest here!\n")
                                new_item = r.choice([item_1, item_2, item_3])
                                print(f"Wow, you found a {new_item.Name_I}!\n")
                                Player_1.Level_P = Player_1.Level_P + 0.5
                                rounded = math.floor(Player_1.Level_P)
                                print(f"You have gained 0.5 levels.\n")
                                print(f"You have now reached level {rounded}.")
                                print(f"{new_item}\n")

                                if new_item.Name_I == (f"{Health} {Elixir}"):
                                    use_elixir = input(f"Do you wish to use the {Health} {Elixir} now? (y/n)\n: ").lower()
                                    if use_elixir == "y":
                                        if Player_1.HP_P == Player_1.MaxHP_P:
                                            print(f"\nYour {HP} is already full at {Player_1.HP_P}/{Player_1.MaxHP_P}.\nThe {Health} {Elixir} has been stored in your item inventory for safe keeping.\n")
                                            item_inventory.append(new_item)
                                            print(f"You now have {len(item_inventory)}/5 items in your item inventory.\n")
                                        else:
                                            Player_1.HP_P += 30
                                            print(f"\nYou used the {Health} {Elixir} and restored 30 {HP}! Your current {HP} is now {Player_1.HP_P}/{Player_1.MaxHP_P}.\n")
                                    elif use_elixir == "n":
                                        print(f"You chose not to use the {Health} {Elixir} now. Its stored in your item inventory for safe keeping\n")
                                        item_inventory.append(new_item)
                                        print(f"You now have {len(item_inventory)}/5 items in your item inventory.\n")
                                    else:
                                        print("Invalid input. The item has been stored in your item inventory for safe keeping.\n")
                                        item_inventory.append(new_item)

                                elif new_item.Name_I == (f"{Strength} {Elixir}"):
                                    use_elixir = input(f"Do you wish to use the {Strength} {Elixir} now? (y/n)\n: ").lower()
                                    if use_elixir == "y":
                                        Player_1.STR_P += 50
                                        print(f"\nYou used the {Strength} {Elixir} and increased your {Strength} by 50! Your current {Strength} is now {Player_1.STR_P}.\n")
                                    elif use_elixir == "n":
                                        print(f"You chose not to use the {Strength} {Elixir} now. Its stored in your item inventory for safe keeping\n")
                                        item_inventory.append(new_item)
                                        print(f"You now have {len(item_inventory)}/5 items in your item inventory.\n")
                                    else:
                                        print("Invalid input. The item has been stored in your item inventory for safe keeping.\n")
                                        item_inventory.append(new_item)

                                elif new_item.Name_I == (f"{Shield}"):
                                    equip_shield = input(f"Do you wish to equip the {Shield} now? (y/n)\n: ").lower()
                                    if equip_shield == "y":
                                        Player_1.MaxHP_P += 30
                                        print(f"\nYou used the {Shield} and increased your max {HP} by 30! Your current max {HP} is now {Player_1.MaxHP_P}.\n")
                                    elif equip_shield == "n":
                                        print(f"You chose not to equip the {Shield} now. Its stored in your item inventory for safe keeping\n")
                                        item_inventory.append(new_item)
                                        print(f"You now have {len(item_inventory)}/5 items in your item inventory.\n")
                                    else:
                                        print("Invalid input. The item has been stored in your item inventory for safe keeping.\n")
                                        item_inventory.append(new_item)
                                        print(f"You now have {len(item_inventory)}/5 items in your item inventory.\n")
                            
                    else: 
                        trap_dmg = r.randint(5,15)
                        trap_room = r.randint(1,3) 
                        if trap_room == 1:
                            Player_1.HP_P -= trap_dmg
                            print(f"\nYou have fallen into a trap room and lost {trap_dmg} {HP}!\n")
                            print(f"You now have {Player_1.HP_P/Player_1.MaxHP_P} {HP}\n")
                        else:
                            print(BLUE("\nYou have found an empty room. Better luck next time!\n"))
                    room_encounter += 1
                    print(f"You have now entered {room_encounter} room(s).\n")
            else: 
                print("Invalid input, going to menu...")          

        # Här hanteras bossmötet när spelaren når rum 30
            if room_encounter >= 30:
                print(f"An ominous presence fills the room as you step forward.\nYou feel the air grow colder, and a deep rumble echoes through the dungeon walls.\nThe boss has awakened, and it's time to face your greatest challenge yet!\n{entity_7}\n")
                # Skapa bosskoden här

            elif room_encounter == 15:
                miniboss_chance = r.choice(["Bellman", "Physics_Entity"])
                print(f"As you step into the room, a sudden chill runs down your spine.\nThe atmosphere shifts, and you sense a powerful presence watching you.\nA shadowy figure emerges from the darkness. A Mini-Boss appears!\n")
                if miniboss_chance == "Bellman":
                    print(entity_6)
                # Skapa minibosskoden för Bellman här


                elif miniboss_chance == "Physics_Entity":
                    print(entity_8)
                # Skapa minibosskoden för Physics_Entity här

    # Här hanteras de andra valen i menyn
        elif player_action == "s":
            print(Player_1)
        elif player_action == "w":
            print("\nYou have the following weapons at your disposal:\n")
            for weapon in weapon_inventory:
                print(f"{weapon}\n")
        elif player_action == "i":
            if len(item_inventory) == 0:
                print("\nYou currently have no items...")
            else:
                print("\nYou have the following items at your disposal:\n")
                for item in item_inventory:
                    print(f"{item}\n")
        elif player_action == "d":
            print(Dictionary)
        elif player_action == "q":
            print("\nThank you for playing! Goodbye!\n")
            alive = False
        elif player_action == "e":
            print(f"\nWelcome to the {Fore.BLACK}black market{Style.RESET_ALL}! Here are the available items:\n")
            

            
        else: 
            print("Invalid input, going to menu...")
        
main()
print("The program has ended.\n\n")