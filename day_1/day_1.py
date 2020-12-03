import time

def read_file():
    result = []
    with open('input.txt', 'r') as file:
        result = file.readlines()

    return list(map(lambda x : int(x), result))


def find_2020_part_1(nums):
    hashtable = {}

    for num in nums:
        hashtable[num] = num

    for num in nums:
        target = 2020 - num
        if (target == num):
            continue

        if (target in hashtable):
            return num * target

    return None


def find_2020_part_2(nums):
    hashtable = {}

    for num in nums:
        hashtable[num] = num

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            target = 2020 - nums[i] - nums[j]
            if (target == nums[i] or target == nums[j]):
                 continue

            if (target in hashtable):
                return nums[i] * nums[j] * target

    return None


def main():
    nums = read_file()

    ts = time.time()
    print(f'Silver: {find_2020_part_1(nums)}')
    print(f'Completed in {time.time() - ts} seconds. \n')
    
    ts = time.time()
    print(f'Gold: {find_2020_part_2(nums)}')
    print(f'Completed in {time.time() - ts} seconds.')


if __name__ == '__main__':
    main()
