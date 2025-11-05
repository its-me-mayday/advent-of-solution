input_part_one = "./inputs/part1.txt"
input_part_two = "./inputs/part2.txt"
input_test_one = "./inputs/test1.txt"
input_test_two = "./inputs/test2.txt"

from file_service import read 
from utils import init_circuit

from logger import get_logger
import logging
from logging.handlers import RotatingFileHandler

log = get_logger(__name__)

file_handler = RotatingFileHandler("app.log", maxBytes=5_000_000, backupCount=5)
file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))

root = logging.getLogger()
root.addHandler(file_handler) 

#print("== PART_ONE: tests ==")
#booklet = read(input_test_one)
#circuit = init_circuit(booklet, log)
#print(circuit.get_wires())
#print("== PART_ONE: end tests ==")

print("== PART_ONE: input ==")
booklet = read(input_part_one)
print("booklet:", booklet)
circuit = init_circuit(booklet, log)
print(circuit.get_wires())
for wires in circuit.get_wires():
    print(wires.get_id(), ":", wires.get_signal())
print("== PART_ONE: end input ==")

#print("== PART_TWO: tests ==")
#content = read(input_test_two)
#print("== PART_TWO: end tests ==")

#print("== PART_TWO: input ==")
#content = read(input_part_two)
#print("== PART_TWO: end input ==")