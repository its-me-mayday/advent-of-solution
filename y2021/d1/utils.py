def count_increases(content, window):
    return sum(b > a for a, b in zip(content, content[window:]))