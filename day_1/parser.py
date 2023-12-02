import re

if __name__ == '__main__':
    sum_1 = 0
    sum_2 = 0

    with open('input.txt', 'r') as f:
        for line in f:
            sum_1 += part_1(line.strip()) 
            sum_2 += part_2(line.strip())

def part_1(str):
    # Get numbers from string
    num_arr = re.findall(r'\d', str)
    return int(num_arr[0] + num_arr[len(num_arr) - 1])

def part_2(str):
    str_to_num = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    num_arr = []
    start, end = 0, 0
    while end < len(str):
        # if substring has digit 
        if str[end].isdigit():
            num_arr.append(str[end])
            # note: don't do end + 1 in case the string is part of another numerical string
            # Ex. 6czklmzsmxgmktzxmxsixmnlfxonetwonesgj
            start = end
        # else check if substring has it spelt out
        else: 
            for str_num in str_to_num.keys():
                # if substring contains number string in dictionary
                if str_num in str[start:end+1]:
                    num_arr.append(str_to_num[str_num])
                    start = end
        end += 1
    return int(num_arr[0] + num_arr[len(num_arr) - 1])
