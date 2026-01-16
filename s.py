import time
import sys
from colorama import Fore, Style, init

init()

text = (
    "You start with a "
    + Fore.BLACK + "Common" + Style.RESET_ALL +
    " Dagger as your weapon."
)

for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.04)
