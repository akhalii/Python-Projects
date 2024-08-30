#Blackjack Project

import random
hit = random.randint(1,11)
hit2 = random.randint(1,11)
hit3 = random.randint(1,11)
hit4 = random.randrange(1,11)
hit5 = random.randint(1,11)
hit6 = random.randint(1,11)
hit7 = random.randint(1,11)
hit8 = random.randrange(1,11)
hit9 = random.randint(1,11)
hit10 = random.randint(1,11)
hit11 = random.randint(1,11)
game = input("Would you like to play blackjack? ")

if game == "yes":
    print (f"here is your hand: {hit}")
else:
    quit()

choice = input("would you like to hit or stand? ")

if choice == "hit":
    print (hit+hit2)
else:
    quit()

if (hit+hit2) > 21:
    print("You busted!")
else:
    choice2 = input("would you like to hit or stand? ")
    if choice2 == "hit":
        print (hit+hit2+hit3)
    else:
        quit()

if (hit+hit2+hit3) > 21:
    print("You busted!")
else:
    choice3 = input("would you like to hit or stand? ")
    if choice3 == "hit":
        print (hit+hit2+hit3+hit4)
    else:
        quit()

if (hit+hit2+hit3+hit4) > 21:
    print("You busted!")
else:
    choice4 = input("would you like to hit or stand? ")
    if choice4 == "hit":
        print (hit+hit2+hit3+hit4+hit5)
    else:
        quit()

if (hit+hit2+hit3+hit4+hit5) > 21:
    print("You busted!")
else:
    choice5 = input("would you like to hit or stand? ")
    if choice5 == "hit":
        print (hit+hit2+hit3+hit4+hit5+hit6)
    else:
        quit()

if (hit+hit2+hit3+hit4+hit5+hit6) > 21:
    print("You busted!")
else:
    choice6 = input("would you like to hit or stand? ")
    if choice6 == "hit":
        print (hit+hit2+hit3+hit4+hit5+hit6+hit7)
    else:
        quit()