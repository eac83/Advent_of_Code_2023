from collections import Counter

with open("data.txt") as file:
    input = file.read().splitlines()

hands = [line.split(" ")[0] for line in input]
bids = [line.split(" ")[1] for line in input]
hand_bids = dict(zip(hands, bids))
card_strength_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
hands_no_J = [hand.replace("J", "") for hand in hands]
hand_mode_count = [
    hand.count(max(Counter(hand), key=Counter(hand).get)) if len(hand) > 0 else 0
    for hand in hands_no_J
]
hand_unique_count = [len(set(hand)) for hand in hands_no_J]
# print(hand_mode_count)
# print(hand_unique_count)

hand_list = []
for i, (hand, mode_count, unique_count) in enumerate(
    zip(hands, hand_mode_count, hand_unique_count)
):
    print(f"-" * 20)
    print(f"Hand {i}: {hand}")
    if "J" in hand:
        print("Hand has Joker(s)!")
        print(f"Number of Jokers: {hand.count('J')}")
        print(f"Number of most common card w/o Jokers: {mode_count}")
        print(f"Number of unique cards w/o Jokers: {unique_count}")
        mode_count += hand.count("J")
        unique_count = max(unique_count, 1)
    print(f"Number of most common card: {mode_count}")
    print(f"Number of unique cards: {unique_count}")
    if mode_count >= 4:  # four or five of a kind
        hand_list.append(str(mode_count + 3) + hand)
    elif mode_count == 3:
        if unique_count == 2:  # full house
            hand_list.append("6" + hand)
        else:  # three of a kind
            hand_list.append("5" + hand)
    elif unique_count == 3:  # two pairs
        hand_list.append("4" + hand)
    else:
        hand_list.append(str(mode_count + 1) + hand)
    print(f"Assigned to: {hand_list[-1]}")
print(hand_list)
print("-" * 20)
print("Sorting hands:")
sorted_hands = sorted(
    hand_list, key=lambda hand: [card_strength_order.index(card) for card in hand]
)
print(sorted_hands)
print("Calculating final score:")
total_scores = [
    int(hand_bids[hand[1:]]) * (i + 1) for i, hand in enumerate(sorted_hands)
]
print(sum(total_scores))
