import time

class IntCodeProcessor:
    def __init__(self, intcodes):
        self.acc = 0
        self.pointer = 0
        self.intcodes = intcodes

    def next_instr(self):
        if self.pointer == len(self.intcodes):
            return True

        instr, value = self.intcodes[self.pointer]

        if instr == 'acc':
            self.acc += value
            self.pointer += 1
        elif instr == 'jmp':
            self.pointer += value
        elif instr == 'nop':
            self.pointer += 1
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
    for i, instruction in enumerate(intcodes):
        intcodes_modified = intcodes.copy()
        instr, value = instruction

        if instr == 'nop':
            intcodes_modified[i] = ['jmp', value]
        elif instr == 'jmp':
            intcodes_modified[i] = ['nop', value]
        else:
            continue

        processor = IntCodeProcessor(intcodes_modified)
        
        visited = set()
        while processor.get_position() not in visited:
            visited.add(processor.get_position())
            result = processor.next_instr()

            if result:
                return processor.get_acc()

    return None


def main():
    intcodes = read_file()

    ts = time.time()
    print(f'Silver: {part_1(intcodes)}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    s = time.time()
    print(f'Gold: {part_2(intcodes)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
