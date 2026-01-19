
import random as r
from shop import *
from colors import *
from bellman import *
from item_class import *
from dictionary import *
from entity_class import *
from weapon_class import *
from player_class import *
from typing_speed import *
from physics_enemy import *


boss_hp = 5000
has_book = False

# Här skapas en funktion för bossen
def boss(player, enemy, weapon_inventory, item_inventory, alive):
    print_slow("An ominous presence fills the room as you step forward.\nYou feel the air grow colder, and a deep rumble echoes through the dungeon walls.\nThe boss has awakened, and it's time to face your greatest challenge yet!\n\n")
    print_slow("Johannes Thessén, your former teacher, stands before you, his eyes filled with a mix of disappointment and determination.\nHe has been corrupted by the dungeon's dark magic and now serves as its final guardian.\n\n")
    print_slow("Johannes Théssen lets out a menacing laugh, 'So, you've made it this far, student. But your journey ends here!'\n")
    print_slow("I've taught you everything I know, but now it's time to see if you've truly learned anything at all!'\n\n")
    print_slow("You grip your weapon tightly, preparing yourself for the battle ahead.\nThis is your chance to prove your worth and overcome the challenges that have brought you to this point.\n\n")
    print(entity_7)
    player.HP_P = player.MaxHP_P
    
    result = Johannes_battle(player, has_book, weapon_inventory, item_inventory)
    if result == "won":
        print(GREEN("\nYou have defeated Johannes Théssen!\n"))
        level_up(player, enemy)
        increase_stat(player, enemy)
        print_slow("You have completed the dungeon. Congratulations on your victory!\n")
        alive = False
    elif result == "dead":
        alive = False
    
    return alive
    
# Här skapas "quotes" för bossen
calm_quotes = [
    "Interesting approach.",
    "Your syntax is acceptable.",
    "Not bad, but not optimal.",
    "This solution works.",
    "Readable code, nice.",
    "Logic is clear.",
    "This will do for now.",
    "You are on the right track.",
    "Acceptable performance.",
    "No errors detected."
]

angry_quotes = [
    "This is getting annoying.",
    "Your code is inefficient!",
    "Stop wasting CPU cycles!",
    "Why would you do it like this?",
    "This loop makes no sense!",
    "Have you even tested this?",
    "This could be done better.",
    "Too many unnecessary variables!",
    "That function name is terrible.",
    "This hurts performance."
]

furious_quotes = [
    "ENOUGH!",
    "Your program should have crashed by now!",
    "I will refactor YOU.",
    "WHAT IS THIS CODE?!",
    "This violates every rule!",
    "I cannot debug this anymore!",
    "This is a nightmare!",
    "DELETE THIS IMMEDIATELY.",
    "I refuse to run this.",
    "My patience has reached zero."
]

# Här skapas funktionen för bossens strid
def Johannes_battle(player, has_book, weapon_inventory, item_inventory):
    global boss_hp
    
    print("Your weapons:")
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
            
# Här skapas vapen-valet
    if chosen_weapon is None:
        print(RED("You don't have that weapon. Using your first weapon instead.\n"))
        chosen_weapon = weapon_inventory[0]
    clear_terminal()
    # Här skapas special item
    choice = input(MAGENTA("You see a glowing item on the ground. Pick it up? (y/n)\n: ")).lower()
    if choice == "y":
        has_book = True
        print(f"You obtained the {Fore.YELLOW}Book of ChatGPT{Style.RESET_ALL}! It might help you in some way...\n")
    else:
        print("You ignored the item.\n\n")
        clear_terminal()
    print("The battle with Johannes Théssen begins!\n")
    if has_book:
        print(GREEN("You threw the Book of ChatGPT at Johannes. Its terrible coding advice weakens Johannes!\n"))

    while boss_hp > 1500 and player.HP_P > 0:

        # Här skapas spelarens val under striden/ själva stiden
        action = input("\nDo you wish to attack (a) or view your items (i)?\n: ").strip().lower()
        if action == "i":
            item_inventory_display(player, item_inventory)

        elif action == "a":
            clear_terminal()
            hits = r.randint(1, chosen_weapon.Hits_W)
            dmg = hits * (chosen_weapon.Dmg_W + player.STR_P)
            if not has_book:
                dmg = int(dmg * 0.4)

            boss_hp -= dmg
            
            print(f"You dealt {dmg} {Damage} with {hits} hits.")
            print(f"Boss {HP}: {boss_hp}")

            boss_attack = r.randint(10, 20)
            player.HP_P -= boss_attack
            print(f"Johannes attacks and deals {boss_attack} {Damage}.")
            print(f"Your {HP}: {player.HP_P}")
            
            if player.HP_P <= 0:
                return "dead"


        if boss_hp > 3000:
            quote = r.choice(calm_quotes)
        elif boss_hp > 1500:
            quote = r.choice(angry_quotes)
        else:
            quote = r.choice(furious_quotes)

        print(RED(f'Johannes Théssen says: "{quote}"'))
        print(f"Your {HP}: {player.HP_P}")
        if player.HP_P <= 0:
            return "dead"

    # fas 2
    clear_terminal()
    boss_hp = 1000
    print(RED("Johannes Théssen is enraged and enters Phase 2 of the battle!\n"))
    print_slow("Johannes is clearly losing his patience.\n")
    # Här skapas frågorna för bossen
    questions = [
        ("What keyword is used to print text in Python?", "print"),
        ("What data type stores whole numbers?", "int"),
        ("What data type stores decimal numbers?", "float"),
        ("What keyword is used for conditions?", "if"),
        ("What symbol is used for comments in Python?", "#"),
        ("What keyword is used to repeat code?", "for", "while"),
        ("What keyword is used to store a value?", "variable"),
        ("What data type stores text?", "str"),
        ("What keyword is used for otherwise in a condition?", "else"),
        ("What keyword is used to check multiple conditions?", "elif"),
        ("What keyword is used to repeat code while a condition is true?", "while"),
        ("What symbol is used to assign a value?", "="),
        ("What keyword is used to define a function?", "def"),
        ("What keyword is used to return a value from a function?", "return"),
        ("What data type stores true or false?", "bool","boolean"),
        ("What keyword is used to stop a loop?", "break"),
        ("What keyword is used to skip one loop iteration?", "continue"),
        ("What function is used to get input from the user?", "input")  
    ]
    r.shuffle(questions)
    rage = 10  
    # Här skapas frågemomentet i bossfighten
    for question, correct in questions:
        answer = input(question + " ").lower()

        if correct in answer:
            clear_terminal()
            print(f"Correct! You deal 100 {Damage}.")
            boss_hp -= 100
        else:
            clear_terminal()
            print("Wrong!")
            print(f"Johannes deals {rage} {Damage}.")
            player.HP_P -= rage
            rage += 30  

        print(f"Boss {HP}: {boss_hp} | Your {HP}: {player.HP_P}\n")

        if boss_hp <= 0 or player.HP_P <= 0:
            break

    # Här beslutas vad som händer när bossen eller spelaren dör
    if boss_hp <= 0:
        print("You defeated Johannes Théssen!")
        print("You have conquered the art of programming and emerged victorious!\n")
        return "won"
    elif player.HP_P <= 0:
        print("You were defeated. You should have studied...")
        return "dead"
    
