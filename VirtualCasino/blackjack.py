import random

dc1 = None
dc2 = None
pc1 = None
pc2 = None

dct = 0
pct = 0

dace = False
pace = 0
pncard = None

wtloana = 0
money = 0
hloan = False
bet = 0
action = None

print("Money: ", money, sep="")
while True:
    if wtloana >= 500:
        print("Lose WAY too much debt")
        break
    elif (money >= 500) and (hloan == False):
        print("Win you broke the house")

    if hloan == True:
        while True:
            if wtloana <= 0:
                hloan = False
                wtloana = 0
                while True:
                    wtroll = input("Want to deal? (y/n): ")
                    if (wtroll.lower() == "y") or (wtroll.lower() == "n"):
                        break
                break
            else:
                while True:
                    wtroll = input("Want to deal or pay some debt? (y/n/d): ")
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
            wtroll = input("Want to deal? (y/n): ")
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
    elif (money >= 500) and (hloan == False):
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
        pct = 0
        dct = 0
        print("\nMoney: ", money, "\n", sep="")
        dc1 = random.randint(1, 13)
        dc2 = random.randint(1, 13)
        pc1 = random.randint(1, 13)
        pc2 = random.randint(1, 13)
        if dc1 > 10: dc1 = 10
        if dc2 > 10: dc2 = 10
        if pc1 > 10: pc1 = 10
        if pc2 > 10: pc2 = 10
        dct += dc1 + dc2
        pct += pc1 + pc2
        if dc1 > 9: dc1 = "0"
        if dc2 > 9: dc2 = "0"
        if pc1 > 9: pc1 = "0"
        if pc2 > 9: pc2 = "0"
        if dc1 == 1: dace = True
        if dc1 == 1: dace = True
        if pc1 == 1: pace += 1
        if pc2 == 1: pace += 1
        if dc1 == 1: dc1 = "A"
        if dc2 == 1: dc2 = "A"
        if pc1 == 1: pc1 = "A"
        if pc2 == 1: pc2 = "A"
        print(" _____     _____       _____     _____\n|     |   |     |     |     |   |     |\n|     |   |     |     |     |   |     |\n|     |   |  ", dc2, "  |     |  ", pc1, "  |   |  ", pc2, "  |\n|     |   |     |     |     |   |     |\n|_____|   |_____|     |_____|   |_____|\n", sep="")
        
        while True:
            if pct > 21:
                print("You bust")
                break
            
            while True:
                action = input("Hit or stand (h/s): ")
                if (action.lower() == "h") or (action.lower() == "s"):
                    break

            if action.lower() == "h":
                pncard = random.randint(1, 13)
                if pncard > 10: pncard = 10
                pct += pncard
                if pncard > 9: pncard = "0"
                if pncard == 1: pace += 1
                if pncard == 1: pncard = "A"

                print(" _____\n|     |\n|     |\n|  ", pncard, "  |\n|     |\n|_____|\n", sep="")

            if action.lower() == "s":
                while True:
                    while (pace > 0) and ((pct + 10) <= 21):
                        action = input("What value is your Ace (1/11): ")
                        if action == "1":
                            break
                        if action == "11":
                            pct += 10
                            break
                    else:
                        break

                print(" _____     _____\n|     |   |     |\n|     |   |     |\n|  ", dc1, "  |   |  ", dc2, "  |\n|     |   |     |\n|_____|   |_____|\n", sep="")
                while dct < 17:
                    pncard = random.randint(1, 13)
                    if pncard > 10: pncard = 10
                    dct += pncard
                    if pncard > 9: pncard = "0"
                    if pncard == 1: dace = True
                    if pncard == 1: pncard = "A"

                    print(" _____\n|     |\n|     |\n|  ", pncard, "  |\n|     |\n|_____|\n", sep="")

                    if (dace == True) and ((dct + 10) == 21):
                        dct += 10
                        break
                break
        
        if pct > 21:
            continue
        elif dct > 21:
            if hloan == True:
                money += round((bet * 2) * 0.9)
                wtloana -= round((bet * 2) * 0.1)
                print("Dealer Busts with", dct, "you had", pct, "you win | Reward:", round(bet * 2 * 0.9))
            else:
                money += bet * 2
                print("Dealer Busts with", dct, "you had", pct, "you win | Reward:", bet * 2)
        elif pct > dct:
            if hloan == True:
                money += round((bet * 2) * 0.9)
                wtloana -= round((bet * 2) * 0.1)
                print(pct, "beats", dct, "you win | Reward:", round(bet * 2 * 0.9))
            else:
                money += bet * 2
                print(pct, "beats", dct, "you win | Reward:", bet * 2)
        elif pct < dct:
            print(dct, "beats", pct, "you lose")
        elif pct == dct:
            money += bet
            print(pct, "ties", dct, "you tie | Reward:", bet)
                    
        if hloan == True:
            print("\nMoney: ", money, sep="")
            wtloana += round(wtloana * 0.02)
            print("Debt: ", wtloana, "\n", sep="")
        else:
            print("\nMoney: ", money, "\n", sep="")