import time
from functools import reduce

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [line.strip() for line in file.readlines()]

    return result


def count_trees_part_1(map):
    x, y, count = 0, 0, 0

    while (y < len(map) - 1):
        x = (x + 3) % len(map[0])
        y += 1

        if map[y][x] == '#':
            count += 1

    return count


def count_trees_part_2(map):
    slopes = { (1, 1): 0, (3, 1): 0, (5, 1): 0, (7, 1): 0, (1, 2): 0 }

    for slope in slopes:
        slope_x, slope_y = slope
        x, y = 0, 0

        while (y < len(map) - 1):
            x = (x + slope_x) % len(map[0])
            y += slope_y

            if map[y][x] == '#':
                slopes[slope] += 1
    
    return reduce(lambda x, y: x * y, slopes.values())


def main():
    map = read_file()

    ts = time.time()
    print(f'Silver: {count_trees_part_1(map)}')
    print(f'Completed in {time.time() - ts} seconds. \n')
    
    ts = time.time()
    print(f'Gold: {count_trees_part_2(map)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
