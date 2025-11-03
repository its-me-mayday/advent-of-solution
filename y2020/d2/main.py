lines = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc",
]

valid_passwords_count = 0

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

entries = map(parse_line, lines)
valid_count = sum(1 for e in entries if is_valid(e))

print(valid_count)

valid_count = 0
lines = []

input_part_one = "./inputs/part1.txt"
input_part_two = "./inputs/part2.txt"

lines = []
with open(input_part_one, 'r') as file:
    for line in file:
        processed_line = line.strip()
        lines.append(processed_line)

entries = map(parse_line, lines)
valid_count = sum(1 for e in entries if is_valid(e))

print(valid_count)