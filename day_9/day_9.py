import time
import math

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [int(line.strip()) for line in file.readlines()]

    return result


def part_1(data):
    length = 25
    prev = set(data[:length])
    for i in range(length, len(data)):
        found = None
        for element in prev:
            target = data[i] - element
            if target in prev:
                found = target
                break
        if found is None:
            return data[i]

        prev.remove(data[i-length])
        prev.add(data[i])

    return None


def part_2(data, target):
    sum = 0
    queue = []
    for i in range(len(data)):
        queue.append(data[i])
        sum += data[i]

        while sum > target:
            sum -= queue[0]
            queue.pop(0)
        
        if sum == target:
            return min(queue) + max(queue)
        
    return None


def main():
    data = read_file()

    ts = time.time()
    result = part_1(data)
    print(f'Silver: {result}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    s = time.time()
    print(f'Gold: {part_2(data, result)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
