import time
import re

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def append(self, node):
        self.next = node


def read_file():
    results = []
    with open('input.txt', 'r') as file:
        results = [int(cup) for line in file.readlines() for cup in line.strip()]

    return results


def part_1(cups):
    low, high = min(cups), max(cups)
    current = cups[0]
    for moves in range(100):
        next_three = [cups[(cups.index(current)+i)%len(cups)] for i in range(1,4)]
        for cup in next_three:
            cups.remove(cup)

        destination = current - 1 if current > low else high
        while destination in next_three:
            destination = destination - 1 if destination > low else high
        
        j = cups.index(destination)
        cups = cups[:j+1] + next_three + cups[j+1:]

        current = cups[(cups.index(current) + 1) % len(cups)]

    return ''.join(str(i) for i in (cups[cups.index(1) + 1:] + cups[:cups.index(1)]))


def part_2(initial):
    full = initial + [x for x in range(max(initial) + 1, 1000001)]
    cups = { }

    cups[initial[0]] = Node(initial[0])
    for i, cup in enumerate(full[1:], 1):
        cups[cup] = Node(cup)
        cups[full[i-1]].append(cups[cup])
    cups[full[-1]].append(cups[initial[0]])

    low, high = min(initial), full[-1]
    current = cups[initial[0]]
    for moves in range(10000000):
        first = current.next
        second = first.next
        third = second.next

        destination = current.data - 1 if current.data > low else high
        while destination in { first.data, second.data, third.data }:
            destination = destination - 1 if destination > low else high
        
        destination = cups[destination]

        tmp = third.next
        current.append(tmp)
        
        last = destination.next
        destination.append(first)
        third.append(last)

        current = cups[current.next.data]

    return cups[1].next.data * cups[1].next.next.data


def main():
    cups = read_file()
    ts = time.time()
    print(f'Silver: {part_1(cups)}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    cups = read_file()
    ts = time.time()
    print(f'Gold: {part_2(cups)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
