"""
Advent of Code Day 7: Camel Cards part 1
"""

from collections import Counter

with open("data.txt") as file:
    input = file.read().splitlines()

hands = [line.split(" ")[0] for line in input]
bids = [line.split(" ")[1] for line in input]
hand_bids = dict(zip(hands, bids))
card_strength_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
hand_mode_count = [hand.count(max(Counter(hand), key=Counter(hand).get)) for hand in hands]
hand_unique_count = [len(set(hand)) for hand in hands]
print(hand_mode_count)
print(hand_unique_count)

hand_list = []
for hand, mode_count, unique_count in zip(hands, hand_mode_count, hand_unique_count):
    if mode_count >= 4:  # four or five of a kind
        hand_list.append(str(mode_count+3) + hand)
    elif mode_count == 3:
        if unique_count == 2: # full house
            hand_list.append("6" + hand)
        else:   # three of a kind
            hand_list.append("5" + hand)
    elif unique_count == 3: # two pairs
        hand_list.append("4" + hand)
    else:
        hand_list.append(str(mode_count+1) + hand)

print(hand_list)

sorted_hands = sorted(hand_list, key=lambda hand: [card_strength_order.index(c) for c in hand])
print(sorted_hands)

total_scores = [int(hand_bids[hand[1:]])*(i+1) for i, hand in enumerate(sorted_hands)]
print(sum(total_scores))
