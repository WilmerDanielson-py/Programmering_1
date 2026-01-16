import time
import random as r
from colors import *
from typing_speed import *
from attack import *

# Här skapas en funktion för minibossen Bellman
def miniboss_Bellman(player, enemy, alive, room_encounter, miniboss_chance):
    
    clear_terminal()
    print_slow("As you step into the room, a sudden chill runs down your spine.\nThe atmosphere shifts, and you sense a powerful presence watching you.\nA shadowy figure emerges from the darkness. A Mini-Boss appears!\n\n")
    print_slow("The Bellman clears his throat. This will take a while.\n\n")
    print_slow("I hope you're ready for some jokes, because I've got a whole arsenal of them!\n\n")
    print_slow("Wait a minute, you look like... never mind. Someone you know is waiting for you at the end of this dungeon... TOO BAD YOU HAVE TO GET PAST ME FIRST!!!!\n")
    if miniboss_chance == "Bellman":
        print(entity_6)
        player.HP_P = player.MaxHP_P
        result = bellman_encounter()
        if result == "won":
            print(GREEN("\nYou have defeated Bellman!\n"))
            level_up(player, enemy)
            increase_stat(player, enemy)
            room_encounter += 1
        elif result == "dead":
            alive = False
    return alive

player_patience = 10

def pause():
    time.sleep(1)

# Här skapas olika attacker för Bellman
def bar_joke():
    print("\nBellman says:")
    print("Two guys walk into a bar...")
    pause()
    pause()
    print("The third one ducks.")
    pause()

def pun_barrage():
    print("\nBellman unleashes a pun barrage!")
    jokes = [
        "I used to be a banker, but I lost interest.",
        "I'm reading a book about anti-gravity. It's impossible to put down.",
        "I tried to catch fog yesterday. Mist.",
        "Why don't skeletons fight each other? They don't have the guts."
    ]
    print(r.choice(jokes))
    pause()

def repeat_attack():
    print("\nBellman grins.")
    print("Have you heard this one?")
    pause()
    print("Two guys walk into a bar...")
    pause()
    print("The third one ducks.")
    pause()


def explain_joke():
    print("\nBellman explains the joke:")
    print("You see, it's funny because the bar is a physical object.")
    pause()
    print("So when they walk into it...")
    pause()
    print("The third one ducks.")
    pause()

def bellman_turn():
    
    global player_patience
    attack = r.choice([bar_joke, pun_barrage, repeat_attack, explain_joke])
    attack()
    player_patience -= r.choice([1, 2, 3])
    print(RED("Your patience decreases."))
# Här skapas funktionen för Bellman-mötet
def bellman_encounter():
    global player_patience
    player_patience = 10
    bellman_patience = 8

    print("\n\nBellman appears.\n")
    print("He clears his throat. This will take a while.")

    while player_patience > 0 and bellman_patience > 0:
        print(f"\nYour Patience: {player_patience} | Bellman's Patience: {bellman_patience}")
        action = input("What do you do? \n   Ignore (i) \n   Respond (r) \n   Explain (e)\n: ").lower()

        if action == "i":
            print(CYAN("You stare into the void. Bellman feels like he´s talking to a brick wall..."))
            print("Bellmans patience decreses.")
            bellman_patience -= r.choice([1, 2, 3])
        elif action == "r":
            print(MAGENTA("You tell a joke and Bellman gets offended..."))
            print("Bellmans patience decreses.")
            bellman_patience -= r.choice([1, 2, 3])
        elif action == "e":
            print(YELLOW("You explain why Bellmans joke is bad. Bellman dosen´t like that..."))
            print("Bellmans patience decreses.")
            bellman_patience -= r.choice([1, 2, 3])
        else:
            print(RED("Invalid action! Bellman takes advantage of your flawed algorithm."))
            player_patience -= 1
        

        if bellman_patience > 0:
            bellman_turn()

    if player_patience <= 0:
        clear_terminal()
        print(RED("\nYou can’t take it anymore. Make it stop!"))
        print("Bellman keeps talking.")
        return "dead"
    else:
        clear_terminal()
        print(GREEN("\nBellman falls silent."))
        print("\"That usually works...\"")
        return "won"