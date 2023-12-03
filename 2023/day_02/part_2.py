with open("input.txt", 'r') as f:
    lines = f.readlines()

def find_maximum_cubes_of_each_colour(game_info):
    hands = [hand.strip() for hand in game_info.split(";")]
    max_colour = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for hand in hands:
        for colour_info in hand.split(","):
            colour_info = colour_info.strip()
            number, colour = tuple(colour_info.split(" "))
            max_colour[colour] = max(max_colour[colour], int(number))
    return max_colour


def parse_line(s):
    s = s.strip()
    game_number, game_info = tuple(s.split(":"))
    game_number = int(game_number.split(" ")[1])
    return game_number, find_maximum_cubes_of_each_colour(game_info)
    
NUM_COLOURS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

ID_SUM = 0
for line in lines:
    game_number, max_colours = parse_line(line)
    product = 1
    for colour in max_colours.keys():
        product *= max_colours[colour]
    ID_SUM += product
    
print(ID_SUM)