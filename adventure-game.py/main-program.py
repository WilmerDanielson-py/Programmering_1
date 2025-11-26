import random as r

from colorama import init, Fore, Style
init(autoreset=True)
from entity_class import *
from weapon_class import *
from colors import *
from item_class import *
from player_class import *


# Här skapas en ordbok för fiendernas beskrivningar
Goblin = f"{Fore.GREEN}\nGoblin{Style.RESET_ALL}: \nGoblins are small, green humanoid creatures known for their mischievous nature and cunning tactics.\nThey often travel in packs and can be found in forests and caves. \nDespite their size, goblins can be quite dangerous due to their agility and numbers. \nThese goblins have a weakness to both Blade and Gun type attacks.\n\n"
Zombie = f"{Fore.YELLOW}Zombie{Style.RESET_ALL}: \nZombies are reanimated corpses that move with a slow, shuffling gait.\nThey are driven by an insatiable hunger for human flesh and are often found in graveyards or abandoned areas.\nZombies are relentless and can infect others with their bite, turning them into more zombies.\nThese zombies have a weakness to Blade type attacks.\n\n"
Ravager = f"{Fore.MAGENTA}Ravager{Style.RESET_ALL}: \nRavagers are large, heavily armored beasts that serve as tanks in battle.\nThey possess immense strength and durability, making them formidable opponents.\nRavagers are often used by dark forces to break through enemy lines and cause chaos on the battlefield.\nThese ravagers have a weakness to Gun type attacks.\n\n"
Warlock = f"{Fore.BLUE}Warlock{Style.RESET_ALL}: \nWarlocks are powerful spellcasters who have made pacts with dark entities to gain their magical abilities.\nThey can cast devastating spells and summon otherworldly creatures to do their bidding.\nWarlocks are often feared for their ability to manipulate the forces of darkness and bend them to their will.\nThese warlocks have a weakness to Gun type attacks.\n\n"
Greger = f"{Fore.BLACK}Greger{Style.RESET_ALL}: \nGreger is a mysterious dark entity known for his cunning and manipulative nature.\nHe thrives in the shadows, using deception and trickery to achieve his goals.\nGreger is a master of dark magic and can summon powerful minions to do his bidding.\nThese Gregers have a weakness to Blade type attacks.\n\n"
Bellman = f"{Fore.RED}Bellman{Style.RESET_ALL}: \nBellman is a jester-like figure who uses humor and wit to disarm his opponents.\nHe is known for his unpredictable nature and ability to turn the tide of battle with his clever tricks.\nBellman often employs illusions and distractions to confuse his enemies and gain the upper hand.\nThese Bellmen have a weakness to Joke type attacks.\n\n"
Johannes_Thessen = f"{Fore.CYAN}Johannes Thessén{Style.RESET_ALL}: \nJohannes Thessén is a legendary coder known for his unparalleled programming skills.\nHe is said to possess the ability to manipulate code in ways that defy conventional logic.\nJohannes is often sought after by those in need of complex software solutions and innovative algorithms.\nThese Johannes Thesséns have a weakness to Sunlight type attacks.\n\n"
Physics_Entity = f"{Fore.GREEN}Physics Entity{Style.RESET_ALL}: \nThis entity represents a complex physics equation that governs fluid dynamics.\nIt embodies the principles of motion, pressure, and viscosity in fluid systems.\nThis physics entity is often studied by scientists and engineers to understand and predict fluid behavior in various applications.\nThese Physics Entities have a weakness to Nikodesmos type attacks.\n\n"
Dictionary = Goblin + Zombie + Ravager + Warlock + Greger + Bellman + Johannes_Thessen + Physics_Entity

# Här skapas en "klass" för färgerna med colorama.

# Här skapas en klass för vapen

# Här skapars en klass för items

# Här skapars en klass för fiender

# Här skapas en klass för spelaren



all_enteties = [entity_1, entity_2,  entity_3, entity_4, entity_5]


# Här skapas huvudfunktionen för spelet
def main():

# Här skapas spelaren
    player_name = input("\nWhat is your name brave one?\n: ")
    Player_1 = Player(f"{player_name}", 100, 100, 1, 0)
    print(GREEN("\nHi " + Player_1.Name_P + ", welcome to the dungeon!\n"))
    print("Your objective is to defeat the boss at the end of the dungeon.\nThe dungeon is composed of many different rooms, trap rooms, monster rooms and loot rooms.\nYou will encounter various enemies along the way and collect more powerful weapons to help you on your journey.")
    print(f"\nYou start with a {Fore.BLACK}Common{Style.RESET_ALL} Dagger as your weapon.\n   The stats are:\n   {Fore.RED}Damage{Style.RESET_ALL}: 15\n   {Fore.BLUE}Attack Speed{Style.RESET_ALL}: 20\n   {Fore.GREEN}Range{Style.RESET_ALL}: 1.\n")
    print("You have " + str(Player_1.HP_P) + f" {HP} and are at {Level} " + str(Player_1.Level_P) + ". Good luck on your adventure!\n")

# Här skapas en räknare för antal rum spelaren har gått igenom, om spelaren når rum 30 så möter den bossen, även vilkoren för att spelet ska fortsätta
    alive = True
    room_encounter = 0 
    while room_encounter < 30 and alive:

    # Här skapas en meny för spelaren att välja vad den vill göra
        player_action = input(CYAN("\nWhat do you wish to do? \n   Enter to a new room? (m) \n   View your stats? (s)\n   View the dictionary? (d)\n   View your weapon inventory? (w)\n   View your item inventory? (i)\n   Exit the game? (q)\n: ")).lower()

    # Här hanteras spelarens val
        if player_action == "m":
            door = input("\nYou see three doors in front of you, do you wish to enter \n   The left door (left), \n   The middle door (middle), \n   The right door (right)?\n: ").lower()

            print(f"\nYou chose the {door} door...\n")
            if door == "left" or door == "middle" or door == "right":
                encounter = r.randint(1,2)
                if encounter == 1:
                    

                # Här skapas en slumpgenerator som väljer en fiende att möta
                    
                    # ,Zombie,"Ravager","Warlock","Greger"
                # Här skapas en strängrepresentation av fienden som valts och vad som händer vid en encounter
                    
                        
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
                                    break




                        elif action == "e":
                            escape = r.randint(1,3) 
                            if escape == 1:
                                print(GREEN("\nYou got scared by the monster and fled.\n"))
                                room_encounter += 1
                            else:
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


                                your_turn = input("Do you(y/n)\n: ").lower()
                                if your_turn == "y":


                                    entity_n.HP_E = entity_n.HP_E - total_dmg
                                    print(f"You dealt a total of {total_dmg} {Fore.RED}damage{Style.RESET_ALL} with {chosen_weapon.Hits_W} hit(s) to the {entity_n.Name_E}!\nIts current {HP} is now {entity_n.HP_E}.\n")
                                    if entity_n.HP_E <= 0:
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
                                    break


                        

                                
                            print(f"You have now entered {room_encounter} rooms.\n")
                    

                   
                                    
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
                                full_inv = input("You must use (u) or drop (d) an item before picking up a new one.\n: ").lower()
                                if full_inv == "u":
                                    for item in item_inventory:
                                        print(item)
                                        use_item = input("Which item do you wish to use?\n: ")
                                        # skriv koden för att använda ett item in
                                
                                elif full_inv == "d":
                                    for item in item_inventory:
                                        print(item)
                                        drop_item = input("Which item do you wish to drop?\n: ")
                                         # skriv koden för att droppa ett item in
                                


                            # Här hanteras items när item_inventory inte är fullt
                            else:
                                print("There seems to be an item chest here!\n")
                                new_item = r.choice([item_1, item_2, item_3])
                                print(f"Wow, you found a {new_item.Name_I}!\n")
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
                                    equip_shield = input(f"Do you wish to Equip the {Shield} now? (y/n)\n: ").lower()
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
                    print(f"You have now entered {room_encounter} rooms.\n")
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
            print("\nYou have the following items at your disposal:\n")
            for item in item_inventory:
                print(f"{item}\n")
        elif player_action == "d":
            print(Dictionary)
        elif player_action == "q":
            print("\nThank you for playing! Goodbye!\n")

            alive = False
        else: 
            print("Invalid input, going to menu...")
            
main()
print("The program has ended.")
# #def draw_room(player_icon="P" , enemy_icon="E", Entity_in_room):
# #    pass
