"""
Advent of Code Day 9: Mirage Maintenance Part 2
"""

with open("data.txt", "r") as file:
    lines = file.read().splitlines()

next_values = []
for i, line in enumerate(lines):
    print(f"-"*20)
    print(f"{i}: {line}")
    differences = [[int(value) for value in line.split(" ")]]
    while not all(value == 0 for value in differences[-1]):
        differences.append(
            [a - b for a, b in zip(differences[-1][1:], differences[-1][:-1])]
        )
    differences.reverse()
    for j, (row_i, row_j) in enumerate(zip(differences[:-1], differences[1:])):
        #print(row_i)
        row_j.insert(0, row_j[0] - row_i[0])
        print(f"{j}: row_i")
    differences.reverse()
    for row in differences: print(row)
    next_values.append(differences[0][0])
    print(next_values)
print(sum(next_values))
