"""
Advent of Code 2023 Day 2: Code Conundrum Part 1
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
    with open("./data.txt") as file:
        print("Reading data.txt", file=log)
        lines = [line[:-1] for line in file]

    game_ids = []
    game_pulls = []
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

    balls_total = {"blue": 14, "red": 12, "green": 13}
    possible_games = []
    for id in games:
        print("-" * 20, file=log)
        print(f"Game {id}:", file=log)
        for game in games[id]:
            game = game.replace(",", "")
            game_words = game.split(" ")
            print(game_words, file=log)
            ball_count = {"blue": 0, "red": 0, "green": 0}
            for i, colour in enumerate(game_words[1::2]):
                ball_count[colour] = int(game_words[2 * i])
                is_game_possible = dict_compare(ball_count, balls_total)
            print(f"Pull possible? {is_game_possible}", file=log)
            if not is_game_possible:
                break

        print(f"Game possible? {is_game_possible}", file=log)
        if is_game_possible:
            possible_games.append(int(id))
            print(f"Current total: {sum(possible_games)}", file=log)

print(f"Final total: {sum(possible_games)}")
