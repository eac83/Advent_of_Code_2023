"""
Solution for Advent of Code 2023 Day 4: Scratch Cards Part 1
"""
import re
import math

with open("data.txt", "r") as data:
    scratch_cards = [line[:-1] for line in data]

ids = []
all_winning_numbers = []
all_owned_numbers = []
for line in scratch_cards:
    line = re.sub(" +", " ", line)
    line_header, line_card = line.split(": ")
    _, card_id = line_header.split(" ")
    winning_numbers, owned_numbers = line_card.split(" | ")
    ids.append(int(card_id))
    all_winning_numbers.append(winning_numbers)
    all_owned_numbers.append(owned_numbers)

print(ids)
print(all_winning_numbers)
print(all_owned_numbers)
card_winning_numbers = dict(zip(ids, all_winning_numbers))
card_owned_numbers = dict(zip(ids, all_owned_numbers))

print(card_winning_numbers)
print(card_owned_numbers)

scores = []
for card in card_winning_numbers:
    card_winning_numbers[card] = card_winning_numbers[card].lstrip().replace("  ", " ")
    card_owned_numbers[card] = card_owned_numbers[card].lstrip().replace("  ", " ")
    winning_numbers = [int(num) for num in card_winning_numbers[card].split(" ")]
    owned_numbers = [int(num) for num in card_owned_numbers[card].split(" ")]
    print("-" * 10)
    print(f"Card {card}")
    print(f"Winning numbers {winning_numbers}")
    print(f"Owned numbers {owned_numbers}")

    matching_numbers = [num for num in winning_numbers if num in owned_numbers]
    card_score = math.floor(2 ** (len(matching_numbers) - 1))
    scores.append(card_score)
    print(f"Matching numbers {matching_numbers}")
    print(f"Card score {card_score}")
    print(f"Running total {sum(scores)}")
