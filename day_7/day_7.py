import time
import re

def read_file():
    result = []
    with open('day_7/input.txt', 'r') as file:
        result = [line.strip().replace('contain', ',').replace('.', '').split(',') for line in file.readlines()]

    vertices = set()
    edges = {}
    for bag in result:
        vertex = bag[0].strip()
        vertices.add(vertex)

        for adjacent in bag[1:]:
            weight = re.search('[0-9]+', adjacent)
            if weight is None:
                continue
            else:
                weight = weight.group()

            if weight == '1':
                adjacent = adjacent + 's'

            if vertex not in edges:
                edges[vertex] = []

            edges[vertex].append((adjacent.replace(weight, '').strip(), int(weight)))

    return (vertices, edges)


def count_bags_part_1(vertices, edges):
    count = 0
    for vertex in vertices - {'shiny gold bags'}:
        worklist = []
        worklist.append(vertex)
        while len(worklist) > 0:
            v = worklist.pop()
            if v == 'shiny gold bags':
                count += 1
                break

            adjacent = []
            if v in edges:
                for edge in edges[v]:
                    adjacent.append(edge[0])

            for adj in adjacent:
                worklist.append(adj)

    return count


def count_bags_part_2(vertices, edges):
    count = 0
    worklist = []
    worklist.append('shiny gold bags')
    while len(worklist) > 0:
        v = worklist.pop()

        adjacent = []
        if v in edges:
            for edge in edges[v]:
                for _ in range(edge[1]):
                    adjacent.append(edge[0])

        for adj in adjacent:
            worklist.append(adj)
            count += 1

    return count


def main():
    vertices, edges = read_file()

    ts = time.time()
    print(f'Silver: {count_bags_part_1(vertices, edges)}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    s = time.time()
    print(f'Gold: {count_bags_part_2(vertices, edges)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
