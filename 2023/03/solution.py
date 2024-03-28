#! usr/bin/python3

# plan
# 1. read schematic
# 2. parse valid numbers
#   2.1. get x,y coordiantes of all symbols
#   2.2. check x,7 coordianates around symbol for int
#   2.3. get all ints connected to positive x,y
# 3. sum the valid numbers

import re
import math

def check(test, result, expectation):
    print(f'{result == expectation}: {test} -- expect {result} to equal {expectation}')

parsed = [467,35,633,617,592,755,664,598]
def schematic(filename='sample'):
    lines = [line.strip() for line in open(filename, 'r')]
    return [line for line in lines]

    return result

class Solution:
    def __init__(self, schematic):
        self.schematic = schematic
        self.used_up = []

    def parse(self):
        result = []
        self.used_up = []
        for x,y in self.get_symbol_coordinates("symbol"):
            for _x,_y in self.get_adjacent_coordinates(x, y):
                if self.is_number(_x, _y):
                    num =  self.scan_line_for_complete_number(_x, _y)
                    if re.match("\\d", num):
                        result.append(int(num))

        return result

    def gear_ratio(self):
        result = []
        self.used_up = []
        for x,y in self.get_symbol_coordinates("gear"):
            gear_nums = []
            for _x,_y in self.get_adjacent_coordinates(x, y):
                if self.is_number(_x, _y):
                    num =  self.scan_line_for_complete_number(_x, _y)
                    if re.match("\\d", num):
                        gear_nums.append(int(num))

            if len(gear_nums) == 2:
                result.append(math.prod(gear_nums))

        return result

    def scan_line_for_complete_number(self, x, starting_y):
        coordinates = []
        # left
        for y in range(starting_y, -1, -1):
            if self.is_number(x, y):
                coordinates.insert(0, [x, y])
            else:
                break

        # right
        for y in range(starting_y + 1, len(self.schematic[x])):
            if self.is_number(x, y):
                coordinates.append([x, y])
            else:
                break

        num = []
        for r,p in coordinates:
            if self.is_number(r, p) and [r, p] not in self.used_up:
                num.append(self.schematic[r][p])
                self.used_up.append([r, p])

        return ''.join(num)

    def get_symbol_coordinates(self, scanfor="symbol"):
        coordinates = []
        for x in range(len(self.schematic)):
            for y in range(len(self.schematic[x])):
                match scanfor:
                    case "symbol":
                        if self.is_symbol(x, y):
                            coordinates.append([x, y])
                    case "gear":
                        if self.is_gear(x, y):
                            coordinates.append([x, y])

        return coordinates

    def get_gear_coordinates(self):
        coordinates = []
        for x in range(len(self.schematic)):
            for y in range(len(self.schematic[x])):
                if self.is_gear(x, y):
                    coordinates.append([x, y])

        return coordinates

    def get_adjacent_coordinates(self, x, y):
        _coordinates = [[x, y-1], [x, y+1], [x-1, y], [x-1, y-1], [x-1, y+1], [x+1, y], [x+1, y-1], [x+1, y+1]]
        return [coordinate for coordinate in _coordinates if self.valid(coordinate[0], coordinate[1])]

    def valid(self, x, y):
        if 0 <= x < len(self.schematic) and 0 <= y < len(self.schematic[x]):
            return True
        else:
            return False

    def is_number(self, x, y):
        if re.match("\\d", self.schematic[x][y]):
            return True
        else:
            return False

    def is_symbol(self, x, y):
        if re.match("\\d|[.]", self.schematic[x][y]):
            return False
        else:
            return True

    def is_gear(self, x, y):
        if re.match("[*]", self.schematic[x][y]):
            return True
        else:
            return False

# Part 1
sample = Solution(schematic())
check("sample", schematic()[0][0], "4")
check("is symbol", sample.is_symbol(0, 1), False)
check("is symbol", sample.is_symbol(1, 3), True)
check("is number", sample.is_number(1, 3), False)
check("is number", sample.is_number(0, 1), True)
check("coordinates", sample.get_symbol_coordinates()[0], [1,3])
check("adjacent", sample.get_adjacent_coordinates(0,3), [[0, 2], [0, 4], [1, 3], [1, 2], [1, 4]])
check("scan line", sample.scan_line_for_complete_number(0,2), '467')

check("parse sample", sorted(sample.parse()), sorted(parsed))
check("sum parsed sample", sum(sample.parse()), sum(parsed))

solution = Solution(schematic('input'))
check("sum parsed", sum(solution.parse()), 536202)

# part 2
check("gear ratio", sample.gear_ratio(), [16345, 451490])
check("gear ratio", sum(sample.gear_ratio()), 467835)
check("sum gears", sum(solution.gear_ratio()), 78272573)
