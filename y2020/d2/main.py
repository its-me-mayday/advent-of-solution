vector_test_one = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc",
]

valid_passwords_count = 0

def parse_ranges(ranges):
    splitted_ranges = ranges.split("-")
    return splitted_ranges[0], splitted_ranges[1]
    
def parse_policy(policy):
    splitted_policy = policy.split(" ")
    low, high = parse_ranges(splitted_policy[0])
    char = splitted_policy[1]
    return int(low), int(high), char

def is_password_valid(low, high, counter):
    return counter >= low and counter <= high

for entry in vector_test_one:
    counter = 0
    cmds = entry.split(":")
    policy = cmds[0]
    password = cmds[1].strip()

    low, high, char = parse_policy(policy)

    for c in password:
        if c == char:
            counter+=1
    
    if(is_password_valid(low, high, counter)):
        valid_passwords_count += 1

print(valid_passwords_count)
