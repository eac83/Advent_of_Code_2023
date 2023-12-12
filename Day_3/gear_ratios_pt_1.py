"""
Advent of Code Day 3: Gear Ratios Part 1
"""

with open("log.txt", "w") as log:
    print("Opening data", file=log)
    with open("data.txt", "r") as data:
        print("Reading data", file=log)
        lines = [line[:-1] for line in data]

    print("-" * 20, file=log)
    print("Finding all unique characters in data", file=log)

    all_characters = set("".join(lines))
    excluded_characters = set("1234567890.")
    characters = all_characters - excluded_characters
    print(f"Unique characters: {characters}", file=log)

    print("-" * 20, file=log)
    print("Adding border around schematic", file=log)
    lines.insert(0, "." * len(lines[0]))
    lines.append("." * len(lines[0]))
    lines = [f".{line}." for line in lines]

    print("-" * 20, file=log)
    print("Finding part numbers", file=log)
    part_nums = []
    for y, line in enumerate(lines):
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
                print(line[x_start : x_end + 1], file=log)
                block = ""
                for i in range(y - 1, y + 2):
                    block += lines[i][x_start - 1 : x_end + 2]
                    print(lines[i][x_start - 1 : x_end + 2], file=log)
                is_part_number = False
                for character in characters:
                    if character in block:
                        is_part_number = True
                        part_nums.append(int(line[x_start : x_end + 1]))
                        break
                print(f"Part number: {is_part_number}", file=log)
                print(f"Total: {sum(part_nums)}", file=log)
                x_start = x_end + 1
                continue
            x_start += 1

print(f"Final total: {sum(part_nums)}")
