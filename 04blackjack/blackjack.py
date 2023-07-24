import random, sys, time

HEARTS   = chr(9829)
DIAMONDS = chr(9830)
SPADES   = chr(9824)
CLUBS    = chr(9827)

def getDeck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Add the numbered cards.
    for rank in ('J', 'Q', 'K', 'A'):
        deck.append((rank, suit))  # Add the face and ace cards.
    random.shuffle(deck)
    return deck

def getBet(money):
    while True:
        bet = input('How much would you like to bet? (Money: {} or "(Q)UIT")'.format(money)).upper().strip()
        if(bet == 'Q'):
            print("Thanks for playing")
            sys.exit()

        if(int(bet) > money):
            print('You do not have enough money to bet that much')
            continue

        return int(bet)


def showHands(player_hand, dealer_hand, showDealerHand):
    #if(showDealerHand):
    print(dealer_hand)
    print('Value: {}'.format(getHandValue(dealer_hand)))
    print(player_hand)
    print('Value: {}'.format(getHandValue(player_hand)))
    

def getAction(hand):
    while True:
        actions = ['(H)it', '(S)tand']
        if(len(hand) == 2 and money >= bet*2):
            actions.append('(D)ouble Down')
        action = input('Select an action: {}'.format(actions))
        if(action.upper() == 'H' or action.upper() == 'S'):
            return action
        if(action.upper() == 'D' and len(actions) > 2):
            return action
        print("Invalid entry, try again")
    
def getHandValue(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card[0]
        if(rank == 'J' or rank =='Q' or rank =='K'):
            value += 10
            continue
        elif(rank == 'A'):
            num_aces += 1
            continue
        value += int(rank)
    for ace in range(num_aces):
        value += 1
    if(value + 10 <= 21 and num_aces > 0):
        value += 10

    return value

money = 5000

while True:
    #Create deck of cards fresh each hand.  Get initial bet if enough money before cards are dealt.   Deal cards
    deck = getDeck()
    if(money <= 0):
        print("You've run out of money")
        sys.exit()
    bet = getBet(money)
    dealer_hand = [deck.pop(), deck.pop()]
    player_hand = [deck.pop(), deck.pop()]

    while True:
        #Show cards.  Get bet.  Get action from player and do action.  Repeat until stand or bust
        showHands(player_hand, dealer_hand, False)
        if(getHandValue(player_hand) > 21):
            print("You busted!")
            break
        action = getAction(player_hand)
        if(action == 'H'):
            card = deck.pop()
            print('You drew a {} of {}'.format(card[0], card[1]))
            player_hand.append(card)
        elif(action == 'S'):
            break
        else:
            bet *= 2
            card = deck.pop()
            print('You drew a {} of {}'.format(card[0], card[1]))
            player_hand.append(card)
            break

    player_value = getHandValue(player_hand)
    dealer_value = getHandValue(dealer_hand)
    if(player_value <= 21):
        while(dealer_value < 17):
            print("The Dealer hits")
            time.sleep(0.5)
            dealer_hand.append(deck.pop())
            dealer_value = getHandValue(dealer_hand)
            showHands(player_hand, dealer_hand, True)

    if(dealer_value > 21):
        print("Dealer bust, you win!")
        money += bet
    elif(player_value > 21 or player_value < dealer_value):
        print("You lose")
        money -= bet
    elif(player_value > dealer_value):
        print("You won!")
        money += bet
    elif(player_value == dealer_value):
        print("It's a tie")
