def classify(hand):
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

def strength(hand):
    return classify(hand),  [card_map.get(card, card) for card in hand]

hands = [line.split() for line in open("input.txt").readlines()]

card_map = {
    "T": "A",
    "J": "B",
    "Q": "C",
    "K": "D",
    "A": "E",
}

hands.sort(key=lambda x: strength(x[0]))

total = 0

for rank, (play, bid)in enumerate(hands, 1):
    total += int(bid) * rank
    
print(total)