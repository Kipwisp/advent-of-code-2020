import time

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = [line.strip() for line in file.readlines()]

    return result


def check_passes_part_1(passes):
    seat_ids = []
    row_size = 2 ** (passes[0].count('F') + passes[0].count('B')) - 1
    col_size = 2 ** (passes[0].count('L') + passes[0].count('R')) - 1

    for boarding_pass in passes:
        seat_rows = (0, row_size)
        seat_columns = (0, col_size)

        for char in boarding_pass:
            middle_row = seat_rows[0] + (seat_rows[1] - seat_rows[0]) // 2
            middle_column = seat_columns[0] + (seat_columns[1] - seat_columns[0]) // 2

            if char == 'F':
                seat_rows = (seat_rows[0], middle_row)
            elif char == 'B':
                seat_rows = (middle_row, seat_rows[1])
            elif char == 'R':
                seat_columns = (middle_column, seat_columns[1])
            else:
                seat_columns = (seat_columns[0], middle_column)

        seat_ids.append(seat_rows[1] * (col_size + 1) + seat_columns[1])

    return(max(seat_ids))


def check_passes_part_2(passes):
    row_size = 2 ** (passes[0].count('F') + passes[0].count('B')) - 1
    col_size = 2 ** (passes[0].count('L') + passes[0].count('R')) - 1
    seat_ids = { i: False for i in range(row_size * col_size) }

    for boarding_pass in passes:
        seat_rows = (0, row_size)
        seat_columns = (0, col_size)

        for char in boarding_pass:
            middle_row = seat_rows[0] + (seat_rows[1] - seat_rows[0]) // 2
            middle_column = seat_columns[0] + (seat_columns[1] - seat_columns[0]) // 2

            if char == 'F':
                seat_rows = (seat_rows[0], middle_row)
            elif char == 'B':
                seat_rows = (middle_row, seat_rows[1])
            elif char == 'R':
                seat_columns = (middle_column, seat_columns[1])
            else:
                seat_columns = (seat_columns[0], middle_column)

        seat_ids[seat_rows[1] * (col_size + 1) + seat_columns[1]] = True

    missing_seats = dict(filter(lambda e: not e[1], seat_ids.items()))

    for missing_seat in missing_seats:
        try:
            if seat_ids[missing_seat - 1] and seat_ids[missing_seat + 1]:
                return missing_seat
        except KeyError:
            continue

    return None

def main():
    passes = read_file()

    ts = time.time()
    print(f'Silver: {check_passes_part_1(passes)}')
    print(f'Completed in {time.time() - ts} seconds. \n')
    
    ts = time.time()
    print(f'Gold: {check_passes_part_2(passes)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
