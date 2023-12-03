import re

res = 0

with open("input.txt") as file:
    for line in file:
        game_number, game_results = re.search(r"(\d+):(.*)", line).groups()
        set_results = re.findall(r"((\d+).(red|blue|green))", game_results)
        game_valid = True
        
        for cube in set_results:
            amount, color = int(cube[1]), cube[2]

            if (color == "red" and amount > 12 or
                color == "green" and amount > 13 or
                color == "blue" and amount > 14):
                game_valid = False

        if game_valid:
            res += int(game_number)


print(res)
