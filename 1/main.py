sum = 0

with open("input.txt") as file:
    for line in file:
        number_in_line = ""
        for character in line:
            if character.isdigit():
                number_in_line += character
        if len(number_in_line) <= 1:
            sum += int(number_in_line + number_in_line)
        else:
            sum += int(number_in_line[0] + number_in_line[-1])

print(sum)