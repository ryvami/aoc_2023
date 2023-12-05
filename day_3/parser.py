def construct_number(string, xpos):
    ret = ""
    if string[xpos - 1].isdigit():
        while xpos > 0 and string[xpos - 1].isdigit():
           xpos -= 1
    if string[xpos + 1].isdigit():
        while xpos < len(string) and string[xpos].isdigit():
           ret = ret + string[xpos] 
           string[xpos] = "x"
           xpos += 1
    elif string[xpos].isdigit():
        ret = string[xpos]
    return int(ret)

def multiply():
    mul_count = 0
    
    def operate(x, y):
        nonlocal mul_count
        if x == 0:
            return y * 1
        mul_count += 1
        return x * y

    def count():
        return count
    
    return operate, count


def surround_total(arr, row, col, operation):
    if operation == "add":
        operation = lambda x, y: x + y
        count = None
    elif operation == "multiply":
        operation, count = multiply()
    total = 0
    # Define the relative positions to check around (row, col)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        # Check if new_row and new_col are within bounds and if the element is a digit
        if 0 <= new_row < len(arr) and 0 <= new_col < len(arr[new_row]) and arr[new_row][new_col].isdigit():
            total = operation(total, construct_number(arr[new_row], new_col))
    if count is not None and count == 1:
        return 0
    return total



def part_1(array):
    total_sum = 0
    for i, code in enumerate(array):
        for j, char in enumerate(code):
            if not char.isdigit() and not char == ".":
                total_sum += surround_total(array, i, j, "add") 
    return total_sum

def part_2(array):
    total = 0
    for i, code in enumerate(array):
        for j, char in enumerate(code):
            if char == "*":
                total += surround_total(array, i, j, "multiply")
    return total

if __name__ == "__main__":
    array = []
    with open("/home/skyler/projects/aoc_2023/day_3/input.txt", "r") as f:
        for line in f:
            array.append(list(line.strip()))
        # print(part_1(array))
        print(part_2(array))