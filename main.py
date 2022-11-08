import random
stood = False
deck = ['2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades',
        '9 of Spades', '10 of Spades', 'J of Spades', 'Q of Spades', 'K of Spades', 'A of Spades', '2 of Clubs',
        '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs',
        'J of Clubs', 'Q of Clubs', 'K of Clubs', 'A of Clubs', '2 of Hearts', '3 of Hearts', '4 of Hearts',
        '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Diamonds', '10 of Diamonds', 'J of Diamonds',
        'Q of Diamonds', 'K of Diamonds', 'A of Diamonds']
dealerHand = []
playerHand = []


def dealCard(person):
    card = random.choice(deck)
    person.append(card)
    deck.remove(card)


def calculate(person):
    sum = 0
    acecount = 0
    facecards = ['J', 'Q', 'K']
    for card in person:
        card = card[0] + card[1]
        if card[1] == '0':
            sum += 10
        else:
            card = card[0]
            if card in facecards:
                sum += 10
            elif card == 'A':
                acecount += 1
                if sum > 11 or acecount >= 2:
                    sum += 1
                else:
                    sum += 11
            else:
                sum += int(card)
    if sum > 21:
        i = 0
        while i < acecount:
            sum -= 10
            i += 1
    return sum


def displayHands():
    print("You Have:")

    for card in playerHand:
        print(card)

    print("The Dealer Has:")
    print(dealerHand[0] + " and 1 hidden card")


def play():
    while len(playerHand) < 2:
        dealCard(playerHand)
    while len(dealerHand) < 2:
        dealCard(dealerHand)
    if calculate(dealerHand) == 21:
        win("dealer", dealerHand)


def win(playername, person):
    if playername == 'dealer':
        print("The Dealer Won with: ")
        for card in person:
            print(card)
        print("Better Luck Next Time!")

    if playername == 'player':
        print("You Won with: ")
        for card in person:
            print(card)
        print("Congratulations!")

    if playername == 'tie':
        print("You Tied!")
        print("The Dealer had: ")
        for card in dealerHand:
            print(card)
    exit()


def checkWincon():
    if calculate(dealerHand) == 21 and calculate(playerHand) == 21:
        win("tie", dealerHand)
        print("You had: ")
        for card in playerHand:
            print(card)
    if calculate(dealerHand) == 21:
        win("dealer", dealerHand)
    if calculate(playerHand) > 21:
        print("You Busted!")
        win("dealer", dealerHand)
    if calculate(playerHand) == 21:
        win("player", playerHand)
    if calculate(dealerHand) > 21:
        print("The Dealer Busted!")
        win("player", playerHand)


def decision():
    choice = str(input("Would you like to Hit(1) or Stand(2)?"))
    if choice == '1':
        dealCard(playerHand)
        return True
    elif choice != '2':
        print("Invalid Input")
        return True
    else:
        return False


play()
displayHands()

print("Dealer Hand Total: At least " + str(dealerHand[0])+" but not a Blackjack!")

print("Player Hand Total: " + str(calculate(playerHand)))
checkWincon()
playerchoice = True
while playerchoice:
    playerchoice = decision()
    print("You Have:")

    for card in playerHand:
        print(card)

    print("Player Hand Total: " + str(calculate(playerHand)))

    checkWincon()
if calculate(dealerHand) < 17:
    while calculate(dealerHand) < 17:
        print("Dealer Hand Total: " + str(calculate(dealerHand)))
        dealCard(dealerHand)
        for card in dealerHand:
            print(card)
    checkWincon()
else:
    print("Dealer Hand Total: " + str(calculate(dealerHand)))
    if calculate(playerHand) == calculate(dealerHand):
        win("tie", dealerHand)
    checkWincon()
    if calculate(playerHand) > calculate(dealerHand):
        win("player", playerHand)
    elif calculate(playerHand) == calculate(dealerHand):
        win("tie", playerHand)
        for card in playerHand:
            print(card)
    else:
        win("dealer", dealerHand)
