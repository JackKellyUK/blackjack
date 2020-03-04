import random
#File Name: blackjack.py
#Author: Jack Kelly

def calculateTotal(index,array):
    total = 0
    aces = array.count(1)

    for i in range (0,index + 1):
        total = total + min(array[i],10)

    for i in range (0,(aces - 1)):
        if(total + 10 <= 21):
            total = total + 10

    return total

def calculateDealer(index,array):
    total = calculateTotal(index,array)

    while (not(total > 21) and total < 17 and index < 5):
        index = index + 1
        total = calculateTotal(index,array)
    
    return total

def playerHit(index,array):
    index = index + 1
    print("Your cards are:",str(array[0:index + 1])[1:-1])

    if (calculateTotal(index,array) > 21 or index > 5):
        result = "stick"
    else:
        result = input("Would you like to stick or twist? ")

    while (result != "stick" and result != "twist"):
        result = input("Please enter stick or twist! ")

    if(result == "stick"):
        dealerTotal = calculateDealer(index,array)
        playerTotal = calculateTotal(index,array)

        if(dealerTotal == playerTotal or (playerTotal > 21 and dealerTotal > 21)):
            print("You drew!")
            print ("Player Total:",playerTotal)
            print("Dealer total:",dealerTotal)
        elif((dealerTotal > 21 and playerTotal <= 21) or (playerTotal <= 21 and playerTotal > dealerTotal) or (playerTotal == 21 and dealerTotal != 21)):
            print("You won!")
            print ("Player Total:",playerTotal)
            print("Dealer total:",dealerTotal)
        else:
            print("You lost!")
            print ("Player Total:",playerTotal)
            print("Dealer total:",dealerTotal)
    else:
        playerHit(index,array)

#--- Start of game
print("Welcome to Blackjack!")

dealerArray = []
for i in range(0,5):
    dealerArray.append(random.randint(1,13))

playerArray = []
for i in range(0,5):
    playerArray.append(random.randint(1,13))

playerIndex = 1
dealerIndex = 1

print("Your cards are:",str(playerArray[0:playerIndex + 1])[1:-1])

result = input("Would you like to stick or twist? ")

while (result != "stick" and result != "twist"):
    result = input("Please enter stick or twist! ")

if(result == "stick"):
    dealerTotal = calculateDealer(dealerIndex,dealerArray)
    playerTotal = calculateTotal(playerIndex,playerArray)

    if(dealerTotal == playerTotal or (playerTotal > 21 and dealerTotal > 21)):
        print("You drew!")
        print ("Player Total:",playerTotal)
        print("Dealer total:",dealerTotal)
    elif(dealerTotal > 21 and playerTotal <= 21 or (playerTotal <= 21 and playerTotal > dealerTotal) or (playerTotal == 21 and dealerTotal != 21)):
        print("You won!")
        print ("Player Total:",playerTotal)
        print("Dealer total:",dealerTotal)
    else:
        print("You lost!")
        print ("Player Total:",playerTotal)
        print("Dealer total:",dealerTotal)
else:
    playerHit(playerIndex,playerArray)
