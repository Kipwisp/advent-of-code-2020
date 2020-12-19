import time
import re

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [line.strip() for line in file.readlines()]

    return result


def decompose(term, part_2):
    open = 0
    current = ''
    terms = []
    for char in term:
        if char == ' ' and open == 0:
            terms.append(current)
            current = ''
        else:
            current += char
            if char == '(':
                open += 1
            elif char == ')':
                open -= 1
                
    terms.append(current)

    for i, expr in enumerate(terms):
        if '(' in expr:
            terms[i] = str(decompose(expr[1:-1], part_2))

    if part_2:
        while '+' in terms:
            i = terms.index('+')
            t_1, op, t_2 = terms[i-1:i+2]
            terms[i-1] = str(eval(t_1 + op + t_2))
            del terms[i:i+2]
    
    result = terms[0]
    for i in range(1, len(terms)-1, 2):
        op, t = terms[i], terms[i+1]
        result = str(eval(result + op + t))

    return int(result)


def part_1(data):
    total = sum(decompose(problem, False) for problem in data)
    return total


def part_2(data):
    total = sum(decompose(problem, True) for problem in data)
    return total


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
