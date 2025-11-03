input_part_one = "./inputs/part1.txt"
input_part_two = "./inputs/part2.txt"

lines = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc",
]

def parse_line(line):
    policy_part, password_part = line.split(":")
    rng, ch = policy_part.strip().split(" ")
    low, high = map(int, rng.split("-"))
    return {
        "low": low,
        "high": high,
        "char": ch,
        "password": password_part.strip(),
    }

def is_valid(entry):
    count = entry["password"].count(entry["char"])
    return entry["low"] <= count <= entry["high"]

## PART-ONE
### test
entries = map(parse_line, lines)
valid_count = sum(1 for e in entries if is_valid(e))

print("PART_ONE (test):", valid_count)

### real input 1
valid_count = 0 # reset
lines = [] # reset

with open(input_part_one, 'r') as file:
    for line in file:
        processed_line = line.strip()
        lines.append(processed_line)

entries = map(parse_line, lines)
valid_count = sum(1 for e in entries if is_valid(e))

print("PART_ONE (real input):", valid_count)

## PART-TWO
### test
valid_count = 0 # reset
lines = [] # reset

entries = map(parse_line, lines)
valid_count = sum(1 for e in entries if is_valid(e))

print("PART_ONE (test):", valid_count)

### exact input 2
valid_count = 0 # reset
lines = [] # reset

with open(input_part_one, 'r') as file:
    for line in file:
        processed_line = line.strip()
        lines.append(processed_line)

entries = map(parse_line, lines)
valid_count = sum(1 for e in entries if is_valid(e))

print("PART_TWO (real input):", valid_count)