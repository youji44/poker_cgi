#!D:/python39/python.exe
# Importing the 'cgi' module
import cgi

print("Content-type: text/html\r\n\r\n")
print("<html><body>")
print('<div class="container"><br/><br/>')

# Helper method
def convert_cardvalue(cards):
    card_values = []
    for card in cards:
        value = card[0]
        if value == 't':
            value = 10
        elif value == 'j':
            value = 11
        elif value == 'q':
            value = 12
        elif value == 'k':
            value = 13
        elif value == 'a':
            value = 14
        card_values.append(int(value))
    return card_values

# ex: 2h 3h 4h 5h 6h
def isStraightFlush(cards):
    if isStraight(cards) and isFlush(cards):
        return True
    return False

# ex: 2h 2d 2s 2c 6h
def isFourOfAKind(cards):
    card_values = convert_cardvalue(cards)
    for i in range(5):
        if card_values.count(card_values[i]) == 4:
            return True
    return False

# ex: 2h 2d 2s 3h 3d
def isFullHouse(cards):
    card_values = convert_cardvalue(cards)
    three = False
    for i in range(5):
        tmp = card_values[i]
        if card_values.count(tmp) == 3:
            card_values.remove(tmp)
            card_values.remove(tmp)
            card_values.remove(tmp)
            three = True
            break

    for i in range(len(card_values)):
        if card_values.count(card_values[i]) == 2 and three:
            return True
    return False

# ex: 2h 3h 5h 7h 9h
def isFlush(cards):
    card_suits = [0,0,0,0]
    for card in cards:
        if card[1] == 'h':
            card_suits[0] += 1
        if card[1] == 'd':
            card_suits[1] += 1
        if card[1] == 's':
            card_suits[2] += 1
        if card[1] == 'c':
            card_suits[3] += 1

    if any(i >= 5 for i in card_suits):
        return True
    else:
        return False

# ex: 2h 3h 4h 5h 6d
def isStraight(cards):

    card_values = convert_cardvalue(cards)
    if 14 in card_values:
        card_values.append(1)
    card_values = list(set(card_values))
    card_values.sort(reverse=True)

    if len(card_values) > 4:
        for i in range(len(card_values)-4):
            if card_values[i] - 1 == card_values[i+1] and card_values[i+1] - 1 == card_values[i+2] and card_values[i+2] - 1 == card_values[i+3] and card_values[i+3] - 1 == card_values[i+4]:
                return True

    return False

# ex: 2h 2d 2s 3h 7h
def isThreeOfAKind(cards):
    card_values = convert_cardvalue(cards)
    for i in range(5):
        if card_values.count(card_values[i]) == 3:
            return True
    return False

# ex: 2h 2d 3s 3h 7h
def isTwoPair(cards):

    card_values = convert_cardvalue(cards)
    two = False
    for i in range(5):
        tmp =  card_values[i]
        if card_values.count(tmp) == 2:
            card_values.remove(tmp)
            card_values.remove(tmp)
            two = True
            break

    for k in range(3):
        if card_values.count(card_values[k]) == 2 and two:
            return True

    return False

# ex: 2h 2d 3s 4h 7h
def isOnePair(cards):
    card_values = convert_cardvalue(cards)
    for i in range(5):
        if card_values.count(card_values[i]) == 2:
            return True
    return False

# others
def isHighCard(cards):
    card_values = convert_cardvalue(cards)
    card_values.sort(reverse=True)
    return card_values

# get result method
def findCategory(deck):
    cards = [value for value in deck]

    if isStraightFlush(cards):
        return "SF"
    elif isFourOfAKind(cards):
        return "4K"
    elif isFullHouse(cards):
        return "FH"
    elif isFlush(cards):
        return "FL"
    elif isStraight(cards):
        return "ST"
    elif isThreeOfAKind(cards):
        return "3K"
    elif isTwoPair(cards):
        return "2P"
    elif isOnePair(cards):
        return "1P"
    elif isHighCard(cards):
        return "HC"

form = cgi.FieldStorage()
msg = {}
msg['SF'] = "Straight Flush"
msg['4K'] = "Four Of A Kind"
msg['FH'] = "Full House"
msg['FL'] = "Flush"
msg['ST'] = "Straight"
msg['3K'] = "Three Of A Kind"
msg['2P'] = "Two Pair"
msg['1P'] = "One Pair"
msg['HC'] = "High Card"

if form.getvalue("cards"):
    deck = form.getvalue("cards")
    if len(deck) == 5:
        res = findCategory(deck)
        print('<center><h1>Your Poker Hand represents a', msg[res].upper(),'!</h1><br/></center>')
    else:
        print('<center><h1>You should choose Five cards</h1><br/></center>')
else:
    print('<center><h1>You should choose Five cards</h1><br/></center>')

print('<center><a class="btn" href = "index.html" style="background-color: #127515; cursor: pointer;border: none;color: white;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;">Poker Hand Again</a></center>')
print('</div>')
