import time
import numpy as np
from functools import reduce

class Piece:
    def __init__(self, img, label=None):
        self.img = img
        self.label = label
        self.np_img = np.array(img)

    def get_data(self):
        return self.np_img

    def get_label(self):
        return self.label

    def get_top(self):
        return tuple(self.np_img[0])

    def get_bottom(self):
        return tuple(self.np_img[-1])

    def get_left(self):
        return tuple(self.np_img[:, 0])

    def get_right(self):
        return tuple(self.np_img[:, -1])

    def rotate(self):
        self.np_img = np.rot90(self.np_img)
        self.img = tuple(self.np_img)
    
    def flip(self):
        self.np_img = np.flip(self.np_img, 0)
        self.img = tuple(self.np_img)
    
    def __str__(self):
        result = ''
        for row in self.img:
            result += f'{str(row)}\n'
        return result


def read_file():
    images = []
    with open('input.txt', 'r') as file:
        images = file.read().split('\n\n')
    
    result = {}
    for image in images:
        data = []
        label, rows = image.split(':\n')
        label = label.replace('Tile ', '')
        for row in rows.split('\n'):
            data.append(tuple(row.strip()))
        result[label] = Piece(tuple(data), label)

    return result


def part_1(data):
    edges = {}
    for label, piece in data.items():
        edges[label] = { piece.get_top(), piece.get_bottom(), piece.get_left(), piece.get_right() }

    pairs = {}
    unmatched = {}
    corner = None
    for label, edge_list in edges.items():
        pairs[label] = {}
        unmatched[label] = []
        for edge in edge_list:
            match = False
            reversed_edge = tuple(reversed(edge))
            for other_label, other in edges.items():
                if other_label != label:
                    if edge in other or reversed_edge in other:
                        pairs[label][edge] = other_label
                        pairs[label][reversed_edge] = other_label
                        match = True
                        break
            if not match:
                unmatched[label].append(edge)
                unmatched[label].append(reversed_edge)
        if len(unmatched[label]) == 4:
            corner = label

    current = corner
    size = int(len(data) ** 0.5)
    tiles = [[None for i in range(size)] for j in range(size)]
    for i in range(len(tiles)):
        for j in range(len(tiles)):
            top = set(unmatched[current]) if i-1 < 0 else set([tiles[i-1][j].get_bottom()])
            left = set(unmatched[current]) if j-1 < 0 else set([tiles[i][j-1].get_right()])
    
            piece = data[current]
            
            oriented = False
            while not oriented:
                piece.flip()
                for k in range(4):
                    if piece.get_top() not in top or piece.get_left() not in left:
                        piece.rotate()
                    else:
                        oriented = True
                        break

            tiles[i][j] = piece

            if j < len(tiles) - 1:
                current = pairs[current][piece.get_right()]
            elif i < len(tiles) - 1:
                current = pairs[tiles[i][0].get_label()][tiles[i][0].get_bottom()]
    
    rows = []
    for i, row in enumerate(tiles):
        for j, element in enumerate(row):
            piece = element.get_data()[1:-1,1:-1]
            if j == 0:
                rows.append(piece)
            else:
                rows[i] = np.concatenate((rows[i], piece), axis=1)
    
    map = rows[0]
    for row in rows[1:]:
        map = np.concatenate((map, row), axis=0)

    return reduce(lambda x, y: x * y, [int(tiles[i][j].get_label()) for i in (0,-1) for j in (0,-1)]), Piece(map)
        

def part_2(map):
    dragon = np.array([[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','#',' '],
                       ['#',' ',' ',' ',' ','#','#',' ',' ',' ',' ','#','#',' ',' ',' ',' ','#','#','#'],
                       [' ','#',' ',' ','#',' ',' ','#',' ',' ','#',' ',' ','#',' ',' ','#',' ',' ',' ']])
    filter = dragon == '#'
    expected = np.count_nonzero(dragon == '#')
    height, width = len(dragon), len(dragon[0])

    count = 0
    rotations = 0
    while count == 0:
        if rotations == 4:
            map.flip()
        map.rotate()
        rotations += 1

        data = map.get_data()
        for i, row in enumerate(data):
            for j, element in enumerate(data):
                dw, dh = j + width, i + height
                if dw <= len(data) and dh <= len(data):
                    slice = data[i:dh,j:dw]
                    if np.count_nonzero(slice[filter] == '#') == expected:
                        count += 1

    return np.count_nonzero(map.get_data() == '#') - (expected * count)

def main():
    data = read_file()

    ts = time.time()
    result, map = part_1(data)
    print(f'Silver: {result}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    ts = time.time()
    print(f'Gold: {part_2(map)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
