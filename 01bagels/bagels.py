import random

stillPlaying = True
numSize = 3
guess = []

#Generate <numSize> random numbers range 0-9, returns as String
def generateNum(numSize):
    num = ''
    for i in range(numSize):
        num+= str(random.randrange(0, 10))
    return num

#Prompt player to enter guess, returns guess
def getGuess():
    guess = input("Enter your guess: ")
    return guess

#Check player guess with answer
#Add Pico to list if one digit correct in wrong spot
#Add Fermi to list if digit correct in right spot
#Add Bagels if loop ends and list is still empty (no right numbers)
def compare(num, guess, numSize):
    result = []
    for i in range(numSize):
        if(num[i] == guess[i]):
            result.append("Pico")
        elif(num[i] in guess):
            result.append("Fermi")
    if(not result):
        result.append("Bagels")
    random.shuffle(result)
    return result

#Get user input for repeating game
def playAgain():
    playingAgain = input("Play again? (y/n)")
    if(playingAgain == 'y'):
        return True
    return False

print("When I say:      That means:")
print("Pico      One digit is correct but in the wrong position")
print("Fermi     One digit is correct and in the right position")
print("Bagels    No digit is correct")
    
#Main playing loop
while(stillPlaying):
    num = generateNum(numSize)
    print("I have thought of a number")
    while(num != guess):
        guess = getGuess()
        result = compare(num, guess, numSize)
        print(result)

    stillPlaying = playAgain()
