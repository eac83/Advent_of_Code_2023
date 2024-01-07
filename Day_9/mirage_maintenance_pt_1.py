"""
Advent of Code Day 9: Mirage Maintenance Part 1
"""

with open("data.txt", "r") as file:
    lines = file.read().splitlines()

next_values = []
for i, line in enumerate(lines):
    print(f"{i}: {line}")
    differences = [[int(value) for value in line.split(" ")]]
    while not all(value == 0 for value in differences[-1]):
        differences.append(
            [a - b for a, b in zip(differences[-1][1:], differences[-1][:-1])]
        )
    next_values.append(sum([row[-1] for row in differences]))
    print(next_values)
print(sum(next_values))
