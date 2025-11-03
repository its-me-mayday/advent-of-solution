def count_increases(content):
    return sum(b > a for a, b in zip(content, content[1:]))