import numpy as np

with open('input.txt') as f:
    input = [line.split(',') for line in f][0]
    input = [int(x) for x in input]

fish = np.array([input.count(8),
                 input.count(7),
                 input.count(6),
                 input.count(5),
                 input.count(4),
                 input.count(3),
                 input.count(2),
                 input.count(1),
                 input.count(0),
                 0], dtype='int64')

print(fish)

elapsed_days = 0
while elapsed_days < 256:
    for i in range(len(fish)-1, 0, -1):
        fish[i] = fish[i-1]

    fish[0] = fish[9]
    fish[2] = fish[2] + fish[9]
    
    elapsed_days += 1
fish[9] = 0

print(np.sum(fish))