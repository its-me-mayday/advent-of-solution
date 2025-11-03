from itertools import groupby

input_part_one = "./inputs/part1.txt"
input_part_two = "./inputs/part2.txt"
input_test_one = "./inputs/test1.txt"
input_test_two = "./inputs/test2.txt"

from passport import Passport
from file_service import read 
from utils import scan

def count_valid_passports_p2(ps):
    count_valid = 0
    for p in ps:
        if(p.is_valid()): count_valid += 1

    return count_valid

def count_valid_passports(ps):
    count_valid = 0
    for p in ps:
        if(p.has_required_fields()): count_valid += 1

    return count_valid

def parse_passports(lines: list[str]) -> list[Passport]:
    groups = (" ".join(g).split() for k, g in groupby(lines, key=bool) if k)
    dicts  = (dict(x.split(":", 1) for x in grp) for grp in groups)
    return [Passport(**{k: d.get(k) for k in Passport.__dataclass_fields__}) for d in dicts]

print("== PART_ONE: tests ==")
content = read(input_test_one)
passports = parse_passports(content)
count = count_valid_passports(passports)
print(count)
print("== PART_ONE: end tests ==")

print("== PART_ONE: input ==")
content = read(input_part_one)
passports = parse_passports(content)
count = count_valid_passports(passports)
print(count)
print("== PART_ONE: end input ==")

print("== PART_TWO: tests ==")
content = read(input_test_two)
passports = parse_passports(content)
count = count_valid_passports_p2(passports)
print(count)
print("== PART_TWO: end tests ==")

print("== PART_TWO: input ==")
content = read(input_part_two)
passports = parse_passports(content)
count = count_valid_passports_p2(passports)
print(count)
print("== PART_TWO: end input ==")