import time

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = file.readlines()

    return result


def count_valid_part_1(passwords):
    count = 0

    for password in passwords:
        low, high, letter, word = password.replace('-', ' ').replace(':', ' ').split()
        low, high = int(low), int(high)

        if (high >= word.count(letter) >= low):
            count += 1

    return count


def count_valid_part_2(passwords):
    count = 0

    for password in passwords:
        pos1, pos2, letter, word = password.replace('-', ' ').replace(':', ' ').split()
        pos1, pos2 = int(pos1) - 1, int(pos2) - 1

        if ((word[pos1] == letter) ^ (word[pos2] == letter)):
            count += 1

    return count


def main():
    passwords = read_file()

    ts = time.time()
    print(f'Silver: {count_valid_part_1(passwords)}')
    print(f'Completed in {time.time() - ts} seconds. \n')
    
    ts = time.time()
    print(f'Gold: {count_valid_part_2(passwords)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
