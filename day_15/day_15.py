import time

def read_file() -> list:
    result = []
    with open('input.txt', 'r') as file:
        result = file.read().strip().split(',')

    return result


def part_1_2(numbers: list, index: int) -> int:
    spoken = { int(n):i for (n,i) in zip(numbers, range(1, len(numbers) + 1)) }

    last = int(numbers[-1])
    turn = len(spoken) + 1
    while turn <= index:
        if last not in spoken:
            spoken[last] = turn - 1
            last = 0
        else:
            tmp = last
            last = (turn - 1) - spoken[tmp]
            spoken[tmp] = turn - 1

        turn += 1

    return last


def main():
    numbers = read_file()

    ts = time.time()
    print(f'Silver: {part_1_2(numbers, 2020)}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    ts = time.time()
    print(f'Gold: {part_1_2(numbers, 30000000)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
