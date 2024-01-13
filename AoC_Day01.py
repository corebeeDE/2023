import re

def get_advent_info():
    return sum( [int(''.join(map(re.findall('\d', y).__getitem__, [0, -1]))) for y in \
                [x for x in open(r'C:\Users\corebee\source\Python\AdventOfCode\input\01_input.txt', 'r')]])
# Alternative
def get_advent_info_alt(input):
    return sum([int(''.join(map(re.findall('\d', line).__getitem__, [0, -1]))) for line in input])

def read_input():
    return list([x for x in open(r'C:\Users\corebee\source\Python\AdventOfCode\2023_Day01\input.txt', 'r')])

def main():
    print(get_advent_info())
    print(get_advent_info_alt(read_input()))

if __name__ == '__main__':
    main()
