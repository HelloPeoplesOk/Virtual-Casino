import subprocess
import time
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def blackjack():
    path = os.path.join(BASE_DIR, "blackjack.py")
    if os.path.exists(path): subprocess.call([sys.executable, path])
    else: print("blackjack.py not found.")

def slots():
    path = os.path.join(BASE_DIR, "slots.py")
    if os.path.exists(path): subprocess.call([sys.executable, path])
    else: print("slots.py not found.")

def numbers():
    path = os.path.join(BASE_DIR, "numbers.py")
    if os.path.exists(path): subprocess.call([sys.executable, path])
    else: print("numbers.py not found.")

print("\nWelcome to the Virtual Casino\n")
time.sleep(1)

while True:
    play = input("Want to play (y/n): ")
    if play.lower() in ("y", "n"): break

if play.lower() == "y":
    time.sleep(0.5)
    print("\nSlots"); time.sleep(1)
    print("\nBlackjack"); time.sleep(1)
    print("\nNumbers"); time.sleep(1)
    while True:
        game = input("\nWhat game do you want to play or q for quit: ")
        if game.lower() == "slots": slots()
        elif game.lower() == "blackjack": blackjack()
        elif game.lower() == "numbers": numbers()
        elif game.lower() == "quit": print("Thanks for playing!"); break
        else: print("Invalid input. Please choose 'slots', 'blackjack', or 'quit'.")
        time.sleep(0.5)
        print("\nSlots"); time.sleep(1)
        print("\nBlackjack"); time.sleep(1)
        print("\nNumbers"); time.sleep(1)
elif play.lower() == "n": print("Bye")