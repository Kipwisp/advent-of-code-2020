import time
import re

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [int(line.strip()) for line in file.readlines()]

    end = max(result) + 3
    result.append(0)
    result.append(end)
    vertices = set(result)
    edges = {}
    for vertex in vertices:
        edges[vertex] = set()
        for i in range(vertex + 1, vertex + 4):
            if i in vertices:
                edges[vertex].add(i)

    return (vertices, edges, end)

def part_1(vertices, edges, end):
    backpointers = {}
    worklist = []
    worklist.append((None, 0))
    while len(worklist) > 0:
        u, v = worklist.pop()

        backpointers[v] = u

        if v == end:
            break

        if v in edges:
            worklist.append((v, min(edges[v])))

    result = []
    backpointer = end
    while backpointers[backpointer] is not None:
        result.append(backpointer - backpointers[backpointer])
        backpointer = backpointers[backpointer]

    return result.count(1) * result.count(3)

def dfs(vertex, edges, memo):
    count = 0
    memo[vertex] = count

    if vertex in edges:
        for adjacent in edges[vertex]:
            if adjacent in memo:
                count += memo[adjacent]
            else:
                result = dfs(adjacent, edges, memo)
                count += result
        
        memo[vertex] = count

    return count


def part_2(vertices, edges, end):
    memo = { end: 1 }

    count = dfs(0, edges, memo)
    
    return count
    
def part_2_iterative_solution(vertices, edges, end):
    memo = { v:0 for v in vertices }
    memo[0] = 1
    worklist = []
    worklist.append((None, 0))
    while len(worklist) > 0:
        u, v = worklist.pop(-1)

        for i in range(v-3, v):
            if i in vertices:
                memo[v] += memo[i]

        if v == end:
            return memo[v]

        if v in edges:
            worklist.append((v, min(edges[v])))
    
    return None


def main():
    vertices, edges, end = read_file()

    ts = time.time()
    print(f'Silver: {part_1(vertices, edges, end)}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    ts = time.time()
    print(f'Gold: {part_2(vertices, edges, end)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
