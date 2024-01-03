"""
Advent of Code Day 8: Haunted Wasteland part 
"""
from math import lcm






with open("data.txt", "r") as file:
    document = file.read().splitlines()

instructions = document[0]
nodes = [line.split(" ")[0] for line in document[2:-1]]
left_nodes = [line.split(" ")[2][1:-1] for line in document[2:-1]]
right_nodes = [line.split(" ")[3][:-1] for line in document[2:-1]]

left_path = dict(zip(nodes, left_nodes))
right_path = dict(zip(nodes, right_nodes))

start_nodes = [node for node in nodes if node[2] == "A"]
i = 0
loop_starts = []
loop_lengths = []
for j, current_node in enumerate(start_nodes):
    print("-" * 20)
    print(f"Path {j}:")
    i = 0
    end_node_count = 0
    end_node = ""
    path = [current_node]
    print(f"Starting node: {current_node}")
    while end_node_count < 2:
        instruction = instructions[i % len(instructions)]
        if instruction == "L":
            current_node = left_path[current_node]
        else:
            current_node = right_path[current_node]
        path.append(current_node)
       # print(path)
        i += 1
        if current_node[-1] == "Z":
            print(f"End node found! {current_node} at turn {i}")
            end_node = current_node
            end_node_count += 1
            print(f"End node counts: {end_node_count}")
            #print(path[0])
            if instruction == "L":
                print(f"Next node: {right_path[current_node]}")
            else:
                print(f"Next node: {left_path[current_node]}")
    loop_starts.append(path.index(end_node))
    loop_lengths.append(len(path) - path.index(end_node) - 1)
    print(f"Loop starts at: {loop_starts[-1]}")
    print(f"Loop length: {loop_lengths[-1]}")
print(loop_starts)
print(loop_lengths)

answer = 1
for loop_length in loop_lengths:
    answer = lcm(loop_length, answer)
print(f"Number of turns: {answer}")
