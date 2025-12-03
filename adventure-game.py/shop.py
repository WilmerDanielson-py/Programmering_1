from weapon_class import *
from item_class import *

class shop:
    def __init__(self):
        self.stock = ["item_1","item_2","item_3","weapon_4","weapon_5","weapon_6","weapon_7"]

    def show(self):
        print("\n---> SHOP <---")
        print("1 Health Elixir - 50 Gold")
        print("2 Strength Elixir - 60 Gold")
        print("3 Shield Upgrade - 50 Gold")
        print("4 Shorre - 100 Gold")
        print("5 Ak 5 - 100 Gold")
        print("6 Golden Scar - 250 Gold")
        print("7 Musket - 600 Gold")

    def buy(self, choice, gold):

        if choice == 1:
            if gold >= 50:
                print("You bought Health Elixir for 50 gold!!!")
                item_inventory.append(item_1)
                return gold - 50
            else:
                print("You can't afford this product!!!")

        if choice == 2:
            if gold >= 60:
                print("You bought Strength Elixir for 60 gold!!!")
                item_inventory.append(item_2)
                return gold - 60
            else:
                print("You can't afford this product!!!")

        if choice == 3:
            if gold >= 50:
                print("You bought Shield Upgrade for 50 gold!!!")
                item_inventory.append(item_3)
                return gold - 50
            else:
                print("You can't afford this product!!!")

        if choice == 4:
            if gold >= 100:
                print("You bought a Shorre for 100 gold!!!")
                weapon_inventory.append(weapon_4)
                return gold - 100
            else:
                print("You can't afford this product!!!")

        if choice == 5:
            if gold >= 100:
                print("You bought an Ak 5 for 100 gold!!!")
                weapon_inventory.append(weapon_5)
                return gold - 100
            else:
                print("You can't afford this product!!!")

        if choice == 6:
            if gold >= 250:
                print("You bought a Golden Scar for 250 gold!!!")
                weapon_inventory.append(weapon_6)
                return gold - 250
            else:
                print("You can't afford this product!!!")

        if choice == 7:
            if gold >= 600:
                print("You bought a Musket for 600 gold!!!")
                weapon_inventory.append(weapon_7)
                return gold - 600
            else:
                print("You can't afford this product!!!")

        print("Error: You can only choose from the items above!!!")
        return gold