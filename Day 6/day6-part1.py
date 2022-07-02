import numpy as np

fish = np.loadtxt('input.txt', max_rows=1, dtype=int, delimiter=',')


simulate_days = 256

i = 0
while i < simulate_days:
    new_fish = 0
    for j in range(len(fish)):
        if fish[j] == 0:
            new_fish += 1
            fish[j] = 6
        else:
            fish[j] = fish[j] - 1

    new_fishies = np.full(new_fish, 8)
    fish = np.append(fish, new_fishies)

    i += 1

print(len(fish))