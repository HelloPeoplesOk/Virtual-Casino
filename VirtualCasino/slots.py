import random

d1 = None
d2 = None
d3 = None

wtloana = 0
while True:
    try:
        cost = int(input("How much does each roll cost: "))
        break
    except:
        continue
money = 0
hloan = False

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
                break
            else:
                while True:
                    wtroll = input("Want to roll or pay some debt? (y/n/d): ")
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
            wtroll = input("Want to roll? (y/n): ")
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
        if money - cost < 0:
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

    if wtroll.lower() == "y":
        money -= cost

        print("\nMoney: ", money, sep="")
        if hloan == True:
            print("Debt: ", wtloana, sep="")

        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        d3 = random.randint(1,6)
        print(" _____ _____ _____ \n|     |     |     |\n|  ", d1, "  |  ", d2, "  |  ", d3, "  |\n|_____|_____|_____|\n", sep="")

        if ((d1 == d2) or (d1 == d3)) and not((d1 == d2) and (d2 == d3)):
            if hloan == True:
                money += round((d1 * 10) * 0.9)
                wtloana -= round((d1 * 10) * 0.1)
                print("Double ", d1, "'s\nReward: ", round((d1 * 10) * 0.9), sep="")
            else:
                money += d1 * 10
                print("Double ", d1, "'s\nReward: ", d1 * 10, sep="")
        elif (d2 == d3) and not((d1 == d2) and (d2 == d3)):
            if hloan == True:
                money += round((d2 * 10) * 0.9)
                wtloana -= round((d2 * 10) * 0.1)
                print("Double ", d1, "'s\nReward: ", round((d2 * 10) * 0.9), sep="")
            else:
                money += d2 * 10
                print("Double ", d2, "'s\nReward: ", d2 * 10, sep="")
        elif (d2 == d3) and (d1 == d2):
            if hloan == True:
                money += round((80 + d1 * 20) * 0.9)
                wtloana -= round((80 + d1 * 20) * 0.1)
                print("Triple ", d1, "'s\nReward: ", round((80 + d1 * 20) * 0.9), sep="")
            else:
                money += 80 + d1 * 20
                print("Triple ", d1, "'s\nReward: ", 80 + d1 * 20, sep="")
        else:
            print("Nothing")
        
        if hloan == True:
            print("\nMoney: ", money, sep="")
            wtloana += round(wtloana * 0.02)
            print("Debt: ", wtloana, "\n", sep="")
        else:
            print("\nMoney: ", money, "\n", sep="")