import random
#File Name: blackjack.py
#Author: Jack Kelly
#Version: V1.11

def numberText(array):
    cardName = {1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}
    cardSuits = ["Hearts","Spades","Diamonds","Clubs"]
    newArray = []

    for i in range(0,len(array)):
        newArray.append(cardName[array[i]] + " Of " + random.choice(cardSuits))

    return newArray

def calculateTotal(index,array):
    total = 0
    aces = array.count(1)

    for i in range (0,index + 1):
        total += min(array[i],10)

    for i in range (0,(aces - 1)):
        if(total + 10 <= 21):
            total += 10

    return total

def calculateDealer(index,array):
    total = calculateTotal(index,array)

    while (not(total > 21) and total < 17 and index < 5):
        index += 1
        total = calculateTotal(index,array)
    
    return total

def printTotal(playerTotal,dealerTotal):
    print("Player Total:",playerTotal)
    print("Dealer Total:",dealerTotal)

def playerHit(index,array,text):
    index += 1
    print("Your cards are:",(', '.join(text[0:index + 1])))

    if (calculateTotal(index,array) >= 21 or index > 4):
        result = "S"
    else:
        result = input("Would you like to [H]it or [S]tand? ").upper()

    while (result != "S" and result != "H"):
        result = input("Please enter [S]tand or [H]it! ").upper()

    if(result == "S"):
        dealerTotal = calculateDealer(dealerIndex,dealerArray)
        playerTotal = calculateTotal(index,array)

        if(dealerTotal == playerTotal or (playerTotal > 21 and dealerTotal > 21)):
            print("You drew!")
            printTotal(playerTotal,dealerTotal)
        elif((dealerTotal > 21 and playerTotal <= 21) or (playerTotal <= 21 and playerTotal > dealerTotal) or (playerTotal == 21 and dealerTotal != 21)):
            print("You won!")
            printTotal(playerTotal,dealerTotal)
        else:
            print("You lost!")
            printTotal(playerTotal,dealerTotal)
    else:
        playerHit(index,array,text)

#--- Start of game
print("Welcome to Blackjack!")

dealerArray = random.sample(range(1, 13), 5)
playerArray = random.sample(range(1, 13), 5)

playerArrayText = numberText(playerArray)
dealerArrayText = numberText(dealerArray)

playerIndex = 1
dealerIndex = 1

print("Your cards are:",(', '.join(playerArrayText[0:playerIndex + 1])))
print("The dealer draws a",dealerArrayText[0])

if (calculateTotal(playerIndex,playerArray) == 21):
    result = "S"
else:
    result = input("Would you like to [H]it or [S]tand? ").upper()

while (result != "S" and result != "H"):
    result = input("Please enter [S]tand or [H]it! ").upper()

if(result == "S"):
    dealerTotal = calculateDealer(dealerIndex,dealerArray)
    playerTotal = calculateTotal(playerIndex,playerArray)

    if(dealerTotal == playerTotal or (playerTotal > 21 and dealerTotal > 21)):
        print("You drew!")
        printTotal(playerTotal,dealerTotal)
    elif(dealerTotal > 21 and playerTotal <= 21 or (playerTotal <= 21 and playerTotal > dealerTotal) or (playerTotal == 21 and dealerTotal != 21)):
        print("You won!")
        printTotal(playerTotal,dealerTotal)
    else:
        print("You lost!")
        printTotal(playerTotal,dealerTotal)
else:
    playerHit(playerIndex,playerArray,playerArrayText)
