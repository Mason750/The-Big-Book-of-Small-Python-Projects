stillPlaying = True
numSize = 3

#Generate <numSize> random numbers range 0-9, returns as String
def generateNum(numSize):
    return '123'

#Prompt player to enter guess, returns guess
def getGuess():
    return '122'

#Check player guess with answer
#Add Pico to list if one digit correct in wrong spot
#Add Fermi to list if digit correct in right spot
#Add Bagels if loop ends and list is still empty (no right numbers)
def compare(num, guess):
    return ['Pico', 'Fermi']

#Get user input for repeating game
def playAgain():
    return False

#Main playing loop
while(stillPlaying):
    print("When I say:      That means:")
    print("Pico      One digit is correct but in the wrong position")
    print("Fermi     One digit is correct and in the right position")
    print("Bagels    No digit is correct")
    
    num = generateNum(numSize)
    print("I have thought of a number")

    guess = getGuess()
    
    result = compare(num, guess)
    print(result)

    stillPlaying = playAgain()
