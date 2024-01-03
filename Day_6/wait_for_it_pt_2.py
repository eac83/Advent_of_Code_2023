"""
Advent of Code 2023 Day 6: Wait For It Part 2
"""
import re
from functools import reduce


def get_distance_made(time_held: int, total_time: int):
    return time_held * (total_time - time_held)


with open("data.txt", "r") as file:
    races = file.read().splitlines()

time = int(re.sub(" +", "", races[0]).split(":")[1])
distance = int(re.sub(" +", "", races[1]).split(":")[1])


distances_made = [
    get_distance_made(time_held, time) for time_held in range(0, time + 1)
]
num_possible = [
    len([distance_made for distance_made in distances_made if distance_made > distance])
]
# print("-" * 20)
# print(f"Distances: {distances_made}")
# print(f"Possible: {num_possible[-1]}")

print(f"Total: {reduce(lambda x, y: x*y, num_possible)}")
