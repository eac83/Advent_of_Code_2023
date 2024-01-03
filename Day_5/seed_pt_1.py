"""
Advent of Code 2023 Day 5: If You Give A Seed A Fertilizer Part 1
"""


def seed_to_location(seed: int, almanac: list[str], lines: list[int]) -> int:
    """
    Maps seed number to location number.

    Keyword arguments:
        seed (int): seed number,
        almanac (list[str]): list of each line in the almanac
        lines (list[int]): list of the start of each map in the almanac.

    Returns:
        trail (int): location number.
    """
    trail = seed
    for start_line, end_line in zip(lines[:-1], lines[1:]):
        for line in almanac[start_line + 1 : end_line - 1]:
            destination, source, length = line.split(" ")
            destination, source, length = int(destination), int(source), int(length)
            if trail >= source and trail <= source + length:
                trail = destination + (trail - source)
                break
    return trail


with open("data.txt", "r") as data:
    almanac = data.read().splitlines()

seeds = [int(seed) for seed in almanac[0].split(" ")[1:]]
print(f"Seeds: {seeds}")
series = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]
lines = [almanac.index(f"{i}-to-{j} map:") for i, j in zip(series[:-1], series[1:])]
almanac.append(["", ""])
lines.append(len(almanac) - 1)

locations = list(
    map(seed_to_location, seeds, [almanac for seed in seeds], [lines for seed in seeds])
)

print(f"Locations: {locations}")
print(f"Min location: {min(locations)}")
