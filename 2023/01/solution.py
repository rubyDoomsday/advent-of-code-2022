#! usr/bin/python3

import re
from typing import List, Dict

def sample() -> List[str]:
    return [
        'two1nine',
        'eightwothree',
        'abcone2threexyz',
        'xtwone3four',
        '4nineeightseven2',
        'zoneight234',
        '7pqrstsixteen'
    ]

def input() -> List[str]:
    with open('input', 'r') as f:
        return f.readlines()

def check(test, result, expectation):
    print(f'{test} -- expect {result} to equal {expectation}: {result == expectation}')

class Solution:
    def __init__(self, lines):
        self.lines = lines
        self.mapper: Dict[str, int] = {
            "eight": 8,
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "nine": 9,
            "zero": 0,
        }

    def answer(self) -> int:
        print(sum(self.build()))

    def build(self):
        result = []
        for line in  self.lines:
            combined = f"{self.from_left(line)}{self.from_right(line)}"
            result.append(int(combined))

        return result

    def from_left(self, line: str) -> str:
        regex = re.compile("|".join(list(self.mapper.keys()) + ["\\d"]))
        return [self.parse(m) for m in regex.findall(line)][0]

    def from_right(self, line: str) -> str:
        _mapper_keys_reversed = ["".join(reversed(k)) for k in self.mapper.keys()]
        regex = re.compile("|".join(_mapper_keys_reversed + ["\\d"]))
        return [self.parse("".join(reversed(m))) for m in regex.findall("".join(reversed(line)))][0]

    def parse(self, string: str) -> str:
        return int(string) if string.isdigit() else self.mapper[string]


# sol = Solution(sample())
# check("parse", sol.parse('1'), 1)
# check("parse", sol.parse('one'), 1)
# check("from_left", sol.from_left('zoneight234'), 1)
# check("from_right", sol.from_right('zoneight234'), 4)
# check("builds", sol.build(), [29, 83, 13, 24, 42, 14, 76 ])
Solution(sample()).answer()
Solution(input()).answer()
