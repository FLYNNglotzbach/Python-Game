#import stuff
import random
import time
import sys, time

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
ShelterHealth = shelterLevel * 10

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

#creating the action farming to gain food
def farmingAction():
    global foodStock
    farming = input("Do you want to farm? (yes/no): ").lower()
    if farming == "yes":
        foodStock += farmLevel
        print("You farmed and gained", farmLevel, "food. Total food:", foodStock)

#defining sleeping to restore energy and health if hunger is a a certain point
def sleeping():
    global day, health, hunger
    sleep = input("Do you want to sleep? (yes/no): ").lower()
    if sleep == "yes":
        day += 1
        hunger -= 2
        if hunger >= 9 and health < 100:
            health += 5
        elif 7 <= hunger <= 8:
            health += 4
        elif 5 <= hunger <= 6:
            health += 3
        elif 3 <= hunger <= 4:
            health += 2
        else:
            health += 1
    else:
        health += 1
    healthCheck()
    hungerCheck()
    typeText(f"Your health is {health}", 0.05, 0.02)
    typeText(f"Your hunger is {hunger}", 0.05, 0.02)
    typeText(f"Your food storage is {foodStock}", 0.05, 0.02)

#creating the statment starving if hunger is below a certain point start to lose health
def starving():
    if hunger <= 5:
        health = health - 5

def RandomEvents():
    global health, hunger, foodStock
    eventChance = random.randint(1, 10)
    if eventChance == 1:
        typeText(f"A random fariy has summoned upon your farm and given you 5 extra pieces of food!!!", 0.05, 0.02)
        foodStock = foodStock + 5
    elif eventChance == 2:
        typeText(f"a fariry has summoned upon you and restored some health", 0.05, 0.02)
        health = health + 5
    elif eventChance == 3:
        typeText(f"Flooding has oocured, your crops are now ruined", 0.05, 0.02)
        foodStock = foodStock - 5
    elif eventChance == 4:
        typeText(f"A tree branch came out of no where and now your are injured", 0.05, 0.02)
        health = health - 5
    elif eventChance == 5:
        typeText(f"A storm has hit and now your shelter is damaged", 0.05, 0.02)
        shelterHealth = ShelterHealth - 5
    else:
        typeText(f"Nothing interesting has happend", 0.05, 0.02)
name = input("What is your name?: ")
typeText(f"Welcome {name}", 0.05, 0.02)
time.sleep(1)
typeText(f"Day {day}", 0.05, 0.02)
skipStory = input("Would you like to skip the story yes or no: ")
if skipStory == "no":
    typeText(f"I was on the cruise ship, coming home from vacation. Everything felt perfect as we sailed across the calm ocean. Then, late at night, the ship shook violently. A loud CRASH echoed through the halls. Rushing to jump of the ship I looked back, the cruise ship had almost sunk completely. Everyone else… was gone. After hours drifting, I finally washed up on a small, deserted island. I’m alone, surrounded by trees and the sound of the ocean. I have no idea how long I’ll survive here…", 0.05, 0.02)
    input("Type next to start: ")
day = day + 1

    
#game start checking to see if player is alive

while alive:
    healthCheck()
    hungerCheck()
    
    typeText(f"Day {day}", 0.05, 0.02)
    typeText(f"Your health is at {health}", 0.05, 0.02)
    typeText(f"Your hunger is at {hunger}", 0.05, 0.02)
    typeText(f"Your food storage is at {foodStock}", 0.05, 0.02)
    typeText(f"Your shelter health is at {ShelterHealth}", 0.05, 0.02)
    
    if day == 1:
        typeText("To survive on the island I should explore, start a farm, and build shelter.", 0.05, 0.02)
        action = input("What should I do today? (explore/farm/shelter): ").lower()
        
        if action == "explore":
            typeText("You find a cave...... but something seems off, your hear a voice, Your are not ready yet. You decide to head home", 0.05, 0.02)
        elif action == "farm":
            typeText("You start a small farm.", 0.05, 0.02)
            farmLevel = farmLevel + 1
        elif action == "shelter":
            typeText("You build a simple shelter to stay safe from the weather.", 0.05, 0.02)
            shelterLevel = shelterLevel + 1
    typeText(f"I'll finish the other two later, time to sleep", 0.05, 0.02)
    sleeping()
    break