import os
import sys
import time



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

 
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(seconds):
    time.sleep(seconds)

