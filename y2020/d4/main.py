input_part_one = "./inputs/part1.txt"
input_part_two = "./inputs/part2.txt"

from passport import Passport
from file_service import FileService

print("== PART_ONE: tests ==")

p = Passport(
    byr="1987", iyr="2015", eyr="2028",
    hgt="183cm", hcl="#623a2f", ecl="brn", pid="000123456"
)

print(p, "is valid?", p.is_valid())

p = Passport(
    byr="1987", iyr="2015", eyr="2028",
    hgt="183cm", hcl="#623a2f", ecl="brn", pid="000123456",
    cid="fajiohf341ufidahf"
)

print(p, "is valid?", p.is_valid())

p = Passport(
    byr=None, iyr=None, eyr="2028",
    hgt="183cm", hcl="#623a2f", ecl="brn", pid="000123456",
    cid="fajiohf341ufidahf"
)

print(p, "is valid?", p.is_valid())

print("== PART_ONE: end tests ==")