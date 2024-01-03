"""
Advent of Code 2023 Day 5: If You Give A Seed A Fertilizer Part 2
"""


def seeds_to_min_location(
    seed_start: int, seed_range: int, almanac: list[str], lines: list[int]
) -> int:
    """
    Maps seed number to location number.

    Keyword arguments:
        seed_starts (int): start of seed range,
        seed_range (int): length of seed range
        almanac (list[str]): list of each line in the almanac
        lines (list[int]): list of the start of each map in the almanac.

    Returns:
        min_location (int): minimum location number of range.
    """
    print("-" * 20)
    print(f"Seed start: {seed_start}, seed range: {seed_range}")
    trail_starts = [seed_start]
    trail_ranges = [seed_range]
    for j, (start_line, end_line) in enumerate(zip(lines[:-1], lines[1:])):
        print(f"-----")
        print(f"Next section: {series[j+1]}")
        for i, (trail_start, trail_range) in enumerate(zip(trail_starts, trail_ranges)):
            print(f"---")
            print(f"{trail_start}, {trail_range}")
            for line in almanac[start_line + 1 : end_line - 1]:
                # print("-" * 10)
                # print(f"Line: {i}")
                destination, source, length = line.split(" ")
                destination, source, length = int(destination), int(source), int(length)

                if (trail_start <= source + length) and (
                    trail_start + trail_range >= source
                ):
                    if trail_start >= source:
                        trail_starts[i] = destination + (trail_start - source)
                        print(
                            f"{series[j]} {trail_start} mapped to {series[j+1]} {trail_starts[i]}"
                        )
                    else:
                        trail_starts.insert(i + 1, source)
                        trail_ranges[i] = trail_range - (source - trail_start)
                        trail_range = trail_ranges[i]
                        trail_ranges.insert(i + 1, source - trail_start)
                        print(
                            f"{series[j]} {trail_start} split into {series[j+1]} {trail_start} {trail_starts[-1]}"
                        )
                        print(trail_ranges[i] + trail_ranges[i])
                    if length < trail_range:
                        trail_ranges[i] = length
                        trail_starts.insert(i + 1, trail_start + length)
                        trail_ranges.insert(i + 1, trail_range - length)
                    break
                if trail_ranges[i] == 0:
                    trail_starts.pop(i)
                    trail_ranges.pop(i)
        print(f"Mapped to {series[j+1]} {trail_starts}, {trail_ranges}")
        print(f"Total number of seeds {sum(trail_ranges)}")

    print(f"Location:")
    print(f"{trail_starts}, {trail_ranges}")
    min_location = min(trail_starts)
    print(f"Min location of range: {min_location}")
    return min_location


with open("data.txt", "r") as data:
    almanac = data.read().splitlines()

seed_starts = [int(seed) for seed in almanac[0].split(" ")[1::2]]
seed_ranges = [int(seed) for seed in almanac[0].split(" ")[2::2]]
print(f"Seed_starts: {seed_starts}")
print(f"Seed_ranges: {seed_ranges}")
# seeds = []
# for seed_start, seed_range in zip(seed_starts, seed_ranges):
#   seeds += [seed for seed in range(seed_start, seed_start + seed_range)]
# print(f"Seeds: {seeds}")
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

# for seed_start, seed_range in zip(seed_starts, seed_ranges):
#   print(f"Seed start: {seed_start}, seed range: {seed_range}")
#  locations = list(
#     map(
#        seed_to_location,
#       [seed for seed in range(seed_start, seed_start + seed_range)],
#      [almanac] * seed_range,
#     [lines] * seed_range,
#        )
#   )
#  min_location = min(min(locations), min_location)
# print(f"Current minimum location: {min_location}")

min_locations = list(
    map(
        seeds_to_min_location,
        seed_starts,
        seed_ranges,
        [almanac] * len(seed_starts),
        [lines] * len(seed_starts),
    )
)
print(f"Min locations: {min_locations}")
print(
    f"Final min location: {min([min_location for min_location in min_locations if min_location >0])}"
)
