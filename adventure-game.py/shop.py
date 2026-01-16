from colors import *
from item_class import *
from weapon_class import *
from player_class import *
# Här skapas shopklassen
class shop:
    def __init__(self):
        self.stock = ["item_1","item_2","item_3","weapon_4","weapon_5","weapon_6","weapon_7"]

    def show(self, gold):
        print(f"\n{Fore.BLACK}---> BLACK MARKET <---{Style.RESET_ALL}\n")
        print(f"You have {gold} {Gold}.\n")
        print(f"1. {Health} {Elixir} - 50 {Gold}\n   {item_1.Effect_I}\n\n")
        print(f"2. {Strength} {Elixir} - 60 {Gold}\n   {item_2.Effect_I}\n\n")
        print(f"3. {Shield} - 50 {Gold}\n   {item_3.Effect_I}\n\n")
        print(f"4. Shorre - 100 {Gold}\n   {weapon_4}\n\n")
        print(f"5. Ak 5 - 100 {Gold}\n   {weapon_5}\n\n")
        print(f"6. Golden Scar - 250 {Gold}\n   {weapon_6}\n\n")
        print(f"7. Musket - 600 {Gold}\n   {weapon_7}\n\n")
        print("0. Exit shop (no purchase)\n")
    # Här skapas en funktion för att köpa saker från shoppen
    def buy(self, choice, gold):
        if choice == 1:
            if len(item_inventory) >= 5:
                print(RED("Your item inventory is full! You cannot buy more items.\n"))
                return gold
            if gold >= 50:
                print(GREEN(f"\nYou bought Health Elixir for 50 {Gold}!!!"))
                item_inventory.append(item_1)
                print(f"You have {len(item_inventory)}/5 items in your inventory.\n")
                return gold - 50
            else:
                print(RED("You can't afford this product!!!"))
                return gold

        elif choice == 2:
            if len(item_inventory) >= 5:
                print(RED("Your item inventory is full! You cannot buy more items.\n"))
                return gold
            if gold >= 60:
                print(GREEN(f"\nYou bought Strength Elixir for 60 {Gold}!!!"))
                item_inventory.append(item_2)
                print(f"You have {len(item_inventory)}/5 items in your inventory.\n")
                return gold - 60
            else:
                print(RED("You can't afford this product!!!"))
                return gold

        elif choice == 3:
            if len(item_inventory) >= 5:
                print(RED("Your item inventory is full! You cannot buy more items.\n"))
                return gold
            if gold >= 50:
                print(GREEN(f"\nYou bought Shield Upgrade for 50 {Gold}!!!"))
                item_inventory.append(item_3)
                print(f"You have {len(item_inventory)}/5 items in your inventory.\n")
                return gold - 50
            else:
                print(RED("You can't afford this product!!!"))
                return gold
                
        elif choice == 4:
            if gold >= 100 and "shorre" not in [w.Name_W.lower() for w in weapon_inventory]:
                print(GREEN(f"\nYou bought a Shorre for 100 {Gold}!!!"))
                weapon_inventory.append(weapon_4)
                return gold - 100
            else:
                print(RED("You either own this product or can't afford it!"))
                return gold

        elif choice == 5:
            if gold >= 100 and "ak 5" not in [w.Name_W.lower() for w in weapon_inventory]:
                print(GREEN(f"\nYou bought an Ak 5 for 100 {Gold}!!!"))
                weapon_inventory.append(weapon_5)
                return gold - 100
            else:
                print(RED("You either own this product or can't afford it!"))
                return gold

        elif choice == 6:
            if gold >= 250 and "golden scar" not in [w.Name_W.lower() for w in weapon_inventory]:
                print(GREEN(f"\nYou bought a Golden Scar for 250 {Gold}!!!"))
                weapon_inventory.append(weapon_6)
                return gold - 250
            else:
                print(RED("You either own this product or can't afford it!"))
                return gold

        elif choice == 7:
            if gold >= 600  and "musket" not in [w.Name_W.lower() for w in weapon_inventory]:
                print(GREEN(f"\nYou bought a Musket for 600 {Gold}!!!"))
                weapon_inventory.append(weapon_7)
                return gold - 600
            else:
                print(RED("You either own this product or can't afford it!"))
                return gold
        
        
        elif choice == 0:
                print("You exited the shop without buying anything.")
                return gold
        
        
        
            
    
                
