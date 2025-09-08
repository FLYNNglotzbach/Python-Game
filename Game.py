#import stuff
import random
import time
import sys

#Creating variables
health = 100
day = 0
hunger = 10
alive = True
foodStock = 0
farming = "no"
sleep = "no"
starving = False
farmLevel = 0
shelterLevel = 0
shelterHealth = 0
exploreDone = False
farmDone = False
shelterDone = False
shelterDestroyed = False
shelterUpgrade = False
farmUpgrade = False
#Creating a typing effect when printing
def typeText(text, speed=0.05, variance=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed + random.uniform(-variance, variance))
    print()

#Checking to see if health goes past 100
def healthCheck():
    global health, alive
    if health >= 100:
        health = 100
    if health <= 0:
        alive = False

#checking to see if hunger goes over 10
def hungerCheck():
    global hunger, starving
    if hunger > 10:
        hunger = 10
    if hunger <= 0:
        starving = True

def foodStorageCheck():
    global foodStock
    if foodStock <= 0:
        foodStock = 0

def shelterHealthCheck():
    global shelterHealth
    if shelterHealth <= 0:
        shelterHealth = 0
        shelterDestroyed = True
        typeText(f"OH NO MY SHELTER IS DESTROYED!!!!!!!!!!!", 0.05, 0.02)

#creating the action farming to gain food
def farmingAction():
    global foodStock
    farming = input("Do you want to farm? (yes/no): ").lower()
    if farming == "yes":
        foodStock += farmLevel
        print("You farmed and gained", farmLevel, "food. Total food:", foodStock)
def upgradeShelter():
    global shelterLevel, shelterHealth, shelterUpgrade
    if shelterUpgrade:
        shelterLevel += 1
        shelterHealth = shelterLevel * 10
        shelterUpgrade = False

def upgradeFarm():
    global farmLevel, farmUpgrade
    if farmUpgrade:
        farmLevel += 1
        farmUpgrade = False

def eat():
    if health < 100 and hunger <  5:
       eating = input("Would you like to eat to restore hunger? yes/no: ")
       if eating == yes:
        foodStock -= 1
        hunger += 1
#defining sleeping to restore energy and health if hunger is a a certain point
def sleeping():
    global day, health, hunger
    sleep = input("Do you want to sleep? (yes/no): ").lower()
    if sleep == "yes" or sleep == "no":
        day += 1
        hunger -= 2
        if hunger >= 9 and health < 100:
            health += 5
        elif 7 <= hunger <= 8:
            health += 4
        elif 5 <= hunger <= 6:
            health += 3

    healthCheck()
    hungerCheck()
    upgradeFarm()
    upgradeShelter()
    typeText(f"Your health is {health}", 0.05, 0.02)
    typeText(f"Your hunger is {hunger}", 0.05, 0.02)
    typeText(f"Your food storage is {foodStock}", 0.05, 0.02)
    typeText(f"shelter health is at {shelterHealth}", 0.05, 0.02)
#creating the statment starving if hunger is below a certain point start to lose health
def starving():
    if hunger < 5:
        health = health - 5

def RandomEvents():
    global health, hunger, foodStock, shelterHealth
    eventChance = random.randint(1, 6)
    if eventChance == 1:
        typeText(f"A random fariy has summoned upon your farm and given you 5 extra pieces of food!!!", 0.05, 0.02)
        foodStock = foodStock + 5
        typeText(f"food storage is now {foodStock}", 0.05, 0.02)
    elif eventChance == 2:
        typeText(f"a fariry has summoned upon you and restored some health", 0.05, 0.02)
        health = health + 5
        typeText(f"Your health is now {health}", 0.05, 0.02)
    elif eventChance == 3:
        typeText(f"Flooding has oocured, your crops are now ruined", 0.05, 0.02)
        foodStock = foodStock - 5
        typeText(f"food storage is now {foodStock}", 0.05, 0.02)
    elif eventChance == 4:
        typeText(f"A tree branch came out of no where and now your are injured", 0.05, 0.02)
        health = health - 5
        typeText(f"Your health is now {health}", 0.05, 0.02)
    elif eventChance == 5:
        typeText(f"A storm has hit and now your shelter is damaged", 0.05, 0.02)
        shelterHealth = shelterHealth - 5
        typeText(f"Your shelter health is now {shelterHealth}", 0.05, 0.02)
    else:
        typeText(f"Nothing interesting has happend", 0.05, 0.02)
    shelterHealthCheck()
    foodStorageCheck()
    
name = input("What is your name?: ")
typeText(f"Welcome {name}", 0.05, 0.02)
time.sleep(1)
typeText(f"Day {day}", 0.05, 0.02)
skipStory = input("Would you like to skip the story yes or no: ")
if skipStory == "no":
    typeText(f"I was on the cruise ship, coming home from vacation. Everything felt perfect as we sailed across the calm ocean. Then, late at night, the ship shook violently. A loud CRASH echoed through the halls. Rushing to jump of the ship I looked back, the cruise ship had almost sunk completely. Everyone else… was gone. After hours drifting, I finally washed up on a small, deserted island. I’m alone, surrounded by trees and the sound of the ocean. I have no idea how long I’ll survive here…", 0.05, 0.02)
    input("Type next to start: ")
else:
    typeText(f"Skipping story", 0.05, 0.02)
day = day + 1

    
#game start checking to see if player is alive

while alive:
    healthCheck()
    hungerCheck()
    
    typeText(f"Day {day}", 0.05, 0.02)
    typeText(f"Your health is at {health}", 0.05, 0.02)
    typeText(f"Your hunger is at {hunger}", 0.05, 0.02)
    typeText(f"Your food storage is at {foodStock}", 0.05, 0.02)
    typeText(f"Your shelter health is at {shelterHealth}", 0.05, 0.02)
    
    if day == 1:
        healthCheck()
        hungerCheck()
        typeText("To survive on the island I should explore, start a farm, and build shelter.", 0.05, 0.02)
        action = input("What should I do? (explore/farm/shelter): ").lower()
        
        if action == "explore":
            typeText("You find a cave...... but something seems off, your hear a voice, Your are not ready yet. You decide to head home", 0.05, 0.02)
            exploreDone = True
        elif action == "farm":
            typeText("You start a small farm.", 0.05, 0.02)
            farmDone = True
            farmLevel = 1
        elif action == "shelter":
            typeText("You build a simple shelter to stay safe from the weather.", 0.05, 0.02)
            shelterUpgrade = True
            selterDone = True
        
        if exploreDone == True:
            typeText("Now I just need to start a farm, and build shelter.", 0.05, 0.02)
            action = input("What should I do next? (farm/shelter): ").lower()
            if action == "farm":
                typeText("You start a small farm.", 0.05, 0.02)
                farmDone = True
                farmLevel = 1
            elif action == "shelter":
                typeText("You build a simple shelter to stay safe from the weather.", 0.05, 0.02)
                shelterUpgrade = True
                shelterDone = True
        elif farmDone == True:
            typeText("Now I just need to explore, and build shelter.", 0.05, 0.02)
            action = input("What should I do next? (explore/shelter): ").lower()
            if action == "explore":
                typeText("You find a cave...... but something seems off, your hear a voice, Your are not ready yet. You decide to head home", 0.05, 0.02)
                exploreDone = True
            elif action == "shelter":
                typeText("You build a simple shelter to stay safe from the weather.", 0.05, 0.02)
                shelterUpgrade = True
                ShelterDone = True
        elif shelterDone == True:
            typeText("Now I just need to explore, and build a farm.", 0.05, 0.02)
            action = input("What should I do next? (explore/farm): ").lower()
            if action == "explore":
                typeText("You find a cave...... but something seems off, your hear a voice, Your are not ready yet. You decide to head home", 0.05, 0.02)
                exploreDone = True
            elif action == "farm":
                typeText("You start a small farm.", 0.05, 0.02)
                farmLevel = 1
                farmDone = True
        if exploreDone == True and farmDone == True:
            typeText("Now I just need to build shelter.", 0.05, 0.02)
            typeText("You build a simple shelter to stay safe from the weather.", 0.05, 0.02)
            shelterUpgrade = True
            shelterDone = True
        elif farmDone == True and shelterDone == True:
            typeText("Now I just need to explore.", 0.05, 0.02)
            typeText("You find a cave...... but something seems off, your hear a voice, Your are not ready yet. You decide to head home", 0.05, 0.02)
            exploreDone = True
        elif shelterDone == True and exploreDone:
            typeText("Now I just need to build a farm.", 0.05, 0.02)
            typeText("You start a small farm.", 0.05, 0.02)
            farmLevel = 1
            farmDone = True
        typeText("Made greate progress today, time to head to bed!", 0.05, 0.02)   
    sleeping()
    wakeUp = input("Time to wake up? yes/no: ")
    if wakeUp == "yes":
        typeText(f"Day {day}", 0.05, 0.02)
    else:
        typeText("Too Bad!", 0.05, 0.02)   
    
    
    if day == 2:
        healthCheck()
        hungerCheck()
        typeText("Now with a farm I can start gaining food!", 0.05, 0.02)
        farmingAction()
        RandomEvents()
        typeText("Still have some time maybe I should go back to the cave I found yesterday", 0.05, 0.02)
        typeText("After walking into the cave you run into a wolf. The wolf pounces on you taking away 15 health from you", 0.05, 0.02)
        health -= 15
        typeText(f"Your health is now at {health} after the wolf attack", 0.05, 0.02)
        typeText("Luckily he runs out of the cave.", 0.05, 0.02)
        time.sleep(1)
        typeText("After going deeper in the cave you find a chest. When you open the chest you find an axe, a picaxe, and a workbench", 0.05, 0.02)
        time.sleep(1)
        typeText("These should be usful to upgrade my farm, and my shelter, better keep that in mind", 0.05, 0.02)
        typeText("That should be enough for today, time to hit the hay", 0.05, 0.02)
        sleeping()
    
    if day == 3:
        healthCheck()
        hungerCheck()
        eat()
    break