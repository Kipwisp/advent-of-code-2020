
import time
from collections import defaultdict

def read_file():
    lines = []
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    result = []
    for line in lines:
        directions = []
        i = 0
        while i < len(line):
            move = line[i] + line[i+1] if line[i] in {'s', 'n'} else line[i]
            directions.append(move)
            i += len(move)
        result.append(directions)

    return result


def part_1(data):
    tiles = defaultdict(lambda: True)
    directions = { 'e': (2, 0), 'se': (1, -1), 'sw': (-1, -1), 'w': (-2, 0), 'nw': (-1, 1), 'ne': (1, 1) }
    for tile in data:
        x, y = 0, 0
        for move in tile:
            dx, dy = directions[move]
            x += dx
            y += dy
    
        tiles[(x, y)] = not tiles[(x, y)]
    
    return list(tiles.values()).count(False), tiles


def part_2(tiles):
    directions = { (2, 0), (1, -1), (-1, -1), (-2, 0), (-1, 1), (1, 1) }
    for tile in list(tiles.keys()):
        if not tiles[tile]:
            x, y = tile
            adjacent = [(x + dx, y + dy) for dx, dy in directions]
            for adj in adjacent:
                tiles[adj] = tiles[adj]
    
    state = dict(tiles)
    for i in range(100):
        updated = set()
        for tile in state:
            x, y = tile
            adjacent = [(x + dx, y + dy) for dx, dy in directions]
            
            count = 0
            for adj in adjacent:
                if adj in state and not state[adj]:
                    count += 1

            if not state[tile] and (count == 0 or count > 2) or state[tile] and count == 2:
                tiles[tile] = not tiles[tile]

            if not tiles[tile]:
                updated.add(tile)
                updated.update(adjacent)

        new = { tile:tiles[tile] for tile in updated }
        state = new
            
    return list(tiles.values()).count(False)


def main():
    data = read_file()

    ts = time.time()
    result, tiles = part_1(data)
    print(f'Silver: {result}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    ts = time.time()
    print(f'Gold: {part_2(tiles)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
