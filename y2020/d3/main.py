slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

input_part_one = "./inputs/part1.txt"
input_part_two = "./inputs/part2.txt"
input_test_one = "./inputs/test1.txt"
input_test_two = "./inputs/test2.txt"

from file_service import read 
from utils import count_trees
from logger import logger as log

print("== PART_ONE: tests ==")
toboggan_map = read(input_test_one)
count = count_trees(toboggan_map, log)
print(count)
print("== PART_ONE: end tests ==")

print("== PART_ONE: input ==")
toboggan_map = read(input_part_one)
count = count_trees(toboggan_map, log)
print(count)
print("== PART_ONE: end input ==")

print("== PART_TWO: tests ==")
toboggan_map = read(input_test_two)
trees = 1
for (dx,dy) in slopes:
    count = count_trees(toboggan_map, log, dx, dy)
    trees *= count
    print(count)
print(trees)
print("== PART_TWO: end tests ==")

print("== PART_TWO: input ==")
toboggan_map = read(input_part_two)
trees = 1
for (dx,dy) in slopes:
    count = count_trees(toboggan_map, log, dx, dy)
    trees *= count
    print(count)
print(trees)
print("== PART_TWO: end input ==")