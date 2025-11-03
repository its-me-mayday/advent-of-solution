input_part_one = "./inputs/part1.txt"
input_part_two = "./inputs/part2.txt"

def read(path):
    with open(path, 'r') as file:
        for line in file:
            processed_line = line.strip()
            lines.append(processed_line)
    return lines