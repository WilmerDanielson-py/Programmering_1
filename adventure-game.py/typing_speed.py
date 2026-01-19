import os
import sys
import time


# Här skapas funktioner för att skriva ut text långsamt eller snabbt
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)

def print_fast(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.001)

# Här skapas en funktion för att rensa terminalen
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')



