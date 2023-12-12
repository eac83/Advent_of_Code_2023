"""
Advent of Code 2023 Day 1 Part 2
"""

# Read file
with open("log.txt", "w") as log:
    log.write("Opening file\n")
    with open("data.txt", "r") as file:
        log.write("Reading lines\n")
        lines = [line[:-1] for line in file]
        log.write("Closed file\n")

    # Set up substrings to look for in lines
    char_range = [str(idx) for idx in range(0, 10)]
    string_range = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    string_to_char = dict(zip(string_range, char_range[1:]))

    # Replace spelled out numbers in lines with numerals
    for idx, line in enumerate(lines):
        log.write("-" * 10 + "\n")
        log.write(f"Line number: {idx} \n")
        log.write(f"Line: {line} \n")
        for num in string_range:
            # Keep first and last letters in case of overlapping numbers e.g. oneight
            line = line.replace(num, num[0] + string_to_char[num] + num[-1])
        lines[idx] = line
        log.write(f"Replaced line: {lines[idx]} \n")

    calibration_values = [0 for line in lines]
    for idx, line in enumerate(lines):
        log.write("-" * 10 + "\n")
        log.write(f"Line number: {idx} \n")
        log.write(f"Line: {line} \n")
        numbers_in_line = [int(char) for char in line if char in char_range]
        log.write(f"Numbers in line: {numbers_in_line} \n")
        calibration_values[idx] = numbers_in_line[0] * 10 + numbers_in_line[-1]
        log.write(f"Calibration_value: {calibration_values[idx]} \n")
        log.write(f"Sum: {sum(calibration_values)} \n")

print(sum(calibration_values))
