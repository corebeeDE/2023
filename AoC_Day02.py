def get_advent_info(input_dict):
    searchpattern = { 'red': 12, 'green': 13, 'blue': 14 }
    output = []
    for dict_key, dict_games in input_dict.items():
        all_conditions = True
        for game_set in dict_games:
            ind_games = game_set.split(',')
            for game in ind_games:
                value, color = game.lstrip().rstrip().split(' ')
                if int(value) > searchpattern[color]:
                    all_conditions = False
        if all_conditions:
            output.append(int(dict_key))
    return sum(output)

def prep_input(input_txt):
    output = dict()
    for line in input_txt:
        buffer = line.split(': ')
        output[str(buffer[0].split(' ')[-1])] = [x.lstrip().rstrip('\n') for x in buffer[1].split(';')]
    return output

def read_input():
    return [x for x in open(r'C:\Users\corebee\source\Python\AdventOfCode\input\02_input.txt', 'r')]

def main():
    print(get_advent_info(prep_input(read_input())))

if __name__ == '__main__':
    main()