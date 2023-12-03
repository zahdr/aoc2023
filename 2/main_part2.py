import re

res = 0

with open("input.txt") as file:
    for line in file:
        game_number, game_results = re.search(r"(\d+):(.*)", line).groups()
        set_results = re.findall(r"((\d+).(red|blue|green))", game_results)
        game_valid = True
        red = [0]
        green = [0]
        blue = [0]

        for cube in set_results:
            amount, color = int(cube[1]), cube[2]
            if color == "red":
                red.append(amount)
            elif color == "green":
                green.append(amount)
            else:
                blue.append(amount)

        res += (max(red) * max(green) * max(blue))

print(res)
