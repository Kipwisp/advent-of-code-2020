import time
import re

def read_file():
    lines = []
    with open('input.txt', 'r') as file:
        lines = [line.strip() for line in file.readlines()]

    result = [{}]
    for line in lines:
        if (len(line) == 0):
            result.append({})
            continue

        fields = line.split(' ')
        for field in fields:
            key, value = field.split(':')
            result[len(result) - 1][key] = value

    return result


def count_valid_part_1(passports):
    count = 0
    fields = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }

    for passport in passports:
        keys = set(passport.keys())
        keys.discard('cid')
        if keys == fields:
            count += 1
    
    return count
    

def count_valid_part_2(passports):
    count = 0
    fields = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' }

    for passport in passports:
        keys = set(passport.keys())
        keys.discard('cid')
        if not keys == fields: continue

        if not 2002 >= int(passport['byr']) >= 1920: continue
        if not 2020 >= int(passport['iyr']) >= 2010: continue
        if not 2030 >= int(passport['eyr']) >= 2020: continue
        
        if 'cm' in passport['hgt']:
            if not 193 >= int(passport['hgt'][:-2]) >= 150: continue
        elif 'in' in passport['hgt']:
            if not 76 >= int(passport['hgt'][:-2]) >= 59: continue
        else:
            continue

        if not re.match('^#[a-f0-9]{6}$', passport['hcl']): continue
        if not passport['ecl'] in { 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth' }: continue
        if not re.match('^[0-9]{9}$', passport['pid']): continue

        count += 1
    
    return count


def main():
    passports = read_file()

    ts = time.time()
    print(f'Silver: {count_valid_part_1(passports)}')
    print(f'Completed in {time.time() - ts} seconds. \n')
    
    ts = time.time()
    print(f'Gold: {count_valid_part_2(passports)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
