
import random as r
from shop import *
from colors import *
from attack import *
from item_class import *
from dictionary import *
from entity_class import *
from weapon_class import *
from player_class import *
from typing_speed import *

weapon_mod = 0  
# Här skapas funktionen dodge
def dodge():
    
        return r.randint(1, 5) == 1

# Här skapas fight-funktionen
def fight(player, enemy, weapon_inventory, room_encounter):
    if room_encounter >= 0 and room_encounter <= 9:
        enemy = r.choice(t1())
        
    elif room_encounter >= 10 and room_encounter <= 19:
        enemy = r.choice(t2())
        
    elif room_encounter >= 20 and room_encounter <= 29:
        enemy = r.choice(t3())
    enemy.HP_E = enemy.MaxHP_E
    print(enemy)
    # Här skapas en loop för fighten
    while enemy.HP_E > 0 and player.HP_P > 0:
        while True:
            action = input("Do you want to use your weapons (w) or use your items? (i)?\n: ").strip().lower()
            if action in ["w", "i"]:
                break
            else:
                print(RED("Invalid choice! Please enter 'w' or 'i'.\n"))
        # Här hanteras spelarens val under striden
        if action == "w":
            clear_terminal()
            print(enemy)
            print("\n\nYour weapons:")
            while True:
                for weaponidx, weapon in enumerate(weapon_inventory, start=1):
                        print(f"{weaponidx}. A {weapon.Type_W} type {weapon.Rarity_W} {weapon.Name_W}\n      {Damage}: {weapon.Dmg_W}\n      {Fore.BLUE}Attack Speed{Style.RESET_ALL}: {weapon.AtkSpeed_W}\n      {Fore.GREEN}Range{Style.RESET_ALL}: {weapon.Range_W}\n")
                
                try:
                    choice = int(input("Which weapon do you want to use? (Enter the weapon number)\n: "))
                    if 1 <= choice <= len(weapon_inventory):
                        chosen_weapon = weapon_inventory[choice - 1]
                        

                        if "Dagger" in chosen_weapon.Name_W:
                            chosen_weapon.Dmg_W = weapon_1.Dmg_W
                        elif "Rapier" in chosen_weapon.Name_W:  
                            chosen_weapon.Dmg_W = weapon_2.Dmg_W
                        elif "Zweihander" in chosen_weapon.Name_W:  
                            chosen_weapon.Dmg_W = weapon_3.Dmg_W
                        elif "Shorre" in chosen_weapon.Name_W:  
                            chosen_weapon.Dmg_W = weapon_4.Dmg_W
                        elif "Ak 5" in chosen_weapon.Name_W:  
                            chosen_weapon.Dmg_W = weapon_5.Dmg_W
                        elif "Golden Scar" in chosen_weapon.Name_W:  
                            chosen_weapon.Dmg_W = weapon_6.Dmg_W
                        elif "Musket" in chosen_weapon.Name_W:  
                            chosen_weapon.Dmg_W = weapon_7.Dmg_W
                        break
                    else:
                        print(RED("Invalid choice. Please enter a valid weapon number.\n"))
                except ValueError:
                    print(RED("Invalid input. Please enter a valid weapon number.\n"))
            
        
            apply_weapon_modifier(chosen_weapon, enemy)
            # Här hanteras vem som är snabbast och vad som händer därefter
            if chosen_weapon.AtkSpeed_W > enemy.AtkSpeed_E:
                clear_terminal()
                print("You are faster! You hit first!")
                
                if chosen_weapon.Hits_W == 0:
                    print("You missed!")
                    
                else:

                    hits = r.randint(1, chosen_weapon.Hits_W)
                    dmg = ((1.5 * chosen_weapon.Dmg_W * hits) + weapon_mod) + (1.5 * player.STR_P)   
                    enemy.HP_E -= dmg
                    print(f"You dealt {dmg} {Damage} with {hits} hit(s).")
                    if enemy.HP_E <= 0:
                        enemy.HP_E = 0
                        level_up(player, enemy)
                        increase_stat(player, enemy)
                            
                        return "won", room_encounter
            
            else:
                print("Too slow! Enemy hits first!")
                player.HP_P -= enemy.STR_E
                print(f"You received {enemy.STR_E} {Damage}.")
                if player.HP_P <= 0:
                    print(RED("You died..."))
                    return room_encounter, "dead"
                    
            # Här skapas en loop för själva striden
            while enemy.HP_E > 0 and player.HP_P > 0:

                while True:
                    choice = input("Continue your attack? (y/n)\n: ").lower().strip()
                    if choice in ["y", "n"]:
                        break
                    else:
                        print(RED("Invalid choice! Please enter 'y' or 'n'.\n"))
                        clear_terminal()
                if choice == "y":
                    clear_terminal()
                    if enemy.HP_E <= 0:
                        enemy.HP_E = 0
                    hits = r.randint(1, chosen_weapon.Hits_W)
                    
                    dmg = hits * (chosen_weapon.Dmg_W + player.STR_P) + weapon_mod
                    enemy.HP_E -= dmg
                    if enemy.HP_E <= 0:
                        enemy.HP_E = 0
                    print(f"You dealt {dmg} {Damage} with {hits} hits.")
                    print(f"The {enemy.Name_E} now has {enemy.HP_E}/{enemy.MaxHP_E} {HP}\n")
                    
                    if enemy.HP_E <= 0:
                        
                        print(GREEN(f"\nYou defeated the {enemy.Name_E}!\n"))
                        level_up(player, enemy)
                        increase_stat(player, enemy)
                        
                        return "won", room_encounter

                    if dodge():
                            print(GREEN("You dodged the enemy's attack!\n"))
                    else: 
                        player.HP_P -= enemy.STR_E
                        print(f"The {enemy.Name_E} hits you for {enemy.STR_E} {Damage}.")
                        print(f"Your {HP} is now {player.HP_P}/{player.MaxHP_P}")
                
                    if player.HP_P <= 0:
                        print(RED("You died..."))
                        return "dead"

                else:
                    clear_terminal()
                    if r.randint(1, 2) == 1:
                        print(GREEN("You escaped successfully!"))
                        
                        return "escaped", room_encounter
                    
                    else:
                        clear_terminal()
                        print(RED(f"You escaped but not unharmed! The enemy hit you for 20 damage!"))
                        player.HP_P -= 20
                        print(f"The {enemy.Name_E} hit you for 20 {Damage}\n")
                        print(f"You now have {player.HP_P}/{player.MaxHP_P} {HP} left.")
                        
                        if player.HP_P <= 0:
                            print(RED("You died..."))
                            return "dead"
                        return "escaped_after_hit", room_encounter
        elif action == "i":
            clear_terminal()
            item_inventory_display(player, item_inventory)