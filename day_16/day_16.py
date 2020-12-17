import time
import math
import re

def read_file() -> tuple:
    sections = []
    with open('input.txt', 'r') as file:
        sections = [line.strip() for line in file.read().split('\n\n')]
    
    fields_section, ticket_section, nearby_section = sections

    fields = {}
    for line in fields_section.split('\n'):
        name, ranges = line.split(': ')
        ranges = re.findall('[0-9]+-[0-9]+', ranges)
        value_range = set()
        for r in ranges:
            lower, upper = r.split('-')
            value_range = value_range.union(set(range(int(lower), int(upper) + 1)))
        fields[name] = value_range

    ticket = tuple(int(i) for i in ticket_section.split('\n')[1].split(','))

    nearby = []
    for line in nearby_section.split('\n')[1:]:
        nearby_ticket = tuple(int(i) for i in line.split(','))
        nearby.append(nearby_ticket)

    return fields, ticket, nearby


def part_1(fields: dict, nearby: list) -> tuple:
    result = 0
    invalid_tickets = set()
    for nearby_ticket in nearby:
        for value in nearby_ticket:
            valid = False
            for value_range in fields.values():
                if value in value_range:
                    valid = True
                    break
            if not valid:
                result += value
                invalid_tickets.add(nearby_ticket)

    valid_tickets = set(nearby).difference(invalid_tickets)

    return result, valid_tickets


def part_2(fields: dict, ticket: tuple, nearby: list) -> int:
    column_values = [set() for i in range(len(fields))]
    for nearby_ticket in nearby:
        for i, value in enumerate(nearby_ticket):
            column_values[i].add(value)
    
    candidates = [[] for i in range(len(fields))]
    for field in fields:
        for i, column_range in enumerate(column_values):
            if column_range.issubset(fields[field]):
                candidates[i].append(field)

    columns = [None for i in range(len(fields))]
    while None in columns:
        for i, candidate_fields in enumerate(candidates):
            if len(candidate_fields) == 1:
                columns[i] = candidate_fields.pop()
            else:
                for field in candidate_fields:
                    if field in columns:
                        candidate_fields.remove(field)

    result = 1
    for i, field in enumerate(columns):
       if 'departure' in field:
            result *= ticket[i]

    return result


def main():
    fields, ticket, nearby = read_file()

    ts = time.time()
    result, valid_tickets = part_1(fields, nearby)
    print(f'Silver: {result}')
    print(f'Completed in {time.time() - ts} seconds. \n')

    nearby = valid_tickets

    ts = time.time()
    print(f'Gold: {part_2(fields, ticket, nearby)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
