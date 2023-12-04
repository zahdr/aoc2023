import re

with open("input.txt") as file:
    grid = file.read().splitlines()

res = 0

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "*":
            cs = set()
            for cr in [r-1, r, r+1]:
                for cc in [c-1, c, c+1]:
                    if cr < 0 or cr >= len(grid) or cc < 0 or cc >= len(grid[cr]) or not grid[cr][cc].isdigit():
                        continue
                    while cc > 0 and grid[cr][cc-1].isdigit():
                        cc -= 1
                    cs.add((cr, cc))

            if len(cs) != 2:
                continue

            numbers = []

            for cr, cc in cs:
                current_number = ""
                while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                    current_number += grid[cr][cc]
                    cc += 1
                numbers.append(int(current_number))
            
            res += numbers[0] * numbers[1]

print(res)
