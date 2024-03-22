#! usr/bin/python3

# plan
# convert the games into a logical store - CSV format or dict
# define an argument interface for input - dict might make most sense here
# check the input against the store and return the result
# add testing along the way

import re
import math
from typing import Dict, List, Any

def check(test, result: Any, expectation: Any):
    print(f'{result == expectation}: {test} -- expect {result} to equal {expectation}')

def bag():
    return {
        "blue": 14,
        "red": 12,
        "green": 13
    }

class Reader:
    def __init__(self, filename):
      self.filename = filename
      self.games = []

    def parse(self) -> "Reader":
        lines = [line.strip() for line in open(self.filename, 'r')]
        for line in lines:
            game, data = line.split(":")
            game_id = "".join(re.findall("\\d", game))

            rounds = data.split(";")
            for round_id, r in enumerate(rounds):
                count_colors = r.split(",")

                _dict = {}
                for count_color in count_colors:
                    count, color = count_color.strip().split(" ")
                    _dict[color] = count

                self.games.append({
                    "game": int(game_id),
                    "round": int(round_id),
                    "blue": int(_dict.get("blue", 0)),
                    "red": int(_dict.get("red", 0)),
                    "green": int(_dict.get("green", 0))
                    })

        return self

class Solution:
    def __init__(self, games: dict, bag: dict):
        self.games = games
        self.bag = bag
        self.game_ids = set([game["game"] for game in games])

    def sum_the_bag(self) -> int:
        return sum(self.possible_game_ids())

    def power(self) -> int:
        powers = [self.power_of_game(game_id) for game_id in self.game_ids]

        return sum(powers)

    def possible_game_ids(self) -> set[int]:
        return sorted(list(self.game_ids - self.impossible_game_ids()))

    def impossible_game_ids(self) -> set:
        result = []
        colors = self.bag.keys()
        result += [self.scan_lines(color) for color in colors]

        return set().union(*result)

    def scan_lines(self, color) -> List[int]:
        invalid_games = []
        for row in self.games:
            if row[color] > self.bag[color]:
                invalid_games.append(row["game"])

        return invalid_games

    def power_of_game(self, game_id) -> int:
        set_of_cubes = []
        for color in self.bag.keys():
            set_of_cubes.append(self.min_color_count(game_id, color))

        return math.prod(set_of_cubes)

    def min_color_count(self, game_id, color) -> int:
        cubes_each_round = []

        for row in self.game(game_id):
            cubes_each_round.append(row[color])

        return max(cubes_each_round)

    def game(self, game_id) -> List[dict]:
        rounds = []
        for row in self.games:
            if row["game"] == game_id:
              rounds.append(row)

        return rounds

# Part 1
sample = Solution(Reader("sample.txt").parse().games, bag())
answer = Solution(Reader("games.text").parse().games, bag())

check("scane lines blue", sample.scan_lines('blue'), [4])
check("scan linest red", sample.scan_lines('red'), [3, 4])
check("scan lines green", sample.scan_lines('green'), [])
check("invalid games", sample.impossible_game_ids(), {3,4})
check("valid games", sample.possible_game_ids(), [1,2,5])
check("sum", sample.sum_the_bag(), sum([1,2,5]))

check("sum", answer.sum_the_bag(), 2683)

# Part 2
check("min color count", sample.min_color_count(1, 'blue'), 6)
check("min color count", sample.min_color_count(1, 'red'), 4)
check("min color count", sample.min_color_count(1, 'green'), 2)
check("power of game", sample.power_of_game(1), 48)
check("game ids", sample.game_ids, [1,2,3,4,5])
check("power", sample.power(), 2286)

check("answer", answer.power(), 49710)
