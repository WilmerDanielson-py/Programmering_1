import random as r
from colorama import init, Fore, Style
init(autoreset=True)

# -------------------------------
# Färgfunktioner
# -------------------------------
def RED(text): return f"{Fore.RED}{text}{Style.RESET_ALL}"
def GREEN(text): return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
def BLUE(text): return f"{Fore.BLUE}{text}{Style.RESET_ALL}"
def YELLOW(text): return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"
def MAGENTA(text): return f"{Fore.MAGENTA}{text}{Style.RESET_ALL}"
def CYAN(text): return f"{Fore.CYAN}{text}{Style.RESET_ALL}"
def BLACK(text): return f"{Fore.BLACK}{text}{Style.RESET_ALL}"

# -------------------------------
# Typdefinitioner
# -------------------------------
Blade, Gun = CYAN("Blade"), YELLOW("Gun")
Health, HP, Strength = RED("Health"), RED("HP"), RED("Strength")
Elixir, Sheild, Level = MAGENTA("Elixir"), BLUE("Sheild"), GREEN("Level")

# -------------------------------
# KLASSER
# -------------------------------
class Entity:
    def __init__(self, name, element, hp, weakness, str_, atk_speed, max_hp, xp_reward, gold_reward):
        self.name = name
        self.element = element
        self.HP = hp
        self.STR = str_
        self.Weak = weakness
        self.AtkSpeed = atk_speed
        self.MaxHP = max_hp
        self.XP = xp_reward
        self.Gold = gold_reward

    def __str__(self):
        return f"{self.name} ({self.element}, weak to {self.Weak})\nHP: {self.HP}/{self.MaxHP}, STR: {self.STR}, AtkSpeed: {self.AtkSpeed}"

class Weapon:
    def __init__(self, rarity, name, type_, dmg, atk_speed, range_, hits):
        self.Rarity = rarity
        self.Name = name
        self.Type = type_
        self.Dmg = dmg
        self.AtkSpeed = atk_speed
        self.Range = range_
        self.Hits = hits

    def __str__(self):
        return f"{self.Name} ({self.Rarity}, {self.Type}) DMG:{self.Dmg} AtkSpeed:{self.AtkSpeed} Hits:{self.Hits} Range:{self.Range}"

class Item:
    def __init__(self, name, effect):
        self.Name = name
        self.Effect = effect
    def __str__(self):
        return f"{self.Name}: {self.Effect}"

class Player:
    def __init__(self, name, hp, max_hp, level, str_, gold=50, xp=0):
        self.Name = name
        self.HP = hp
        self.MaxHP = max_hp
        self.Level = level
        self.STR = str_
        self.XP = xp
        self.Gold = gold

    def __str__(self):
        return f"{self.Name} - HP: {self.HP}/{self.MaxHP}, STR: {self.STR}, Level: {self.Level}, XP: {self.XP}, Gold: {self.Gold}"

    def add_xp(self, xp_gain):
        self.XP += xp_gain
        print(f"\nYou gained {xp_gain} XP!")
        while self.Level < 20 and self.XP >= xp_table[self.Level]:
            self.Level += 1
            self.MaxHP += 20
            self.HP += 10
            self.STR += 15
            print(f"{GREEN('Level Up!')} You are now level {self.Level}!")
            print(f"Max HP +20, HP +10, STR +15")

    def add_gold(self, amount):
        self.Gold += amount
        print(f"You gained {amount} gold. Current gold: {self.Gold}")

    def spend_gold(self, amount):
        if self.Gold >= amount:
            self.Gold -= amount
            return True
        else:
            print(RED("Not enough gold!"))
            return False

# -------------------------------
# XP TABLE
# -------------------------------
xp_table = [0]
for lvl in range(1, 21):
    xp_table.append(xp_table[-1] + 50 + lvl*10)

# -------------------------------
# FIENDER
# -------------------------------
entity_1 = Entity("Goblin", "Normal", 150, "Blade/Gun", 5, 10, 150, xp_reward=20, gold_reward=10)
entity_2 = Entity("Zombie", "Undead", 170, "Blade", 10, 12, 170, xp_reward=30, gold_reward=15)
entity_3 = Entity("Ravager", "Tank", 1000, "Gun", 3, 8, 1000, xp_reward=100, gold_reward=50)
entity_4 = Entity("Warlock", "Berserker", 70, "Gun", 49, 15, 70, xp_reward=40, gold_reward=30)
entity_5 = Entity("Greger", "Dark", 1337, "Blade", 24, 15, 1337, xp_reward=120, gold_reward=80)
entity_6 = Entity("Bellman", "Jester", 500, "Joke", 10, 1, 500, xp_reward=70, gold_reward=50)
entity_7 = Entity("Johannes Thessén", "Coder", 5000, "Sunlight", 99, 20, 5000, xp_reward=300, gold_reward=150)
entity_8 = Entity("Physics Entity", "Physics", 2500, "Nikodesmos", 35, 18, 2500, xp_reward=200, gold_reward=100)

# -------------------------------
# VAPEN
# -------------------------------
weapon_1 = Weapon(BLACK("Common"), "Dagger", Blade, 15, 20, 1, 1)
weapon_2 = Weapon(GREEN("Uncommon"), "Rapier", Blade, 45, 10, 20, 1)
weapon_3 = Weapon(BLUE("Rare"), "Zweihander", Blade, 60, 8, 25, r.randint(0,3))
weapon_4 = Weapon(BLUE("Rare"), "Shorre", Gun, 50, 7, 30, r.randint(0,5))
weapon_5 = Weapon(MAGENTA("Epic"), "Ak 5", Gun, 7, 25, 100, r.randint(0,25))
weapon_6 = Weapon(YELLOW("Legendary"), "Golden Scar", Gun, 10, 30, 150, r.randint(0,20))
weapon_7 = Weapon(RED("Mythic"), "Musket", Gun, 2000, 1, 200, 1)
weapon_inventory = [weapon_1]

# -------------------------------
# ITEMS
# -------------------------------
item_1 = Item(f"{Health} {Elixir}", f"Restores 30 HP")
item_2 = Item(f"{Strength} {Elixir}", f"Increases STR by 50")
item_3 = Item(f"{Sheild}", f"Increases max HP by 30")
item_inventory = []

# -------------------------------
# SHOP
# -------------------------------
def shop(player: Player):
    print(f"\n{CYAN('Welcome to the Shop!')} Gold: {player.Gold}")
    shop_items = [
        {"name": "Health Elixir", "cost": 20, "type": "item", "effect": item_1},
        {"name": "Strength Elixir", "cost": 50, "type": "item", "effect": item_2},
        {"name": "Shield", "cost": 50, "type": "item", "effect": item_3},
        {"name": "Sunstone", "cost": 500, "type": "special"},
        {"name": "Revive", "cost": 1000, "type": "special"},
        {"name": weapon_2.Name, "cost": 100, "type": "weapon", "object": weapon_2},
        {"name": weapon_3.Name, "cost": 200, "type": "weapon", "object": weapon_3},
        {"name": weapon_4.Name, "cost": 250, "type": "weapon", "object": weapon_4},
    ]

    for i, item in enumerate(shop_items):
        print(f"{i+1}. {item['name']} - {item['cost']} gold")
    
    choice = input("Enter number to buy (or 'q' to exit): ").lower()
    if choice == 'q':
        return
    if choice.isdigit() and 1 <= int(choice) <= len(shop_items):
        selected = shop_items[int(choice)-1]
        if player.spend_gold(selected["cost"]):
            if selected["type"] == "item" or selected["type"] == "special":
                item_inventory.append(selected["name"])
                print(f"You bought {selected['name']}!")
            elif selected["type"] == "weapon":
                weapon_inventory.append(selected["object"])
                print(f"You bought {selected['name']}!")

# -------------------------------
# SPELLOOP (Förenklad)
# -------------------------------
def main():
    player_name = input("Enter your name: ")
    Player_1 = Player(player_name, 100, 100, 1, 10)

    alive = True
    room_counter = 0
    all_entities = [entity_1, entity_2, entity_3, entity_4, entity_5]

    print(f"\nWelcome {Player_1.Name} to the dungeon!")

    while alive and room_counter < 30:
        action = input("\nEnter (m)ove, (s)tats, (w)eapons, (i)tems, (d)ictionary, (shop), (q)uit: ").lower()
        if action == "m":
            encounter = r.randint(0,1)
            if encounter:
                entity = r.choice(all_entities)
                entity.HP = entity.MaxHP
                print(f"\nYou encountered {entity.name}!\n{entity}")
                # Förenklad fight: ge XP och guld direkt
                Player_1.add_xp(entity.XP)
                Player_1.add_gold(entity.Gold)
                print(f"You defeated {entity.name}!\n")
            else:
                print("Empty room or loot room")
            room_counter += 1
        elif action == "s":
            print(Player_1)
        elif action == "w":
            for w in weapon_inventory:
                print(w)
        elif action == "i":
            for item in item_inventory:
                print(item)
        elif action == "d":
            print("Dictionary feature goes here")
        elif action == "shop":
            shop(Player_1)
        elif action == "q":
            print("Thanks for playing!")
            break

main()
