# got stuck so had to look up answer...
# Solution: https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day05p1.py
seeds, *blocks = open("input.txt").read().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))
for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    for x in seeds:
        for a, b, c in ranges:
            # if it is in one of the ranges given in the input
            if x in range(b, b + c):
                # (x - b) the offset for the matching number
                # (x - b) + a is the new destination
                new.append(x - b + a)
                break
        else:
            new.append(x)
    seeds = new
print(min(seeds))

