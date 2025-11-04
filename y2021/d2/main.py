input_part_one = "./inputs/part1.txt"
input_part_two = "./inputs/part2.txt"
input_test_one = "./inputs/test1.txt"
input_test_two = "./inputs/test2.txt"

from file_service import read 

count = 0

print("== PART_ONE: tests ==")
content = read(input_test_one)
print(count)
print("== PART_ONE: end tests ==")

print("== PART_ONE: input ==")
content = read(input_part_one)
print(count)
print("== PART_ONE: end input ==")

print("== PART_TWO: tests ==")
content = read(input_test_two)
print(count)
print("== PART_TWO: end tests ==")

print("== PART_TWO: input ==")
content = read(input_part_two)
print(count)
print("== PART_TWO: end input ==")