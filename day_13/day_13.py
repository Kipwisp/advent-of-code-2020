import time
import math

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [line.strip() for line in file.readlines()]

    return result


def part_1(data):
    earliest = int(data[0])
    buses = data[1].split(',')
    buses = { int(v) for v in buses if v != 'x'}

    timestamps = {}
    best = math.inf
    for bus in buses:
        timestamp = (earliest // bus) * bus + bus
        if timestamp < best:
            best = timestamp
        timestamps[timestamp] = bus

    return (best - earliest) * timestamps[best]


def part_2(data):
    buses = data[1].split(',')
    buses = { i:int(v) for i,v in enumerate(buses) if v != 'x'}

    i = 0
    delta = buses.pop(0)
    while len(buses) > 0:
        i += delta
        offsets = [*buses.keys()]
        for offset in offsets:
            if (i + offset) % buses[offset] != 0:
                break
            delta = delta * buses[offset]
            buses.pop(offset)

    return i


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
