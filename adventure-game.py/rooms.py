import random as r
from attack import *
from colors import *
from Johannes import boss
from weapon_class import *
from player_class import *
from typing_speed import *
from entity_class import *
from bellman import miniboss_Bellman
from physics_enemy import miniboss_Physics

def ta_player_action():
    
    valid_actions = ["m", "e", "s", "d", "w", "i", "q"]
    while True:
        player_action = input(CYAN("\nWhat do you wish to do? \n   Enter to a new room? (m)\n   Enter the market? (e)\n   View your stats? (s)\n   View the dictionary? (d)\n   View your weapon inventory? (w)\n   Use/View your item inventory? (i)\n   Exit the game? (q)\n: ")).lower().strip()
        clear_terminal()
        if player_action in valid_actions:
            return player_action
        else:
            print(RED("\nInvalid choice! Please select one of the options:"))
            clear_terminal()

def rooms(player, weapon_inventory, item_inventory, player_action, room_encounter, alive, miniboss_trigger, boss_trigger):
    if player_action == "m":
        if miniboss_trigger:
            miniboss_chance = r.choice(["Bellman", "Physics_Entity"])
            if miniboss_chance == "Bellman":
                alive = miniboss_Bellman(player, entity_6, alive, room_encounter, miniboss_chance)
            elif miniboss_chance == "Physics_Entity":
                alive = miniboss_Physics(player, entity_8, alive, room_encounter, miniboss_chance)
            miniboss_trigger = False
        elif boss_trigger:
            alive = boss(player, entity_7, weapon_inventory, item_inventory, alive)
            boss_trigger = False
        else:
            valid_doors = ["l", "m", "r"]
            while True:
                door = input("\nYou see three doors in front of you, do you wish to enter \n   The left door (l), \n   The middle door (m), \n   The right door (r)?\n: ").lower().strip()
                
                if door in valid_doors:
                    break
                else:
                    print(RED("Invalid choice!\n"))
    # Här hanteras rummets innehåll när spelaren väljer en dörr
            
            clear_terminal()
            if door == "l" or door == "m" or door == "r":
                encounter = r.randint(1,2)
                if encounter == 1:



                    enemy = r.choice(all_enteties)
                    enemy.HP_E = enemy.MaxHP_E
                    result = fight(player, enemy, weapon_inventory, room_encounter)

                    if result == "won":
                        room_encounter += 1

                    elif result in ["escaped", "escaped_after_hit"]:
                        room_encounter += 1

                    elif result == "dead":
                        alive = False
                    


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
                            
                            weapon_already_owned = any(i.Name_W == new_weapon.Name_W for i in weapon_inventory)
                            if weapon_already_owned:
                                print(RED("You already have this weapon! It remains in the chest.\n"))
                                player.Level_P = player.Level_P + 1
                                rounded = math.floor(player.Level_P)
                                print(f"You have gained 1 {Level}(s).\n")
                                print(f"You have now reached {Level} {rounded}.")
                            else:
                                
                                print(f"{new_weapon}\n")
                                player.Level_P = player.Level_P + 1
                                rounded = math.floor(player.Level_P)
                                print(f"You have gained 1 {Level}(s).\n")
                                print(f"You have now reached {Level} {rounded}.")
                                weapon_inventory.append(new_weapon)
                        else:
                            
                            # Här hanteras item inventory
                            if len(item_inventory) == 5:
                                print(RED("Your item inventory is full!\n"))
                                if item_inventory:
                                    print("Your items:")
                                    for item in item_inventory:
                                        print(f"{item}")
                                else:
                                    print("Your item inventory is empty.")
                                while True:
                                    full_inv = input("You must use (u) an item before picking up a new one.\n: ").lower().strip()
                                    if full_inv == "u":
                                        break
                                    else:
                                        print(RED("Invalid choice! Please enter 'u' to use an item.\n"))
                                for item in item_inventory:
                                    print(item)
                                valid_items = ["hp", "str", "sh"]
                                while True:
                                    use_item = input("Which item do you wish to use? (HP, STR, SH) \n: ").lower().strip()
                                    if use_item in valid_items:
                                        break
                                    else:
                                        print(RED("Invalid choice! Please enter 'HP', 'STR', or 'SH'.\n"))
                                if use_item == "hp":
                                    player.HP_P = player.HP_P + 30
                                elif use_item == "str":
                                    player.STR_P = player.STR_P + 5
                                elif use_item == "sh":
                                    player.MaxHP_P = player.MaxHP_P + 30
                                        
                                
                     
                            else:
                                print("There seems to be an item chest here!\n")
                                new_item = r.choice([item_1, item_2, item_3])
                                print(f"Wow, you found a {new_item.Name_I}!\n")
                                
                                player.Level_P = player.Level_P + 1
                                rounded = math.floor(player.Level_P)
                                print(f"You have gained 1 {Level}.")
                                print(f"You have now reached {Level} {rounded}.\n")
                                print(f"{new_item}\n")

                                add_item_to_inventory(player, item_inventory, new_item)
                    else: 
                        trap_dmg = r.randint(5,15)
                        trap_room = r.randint(1,3) 
                        if trap_room == 1:
                            player.HP_P = player.HP_P - trap_dmg
                            print(f"\nYou have fallen into a trap room and lost {trap_dmg} {HP}!\n")
                            print(f"You now have {player.HP_P}/{player.MaxHP_P} {HP}\n")
                        else:
                            print(BLUE("\nYou have found an empty room. Better luck next time!\n"))
                room_encounter += 1
                print(f"You have now entered {room_encounter} room(s).\n")
                if room_encounter == 15:
                    miniboss_trigger = True
                elif room_encounter == 30:
                    boss_trigger = True
        
    
    return room_encounter, alive, miniboss_trigger, boss_trigger