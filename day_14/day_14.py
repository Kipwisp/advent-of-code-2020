import time
import re

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [line.strip().split(' = ') for line in file.readlines()]

    return result


def part_1(instructions):
    mask = ''
    registers = {}
    for op, value in instructions:
        if op == 'mask':
            mask = value
        else:
            slot = int(re.search('[0-9]+', op).group())
            value = bin(int(value))[2:]
            
            masked_value = ''
            offset = len(mask) - len(value)
            for i, bit in enumerate(mask):
                if bit == 'X':
                    masked_value += '0' if i < offset else value[i - offset]
                else:
                    masked_value += bit
    
            registers[slot] = int(masked_value, 2)
    
    return sum(registers.values())


def part_2(instructions):
    mask = ''
    registers = {}
    for op, value in instructions:
        if op == 'mask':
            mask = value
        else:
            slot = bin(int(re.search('[0-9]+', op).group()))[2:]
            value = int(value)

            floating_bits = []
            masked_address = ''
            offset = len(mask) - len(slot)
            for i, bit in enumerate(mask):
                if bit == 'X':
                    floating_bits.append(i)
                    masked_address += bit
                else:
                    masked_address += bit if i < offset else str(int(bit) | int(slot[i - offset]))
            

            results = [list(masked_address)]
            for i in floating_bits:
                addresses = []
                for address in results:
                    for bit in ('0', '1'):
                        bits = address.copy()
                        bits[i] = bit
                        addresses.append(bits)
                results = addresses
            
            for address in results:
                registers[int(''.join(address), 2)] = value

    return sum(registers.values())


def main():
    instructions = read_file()

    ts = time.time()
    print(f'Silver: {part_1(instructions)}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    ts = time.time()
    print(f'Gold: {part_2(instructions)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
