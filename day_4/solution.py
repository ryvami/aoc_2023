# Had to get inspiration because I was stuck...
# Thank you Flyingplatypus5
# https://www.reddit.com/r/adventofcode/comments/18actmy/comment/kbx6htf/ 

def parse_string(line: str):
    line = line.split(":")[1]
    a, b = line.split("|")
    a, b = a.split(), b.split()

    return a, b
     
if __name__ == "__main__":
    f = open("input.txt").readlines()

    total = 0
    cards = [1 for _ in f]

    for idx, line in enumerate(f):
        parse_string(line)
        a, b = parse_string(line)
        n = len(set(a) & set(b))
        if n > 0:
            total += 2 ** (n - 1)
        for i in range(n):
            num_next_cards = idx + i
            if num_next_cards < len(cards):
                cards[num_next_cards + 1] += cards[idx]

    print(total, sum(cards))
