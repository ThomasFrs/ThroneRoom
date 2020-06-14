# -- Throne Room
# -- Date : 05/26/20
# -- Dev : Heartbreaker

# Modules
import threading
import time
from os import system, name
import sys
import winsound

#Variables
wood = 100
stone = 100
food = 100
money = 0

sawmill = 1
quarry = 1
crop = 1
soldier = 0

barrack = 0
expansion = 0
buildlimit = 10
woodprod = 1
stoneprod = 1
foodprod = 1

glory = 0
battle = 0
victory = 0
rank = "Chevalier"
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
    choice = input("\n1)> JOUER\n\
2)> TUTORIEL\n\
3)> CREDITS\n\
4)> QUITTER\n\
---> ")
    if choice == "1":
        gototutorial = input("\nTu es sûr de vouloir passer le Tutoriel?\n\
1) Oui\n\
2) Tutoriel\n\
---> ")
        if gototutorial == "1":
            clear()
            intro()
        else:
            clear()
            tutorial()
    elif choice == "2" or choice == "tutoriel":
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
    print(" -- BIENVENUE AU TUTORIEL --")
    print("\n1> Bases:\n\
- Entre le chiffre de l'option voulue\n\
Ex: 1) Bûcheron ---> 1\n\
- Va au menu en pressant n'importe quelle touche\n\
Ex: 1) Bûcheron ---> m")
    print("\n2> Production:\n\
- Produis des ressources en achetant des bâtiments\n\
Ex: Menu > Marché > Bûcheron > Oui\n\
- Regarde la production dans les Stats\n\
Ex: Menu > Stats\n\
- Améliore les bâtiments pour booster la production\n\
Ex: Menu > Marché > Améliorations\n\
- Vends des ressources pour gagner de l'argent\n\
Ex: Menu > Marché > Vendre\n\
\n- Fais attention aux messages!\n\
Ex: Tu manques de bois")
    print("\n3> Guerre:\n\
- Achète des soldats avec de l'argent\n\
Ex: Menu > Marché > Soldats\n\
- Ton titre dépend de tes points de Gloire\n\
Ex: Chevalier ---> <50 points de Gloire\n\
- Tes points de Gloire déterminent la force de ton ennemi\n\
Ex: Loups ---> <50 points de Gloire (5 Soldats requis)")
    gotomainmenu = input("\n> Aller au Menu principal?\n\
1) Oui\n\
2) Non\n\
---> ")
    if gotomainmenu == "1":
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
    gotomainmenu = input("\n> Aller au Menu principal?\n\
1) Oui\n\
2) Non\n\
---> ")
    if gotomainmenu == "1":
        clear()
        throneroom()
    else:
        clear()
        throneroom()

def intro():
    global lordname
    clear()
    lord = input("Quel est le nom de notre sauveur?\n\
---> ")
    clear()
    lordname = lord
    variable_name = f"\nAprès une longue décennie de combat, Ser {lord} a battu\n\
l'ennemi, l'horrible Roi de l'Océan...     \n\
Sir {lord} est maintenant à la tête du Royaume pour les années à venir...    \n\
Longue vie à Ser {lord}!\n"

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
> Où voulez-vous aller?\n\
1) Marché\n\
2) Guerre\n\
3) Stats\n\
Q) Quitter\n\
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
    global wood, stone, food, money, sawmill, quarry, crop, soldier, barrack, expansion, buildlimit, woodprod, stoneprod, foodprod
    marketing = input("\n     __  __             _         _    \n\
### |  \/  | __ _  _ _ | |__ ___ | |_  ###\n\
### | |\/| |/ _` || '_|| / // -_)|  _| ###\n\
### |_|  |_|\__,_||_|  |_\_\|___| \__| ###\n\
> Que voulez-vous faire?\n\
|1) Bûcheron |4) Soldats   |7) Vendre    | \n\
|2) Carrière |5) Caserne   |8) Améliorer |\n\
|3) Moisson  |6) Expansion |m) Menu      |\n\
---> ")
    if marketing == "1":
        clear()
        buildsawmill = input("\n                          _ _ _ \n\
    ___ __ ___ __ ___ __ (_) | |\n\
## (_-</ _` \ V  V / '  \| | | | ##\n\
## /__/\__,_|\_/\_/|_|_|_|_|_|_| ##\n\
-----------------------------------\n\
> Construire un Bûcheron?(-50 Bois)\n\
1) Oui\n\
2) Non\n\
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
            print("Vous manquez d'espace!")
            print("Achetez une Expansion!")
            time.sleep(2)
            stats()
        else:
            print("Vous manquez de Bois!")
            time.sleep(2)
            stats()

    elif marketing == "2":
        clear()
        buildquarry = input("\n      __ _ _   _  __ _ _ __ _ __ _   _ \n\
##   / _` | | | |/ _` | '__| '__| | | | ##\n\
##  | (_| | |_| | (_| | |  | |  | |_| | ##\n\
##   \__, |\__,_|\__,_|_|  |_|   \__, | ##\n\
--------|_|----------------------|___/----\n\
> Construire une Carrière?(-50 Pierre)\n\
1) Oui\n\
2) Non\n\
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
            print("Vous manquez d'espace!")
            print("Achetez une Expansion!")
            time.sleep(2)
            stats()
        else:
            print("Vous manquez de Pierre!")
            time.sleep(2)
            stats()

    elif marketing == "3":
        clear()
        buildcrop = input("\n      ___  _ __  ___   _ __     \n\
##   / __|| '__|/ _ \ | '_ \  ##\n\
##  | (__ | |  | (_) || |_) | ##\n\
##   \___||_|   \___/ | .__/  ##\n\
----------------------|_|-------\n\
> Faire une Moisson?(-25 Bois/Pierre)\n\
1) Oui\n\
2) Non\n\
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
            print("Vous manquez d'espace!")
            print("Achetez une Expansion!")
            time.sleep(2)
            clear()
            menu()
        else:
            print("Vous manquez de Bois/Pierre!")
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
> Achetez Soldat(s)?(-2$/)\n\
1) Oui\n\
2) Non\n\
---> ")
        if buysoldier == "1" and barrack >= 1:
            amountsoldier = input("> Combien?\n\
---> ")
            if money >= int(amountsoldier) * 2 and amountsoldier > str(0):
                money -= 2 * int(amountsoldier)
                soldier += int(amountsoldier)
                clear()
                stats()
            else:
                print("Vous manquez d'Argent!")
                time.sleep(2)
                stats()
        elif buysoldier == "2":
            clear()
            menu()
        elif buysoldier == "1" and barrack < 1:
            print("Vous devez construire une Caserne!")
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
> Construire une Caserne?(-100 Bois)\n\
1) Oui\n\
2) Non\n\
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
            print("Vous manquez de Bois!")
            time.sleep(2)
            stats()
        elif buildbarrack == "1" and barrack >= 1:
            print("Vous ne pouvez construire qu'une Caserne!")
            time.sleep(2)
            clear()
            menu()
        elif buildbarrack == "1" and buildlimit < 1:
            print("Vous manquez d'espace!")
            print("Achetez une Expansion!")
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
> Construire un Expansion?(-100 Bois/Pierre)\n\
1) Oui\n\
2) Non\n\
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
            print("Vous manquez de Bois/Pierre!")
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
> Que voulez-vous vendre?\n\
1) Bois\n\
2) Pierre\n\
m) Menu\n\
---> ")
        if selling == "1":
            wquantity = input("> Combien de Bois voulez-vous vendre?(1$/10 Bois)\n\
---> ")
            if wquantity >= str(0) and wquantity <= str(wood):
                wood -= 1 * float(wquantity)
                money += 0.1 * float(wquantity)
                stats()
            elif wquantity < str(0):
                print("Entrez un vrai nombre!")
                time.sleep(2)
                clear()
                menu()
            else:
                print("Vous manquez de Bois!")
                time.sleep(2)
                clear()
                stats()

        elif selling == "2":
            squantity = input("> Combien de Pierre voulez-vous vendre?(1$/10 Stone)\n\
---> ")
            if squantity >= str(0) and squantity <= str(stone):
                stone -= 1 * float(squantity)
                money += 0.1 * float(squantity)
                stats()
            elif squantity < str(0):
                print("Entrez un vrai nombre!")
                time.sleep(2)
                clear()
                menu()
            else:
                print("Vous manquez de Pierre!")
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
> Que voulez-vous améliorer?\n\
1) Bûcheron\n\
2) Carrière\n\
3) Moisson\n\
m) Menu\n\
---> ")
        if upgrading == "1":
            upgrades = input("> Voulez-vous améliorer vos Bûcherons?(-1000 Bois)\n\
1) Oui\n\
2) Non\n\
---> ")
            if upgrades == "1" and wood >= 1000 and woodprod <= 1000000:
                wood -= 1000
                woodprod = woodprod * 2
                clear()
                stats()
            elif wood < 1000:
                print("Vous manquez de Bois!")
                time.sleep(2)
                clear()
                stats()
            elif woodprod > 1000000:
                print("Il est temps de vendre du Bois")
                time.sleep(2)
                clear()
                stats()
            else:
                clear()
                stats()

        elif upgrading == "2":
            upgradeq = input("> Voulez-vous améliorer vos Carrières?(-1000 Pierre)\n\
1) Oui\n\
2) Non\n\
---> ")
            if upgradeq == "1" and stone >= 1000 and stoneprod <= 1000000:
                stone -= 1000
                stoneprod = stoneprod * 2
                clear()
                stats()
            elif stone < 1000:
                print("Vous manquez de Bois!")
                time.sleep(2)
                clear()
                stats()
            elif stoneprod > 1000000:
                print("Il est temps de vendre de la Pierre")
                time.sleep(2)
                clear()
                stats()
            else:
                clear()
                stats()

        elif upgrading == "3":
            upgradec = input("> Voulez-vous améliorer vos Moissons?(-1000 Bois/Pierre)\n\
1) Oui\n\
2) Non\n\
---> ")
            if upgradec == "1" and wood >= 1000 and stone >= 1000 and foodprod <= 1000000:
                wood -= 1000
                stone -= 1000
                foodprod = foodprod * 2
                clear()
                stats()
            elif wood < 1000 or stone < 1000:
                print("Vous manquez de Bois/Pierre!")
                time.sleep(2)
                clear()
                stats()
            elif foodprod > 1000000:
                print("Il est temps de nourrir des Soldats")
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
    global glory, battle, victory, soldier, rank, opponent, requiredsoldier
    if glory < 50:
        rank = "Chevalier"
        opponent = "Loups"
        requiredsoldier = 5
    elif glory >= 50 and glory < 500:
        rank = "Baron"
        opponent = "Paysants"
        requiredsoldier = 100
    elif glory >= 500 and glory < 2000:
        rank = "Duc"
        opponent = "Rebelles"
        requiredsoldier = 1000
    elif glory >= 2000 and glory < 2500:
        rank = "Prince"
        opponent = "Seigneur"
        requiredsoldier = 5000
    elif glory >= 2500 and glory < 10000:
        rank = "Roi"
        opponent = "Seigneur avec Dragon"
        requiredsoldier = 10000
    elif glory >= 10000:
        rank = "Empereur"
        opponent = "Roi des Géants"
        requiredsoldier = 100000
    print("\n    __      __             \n\
### \ \    / /__ _  _ _  ###\n\
###  \ \/\/ // _` || '_| ###\n\
###   \_/\_/ \__,_||_|   ###")
    print(f"> VOUS ÊTES LE {rank} {lordname}!<")
    print(f"\nVous avez {glory} points de Gloire!")
    print(f"Vous avez lancé {battle} Bataille(s)!")
    print(f"Vous avez gagné {victory} Bataille(s)!")
    print("")
    war = input(f"> Voulez-vous commencer la Guerre?\n\
Vous affronterez des {opponent}. \n\
Vous aurez besoin de {requiredsoldier} Soldat(s).\n\
1) Oui\n\
2) Non\n\
---> ")
    if war == "1" and soldier == 0:
        print("Vous avez besoin de Soldats pour combattre!")
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
        print("Vous avez affronté des Loups")
        time.sleep(2)
        if soldier >= 5:
            print("Vous avez battu les Loups!\n\
Vous avez gagné 10 points de Gloire")
            glory += 10
            battle += 1
            victory += 1
            time.sleep(2)
            gotomenu()
        else:
            print("Vous avez perdu et vos soldats sont morts au combat...\n\
Un coup de chance!\n\
Heureusement vous n'avez pas perdu de points de Gloire...")
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
        print("Vous avez déclaré la Guerre à des Paysants")
        time.sleep(2)
        if soldier >= 100:
            print("Vous avez tué les Paysans en colère!\n\
Vous avez seulement perdu " + str(soldier * 0.05) + " soldats\n\
Et vous avez gagné 25 points de Gloire!")
            soldier -= soldier * 0.05
            glory += 25
            battle += 1
            victory += 1
            time.sleep(2)
            clear()
            menu()
        else:
            print("Vous avez perdu et vos hommes ont été tués par les épées ennemies... \n\
Béni soit-elles!\n\
Vous avez perdu 10 points de Gloire...")
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
        print("Vous avez lancé une attaque contre les Rebelles")
        time.sleep(2)
        if soldier >= 1000:
            print("Vous avez écrasé ces gueux!\n\
Vous avez seulement perdu " + str(soldier * 0.2) + " soldats\n\
Mais vous avez gagné 50 points de Gloire!")
            soldier -= soldier * 0.2
            glory += 50
            battle += 1
            victory += 1
            time.sleep(2)
            gotomenu()
        else:
            print("Vous avez perdu et vos soldats sont morts dans la boue... \n\
Qu'ils y restent!\n\
Tristement, vous avez perdu 50 points de Gloire...")
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
        print("Vous avez attaqué un seigneur étranger")
        time.sleep(2)
        if soldier >= 5000:
            print("Vous l'avez glorieusement battu!\n\
Vous avez seulement perdu " + str(soldier * 0.3) + " soldats\n\
Avec un ajout de 200 points de Gloire!")
            soldier -= soldier * 0.3
            glory += 200
            battle += 1
            victory += 1
            time.sleep(2)
            gotomenu()
        else:
            print("Vous avez perdu et vos soldats ont étés brûlés vifs... \n\
Une sage décision!\n\
Vous avez perdu 200 points de Gloire...")
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
        print("Vous avez commencé une Guerre contre un seigneur avec des Dragons")
        time.sleep(2)
        if soldier >= 10000:
            print("Vous avez égorgé le Seigneur et pendu les Dragons!\n\
Vous avez seulement perdu " + str(soldier * 0.5) + " soldats\n\
Et vous avez gagné 1000 points de Gloire!")
            soldier -= soldier * 0.5
            glory += 1000
            battle += 1
            victory += 1
            time.sleep(2)
            gotomenu()
        else:
            print("Vous avez perdu et vos soldats ont été écorchés vifs... \n\
Le ciel vous en récompensera!\n\
Malheureusement vous avez perdu 1500 points de Gloire...")
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
        print("Vous avez déclaré la guerre au Roi des Géants")
        time.sleep(2)
        if soldier >= 100000:
            print("Vous avez brûlé le Roi des Géants et son misérable peuple!")
            soldier -= soldier * 0.9
            glory += 100000
            battle += 1
            victory += 1
            time.sleep(2)
            variable_name2 = f"\nCommandant: La guerre est finie! Vous avez réussi à apporter la paix et la prospérité au peuple!\n\
Comme vous avez construit assez de constructions et cultivé assez de cultures pour tout le Royaume,\n\
Il est enfin temps de terminer votre règne dans votre ch-...\n\
{rank} {lordname}: Je sais que j'ai gagné! Je ne veux pas finir mon règne! Maintenant tout est à moi! Ceci est à moi! Tu es à moi!\n\
Tuez ceux qui disent le contraire! Tuez les! Tuez les to-\n\
Commandant: *Poignardant {rank} {lordname}* Non... Maintenant tu ne feras plus de mal à personne...\n\
Regarde-moi dans les yeux... J'ai le pouvoir... C'est fini..."
            for char in variable_name2:
                time.sleep(0.1)
                sys.stdout.write(char)
            time.sleep(2)
            clear()
            throneroom()
        else:
            print("Vous avez été défait est vos hommes ont servis d'exemples... \n\
Puissent-ils ne plus vous décevoir!\n\
A cause d'eux vous avez perdu 5000 points de Gloires...")
            soldier = 0
            glory -= 5000
            battle += 1
            time.sleep(3)
            gotomenu()

    else:
        clear()
        menu()

def stats():
    global crop, soldier
    print("\n     ___  _          _         \n\
### / __|| |_  __ _ | |_  ___ ###\n\
### \__ \|  _|/ _` ||  _|(_-< ###\n\
### |___/ \__|\__,_| \__|/__/ ###\n\
")
    # Wood
    print("### Bois ### ")
    print("Vous avez " + str(wood) + " Bois")
    print("Vous avez " + str(sawmill) + " Bûcheron(s)")
    print("You produce " + str(sawmill * woodprod) + " Bois par seconde")
    print("")

    # Stone
    print("### Pierre ### ")
    print("Vous avez " + str(stone) + " Pierre(s)")
    print("Vous avez " + str(quarry) + " Carrières")
    print("Vous produisez " + str(quarry * stoneprod) + " Pierre(s) par seconde")
    print("")

    # Food
    print("### Nourriture ### ")
    print("Vous avez " + str(food) + " Pain(s)")
    print("Vous avez fait " + str(crop) + " Moisson(s)")
    print("Vous produisez " + str(foodprod * crop) + " Pain(s) par seconde")
    print("Vous pouvez nourrir " + str((crop * foodprod) * 100) + " Soldat(s)")
    print("")

    # Money
    print("### Argent ### ")
    print("Vous avez " + str(money) + " Pièces")
    print("")

    # War
    # Soldier
    print("### Soldats ### ")
    print("Vous avez " + str(soldier) + " Soldats(s)")
    print("")

    # Expansion
    print("### Expansion ### ")
    print("Vous avez " + str(expansion) + " Expansion(s)")
    print("Vous pouvez construire " + str(buildlimit) + " Bâtiments de plus")

    gotomenu()

def foodcomsuption():
    global food, soldier
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
    gotomenu = input("\n> Aller au menu?\n\
1) Oui\n\
2) Non\n\
---> ")
    if gotomenu == "1":
        clear()
        menu()
    else:
        clear()
        menu()

winsound.PlaySound("BrownFoxInn.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
throneroom()

