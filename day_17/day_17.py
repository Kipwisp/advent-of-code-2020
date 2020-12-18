import time

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [line.strip() for line in file.readlines()]

    return result


def generate_coords(lines, dimensions):
    result = {}
    for y in range(-1, len(lines) + 1):
            for x in range(-1, len(lines[0]) + 1):
                result[(x, y)] = lines[y][x] == '#' if 0 <= x < len(lines[0]) and 0 <= y < len(lines) else False

    layers = [range(-1, 2) for i in range(dimensions - 2)]
    for layer in layers:
        new = {}
        for z in layer:
            for coord in result:
                new[(*coord, z)] = result[coord] if z == 0 else False
        result = new
    
    return result


def get_adjacent(state, point):
    neighbors = set((point[0] + i,) for i in range(-1, 2))
    dimensions = [range(-1, 2) for i in range(len(point) - 1)]
    for i, dimension in enumerate(dimensions):
        new = set()
        for x in dimension:
            for neighbor in neighbors:
                new.add((*neighbor, point[i+1] + x))
        neighbors = new

    neighbors.remove(point)

    activated = len([neighbor for neighbor in neighbors if neighbor in state and state[neighbor]])

    return activated, neighbors


def part_1_2(data):
    state = data.copy()
    for cycle in range(6):
        updated = set()
        for point in state:
            activated, neighbors = get_adjacent(state, point)
            
            if state[point] and not 2 <= activated <= 3 or not state[point] and activated == 3:
                data[point] = not state[point]
                updated.add(point)
                updated.update(neighbors)

        new = { point:(data[point] if point in data else False) for point in updated }
        state = new
    
    return list(data.values()).count(True)


def main():
    lines = read_file()

    points = generate_coords(lines, 3)
    ts = time.time()
    print(f'Silver: {part_1_2(points)}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    points = generate_coords(lines, 4)
    ts = time.time()
    print(f'Gold: {part_1_2(points)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
