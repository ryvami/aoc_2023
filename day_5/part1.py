seeds, *blocks = open("example.txt").read().split("\n\n")

seeds = list(map(int, seeds.split(":")[1].split()))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    for x in seeds:
        for a, b, c in ranges:
            # check if there is a seed within one of the ranges
            if x in range(b, b + c):
                # x is within the range of b + c
                # need to find the corresponding destination
                # we do this by calculating the offset (x - b)
                # add the offset to the start of the range for the destination
                new.append(x - b + a)
                # we found a seed within a range, so we can go to the next seeds
                break
        else:
            # if there is no seed within a range, the seed must not be in the defined ranges
            # Therefore, the seed will just be mapped to the same value
            new.append(x)
    seeds = new

        
        