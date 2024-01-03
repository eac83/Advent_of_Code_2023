"""
Advent of Code 2023 Day 6: Wait For It Part 1
"""
import re
from functools import reduce


def distance_made(time_held: int, total_time: int):
    return time_held * (total_time - time_held)


with open("data.txt", "r") as file:
    races = file.read().splitlines()

times = [int(time) for time in re.sub(" +", " ", races[0]).split(" ")[1:]]
distances = [int(distance) for distance in re.sub(" +", " ", races[1]).split(" ")[1:]]


num_possible = []
for i, time in enumerate(times):
    distances_made = [
        distance_made(time_held, time) for time_held in range(0, time + 1)
    ]
    num_possible.append(
        len([distance for distance in distances_made if distance > distances[i]])
    )
    print("-" * 20)
    print(f"Race: {i}")
    print(f"Distances: {distances_made}")
    print(f"Possible: {num_possible[-1]}")

print(f"Total: {reduce(lambda x, y: x*y, num_possible)}")
