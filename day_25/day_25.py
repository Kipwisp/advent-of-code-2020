
import time

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [int(line.strip()) for line in file.readlines()]

    return result


def part_1(card, door):
    loops = 0
    value = 1
    while value != card:
        value *= 7
        value = value % 20201227
        loops += 1

    value = 1
    for i in range(loops):
        value *= door
        value = value % 20201227

    return value


def main():
    card, door = read_file()

    ts = time.time()
    print(f'Silver: {part_1(card, door)}')
    print(f'Completed in {time.time() - ts} seconds. \n')


if __name__ == '__main__':
    main()
