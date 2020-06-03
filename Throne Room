# -- Throne Room
# -- Date : 05/26/20
# -- Dev : Heartbreaker

# Modules
import threading
import time
from os import system, name
import sys
import winsound

## Variables ##
# Resources
wood = 100
stone = 100
food = 100
money = 0

# Buildings
sawmill = 1
quarry = 1
crop = 1
soldier = 1

barrack = 0
expansion = 0
buildlimit = 10
woodprod = 1
stoneprod = 1
foodprod = 1

# War
glory = 0
battle = 0
victory = 0
rank = "Knight"
title = "0"
lordname = 0
opponent = 0
requiredsoldier = 0

# Threading
class ThreadingExample(object):

    def __init__(self, interval=0):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            global wood
            global stone
            global food
            global crop
            global soldier
            global woodprod
            global stoneprod
            global foodprod
            global flag
            time.sleep(1)
            wood += (woodprod * sawmill)
            stone += (stoneprod * quarry)
            food += (foodprod * crop)
            food -= (0.01 * soldier)

            foodcomsuption()

            time.sleep(self.interval)

example = ThreadingExample()

# Functions

# InGame

def clear():
    if name == 'nt':
        _ = system('cls')
        print('\n' * 50)

def throneroom():
    clear()
    print("\n                                 |)))                        |))) \n\
                                 |                           | \n\
                             _  _|_  _                   _  _|_  _\n\
                             | |_| |_| |                 | |_| |_| |\n\
                             \  .      /                 \ .    .  /\n\
                              \    ,  /                   \    .  /\n\
                               | .   |_   _   _   _   _   _| ,   |\n\
                               |    .| |_| |_| |_| |_| |_| |  .  |\n\
                               | ,   | .    .     .      . |    .|\n\
                               |   . |  .     . .   .  |   |.    |\n\
                   ___----_____| .   |.   ,  _______   |   |   , |---~_____\n\
              _---~            |     |  .   /+++++++\    . | .   |         ~---_\n\
                               |.    | .    |+++++++| .    |   . |              ~-_\n\
                            __ |   . |   ,  |+++++++|.  . _|__   |                 ~-_\n\
                   ____--`~    '--~~__ .    |++++ __|----~    ~`---,              ___^~-__\n\
              -~--~                   ~---__|,--~'                  ~~----_____-~'   `~----~\n\
                _______ _    _ _____   ____  _   _ ______ _____   ____   ____  __  __ \n\
               |__   __| |  | |  __ \ / __ \| \ | |  ____|  __ \ / __ \ / __ \|  \/  |\n\
                  | |  | |__| | |__) | |  | |  \| | |__  | |__) | |  | | |  | | \  / |\n\
                  | |  |  __  |  _  /| |  | | . ` |  __| |  _  /| |  | | |  | | |\/| |\n\
                  | |  | |  | | | \ \| |__| | |\  | |____| | \ \| |__| | |__| | |  | |\n\
                  |_|  |_|  |_|_|  \_\(____/|_| \_|______|_|  \_\(____/ \____/|_|  |_|\n\
    ")
    start()

def start():
    choice = input("\n1)> PLAY\n\
2)> TUTORIAL\n\
3)> CREDIT\n\
4)> QUIT\n\
---> ")
    if choice == "1":
        gototutorial = input("\nAre you sure you want to skip the Tutorial?\n\
1) Yes\n\
2) Tutorial\n\
---> ")
        if gototutorial == "1":
            clear()
            intro()
        else:
            clear()
            tutorial()
    elif choice == "2" or choice == "tutorial":
        clear()
        tutorial()
    elif choice == "3":
            clear()
            credit()
    elif choice == "4":
        quit()
    else:
        throneroom()

def tutorial():
    print(" -- WELCOME TO THE TUTORIAL --")
    print("\n1> Basics:\n\
- Enter the number of the choice you want\n\
Ex: 1) Sawmill ---> 1\n\
- Go back to the Menu by pressing any other Key\n\
Ex: 1) Sawmill ---> m")
    print("\n2> Production:\n\
- Gain resources by buying buildings in the Market\n\
Ex: Menu > Market > Sawmill > Yes\n\
- See the amount of resources in Stats\n\
Ex: Menu > Stats\n\
- Upgrade buildings to boost your production\n\
Ex: Menu > Market > Upgrade\n\
- Sell resources to gain money\n\
Ex: Menu > Market > Sell\n\
\n- Watch Out for Error messages!\n\
Ex: You are short on Wood")
    print("\n3> War:\n\
-Buy Soldiers with Money\n\
Ex: Menu > Market > Soldier\n\
- Your title depends on your Glory Points\n\
Ex: Knight ---> <50 Glory Points\n\
- Your Glory Points determine your enemy's strength\n\
Ex: Wolves ---> <50 Glory Points (5 Soldier Required)")
    gotomainmenu = input("\n> Go to Main menu?\n\
1) Yes\n\
2) No\n\
---> ")
    if gotomainmenu == "yes":
        clear()
        throneroom()
    else:
        clear()
        throneroom()

def credit():
    clear()
    print("           -- CREDITS --")
    print("\n-- Throne Room made by Heartbreaker --\n\
-- Project started on: 05/26/2020 --\n\
    -- Released on: 06/1/2020 --\n\
    \n          -- Version 1.0 --")
    gotomainmenu = input("\n> Go to Main menu?\n\
1) Yes\n\
2) No\n\
---> ")
    if gotomainmenu == "yes":
        clear()
        throneroom()
    else:
        clear()
        throneroom()

def intro():
    global lordname
    clear()
    lord = input("How do we call our saviour?\n\
---> ")
    clear()
    lordname = lord
    variable_name = "\nAfter a long decade of fighting, Ser " + str(lord) + " defeated\n\
the enemy, The insane King of the Ocean...     \n\
Ser " + str(lord) + " is now the rightful ruler of the realm for the years to come...    \n\
Long live Ser " + str(lord) + "!\n"

    time.sleep(1)
    for char in variable_name:
        time.sleep(0.1)
        sys.stdout.write(char)
    time.sleep(1)
    clear()
    menu()

def menu():
    category = input("\n     __  __                    \n\
### |  \/  | ___ __  _ _  _  ###\n\
### | |\/| |/ -_)| |\|| || | ###\n\
### |_|  |_|\___||_||_|\_,_| ###\n\
> Where would you like to go?\n\
1) Market\n\
2) War\n\
3) Stats\n\
Q) Quit\n\
---> ")
    if category == "1":
        clear()
        market()
    elif category == "2":
        clear()
        war()
    elif category == "3":
        clear()
        stats()
    elif category == "Q" or category == "q":
        quit()
    else:
        clear()
        menu()

def market():
    global wood
    global stone
    global food
    global money
    global sawmill
    global quarry
    global crop
    global soldier
    global barrack
    global expansion
    global buildlimit
    global woodprod
    global stoneprod
    global foodprod

    marketing = input("\n     __  __             _         _    \n\
### |  \/  | __ _  _ _ | |__ ___ | |_  ###\n\
### | |\/| |/ _` || '_|| / // -_)|  _| ###\n\
### |_|  |_|\__,_||_|  |_\_\|___| \__| ###\n\
> What would you like to do?\n\
|1) Sawmill |4) Soldier   |7) Sell    | \n\
|2) Quarry  |5) Barrack   |8) Upgrade |\n\
|3) Crop    |6) Expansion |m) Menu    |\n\
---> ")
    if marketing == "1":
        clear()
        buildsawmill = input("\n                          _ _ _ \n\
    ___ __ ___ __ ___ __ (_) | |\n\
## (_-</ _` \ V  V / '  \| | | | ##\n\
## /__/\__,_|\_/\_/|_|_|_|_|_|_| ##\n\
-----------------------------------\n\
> Build a Sawmill?(-50 Wood)\n\
1) Yes\n\
2) No\n\
---> ")
        if buildsawmill == "1" and wood >= 50 and buildlimit >= 1:
            wood -= 50
            sawmill += 1
            buildlimit -= 1
            clear()
            stats()
        elif buildsawmill == "2":
            clear()
            menu()
        elif buildsawmill == "1" and buildlimit < 1:
            print("You are out of space!")
            print("Buy an Expansion!")
            time.sleep(2)
            stats()
        else:
            print("You are short on Wood!")
            time.sleep(2)
            stats()

    elif marketing == "2":
        clear()
        buildquarry = input("\n      __ _ _   _  __ _ _ __ _ __ _   _ \n\
##   / _` | | | |/ _` | '__| '__| | | | ##\n\
##  | (_| | |_| | (_| | |  | |  | |_| | ##\n\
##   \__, |\__,_|\__,_|_|  |_|   \__, | ##\n\
--------|_|----------------------|___/----\n\
> Build a Quarry?(-50 Stone)\n\
1) Yes\n\
2) No\n\
---> ")
        if buildquarry == "1" and stone >= 50 and buildlimit >= 1:
            stone -= 50
            quarry += 1
            buildlimit -= 1
            clear()
            stats()
        elif buildquarry == "2":
            clear()
            menu()
        elif buildquarry == "1" and buildlimit < 1:
            print("You are out of space!")
            print("Buy an Expansion!")
            time.sleep(2)
            stats()
        else:
            print("You are short on Stone!")
            time.sleep(2)
            stats()

    elif marketing == "3":
        clear()
        buildcrop = input("\n      ___  _ __  ___   _ __     \n\
##   / __|| '__|/ _ \ | '_ \  ##\n\
##  | (__ | |  | (_) || |_) | ##\n\
##   \___||_|   \___/ | .__/  ##\n\
----------------------|_|-------\n\
> Build a Crop?(-25 Wood/Stone)\n\
1) Yes\n\
2) No\n\
---> ")
        if buildcrop == "1" and wood >= 25 and stone >= 25 and buildlimit >= 1:
            wood -= 25
            stone -= 25
            crop += 1
            buildlimit -= 1
            clear()
            stats()
        elif buildcrop == "2":
            clear()
            menu()
        elif buildcrop == "1" and buildlimit < 1:
            print("You are out of space!")
            print("Buy an Expansion!")
            time.sleep(2)
            clear()
            menu()
        else:
            print("You are short on Wood/Stone!")
            time.sleep(2)
            clear()
            menu()


    elif marketing == "4":
        clear()
        buysoldier = input("\n                 _      _  _             \n\
     ___   ___  | |  __| |(_)  ___  _ __    \n\
##  / __| / _ \ | | / _` || | / _ \| '__| ##\n\
##  \__ \| (_) || || (_| || ||  __/| |    ##\n\
##  |___/ \___/ |_| \__,_||_| \___||_|    ##\n\
--------------------------------------------\n\
> Buy Soldier(s)?(-2$/)\n\
1) Yes\n\
2) No\n\
---> ")
        if buysoldier == "1" and barrack >= 1:
            amountsoldier = input("> How many?\n\
---> ")
            if money >= int(amountsoldier) * 2 and amountsoldier > str(0):
                money -= 2 * int(amountsoldier)
                soldier += int(amountsoldier)
                clear()
                stats()
            else:
                print("You are short on Money!")
                time.sleep(2)
                stats()
        elif buysoldier == "2":
            clear()
            menu()
        elif buysoldier == "1" and barrack < 1:
            print("You need to build a barrack!")
            time.sleep(2)
            clear()
            menu()
        else:
            clear()
            menu()

    elif marketing == "5":
        clear()
        buildbarrack = input("\n     _                                     _    \n\
    | |__    __ _  _ __  _ __  __ _   ___ | | __\n\
##  | '_ \  / _` || '__|| '__|/ _` | / __|| |/ / ##\n\
##  | |_) || (_| || |   | |  | (_| || (__ |   <  ##\n\
##  |_.__/  \__,_||_|   |_|   \__,_| \___||_|\_( ##\n\
---------------------------------------------------\n\
> Build a Barrack?(-100 Wood)\n\
1) Yes\n\
2) No\n\
---> ")
        if buildbarrack == "1" and wood >= 100 and barrack < 1 and buildlimit >= 1:
            wood -= 100
            barrack += 1
            buildlimit -= 1
            clear()
            stats()
        elif buildbarrack == "2":
            clear()
            menu()
        elif buildbarrack == "1" and wood < 100:
            print("You are short on Wood!")
            time.sleep(2)
            stats()
        elif buildbarrack == "1" and barrack >= 1:
            print("You can only build this building once!")
            time.sleep(2)
            clear()
            menu()
        elif buildbarrack == "1" and buildlimit < 1:
            print("You are out of space!")
            print("Buy an Expansion!")
            time.sleep(2)
            stats()
        else:
            clear()
            menu()

    elif marketing == "6":
        clear()
        buildexp = input("\n      ___ __  __ _ __    __ _  _ __   ___ (_)  ___   _ __  \n\
##   / _ )\ \/ /| '_ \  / _` || '_ \ / __|| | / _ \ | '_ \  ##\n\
##  |  __/ >  < | |_) || (_| || | | |\__ \| || (_) || | | | ##\n\
##   \___|/_/\_\| .__/  \__,_||_| |_||___/|_| \___/ |_| |_| ##\n\
----------------|_|-------------------------------------------\n\
> Build an Expansion?(-100 Wood/Stone)\n\
1) Yes\n\
2) No\n\
---> ")
        if buildexp == "1" and wood >= 100 and stone >= 100:
            wood -= 100
            stone -= 100
            expansion += 1
            buildlimit += 10
            clear()
            stats()
        elif buildexp == "2":
            clear()
            menu()
        else:
            print("you are short on Wood/Stone!")
            time.sleep(2)
            stats()

    elif marketing == "7":
        clear()
        selling = input("\n                _  _ \n\
     ___   ___ | || |\n\
##  / __| / _ \| || | ##\n\
##  \__ \|  __/| || | ##\n\
##  |___/ \___||_||_| ##\n\
------------------------\n\
> What do you want to sell?\n\
1) Wood\n\
2) Stone\n\
m) Menu\n\
---> ")
        if selling == "1":
            wquantity = input("> How much Wood do you want to sell?(1$/10 Wood)\n\
---> ")
            if wquantity >= str(0) and wquantity <= str(wood):
                wood -= 1 * float(wquantity)
                money += 0.1 * float(wquantity)
                stats()
            elif wquantity < str(0):
                print("Enter a real value!")
                time.sleep(2)
                clear()
                menu()
            else:
                print("You are short on Wood!")
                time.sleep(2)
                clear()
                stats()

        elif selling == "2":
            squantity = input("> How much Stone do you want to sell?(1$/10 Stone)\n\
---> ")
            if squantity >= str(0) and squantity <= str(stone):
                stone -= 1 * float(squantity)
                money += 0.1 * float(squantity)
                stats()
            elif squantity < str(0):
                print("Enter a real value!")
                time.sleep(2)
                clear()
                menu()
            else:
                print("You are short on Stone!")
                time.sleep(2)
                clear()
                stats()
        else:
            clear()
            menu()

    elif marketing == "8":
        clear()
        upgrading = input("\n     _   _  _ __    __ _  _ __  __ _   __| |  ___ \n\
##  | | | || '_ \  / _` || '__|/ _` | / _` | / _ ) ##\n\
##  | |_| || |_) || (_| || |  | (_| || (_| ||  __/ ##\n\
##   \__,_|| .__/  \__, ||_|   \__,_| \__,_| \___| ##\n\
-----------|_|-----|___/-----------------------------\n\
> What do you want to upgrade?\n\
1) Sawmill\n\
2) Quarry\n\
3) Crop\n\
m) Menu\n\
---> ")
        if upgrading == "1":
            upgrades = input("> Do you want to upgrade your Sawmills?(-1000 Wood)\n\
1) Yes\n\
2) No\n\
---> ")
            if upgrades == "1" and wood >= 1000:
                wood -= 1000
                woodprod = woodprod * 2
                clear()
                stats()
            elif wood < 1000:
                print("You are short on Wood!")
                time.sleep(2)
                clear()
                stats()
            else:
                clear()
                stats()

        elif upgrading == "2":
            upgradeq = input("> Do you want to upgrade your Quarries?(-1000 Stone)\n\
1) Yes\n\
2) No\n\
---> ")
            if upgradeq == "1" and stone >= 1000:
                stone -= 1000
                stoneprod = stoneprod * 2
                clear()
                stats()
            elif stone < 1000:
                print("You are short on Stone!")
                time.sleep(2)
                clear()
                stats()
            else:
                clear()
                stats()

        elif upgrading == "3":
            upgradec = input("> Do you want to upgrade your Crops?(-1000 Wood/Stone)\n\
1) Yes\n\
2) No\n\
---> ")
            if upgradec == "1" and wood >= 1000 and stone >= 1000:
                wood -= 1000
                stone -= 1000
                foodprod = foodprod * 2
                clear()
            elif wood < 1000 or stone < 1000:
                print("You are short on Wood/Stone!")
                time.sleep(2)
                clear()
                stats()
            else:
                clear()
                stats()
        else:
            clear()
            menu()

    else:
        clear()
        menu()

def war():
    global glory
    global battle
    global victory
    global soldier
    global rank
    global title
    global opponent
    global requiredsoldier
    if glory < 50:
        rank = "Knight"
        title = "Ser"
        opponent = "Wolves"
        requiredsoldier = 5
    elif glory >= 50 and glory < 500:
        rank = "Baron"
        title = "Baron"
        opponent = "Peasants"
        requiredsoldier = 100
    elif glory >= 500 and glory < 2000:
        rank = "Duke"
        title = "Duke"
        opponent = "Rebels"
        requiredsoldier = 1000
    elif glory >= 2000 and glory < 2500:
        rank = "Prince"
        title = "Prince"
        opponent = "Lord"
        requiredsoldier = 5000
    elif glory >= 2500 and glory < 10000:
        rank = "King"
        title = "King"
        opponent = "Lord with Dragon"
        requiredsoldier = 10000
    elif glory >= 10000:
        rank = "Emperor"
        title = "Emperor"
        opponent = "Giant King"
        requiredsoldier = 100000
    print("\n    __      __             \n\
### \ \    / /__ _  _ _  ###\n\
###  \ \/\/ // _` || '_| ###\n\
###   \_/\_/ \__,_||_|   ###")
    print("> YOU ARE THE " + rank + " " + str(lordname) + "!<")
    print("\nYou have " + str(glory) + " Glory points")
    print("You have launched " + str(battle) + " Battle(s)")
    print("You have won " + str(victory) + " Victory")
    print("")
    war = input("> Do you want to start a War?\n\
You will fight the " + str(opponent) + ". \n\
You will need " + str(requiredsoldier) + " Soldiers.\n\
1) Yes\n\
2) No\n\
---> ")
    if war == "1" and soldier == 0:
        print("You need soldiers to fight!")
        time.sleep(2)
        clear()
        menu()
    elif war == "1" and glory < 50 and soldier > 0:
        clear()
        print("\n   ____                            _   ")
        print("  |  _ \  ___  _ __    ___   _ __ | |_ \n\
# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n\
# |  _ <|  __/| |_) || (_) || |   | |_  #\n\
# |_| \_)\___|| .__/  \___/ |_|    \__| #\n\
--------------|_|-----------------------")
        print("You have started a battle against some wolves")
        time.sleep(2)
        if soldier >= 5:
            print("You won against the wolves!\n\
You have gained 10 Glory points!")
            glory += 10
            battle += 1
            victory += 1
            time.sleep(2)
            gotomenu()
        else:
            print("You Lost and your soldiers died fighting...\n\
A fair treatment!\n\
Fortunately, you didn't lost any Glory points...")
            soldier = 0
            battle += 1
            time.sleep(3)
            gotomenu()

    elif war == "1" and glory >= 50 and glory < 500 and soldier > 0:
        print("\n   ____                            _   ")
        print("  |  _ \  ___  _ __    ___   _ __ | |_ \n\
# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n\
# |  _ <|  __/| |_) || (_) || |   | |_  #\n\
# |_| \_)\___|| .__/  \___/ |_|    \__| #\n\
--------------|_|-----------------------")
        print("You have declared War to some peasants")
        time.sleep(2)
        if soldier >= 100:
            print("You have defeated the angry peasants!\n\
You only had " + str(soldier * 0.05) + " casualties\n\
And you have gained 25 Glory Points!")
            soldier -= soldier * 0.05
            glory += 25
            battle += 1
            victory += 1
            time.sleep(2)
            clear()
            menu()
        else:
            print("You Lost and your soldiers died by the swords of your enemy... \n\
A fair treatment!\n\
You lost 10 Glory points...")
            soldier = 0
            glory -= 10
            battle += 1
            time.sleep(3)
            gotomenu()

    elif war == "1" and glory >= 500 and glory < 2000 and soldier > 0:
        print("\n   ____                            _   ")
        print("  |  _ \  ___  _ __    ___   _ __ | |_ \n\
# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n\
# |  _ <|  __/| |_) || (_) || |   | |_  #\n\
# |_| \_)\___|| .__/  \___/ |_|    \__| #\n\
--------------|_|-----------------------")
        print("You have started a War against some Rebels")
        time.sleep(2)
        if soldier >= 1000:
            print("You have defeated the filthy Rebels!\n\
You only had " + str(soldier * 0.2) + " casualties\n\
And you have gained 50 Glory Points!")
            soldier -= soldier * 0.2
            glory += 50
            battle += 1
            victory += 1
            time.sleep(2)
            gotomenu()
        else:
            print("You Lost and your soldiers died in the mud... \n\
A fair treatment!\n\
Sadly, you lost 50 Glory points...")
            soldier = 0
            glory -= 50
            battle += 1
            time.sleep(3)
            gotomenu()

    elif war == "1" and glory >= 2000 and glory < 2500 and soldier > 0:
        print("\n   ____                            _   ")
        print("  |  _ \  ___  _ __    ___   _ __ | |_ \n\
# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n\
# |  _ <|  __/| |_) || (_) || |   | |_  #\n\
# |_| \_)\___|| .__/  \___/ |_|    \__| #\n\
--------------|_|-----------------------")
        print("You have started a War against a foreign Lord")
        time.sleep(2)
        if soldier >= 5000:
            print("You have gloriously defeated him!\n\
You only had " + str(soldier * 0.3) + " casualties\n\
And you have gained 200 Glory Points!")
            soldier -= soldier * 0.3
            glory += 200
            battle += 1
            victory += 1
            time.sleep(2)
            gotomenu()
        else:
            print("You Lost and your soldiers were burned alive... \n\
A fair treatment!\n\
You lost 200 Glory points...")
            soldier = 0
            glory -= 200
            battle += 1
            time.sleep(3)
            gotomenu()

    elif war == "1" and glory >= 2500 and glory < 10000 and soldier > 0:
        print("\n   ____                            _   ")
        print("  |  _ \  ___  _ __    ___   _ __ | |_ \n\
# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n\
# |  _ <|  __/| |_) || (_) || |   | |_  #\n\
# |_| \_)\___|| .__/  \___/ |_|    \__| #\n\
--------------|_|-----------------------")
        print("You have started a War against a Lord with a Dragon")
        time.sleep(2)
        if soldier >= 10000:
            print("You have defeated the Lord and his Dragon!\n\
You only had " + str(soldier * 0.5) + " casualties\n\
And you have gained 1000 Glory Points!")
            soldier -= soldier * 0.5
            glory += 1000
            battle += 1
            victory += 1
            time.sleep(2)
            gotomenu()
        else:
            print("You Lost and your soldiers were skinned alive... \n\
A fair treatment!\n\
Unfortunately, you lost 1500 Glory points...")
            soldier = 0
            glory -= 1500
            battle += 1
            time.sleep(3)
            gotomenu()

    elif war == "1" and glory >= 10000 and soldier > 0:
        print("\n   ____                            _   ")
        print("  |  _ \  ___  _ __    ___   _ __ | |_ \n\
# | |_) |/ _ \| '_ \  / _ \ | '__|| __| #\n\
# |  _ <|  __/| |_) || (_) || |   | |_  #\n\
# |_| \_)\___|| .__/  \___/ |_|    \__| #\n\
--------------|_|-----------------------")
        print("You have started a War against The Giant King")
        time.sleep(2)
        if soldier >= 100000:
            print("You have defeated the Giant King!")
            soldier -= soldier * 0.9
            glory += 100000
            battle += 1
            victory += 1
            time.sleep(2)
            variable_name2 = "\nCommander: The War is over! You have managed to bring peace and freedom among your people!\n\
As you built enough buildings and supplied enough supplies for the whole Kingdom!\n\
It is finally the time to retire in your cas-...\n\
" + str(title) + " " + str(lordname) + ": I know I won! And I don't want to retire! Now, all is mine! This is mine! You are mine!\n\
Kill those who say the opposite! Kill them all! Kill th-\n\
Commander: *Stabbing " + str(title) + " " + str(lordname) + "* No... Now you won't cause any more damage to anyone...\n\
Now look me in the eyes... I am in charge... It's over..."
            for char in variable_name2:
                time.sleep(0.1)
                sys.stdout.write(char)
            time.sleep(2)
            clear()
            throneroom()
        else:
            print("You Lost and your soldiers were hanged as an example... \n\
A fair treatment!\n\
Because of them, you lost 10000 Glory points...")
            soldier = 0
            glory -= 5000
            battle += 1
            time.sleep(3)
            gotomenu()

    else:
        clear()
        menu()

def stats():
    global crop
    global soldier
    print("\n     ___  _          _         \n\
### / __|| |_  __ _ | |_  ___ ###\n\
### \__ \|  _|/ _` ||  _|(_-< ###\n\
### |___/ \__|\__,_| \__|/__/ ###\n\
")
    # Wood
    print("### Wood ### ")
    print("You have " + str(wood) + " Wood")
    print("You have " + str(sawmill) + " Sawmill(s)")
    print("You produce " + str(sawmill * woodprod) + " Wood per second")
    print("")

    # Stone
    print("### Stone ### ")
    print("You have " + str(stone) + " Stone")
    print("You have " + str(quarry) + " Quarry")
    print("You produce " + str(quarry * stoneprod) + " Stone per second")
    print("")

    # Food
    print("### Food ### ")
    print("You have " + str(food) + " Food")
    print("You have " + str(crop) + " Crop(s)")
    print("You produce " + str(foodprod * crop) + " Food per second")
    print("You can feed " + str((crop * foodprod) * 100) + " Soldier(s)")
    print("")

    # Money
    print("### Money ### ")
    print("You have " + str(money) + " Money")
    print("")

    # War
    # Soldier
    print("### Soldier ### ")
    print("You have " + str(soldier) + " Soldier(s)")
    print("")

    # Expansion
    print("### Expansion ### ")
    print("You have " + str(expansion) + " Expansion(s)")
    print("You can build " + str(buildlimit) + " more Building(s)")

    gotomenu()

def foodcomsuption():
    global food
    global soldier
    if food <= int(0) and crop > 0:
        soldier = (crop * foodprod) * 100
        food = 0
        print("")
        print("You lost many soldiers due to starvation\n\
Build more Crops! ")
        time.sleep(2)
        clear()
        stats()
    elif food <= int(0) and crop <= 0:
        soldier = 0
        food = 0
        print("\nYou lost many soldiers due to starvation\n\
Build more Crops! ")
        time.sleep(2)
        clear()
        stats()

def gotomenu():
    gotomenu = input("\n> Go to menu?\n\
1) Yes\n\
2) No\n\
---> ")
    if gotomenu == "yes":
        clear()
        menu()
    else:
        clear()
        menu()

winsound.PlaySound("BrownFoxInn.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
throneroom()
