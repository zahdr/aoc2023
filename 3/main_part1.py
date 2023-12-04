import re

with open("input.txt") as file:
    grid = file.read().splitlines()

res = []
cs = set()
special_characters = ["+", "*", "=", "%", "@", "#", "&", "/", "-", "$"]


for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch in special_characters:
            for cr in [r-1, r, r+1]:
                for cc in [c-1, c, c+1]:
                    if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and grid[cr][cc-1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))

for r, c in cs:
    current_number = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        current_number += grid[r][c]
        c += 1
    res.append(int(current_number))

print(sum(res))