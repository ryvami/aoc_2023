time, distance = [list(map(int, line.split(":")[1].split())) for line in open("input.txt").readlines()]

p = 1

for time, distance in zip(time, distance):
    s = 0
    for x in range(time):
        if (time - x)  * x > distance:
            s += 1
    p *= s

print(p)