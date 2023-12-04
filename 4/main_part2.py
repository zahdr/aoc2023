with open("input.txt") as file:
    cards = file.read().splitlines()

res = 0

card_copies = {}
for i in range(len(cards)):
    card_copies[i+1] = 1

for card in cards:
    card_number = int(card.split(":")[0].split(" ")[-1])
    winning_numbers = card.split(":")[1].split("|")[0].strip().split(" ")
    my_numbers = card.split(":")[1].split("|")[1].strip().split(" ")
    winning_numbers = list(filter(None, winning_numbers))
    my_numbers  = list(filter(None, my_numbers))

    card_points = 0
    for number in my_numbers:
        if number in winning_numbers:
            card_points +=1
    
    for i in range(card_points):
        inc_card = card_number + i + 1
        if inc_card <= len(cards):
            card_copies[inc_card] += card_copies[card_number]

    res += card_copies[card_number]

print(res)