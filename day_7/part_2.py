def score(hand):
    counts = [hand.count(card) for card in hand]

    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    if 1 in counts:
        return 0

def replacements(hand):
    if hand == "":
        return [""]
    
    return [
            x + y 
            for x in ("23456789KQTA" if  hand[0] == "J" else hand[0])
            for y in replacements(hand[1:]) 
        ]
    
print(replacements("JJS"))

def classify(hand):
    return max(map(score, replacements(hand)))

def strength(hand):
    return classify(hand),  [card_map.get(card, card) for card in hand]

hands = [line.split() for line in open("input.txt").readlines()]

card_map = {
    "J": ".",
    "T": "B",
    "Q": "C",
    "K": "D",
    "A": "E",
}

hands.sort(key=lambda x: strength(x[0]))

total = 0

for rank, (play, bid)in enumerate(hands, 1):
    total += int(bid) * rank
    
print(total)