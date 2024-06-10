#! usr/bin/python3

# plan

import re
import math

def check(test, result, expectation):
    print(f'{result == expectation}: {test} -- expect {result} to equal {expectation}')

def scratchers(filename='sample'):
    lines = [line.strip() for line in open(filename, 'r')]
    return [line for line in lines]

total_points = 13

class Solution:
    def __init__(self, lines):
        self.lines = lines

    def results(self):
        results = []
        for game in self.games().values():
            points = self.tally(game)
            results.append(points)

        return results

    def games(self):
        def safe_int(n):
            try:
                return int(n)
            except ValueError:
                return None

        games = {}
        for line in self.lines:
            game_id, numbers = line.split(":")
            winning_numbers, my_numbers = numbers.split("|")
            games[game_id] = {
                "winning_numbers": sorted(filter(None, [safe_int(n.strip()) for n in winning_numbers.split(" ")])),
                "my_numbers": sorted(filter(None, [safe_int(n.strip()) for n in my_numbers.split(" ")]))
            }

        return games

    def tally(self, game):
        points = 0
        for winning_number in game["winning_numbers"]:
            if winning_number in game["my_numbers"]:
                if points == 0:
                    points += 1
                else:
                    points = math.prod([points, 2])

        return points

# Part 1
sample = Solution(scratchers())
check("results", sample.results(), [8,2,2,1,0,0])
check("total_points", sum(sample.results()), total_points)

solution = Solution(scratchers("input"))
check("total_points", sum(solution.results()), 32609)

# Part 2
