import numpy as np

puzzle_data = np.loadtxt('input.txt', dtype=str)

puzzle_data = [list(line) for line in puzzle_data]

puzzle_data = np.array(puzzle_data)


def part_one(data):
    gamma = ""
    for i in range(len(data[0])):
        counts = np.bincount(np.array(data[:, i], dtype=int))
        most_common = str(np.argmax(counts))
        gamma += most_common

    epsilon = int(gamma, 2) ^ int('111111111111', 2)

    return int(gamma, 2) * epsilon


print(part_one(puzzle_data))


def get_rating(data, rating):
    for i in range(len(data[0])):
        if len(data) == 1:
            break

        zero_count = 0
        one_count = 0
        for k in range(len(data)):
            if data[k, i] == '0':
                zero_count += 1
            else:
                one_count += 1

        if rating == 'oxygen':
            if zero_count == one_count:
                most_common = '1'
            elif zero_count > one_count:
                most_common = '0'
            else:
                most_common = '1'
        else:
            if zero_count == one_count:
                most_common = '0'
            elif zero_count < one_count:
                most_common = '0'
            else:
                most_common = '1'

        temp_data = []
        for j in range(len(data)):
            if data[j, i] == most_common:
                temp_data.append(data[j])
        data = np.array(temp_data, ndmin=2)

    return data


oxygen_rating = get_rating(puzzle_data, rating='oxygen').flatten()
co2_rating = get_rating(puzzle_data, rating='C02').flatten()


def merge_and_convert_to_int(np_array):
    binstring = ""
    for i in range(len(np_array)):
        binstring += np_array[i]

    return int(binstring, 2)


part_two = merge_and_convert_to_int(oxygen_rating) * merge_and_convert_to_int(co2_rating)

print(part_two)