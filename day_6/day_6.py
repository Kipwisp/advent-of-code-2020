import time

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [line.strip().split() for line in file.read().split('\n\n')]

    return result


def count_answers_part_1(answers):
    count = 0
    for group in answers:
        count += len(set([answer for person in group for answer in person]))

    return count


def count_answers_part_2(answers):
    count = 0
    
    for group in answers:
        answers_given = [answer for person in group for answer in person]
        available = set([answer for person in group for answer in person])

        for letter in available:
            if answers_given.count(letter) == len(group):
                count += 1
    
    return count


def main():
    answers = read_file()

    ts = time.time()
    print(f'Silver: {count_answers_part_1(answers)}')
    print(f'Completed in {time.time() - ts} seconds. \n')
    
    ts = time.time()
    print(f'Gold: {count_answers_part_2(answers)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
