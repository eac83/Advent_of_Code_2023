"""
Advent of Code 2023 Day 2: Code Conundrum Part 2
"""


def dict_compare(dict_1, dict_2):
    """Takes in two dictionaries, returns False if any value in dict_1 is
    greater than that of dict_2, else returns True"""
    for key in dict_1:
        if dict_1[key] > dict_2[key]:
            return False
    return True


with open("./log.txt", "w") as log:
    print("Opening data.txt", file=log)
    with open("./data.txt") as data:
        print("Reading data.txt", file=log)
        lines = [line[:-1] for line in data]

    game_ids = []
    game_pulls = []

    print("-" * 30, file=log)
    print("Splitting lines into game ID and pulls", file=log)
    for i, game in enumerate(lines):
        print("-" * 10, file=log)
        print(f"Game {i+1}", file=log)
        print(game, file=log)
        game_header, game_pull_descriptions = game.split(": ")
        _, game_id = game_header.split(" ")
        game_ids.append(game_id)
        game_pulls_split = game_pull_descriptions.split("; ")
        game_pulls.append(game_pulls_split)
        print(f"Game ID: {game_id}", file=log)
        print(f"Pulls: {game_pulls_split}", file=log)

    print("-" * 20, file=log)
    print(f"All IDs: {game_ids}", file=log)
    print(f"All pulls: {game_pulls}", file=log)
    games = dict(zip(game_ids, game_pulls))
    print(f"Combined dictionary: {games}", file=log)

    cubes_total = {"blue": 14, "red": 12, "green": 13}
    powers = []
    print("-" * 30, file=log)
    print("Finding minimum cubes per game", file=log)
    for id in games:
        cube_counts = {"blue": [], "red": [], "green": []}

        print("-" * 20, file=log)
        print(f"Game {id}:", file=log)
        for game in games[id]:
            game = game.replace(",", "")
            game_words = game.split(" ")
            print(game_words, file=log)
            cube_count = {"blue": 0, "red": 0, "green": 0}
            for i, colour in enumerate(game_words[1::2]):
                cube_count[colour] = int(game_words[2 * i])

            for colour in cube_counts:
                cube_counts[colour].append(cube_count[colour])
        print(cube_counts, file=log)
        min_counts = {"blue": 0, "red": 0, "green": 0}

        for colour in min_counts:
            # breakpoint()
            min_counts[colour] = max(cube_counts[colour])
        print(f"Min counts: {min_counts}", file=log)
        set_power = min_counts["blue"] * min_counts["red"] * min_counts["green"]
        print(f"Set power: {set_power}", file=log)
        powers.append(set_power)
        print(f"Total power: {sum(powers)}", file=log)


print(f"Final total: {sum(powers)}")
