"""
Advent of Code 2023 Day 1 Part 1
"""

print("Opening file")
with open("data.txt", "r") as file:
    print("Reading lines")
    lines = [line[:-1] for line in file]
print("Closed file")
char_range = [str(idx) for idx in range(0, 10)]
calibration_values = [0] * len(lines)
for idx, line in enumerate(lines):
    print("-"*10)
    print(f"Line number: {idx}")
    print(f"Line: {line}")
    numbers_in_line = [int(char) for char in line if char in char_range]
    print(f"Numbers in line: {numbers_in_line}")
    calibration_values[idx] = numbers_in_line[0] * 10 + numbers_in_line[-1]
    print(f"Calibration_value: {calibration_values[idx]}")
    print(f"Sum: {sum(calibration_values)}")

print(sum(calibration_values))
