import math
import re


def part_1(string):
    color_limit = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    line = string.split(":")
    game_number = int(re.search(r"\d+", line[0]).group(0))
    games = line[1].split(";") 
    for cubes in games:
        cube_colors = cubes.split(", ")
        for cube in cube_colors:
            number = int(re.search(r"\d+", cube).group(0))
            for color in color_limit.keys():
                if color in cube and number > color_limit[color]:
                    return 0
    return game_number

def part_2(string):
    color_maximum = {
        "red": -math.inf,
        "green": -math.inf,
        "blue": -math.inf
    }
    games = string.split(":")[1].split(";")
    for cubes in games:
        product = 1
        cube_colors = cubes.split(", ")
        for cube in cube_colors:
            number = int(re.search(r"\d+", cube).group(0))
            for color in color_maximum.keys():
                if color in cube and number >= color_maximum[color]:
                    color_maximum[color] = number
    return color_maximum["red"] * color_maximum["green"] * color_maximum["blue"]
    

if __name__ == "__main__":
    count_1 = 0
    count_2 = 0
    with open("input.txt", "r") as f:
        for line in f:
            count_1 += part_1(line.strip())
            count_2 += part_2(line.strip())

    print(count_1)
    print(count_2)

