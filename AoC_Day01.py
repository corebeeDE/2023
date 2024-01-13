###################################################################################################
#####   SHORTEST VERSION
###################################################################################################
import re

def get_advent_info():
    return sum( [int(''.join(map(re.findall('\d', y).__getitem__, [0, -1]))) for y in \
                [x for x in open(r'C:\Users\corebee\source\Python\AdventOfCode\input\01_input.txt', 'r')]])

def main():
    print(get_advent_info())

if __name__ == '__main__':
    main()

###################################################################################################
#####   SHORTER VERSION
###################################################################################################    
# import re

# def get_advent_info(input):
#     return sum([int(''.join(map(re.findall('\d', line).__getitem__, [0, -1]))) for line in input])

# def read_input():
#     return list([x for x in open(r'C:\Users\corebee\source\Python\AdventOfCode\2023_Day01\input.txt', 'r')])

# def main():
#     print(get_advent_info(read_input()))

# if __name__ == '__main__':
#     main()

###################################################################################################
#####   FIRST VERSION
###################################################################################################
# import re

# def get_advent_info(input):
#     output = []
#     for line in input:
#         buffer = []
#         for char in line:
#             if re.match('[0-9]', char):
#                 buffer.append(char)
#         output.append([buffer[0], buffer[-1]])
#     return output

# def read_input():
#     return list([x for x in open(r'C:\Users\corebee\source\Python\AdventOfCode\input\01_input.txt', 'r')])

# def main():
#     sum = get_advent_info(read_input())
#     output = 0
#     for line in sum:
#         buffer = ''
#         for value in line:
#             buffer += value
#         output += int(buffer)
#     print(output)

# if __name__ == '__main__':
#     main()