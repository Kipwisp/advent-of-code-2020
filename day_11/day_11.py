import time
import numpy
from functools import reduce

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = numpy.array([list(line.strip()) for line in file.readlines()])

    return result


def part_1(layout):
    state = numpy.array([])
    while not numpy.array_equal(state, layout):
        state = numpy.copy(layout)
        for r, row in enumerate(layout):
            for c, seat in enumerate(layout[r]):
                if seat == '.':
                    continue

                adjacent = state[max(r-1, 0):min(r+2, len(layout)+1), max(c-1, 0):min(c+2, len(layout[0])+1)]
                if seat == 'L' and numpy.count_nonzero(adjacent == '#') == 0:
                    layout[r][c] = '#'
                elif seat == '#' and numpy.count_nonzero(adjacent == '#') > 4:
                    layout[r][c] = 'L'

    return numpy.count_nonzero(state == '#')


def part_2(layout):
    state = numpy.array([])
    slopes = { (0,1), (1,1), (1,0), (1,-1), (0, -1), (-1, -1), (-1, 0), (-1, 1) }
    while not numpy.array_equal(state, layout):
        state = numpy.copy(layout)
        for r, row in enumerate(layout):
            for c, seat in enumerate(layout[r]):
                if seat == '.':
                    continue

                occupied = 0
                
                for rise, run in slopes:
                    x, y = c + run, r + rise
                    while 0 <= y < len(state) and 0 <= x < len(state[0]):
                        if state[y][x] == '#':
                            occupied += 1
                            break
                        elif state[y][x] == 'L':
                            break

                        x += run
                        y += rise
                
                if seat == 'L' and occupied == 0:
                    layout[r][c] = '#'
                elif seat == '#' and occupied >= 5:
                    layout[r][c] = 'L'

    return numpy.count_nonzero(state == '#')


def main():
    layout = read_file()
    ts = time.time()
    print(f'Silver: {part_1(layout)}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    layout = read_file()
    ts = time.time()
    print(f'Gold: {part_2(layout)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
