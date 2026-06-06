class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.ranks = []
        self.suits = []
        for card in cards:
            if len(card) == 2:
                rank = card[0]
            else:
                rank = card[0:2]
            suit = card[-1]
        
            if   rank == "A" : rank = 14
            elif rank == "K" : rank = 13
            elif rank == "Q" : rank = 12
            elif rank == "J" : rank = 11
            
            self.ranks.append(int(rank))
            self.suits.append(suit)
    
    def getSuits(self):
        return self.suits

    def getRanks(self):
        return self.ranks
        


def flush(hand):
    suits = hand.suits
    if suits.count(suits[0])==5:
        return True
    return False
    
def straight(hand):
    ranks = hand.ranks
    if sorted(ranks) == list(range(min(ranks), min(ranks)+5)):
        return True
    return False

def royalFlush(hand):
    ranks = hand.ranks
    if flush(hand) and (sorted(ranks) == [10, 11, 12, 13, 14]):
        return True
    return False

def straightFlush(hand):
    ranks = hand.ranks
    if flush(hand) and straight(hand):
        return True
    return False

def fourOfAKind(hand):
    ranks = hand.ranks
    for rank in ranks:
        if ranks.count(rank) == 4:
            return True
    return False
    
def fullHouse(hand):
    ranks = hand.ranks
    hasThree = False
    hasTwo = False
    for rank in ranks:
        if ranks.count(rank) == 3:
            hasThree = True
        elif ranks.count(rank) == 2:
            hasTwo = True
    return hasThree and hasTwo

def twoPair(hand):
    ranks = hand.ranks
    pairs = len(set(r for r in ranks if ranks.count(r) == 2))
    return pairs == 2

def onePair(hand):
    ranks = hand.ranks
    for rank in ranks:
        if ranks.count(rank) == 2:
            return True
    return False

def highCard(hand):
    return max(hand.ranks)

pokerHandRanks = {
    "Royal Flush": 10,
    "Straight Flush": 9,
    "Four of a Kind": 8,
    "Full House": 7,
    "Flush": 6,
    "Straight": 5,
    "Three of a Kind": 4,
    "Two Pair": 3,
    "One Pair": 2,
    "High Card": 1
}

def findPokerHand(hand):
    h = Hand(hand)
    if royalFlush(h):    return "Royal Flush"
    if straightFlush(h): return "Straight Flush"
    if fourOfAKind(h):   return "Four of a Kind"
    if fullHouse(h):     return "Full House"
    if flush(h):         return "Flush"
    if straight(h):      return "Straight"
    if any(h.ranks.count(r) == 3 for r in h.ranks): return "Three of a Kind"
    if twoPair(h):       return "Two Pair"
    if onePair(h):       return "One Pair"
    return f"High Card"

if __name__ == "__main__":
    suits = ['H', 'D', 'C', 'S']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cards = [r + s for s in suits for r in ranks]

    print(findPokerHand(["AH", "KH", "QH", "JH", "10H"]))   # Royal Flush
    print(findPokerHand(["QC", "JC", "10C", "9C", "8C"]))   # Straight Flush
    print(findPokerHand(["5C", "5S", "5H", "5D", "QH"]))    # Four of a Kind
    print(findPokerHand(["2H", "2D", "2S", "10H", "10C"]))  # Full House
    print(findPokerHand(["2D", "KD", "7D", "6D", "5D"]))    # Flush
    print(findPokerHand(["9H", "8D", "7C", "6S", "5H"]))    # Straight
    print(findPokerHand(["3H", "3D", "3C", "KS", "7H"]))    # Three of a Kind
    print(findPokerHand(["4H", "4D", "9C", "9S", "KH"]))    # Two Pair
    print(findPokerHand(["6H", "6D", "2C", "8S", "KH"]))    # One Pair
    print(findPokerHand(["2H", "5D", "7C", "9S", "KH"]))    # High Card
