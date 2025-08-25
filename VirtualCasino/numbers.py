import random

wtloana = 0
money = 0
hloan = False
bet = 0

dificulty = None
action = None
number = None
tries = None

print("Money: ", money, sep="")
while True:
    if wtloana >= 500:
        print("Lose WAY too much debt")
        break
    elif (money >= 5000) and (hloan == False):
        print("Win you broke the house")
        break

    if hloan == True:
        while True:
            if wtloana <= 0:
                hloan = False
                wtloana = 0
                while True:
                    wtroll = input("Want to Guess? (y/n): ")
                    if (wtroll.lower() == "y") or (wtroll.lower() == "n"):
                        break
                break
            else:
                while True:
                    wtroll = input("Want to guess or pay some debt? (y/n/d): ")
                    if (wtroll.lower() == "y") or (wtroll.lower() == "n") or (wtroll.lower() == "d"):
                        break
                if wtroll == "d":
                    while True:
                        try:
                            payb = int(input("How much of your loan do you want to pay back: "))
                            if money - payb < 0:
                                print("Your too poor try again")
                            else:
                                break
                        except:
                            continue
                    wtloana -= payb
                    money -= payb
                    print("Money: ", money, sep="")
                    print("Debt: ", wtloana, sep="")
                else:
                    break 
    else:
        while True:
            wtroll = input("Want to Guess? (y/n): ")
            if (wtroll.lower() == "y") or (wtroll.lower() == "n"):
                break
    
    if wtroll.lower() == "n":
            if hloan == True:
                if (money - wtloana) >= 0:
                    money -= wtloana
                    print("Win? you only made", money)
                else:
                    print("Lose you owe", wtloana)
            elif money == 0:
                print("Win??? I mean you didn't lose money")
            else:
                print("Win? you only made", money)
            break
    
    while True:
        if money == 0:
            print("Your Poor\nYou need a loan")
            if (hloan == False):
                while True:
                    try:
                        wtloana = int(input("How much is your loan for: "))
                        break
                    except:
                        continue
                money += wtloana
                wtloana += round(wtloana * 0.2)
                hloan = True
            elif (hloan == True):
                while True:
                    try:
                        aloan = int(input("How much is your loan for: "))
                        break
                    except:
                        continue
                money += aloan
                wtloana += round(aloan * 1.2)
            else:
                break
        else: 
            break

    if wtloana >= 500:
        print("Lose WAY too much debt")
        break
    elif (money >= 5000) and (hloan == False):
        print("Win you broke the house")

    if hloan == True:
        print("\nMoney: ", money, sep="")
        print("Debt: ", wtloana, "\n", sep="")
    else:
        print("\nMoney: ", money, "\n", sep="")

    while True:  
        try:
            bet = int(input("How much do you want to bet: "))
            if money - bet >= 0:
                money -= bet
                break
            else:
                print("Your too poor try again")
        except:
            continue

    if wtroll.lower() == "y":
        while True:
            dificulty = input("What is the dificulty\nE | 1 - 100 | x 2\nM | 1 - 300 | x 5\nH | 1 - 1000 | x 10\n").lower()
            if dificulty in ("e", "m", "h"): break

        if dificulty == "e":
            number = random.randint(1, 100)
            tries = 6
        elif dificulty == "m":
            number = random.randint(1, 300)
            tries = 7
        elif dificulty == "h":
            number = random.randint(1, 1000)
            tries = 8
        
        for i in range(tries):
            while True:
                try:
                    action = int(input("\nWhat is your guess: "))
                    if (action < 1) or (((action > 100) and (dificulty == "e")) or ((action > 300) and (dificulty == "m"))  or ((action > 1000) and (dificulty == "h"))):
                        print("Your guess is out of range. Try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter an Intager.")
            if action == number:
                if dificulty == "e": 
                    if hloan == True:
                        money += round((bet * 2) * 0.9)
                        wtloana -= round((bet * 2) * 0.1)
                        print("You guessed the number in Easy | Reward: ", round((bet * 2) * 0.9), sep="")
                        break
                    else:
                        money += bet * 2
                        print("You guessed the number in Easy | Reward: ", bet * 2, sep="")
                        break
                elif dificulty == "m": 
                    if hloan == True:
                        money += round((bet * 5) * 0.9)
                        wtloana -= round((bet * 5) * 0.1)
                        print("You guessed the number in Medium | Reward: ", round((bet * 4) * 0.9), sep="")
                        break
                    else:
                        money += bet * 4
                        print("You guessed the number in Medium | Reward: ", bet * 4, sep="")
                        break
                elif dificulty == "h": 
                    if hloan == True:
                        money += round((bet * 10) * 0.9)
                        wtloana -= round((bet * 10) * 0.1)
                        print("You guessed the number in Hard | Reward: ", round((bet * 10) * 0.9), sep="")
                        break
                    else:
                        money += bet * 10
                        print("You guessed the number in Hard | Reward: ", bet * 10, sep="")
                        break
            elif action < number:
                print("More |", tries - i - 1, "tries left")
            elif action > number:
                print("Less |", tries - i - 1, "tries left")
        if action != number:
            print("You lose the number was", number)

        if hloan == True:
            print("\nMoney: ", money, sep="")
            wtloana += round(wtloana * 0.02)
            print("Debt: ", wtloana, "\n", sep="")
        else:
            print("\nMoney: ", money, "\n", sep="")