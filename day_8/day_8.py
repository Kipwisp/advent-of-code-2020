import time

class IntCodeProcessor:
    def __init__(self, intcodes, pointer=0, acc=0):
        self.pointer = pointer
        self.acc = acc
        self.intcodes = intcodes

    def next_instr(self):
        if self.pointer >= len(self.intcodes):
            return True

        instr, value = self.intcodes[self.pointer]
        delta = 1

        if instr == 'acc':
            self.acc += value
        elif instr == 'jmp':
            delta = value

        self.pointer += delta
        return False

    def get_position(self):
        return self.pointer
    
    def get_acc(self):
        return self.acc


def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [[i, int(v)] for i, v in (line.strip().split() for line in file.readlines())]

    return result


def part_1(intcodes):
    processor = IntCodeProcessor(intcodes)
    visited = set()

    while processor.get_position() not in visited:
        visited.add(processor.get_position())
        processor.next_instr()

    return processor.get_acc()


def part_2(intcodes):
    main = IntCodeProcessor(intcodes)
    swap = {'nop': 'jmp', 'jmp': 'nop'}
    memo = set()
    seen = set()
    while main.get_position() not in seen:
        i = main.get_position()
        instr, value = intcodes[i]

        original = intcodes[i]
        if instr in swap:
            intcodes[i] = [swap[instr], value]

            alt = IntCodeProcessor(intcodes, i, main.get_acc())
            visited = set()
            while alt.get_position() not in visited:
                current = alt.get_position()
                visited.add(current)
                memo.add(current)

                result = alt.next_instr()
                if result:
                    return alt.get_acc()
                if alt.get_position() in memo:
                    break

            intcodes[i] = original

        seen.add(i)
        main.next_instr()

    return None


def main():
    intcodes = read_file()

    ts = time.time()
    print(f'Silver: {part_1(intcodes)}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    ts = time.time()
    print(f'Gold: {part_2(intcodes)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
