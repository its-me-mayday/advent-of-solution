def count_trees(toboggan_map, log=None, dx=3, dy=1):
    rows = [r.strip() for r in toboggan_map if r.strip() != ""]
    H = len(rows)
    W = len(rows[0])

    r = 0
    c = 0
    trees = 0

    while True:
        r += dy
        c += dx
        if r >= H:
            break
        if rows[r][c % W] == '#':
            trees += 1

    if log:
        log.info(f"trees={trees}")
    return trees