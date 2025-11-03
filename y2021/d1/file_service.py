def read(path):
    lines = [] 
    with open(path, 'r') as file:
        for line in file:
            processed_line = line.strip()
            lines.append(int(processed_line))
    
    return lines