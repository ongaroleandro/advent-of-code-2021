import numpy as np

with open('input.txt') as f:
    lines = [line.rsplit() for line in f]
    lines = [[line[0], line[2]] for line in lines]
    lines = [[line[0].split(','), line[1].split(',')] for line in lines]
    lines = [[int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1])] for line in lines]

grid = np.zeros([1000, 1000], dtype=int)
for line in lines:
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]

    if x1 == x2:
        grid[min(y1, y2):max(y1, y2)+1, x1] += 1

    elif y1 == y2:
        grid[y1, min(x1, x2):max(x1, x2)+1] += 1

    else:
        x_coords = range(min(x1, x2), max(x1, x2)+1)
        if x2 < x1:
            x_coords = x_coords[::-1]
        y_coords = range(min(y1, y2), max(y1, y2)+1)
        if y2 < y1:
            y_coords = y_coords[::-1]

        zipped_coords = zip(x_coords, y_coords)

        for coords in zipped_coords:
            grid[coords[1], coords[0]] += 1

print(grid)
overlapping_points = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i, j] > 1:
            overlapping_points += 1

print(overlapping_points)
