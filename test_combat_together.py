# Här importeras random för att kunna använda slumpgeneratorer
import random as r
# Här importeras colorama för att kunna använda färger i terminalen
from colorama import init, Fore, Style
init(autoreset=True)
# Här skapas funktioner för olika färger
def RED(text, color=Fore.RED):
    return f"{color}{text}{Style.RESET_ALL}"   
def GREEN(text, color=Fore.GREEN):
    return f"{color}{text}{Style.RESET_ALL}" 
def BLUE(text, color=Fore.BLUE):
    return f"{color}{text}{Style.RESET_ALL}" 
def YELLOW(text, color=Fore.YELLOW):
    return f"{color}{text}{Style.RESET_ALL}" 
def MAGENTA(text, color=Fore.MAGENTA):
    return f"{color}{text}{Style.RESET_ALL}" 
def CYAN(text, color=Fore.CYAN):
    return f"{color}{text}{Style.RESET_ALL}"  
def BLACK(text, color=Fore.BLACK):
    return f"{color}{text}{Style.RESET_ALL}"

# Här skapas färgade typer för vapen   
Blade = CYAN("Blade")
Gun = YELLOW("Gun")

Health = RED("Health")
HP = RED("HP")
Strength = RED("Strength")
Elixir = MAGENTA("Elixir")
Sheild = BLUE("Sheild")
Level = GREEN("Level")

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

# Här skapas en klass för vapen
class weapon():
    def __init__(self, Rarity_W, Name_W, Type_W, Dmg_W, AtkSpeed_W, Range_W):
        self.Dmg_W = Dmg_W
        self.Range_W = Range_W
        self.AtkSpeed_W = AtkSpeed_W
        self.Type_W = Type_W
        self.Name_W = Name_W
        self.Rarity_W = Rarity_W

# Här skapas en strängrepresentation av vapnet
    def __str__(self):
        return f"\n{self.Name_W}\nThis {self.Rarity_W} {self.Name_W} is a {self.Type_W} type weapon.\n   Stats are:\n   Damage: {self.Dmg_W}\n   AtkSpeed: {self.AtkSpeed_W}\n   Range: {self.Range_W} "

# Här skapas vapenobjekt
# weapon = weapon("rarity", "name","type","dmg","Atkspeed","range")
weapon_1 = weapon(BLACK("Common"), "Dagger", Blade, 15, 20, 1)
weapon_2 = weapon(GREEN("Uncommon"), "Rapier", Blade, 45, 10, 20)
weapon_3 = weapon(BLUE("Rare"), "Zweihander", Blade, 60, 8, 25)
weapon_4 = weapon(BLUE("Rare"), "Shorre", Gun, 250, 7, 30)
weapon_5 = weapon(MAGENTA("Epic"), "Ak 5", Gun, 7, 25, 100)
weapon_6 = weapon(YELLOW("Legendary"), "Golden Scar", Gun, 10, 30, 150)
weapon_7 = weapon(RED("Mythic"), "Musket", Gun, 2000, 1, 200)

# Här skapas en lista för spelarens vapen-inventory
weapon_inventory = [weapon_1]

# Här skapars en klass för items
class item():
    def __init__(self, Name_I, Effect_I):
        self.Name_I = Name_I
        self.Effect_I = Effect_I

    def __str__(self):
        return f"{self.Name_I}: {self.Effect_I}"
    
# Här skapas itemobjekt
item_1 = item(f"{Health} {Elixir}", f"Restores 30 {HP}")
item_2 = item(f"{Strength} {Elixir}", f"Increases {Strength} by 50")
item_3 = item(f"{Sheild}", f"Increases max {HP} by 30")

# Här skapas en lista för spelarens item-inventory
item_inventory = []



# Här skapars en klass för fiender
class entity():
    def __init__(self, Name_E, Element_E, HP_E, Weak_E, STR_E, AtkSpeed_E):
        self.Name_E = Name_E
        self.STR_E = STR_E
        self.HP_E = HP_E
        self.Element_E = Element_E
        self.Weak_E = Weak_E
        self.AtkSpeed_E = AtkSpeed_E

# Här skapas en strängrepresentation av fienden
    def __str__(self):
        return f"You have encountered a {self.Element_E} type {self.Name_E} meaning its weak to {self.Weak_E} type attacks.\nIts stats are:\n   {Strength}: {self.STR_E}\n   {HP}: {self.HP_E}\n   {Fore.BLUE}AtkSpeed{Style.RESET_ALL}: {self.AtkSpeed_E}\n"
    
# Här skapas fiendeobjekt
# entity = entity("name","type","HP","weak","STR")
entity_1 = entity("Goblin","Normal",150,Blade + " and " + Gun,5, 10)
entity_2 = entity("Zombie","Undead",170,Blade,10, 12)
entity_3 = entity("Ravager","Tank",1000,Gun,3, 8)
entity_4 = entity("Warlock","Berserker",70,Gun,49, 15)
entity_5 = entity("Greger","Dark",1337,Blade,24, 15)
entity_6 = entity("Bellman","Jester","inf","Joke",10, 1)
entity_7 = entity("Johannes Thessén","Coder",5000,"Sunlight",99, 20)
entity_8 = entity(r" ρ * ( ∂u/∂t  +  (u · ∇)u )  =  -∇p  +  μ ∇²u  +  f","Physics",2500,"Nikodesmos",35, 18)

# Här skapas en lista med alla fiender
entity_n = [entity_1, entity_2, entity_3, entity_4, entity_5]
# entity_6, entity_7, entity_8

# Här skapas en klass för spelaren
class Player():
    def __init__(self, Name_P, HP_P, MaxHP_P, Level_P, STR_P):
        self.Name_P = Name_P
        self.HP_P = HP_P
        self.MaxHP_P = MaxHP_P
        self.Level_P = Level_P
        self.STR_P = STR_P

# Här skapas en strängrepresentation av spelaren
    def __str__(self):
        return f"\nPlayer {Fore.GREEN}Name{Style.RESET_ALL}: {self.Name_P}\nPlayer {HP}: {self.HP_P}/{self.MaxHP_P}\nPlayer {Strength}: {self.STR_P}\nPlayer {Level}: {self.Level_P}\n"

# Här skapas huvudfunktionen för spelet
def main():

# Här skapas spelaren
    player_name = input("\nWhat is your name brave one?\n:")
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
        player_action = input(CYAN("\nWhat do you wish to do? \n   Enter to a new room? (m) \n   View your stats? (s)\n   View the dictionary? (d)\n   View your  weapon inventory? (w)\n   View your item inventory? (i)\n   Exit the game? (q)\n:")).lower()

    # Här hanteras spelarens val
        if player_action == "m":
            door = input("\nYou see three doors in front of you, do you wish to enter \n   The left door (left), \n   The middle door (middle), \n   The right door (right)?\n:").lower()

            print(f"\nYou chose the {door} door...\n")
            if door == "left" or door == "middle" or door == "right":
                encounter = r.randint(1,2)
                if encounter == 1:
                    

                # Här skapas en slumpgenerator som väljer en fiende att möta
                    
                    # ,"Zombie","Ravager","Warlock","Greger"
                # Här skapas en strängrepresentation av fienden som valts och vad som händer vid en encounter
                    def Entity_in_room_function(monster):
                        """Handle encounter for the passed monster."""
                        nonlocal room_encounter
                        print(monster)
                        action = input("Do you wish to attack (a), or do you wish to escape (e)?\n: ").lower()
                        if action == "a":
                            if weapon_inventory:
                                print("Your weapons:")
                                for _weapon in weapon_inventory:
                                    print(f"{_weapon}\n")
                            weapon_choice = input("What weapon do you wish to use?\n:").strip().lower()

                            # find chosen weapon
                            chosen_weapon = None
                            for _weapon in weapon_inventory:
                                if _weapon.Name_W.lower() == weapon_choice:
                                    chosen_weapon = _weapon
                                    break
                            if chosen_weapon is None:
                                print(RED("You don't have that weapon. Using your first weapon instead.\n"))
                                chosen_weapon = weapon_inventory[0]

                            # compare attack speed and resolve
                            if chosen_weapon.AtkSpeed_W > monster.AtkSpeed_E:
                                print(f"You have chosen to attack with the {chosen_weapon.Name_W}.\n")
                                dmg_chosen_weapon = chosen_weapon.Dmg_W
                                total_dmg = Player_1.STR_P + dmg_chosen_weapon
                                monster.HP_E = monster.HP_E - total_dmg
                                print(f"You dealt {total_dmg} {Fore.RED}damage{Style.RESET_ALL} to the {monster.Name_E}!\nIts current {HP} is now {monster.HP_E}.\n")
                            else:
                                print("\nToo slow!\n")
                                print(f"The {monster.Name_E} is faster!\n")
                                Player_1.HP_P = Player_1.HP_P - monster.STR_E
                                print(f"You received {monster.STR_E} {Fore.RED}damage{Style.RESET_ALL} from the {monster.Name_E}!\nYour current {HP} is now {Player_1.HP_P}/{Player_1.MaxHP_P}.\n")
                        elif action == "e":
                            escape = r.randint(1,3)
                            if escape == 1:
                                print(GREEN("\nYou escaped successfully!\n"))
                            else:
                                print(RED("\nYou failed to escape! You must now prepare for battle!\n"))
                            room_encounter += 1
                            print(f"You have now entered {room_encounter} rooms.\n")
                    Entity_in_room_function(monster=r.choice(entity_n))
                        

                    
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
                                full_inv = input("You must use (u) or drop (d) an item before picking up a new one.\n:").lower()
                                if full_inv == "u":
                                    for item in item_inventory:
                                        print(item)
                                        use_item = input("Which item do you wish to use?\n:")
                                        # skriv koden för att använda ett item in
                                
                                elif full_inv == "d":
                                    for item in item_inventory:
                                        print(item)
                                        drop_item = input("Which item do you wish to drop?\n:")
                                         # skriv koden för att droppa ett item in

                            # Här hanteras items när item_inventory inte är fullt
                            else:
                                print("There seems to be an item chest here!\n")
                                new_item = r.choice([item_1, item_2, item_3])
                                print(f"Wow, you found a {new_item.Name_I}!\n")
                                print(f"{new_item}\n")


                                if new_item.Name_I == (f"{Health} {Elixir}"):
                                    use_elixir = input(f"Do you wish to use the {Health} {Elixir} now? (y/n)\n:").lower()
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
                                    use_elixir = input(f"Do you wish to use the {Strength} {Elixir} now? (y/n)\n:").lower()
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


                                elif new_item.Name_I == (f"{Sheild}"):
                                    equip_sheild = input(f"Do you wish to Equip the {Sheild} now? (y/n)\n:").lower()
                                    if equip_sheild == "y":
                                        Player_1.MaxHP_P += 30
                                        print(f"\nYou used the {Sheild} and increased your max {HP} by 30! Your current max {HP} is now {Player_1.MaxHP_P}.\n")
                                    elif equip_sheild == "n":
                                        print(f"You chose not to equip the {Sheild} now. Its stored in your item inventory for safe keeping\n")
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
                        else:
                            print(BLUE("\nYou have found an empty room. Better luck next time!\n"))
                    room_encounter += 1
                    print(f"You have now entered {room_encounter} rooms.\n")
                        

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
        elif player_action == "W":
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
            
main()

# #def draw_room(player_icon="P" , enemy_icon="E", Entity_in_room):
# #    pass
