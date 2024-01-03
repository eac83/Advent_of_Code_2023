"""
Advent of Code Day 8: Haunted Wasteland part 1
"""

with open("data.txt", "r") as file:
    document = file.read().splitlines()
print(document)
instructions = document[0]
print(instructions)
nodes = [line.split(" ")[0] for line in document[2:-1]]
print(nodes)
left_nodes = [line.split(" ")[2][1:-1] for line in document[2:-1]]
right_nodes = [line.split(" ")[3][:-1] for line in document[2:-1]]

left_path = dict(zip(nodes, left_nodes))
right_path = dict(zip(nodes, right_nodes))

current_node = "AAA"
i = 0

while current_node != "ZZZ":
    print(current_node)
    instruction = instructions[i % len(instructions)]
    print(instruction)
    if instruction == "L":
        current_node = left_path[current_node]
    elif instruction == "R":
        current_node = right_path[current_node]
    else:
        print("Panic")
    i += 1
print(i)
