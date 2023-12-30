import time
from colorama import Fore

mins = int(input("Enter time of mins: "))
Seconds = int(input("Enter time of Seconds: "))

Seconds = mins * 60 + Seconds
for x in range(Seconds):
    SecondsRemaining = Seconds - x
    Secondhand = SecondsRemaining % 60
    Minhand = int( SecondsRemaining / 60) % 60
    Hourhand = int(SecondsRemaining / 3600)
    print(f"Timer:{Fore.GREEN}{Hourhand:02}:{Minhand:02}:{Secondhand:02}{Fore.RESET}",end="\r")
    time.sleep(1)
