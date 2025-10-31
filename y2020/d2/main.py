vector_test_one = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc",
]

complain_passwords = 0

def define_ranges(ranges):
    splitted_ranges = ranges.split("-")
    return splitted_ranges[0], splitted_ranges[1]
    
def define_policy(policy):
    splitted_policy = policy.split(" ")
    low, high = define_ranges(splitted_policy[0])
    char = splitted_policy[1]
    return int(low), int(high), char

def complain(low, high, counter):
    return counter >= low and counter <= high

counter = 0

for vector in vector_test_one:
    cmds = vector.split(":")
    policy = cmds[0]
    password = cmds[1]

    low, high, char = define_policy(policy)

    for c in password:
        if c is char:
            counter+=1
    
    if(complain(low, high, counter)):
        complain_passwords += 1

print(complain_passwords)
