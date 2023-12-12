"""
Advent of Code Day 3: Gear Ratios Part 2
"""

with open("log.txt", "w") as log:
    print("Opening data", file=log)
    with open("data.txt", "r") as data:
        print("Reading data", file=log)
        schematic = [line[:-1] for line in data]

    print("-" * 20, file=log)
    print("Adding border around schematic", file=log)
    schematic.insert(0, "." * len(schematic[0]))
    schematic.append("." * len(schematic[0]))
    schematic = [f".{line}." for line in schematic]

    print("-" * 20, file=log)
    print("Finding part numbers and coordinates", file=log)
    part_numbers = []
    part_coordinates = []
    for y, line in enumerate(schematic):
        print("-" * 20, file=log)
        print(f"Line {y}", file=log)
        print(line, file=log)
        x_start = 0
        while x_start < len(line):
            char = line[x_start]

            if char.isdigit():
                for x_end, char_end in enumerate(line[x_start:]):
                    if not char_end.isdigit():
                        x_end += x_start - 1
                        break
                part_number = int(line[x_start : x_end + 1])
                part_coords = [(x, y) for x in range(x_start, x_end + 1)]
                print(part_number, file=log)
                print(part_coords, file=log)
                part_numbers.append(part_number)
                part_coordinates.append(part_coords)
                x_start = x_end + 1
                continue
            x_start += 1

    print("-" * 20, file=log)
    print("Finding gears", file=log)
    gear_ratios = []
    for y, line in enumerate(schematic):
        print("-" * 20, file=log)
        print(f"Line {y}", file=log)
        if y > 0:
            print(schematic[y - 1], file=log)
        print(line, file=log)
        if y < len(schematic) - 1:
            print(schematic[y + 1], file=log)
        for x, char in enumerate(line):
            if char == "*":
                print(f"Potential gear found at ({x}, {y})", file=log)
                for j in range(y - 1, y + 2):
                    print(schematic[j][x - 1 : x + 2], file=log)
                border = [
                    (i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2)
                ]
                print(f"Border: {border}", file=log)
                adjacent_numbers = [
                    part
                    for i, part in enumerate(part_numbers)
                    if any(
                        digit_coordinate in border
                        for digit_coordinate in part_coordinates[i]
                    )
                ]
                print(
                    f"Adjacent parts: {[num for num in adjacent_numbers]}",
                    file=log,
                )

                if len(adjacent_numbers) == 2:
                    print("It's a gear!", file=log)
                    gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
                    print(f"Gear ratio: {gear_ratio}", file=log)
                    gear_ratios.append(gear_ratio)
                    print(f"Running total {sum(gear_ratios)}", file=log)

print(f"Final total: {sum(gear_ratios)}")
