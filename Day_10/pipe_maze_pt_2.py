"""
Advent of Code Day 10: Pipe Maze part 2
"""
from typing import Tuple

NORTH = (0, -1)
SOUTH = (0, 1)
EAST = (1, 0)
WEST = (-1, 0)

ROUTE_MOVES = {
    "|": [NORTH, SOUTH],
    "-": [WEST, EAST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [SOUTH, WEST],
    "F": [SOUTH, EAST],
}


def reroute(path: str, entry_direction: Tuple[int]) -> Tuple[int]:
    """
    Returns the new direction after a corner given the entry direction.

    Args:
        path (str): Char denoting corner shape.
        entry_direction (Tuple[int]): Vector of direction of entry into
        corner.

    Returns:
        (Tuple[int]): Vector of direction of exit from corner.
    """
    backwards = tuple(-i for i in entry_direction)
    return (
        ROUTE_MOVES[path][1]
        if ROUTE_MOVES[path][0] == backwards
        else ROUTE_MOVES[path][0]
    )


with open("data.txt", "r") as file:
    maze = file.read().splitlines()

for i, line in enumerate(maze):
    if "S" in line:
        start_x, start_y = (line.index("S"), i)
        break

print(f"S found at: ({start_x}, {start_y})")
for x, y in [NORTH, SOUTH, EAST, WEST]:
    if (
        maze[start_y + y][start_x + x] in ROUTE_MOVES
        and (-x, -y) in ROUTE_MOVES[maze[start_y + y][start_x + x]]
    ):
        direction = (x, y)
        x += start_x
        y += start_y
        print(maze[y][x])
        break

path = maze[y][x]
perimeter = 1
corner_coordinates = []

# Find number of exterior points b
while path != "S":
    if path not in ["|", "-"]:
        direction = reroute(path, direction)
    x += direction[0]
    y += direction[1]
    path = maze[y][x]
    if path in ["L", "J", "7", "F"]:
        print(f"Adding corner {path} at ({x}, {y})")
        corner_coordinates.append((x, y))
    perimeter += 1
print(f"Number of points around loop: {perimeter}")

# Calculate area of loop A using the Shoelace formula
# A = 1/2 \sum_i (y_i + y_{i+1}) (x_i - x_{i+1})
area = 0
num_corners = len(corner_coordinates)
for i, (x_i, y_i) in enumerate(corner_coordinates):
    x_j, y_j = corner_coordinates[(i + 1) % num_corners]
    area += 1 / 2 * (y_i + y_j) * (x_i - x_j)

print(f"Area of loop: {area}")

# Calculate number of interior points i using Pick's theorem
# i = A - b/2 + 1
print(f"Number of interior points: {area - perimeter / 2 + 1}")
