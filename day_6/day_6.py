import time

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [line.strip().split() for line in file.read().split('\n\n')]

    return result


def count_answers_part_1(groups):
    count = 0
    for group in groups:
        answers = [set(x) for x in group]
        count += len(set.union(*answers))

    return count


def count_answers_part_2(groups):
    count = 0
    for group in groups:
        answers = [set(x) for x in group]
        count += len(set.intersection(*answers))
    
    return count


def main():
    groups = read_file()

    ts = time.time()
    print(f'Silver: {count_answers_part_1(groups)}')
    print(f'Completed in {time.time() - ts} seconds. \n')
    
    ts = time.time()
    print(f'Gold: {count_answers_part_2(groups)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
