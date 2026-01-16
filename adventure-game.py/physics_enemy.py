import random
from colors import *
from typing_speed import *
from player_class import *
from attack import *

# 
def miniboss_Physics(player, enemy, alive, room_encounter, miniboss_chance):
    if miniboss_chance == "Physics_Entity":
        print_slow(f"As you step into the room, a sudden chill runs down your spine.\nThe atmosphere shifts, and you sense a powerful presence watching you.\nA shadowy figure emerges from the darkness. A Mini-Boss appears!\n\n")
        print_slow("The Physics Entity lets out a deep, resonating voice, 'You dare challenge the very laws that govern our universe?'\n")
        print_slow("'Prepare to face the consequences of your ignorance!'\n\n")
        print_slow("By the way... did you know that the Navier-Stokes equations describe the motion of fluid substances?\nJust something to ponder while we battle!\n\n")
        print("Another \"By the way\"... someone you know is waiting for you at the end of this dungeon... TOO BAD YOU HAVE TO GET PAST ME FIRST!!!!\n")
        print(entity_8)
        player.HP_P = player.MaxHP_P
        result = physics_enemy_battle(player.HP_P)
        if result == "won":
            print(GREEN("\nYou have defeated the Physics Entity!\n"))
            level_up(player, enemy)
            increase_stat(player, enemy)
            room_encounter += 1
        elif result == "dead":
            alive = False
    return alive

def physics_enemy_battle(player_hp):
    boss_hp = 2500
    boss_name = "ρ( ∂u/∂t + (u · ∇)u )=-∇p + μ ∇²u + f"

    questions = [
        ("48 / 6", 8),
        ("17 + 29", 46),
        ("72 - 35", 37),
        ("14 * 9", 126),
        ("120 / 8", 15),
        ("63 + 47", 110),
        ("200 - 84", 116),
        ("16 * 12", 192),
        ("144 / 12", 12),
        ("89 + 56", 145),
        ("300 - 127", 173),
        ("25 * 24", 600),
        ("256 / 16", 16),
        ("74 + 68", 142),
        ("500 - 219", 281),
        ("18 * 17", 306),
        ("324 / 18", 18),
        ("91 + 39", 130),
        ("640 - 275", 365),
        ("27 * 14", 378)

    ]

    random.shuffle(questions)
    
    print("A wild ρ( ∂u/∂t + (u · ∇)u )=-∇p + μ ∇²u + f appears!")
    print("Answer the math questions to defeat it!\n")

    for question, answer in questions:
        if player_hp <= 0 or boss_hp <= 0:
            break

        print(f"Your {HP}: {player_hp} | {boss_name} {HP}: {boss_hp}")
        user_answer = input(f"Solve: {question} = ")

        try:
            if int(user_answer) == answer:
                boss_hp -= 250
                print(f"{Fore.GREEN}Correct! The ρ( ∂u/∂t + (u · ∇)u )=-∇p + μ ∇²u + f loses 250 {HP}!\n")
            else:
                player_hp -= 25
                print(f"{Fore.RED}Wrong! You lose 25 {HP}!\n")
        except ValueError:
            player_hp -= 10
            print(f"{Fore.RED}Invalid input! You lose 10 {HP}!\n")

    if boss_hp <= 0:
        print(GREEN("You defeated the ρ( ∂u/∂t + (u · ∇)u )=-∇p + μ ∇²u + f! Math and physics has now gone extinct, HOORRRAAAY!!!!"))
        return "won"
    elif player_hp <= 0:
        print(RED("You were defeated... The ρ( ∂u/∂t + (u · ∇)u )=-∇p + μ ∇²u + f reigns supreme!"))
        return "dead"
    else:
        print(BLACK("The battle ended without a clear winner."))
