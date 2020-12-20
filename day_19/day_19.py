
import time
import re

def read_file():
    rules, messages = '', ''
    with open('input.txt', 'r') as file:
        rules, messages = file.read().split('\n\n')

    result = {}
    for rule in rules.split('\n'):
        key, value = rule.split(': ')
        result[key] = value.replace('"', '').split(" | ")

    return result, messages.split()


def dfs(rule, rules, memo):
    memo[rule] = set()
    for option in rules[rule]:
        results = set([''])
        for subrule in option.split(' '):
            if subrule.isalpha():
                new = set()
                for result in results:
                    new.add(result + subrule)
                results = new
            else:
                if subrule not in memo:
                    dfs(subrule, rules, memo)

                new = set()
                for string in memo[subrule]:
                    for result in results:
                        new.add(result + string)
                results = new
            
        memo[rule].update(results)


def part_1(rules, messages):
    memo = {}

    dfs('0', rules, memo)

    match = 0
    for message in messages:
        if message in memo['0']:
            match += 1
    return match, memo


def part_2(memo, messages):
    length_42 = len(list(memo['42'])[0])
    length_31 = len(list(memo['31'])[0])
    match = 0
    for message in messages:
        if message in memo['0']:
            match += 1
        else:
            i = length_31
            l = len(message)
            c1 = 0
            while message[l - i: l - i + length_31] in memo['31']:
                c1 += 1
                i += length_31

            if c1 == 0:
                continue

            c2 = 0
            while message[l - i: l - i + length_42] in memo['42']:
                c2 += 1
                i += length_42

            if i - length_42 != l:
                continue

            if c2 > c1:
                match += 1

    return match


def main():
    rules, messages = read_file()

    ts = time.time()
    result, memo = part_1(rules, messages)
    print(f'Silver: {result}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    ts = time.time()
    print(f'Gold: {part_2(memo, messages)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
