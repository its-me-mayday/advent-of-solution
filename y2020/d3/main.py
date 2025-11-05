from itertools import groupby

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

#print("== PART_TWO: tests ==")
#toboggan_map = read(input_test_one)
#count = count_trees(toboggan_map, log)
#print(count)
#print("== PART_TWO: end tests ==")

#print("== PART_TWO: input ==")
#toboggan_map = read(input_test_one)
#count = count_trees(toboggan_map, log)
#print(count)
#print("== PART_TWO: end input ==")