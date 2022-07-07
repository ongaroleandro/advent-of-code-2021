import numpy as np

positions = np.loadtxt('input.txt', max_rows=1, dtype=int, delimiter=',')

most_common_position = np.bincount(positions).argmax()

print(most_common_position)


def sum_consecutive_numbers(n):
    return (n*(n+1))/2


def get_total_fuel_for_position(array, position):
    total_fuel = 0
    for i in range(len(array)):
        total_fuel = total_fuel + sum_consecutive_numbers(abs(array[i]-position))

    return total_fuel


optimal_found = False
current_best_position = most_common_position
current_best_total_fuel = 0
look_ahead = True
i = 1
while not optimal_found:
    total_fuel = get_total_fuel_for_position(positions, current_best_position)
    current_best_total_fuel = total_fuel
    if look_ahead:
        new_total_fuel = get_total_fuel_for_position(positions, current_best_position+i)

        if new_total_fuel < total_fuel:
            current_best_position += i
            current_best_total_fuel = new_total_fuel
        else:
            look_ahead = False
    else:
        new_total_fuel = get_total_fuel_for_position(positions, current_best_position-i)

        if new_total_fuel < total_fuel:
            current_best_position -= i
            current_best_total_fuel = new_total_fuel
        else:
            optimal_found = True

print(current_best_position, current_best_total_fuel)