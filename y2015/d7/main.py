input_part_one = "./inputs/part1.txt"
input_part_two = "./inputs/part2.txt"
input_test_one = "./inputs/test1.txt"
input_test_two = "./inputs/test2.txt"

from file_service import read 
from utils import init_circuit

x = 123
y = 456
d = x&y
e = x|y
f = x<<2
g = y>>2
h = abs(~x+1)
i = abs(~y+1)

print("== PART_ONE: tests ==")
booklet = read(input_test_one)
circuit = init_circuit(booklet)
print(circuit.get_wires())
print("== PART_ONE: end tests ==")

print("== PART_ONE: input ==")
content = read(input_part_one)
print("== PART_ONE: end input ==")

print("== PART_TWO: tests ==")
content = read(input_test_two)
print("== PART_TWO: end tests ==")

print("== PART_TWO: input ==")
content = read(input_part_two)
print("== PART_TWO: end input ==")