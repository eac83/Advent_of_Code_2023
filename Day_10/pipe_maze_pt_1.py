"""
Advent of Code Day 10: Pipe Maze
"""

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


def reroute(path, direction):
    backwards = tuple(-i for i in direction)
    return (
        ROUTE_MOVES[path][1]
        if ROUTE_MOVES[path][0] == backwards
        else ROUTE_MOVES[path][0]
    )

print(reroute("L", SOUTH))
breakpoint()
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
        print(f"Moving ({x}, {y})")
        direction = (x, y)
        x += start_x
        y += start_y
        print(maze[y][x])
        break

path = maze[y][x]
i = 1

while path != "S":
    #    breakpoint()
    print(f"Step {i}: {path} at ({x}, {y})")
    if path not in ["|", "-"]:
        direction = reroute(path, direction)
    print(f"Moving by ({direction[0], direction[1]})")
    x += direction[0]
    y += direction[1]
    path = maze[y][x]
    i += 1

print(i / 2)
