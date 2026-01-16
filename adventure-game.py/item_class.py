from colors import *
from typing_speed import *
from player_class import *

# Här skapas itemklassen
class item():
    def __init__(self, Name_I, Effect_I):
        self.Name_I = Name_I
        self.Effect_I = Effect_I

    def __str__(self):
        return f"{self.Name_I}:\n   {self.Effect_I}"
    

# Här skapas itemobjekt
item_1 = item(f"{Health} {Elixir}", f"Restores 30 {HP}")
item_2 = item(f"{Strength} {Elixir}", f"Increases {Strength} by 5")
item_3 = item(f"{Shield}", f"Increases max {HP} by 30")



# Här skapas en lista för spelarens item-inventory
item_inventory = []
# Här skapas en funktion för att lägga till items till spelarens inventory
def add_item_to_inventory(player, item_inventory, new_item):
    if new_item.Name_I == (f"{Health} {Elixir}"):
        while True:
            use_elixir = input(f"Do you wish to use the {Health} {Elixir} now? (y/n)\n: ").lower().strip()
            if use_elixir in ["y", "n"]:
                break
            else:
                print(RED("Invalid choice!\n"))
        if use_elixir == "y":
            if player.HP_P == player.MaxHP_P:
                print(f"\nYour {HP} is already full at {player.HP_P}/{player.MaxHP_P}.\nThe {Health} {Elixir} has been stored in your item inventory for safe keeping.\n")
                item_inventory.append(new_item)
                print(f"You now have {len(item_inventory)}/5 items in your item inventory.\n")
            else:
                player.HP_P += 30
                print(f"\nYou used the {Health} {Elixir} and restored 30 {HP}! Your current {HP} is now {player.HP_P}/{player.MaxHP_P}.\n")
        elif use_elixir == "n":
            print(f"You chose not to use the {Health} {Elixir} now. Its stored in your item inventory for safe keeping\n")
            item_inventory.append(new_item)
            print(f"You now have {len(item_inventory)}/5 items in your item inventory.\n")
        else:
            print("Invalid input. The item has been stored in your item inventory for safe keeping.\n")
            item_inventory.append(new_item)

    elif new_item.Name_I == (f"{Strength} {Elixir}"):
        while True:
            use_elixir = input(f"Do you wish to use the {Strength} {Elixir} now? (y/n)\n: ").lower().strip()
            if use_elixir in ["y", "n"]:
                break
            else:
                print(RED("Invalid choice!\n"))
        if use_elixir == "y":
            player.STR_P += 5
            print(f"\nYou used the {Strength} {Elixir} and increased your {Strength} by 5! Your current {Strength} is now {player.STR_P}.\n")
        elif use_elixir == "n":
            print(f"You chose not to use the {Strength} {Elixir} now. Its stored in your item inventory for safe keeping\n")
            item_inventory.append(new_item)
            print(f"You now have {len(item_inventory)}/5 items in your item inventory.\n")
        else:
            print("Invalid input. The item has been stored in your item inventory for safe keeping.\n")
            item_inventory.append(new_item)

    elif new_item.Name_I == (f"{Shield}"):
        while True:
            equip_shield = input(f"Do you wish to equip the {Shield} now? (y/n)\n: ").lower()
            if equip_shield in ["y", "n"]:
                break
            else:
                print(RED("Invalid choice!\n"))
        if equip_shield == "y":
            player.MaxHP_P += 30
            print(f"\nYou used the {Shield} and increased your max {HP} by 30! Your current max {HP} is now {player.MaxHP_P}.\n")
        elif equip_shield == "n":
            print(f"You chose not to equip the {Shield} now. Its stored in your item inventory for safe keeping\n")
            item_inventory.append(new_item)
            print(f"You now have {len(item_inventory)}/5 items in your item inventory.\n")
        else:
            print("Invalid input. The item has been stored in your item inventory for safe keeping.\n")
            item_inventory.append(new_item)
            print(f"You now have {len(item_inventory)}/5 items in your item inventory.\n")

# Här skapas en funktion för att visa och använda items från spelarens inventory
def item_inventory_display(player, item_inventory):
    clear_terminal()
    if not item_inventory:
        print(RED("Your item inventory is empty!\n"))
        
    else:
        print("Your items:")
        
        for idx, item in enumerate(item_inventory, start=1):
            print(f"{idx}. {item.Name_I}")
        
        try:
            print("\n0. Exit\n")
            choice = int(input("Which item do you want to use? (Enter the number)\n: "))
            if 1 <= choice <= len(item_inventory):
                selected_item = item_inventory[choice - 1]
                
                if "Health" in selected_item.Name_I:  
                    player.HP_P = min(player.HP_P + 30, player.MaxHP_P)
                    clear_terminal()
                    if player.HP_P > player.MaxHP_P:
                        player.HP_P = player.MaxHP_P
                        print(f"You used {selected_item.Name_I} and restored to full {HP}! Your {HP} is now {player.HP_P}/{player.MaxHP_P}.\n")
                    else:
                        print(f"You used {selected_item.Name_I} and restored 30 {HP}! Your {HP} is now {player.HP_P}/{player.MaxHP_P}.\n")
        
                elif "Strength" in selected_item.Name_I:  
                    player.STR_P += 5
                    clear_terminal()
                    print(f"You used {selected_item.Name_I} and gained 5 {Strength}! Your {Strength} is now {player.STR_P}.\n")

                elif "Shield" in selected_item.Name_I:  
                    player.MaxHP_P += 30
                    clear_terminal()
                    print(f"You used {selected_item.Name_I} and increased your Max {HP} by 30! Your Max {HP} is now {player.MaxHP_P}.\n")
                    
                    
                else:
                    print(RED("Unknown item effect. Nothing happened.\n"))
                    
                item_inventory.pop(choice - 1)
                print(f"You now have {len(item_inventory)}/5 items left.\n")
            elif choice == 0:
                clear_terminal()
                print("Exited item inventory.\n")
                
            else:
                print(RED("Invalid choice. Please select a valid item number.\n"))
        except ValueError:
            print(RED("Invalid input. Please enter a number.\n"))

# Här skapas en funktion för att kolla om item-inventory är fullt
def full_item_inv(item_inventory):
    if len(item_inventory) == 5:
            print(RED("Your item inventory is full!\n"))
            if item_inventory:
                print("Your items:")
                for item in item_inventory:
                    print(f"{item}")