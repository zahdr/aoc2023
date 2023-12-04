with open("input.txt") as file:
    cards = file.read().splitlines()

res = 0

for card in cards:
    winning_numbers = card.split(":")[1].split("|")[0].strip().split(" ")
    my_numbers = card.split(":")[1].split("|")[1].strip().split(" ")
    winning_numbers = list(filter(None, winning_numbers))
    my_numbers  = list(filter(None, my_numbers))

    card_points = 0
    for number in my_numbers:
        if number in winning_numbers:
            if card_points == 0:
                card_points +=1
            else:
                card_points += card_points
    res += card_points

print(res)