import time
import math

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [line.strip() for line in file.readlines()]

    return result


def rotate(x, y, theta):
    radians = math.radians(theta)
    return round(x * math.cos(radians) - y * math.sin(radians)), round(x * math.sin(radians) + y * math.cos(radians))


def part_1(data):
    rotations = { 'R': -1, 'L': 1 }
    directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0), 'F': (1, 0)}
    x, y = 0, 0

    for instruction in data:
        action, value = instruction[0], int(instruction[1:])

        if action in rotations:
            directions['F'] = rotate(*directions['F'], value * rotations[action])
        else:
            dx, dy = map(lambda x: x * value, directions[action])
            x += dx
            y += dy

    return abs(x) + abs(y)


def part_2(data):
    rotations = { 'R': -1, 'L': 1 }
    directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0) }
    ship_x, ship_y = 0, 0
    point_x, point_y = 10, 1

    for instruction in data:
        action, value = instruction[0], int(instruction[1:])

        if action in rotations:
            point_x, point_y = rotate(point_x, point_y, value * rotations[action])
        elif action == 'F':
            ship_x += point_x * value
            ship_y += point_y * value
        else:
            dx, dy = map(lambda x: x * value, directions[action])
            point_x += dx
            point_y += dy

    return abs(ship_x) + abs(ship_y)


def main():
    data = read_file()

    ts = time.time()
    print(f'Silver: {part_1(data)}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    ts = time.time()
    print(f'Gold: {part_2(data)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
