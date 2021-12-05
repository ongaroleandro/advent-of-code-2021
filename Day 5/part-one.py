import re

with open('input.txt') as f:
    lines = [line.rsplit() for line in f]
    lines = [[line[0], line[2]] for line in lines]
    lines = [[line[0].split(','), line[1].split(',')] for line in lines]
    lines = [[int(line[0][0]), int(line[0][1]), int(line[1][0]), int(line[1][1])] for line in lines]
    horizontal_lines = [line for line in lines if line[1] == line[3]]
    vertical_lines = [line for line in lines if line[0] == line[2]]


# horizontal_lines = sorted(horizontal_lines, key=lambda x: x[1])


def get_start_end_coord_hor(line):
    if line[0] < line[2]:
        start = line[0]
        end = line[2]
    else:
        start = line[2]
        end = line[0]

    return start, end


def get_start_end_coord_vert(line):
    if line[1] < line[3]:
        start = line[1]
        end = line[3]
    else:
        start = line[3]
        end = line[1]

    return start, end


hor_lines_coords = []
overlapping_points = 0
for hor in horizontal_lines:
    start_coord, end_coord = get_start_end_coord_hor(hor)
    for i in range(start_coord, end_coord+1):
        current_point = (i, hor[1])
        if current_point not in hor_lines_coords:
            hor_lines_coords.append(current_point)
        else:
            overlapping_points += 1


vert_lines_coords = []
for vert in vertical_lines:
    start_coord, end_coord = get_start_end_coord_vert(vert)
    for i in range(start_coord, end_coord+1):
        current_point = (vert[0], i)
        if (current_point not in vert_lines_coords) and (current_point not in hor_lines_coords):
            vert_lines_coords.append(current_point)
        else:
            overlapping_points += 1


checked_overlapping_point = []
for coord in vert_lines_coords:
    if (coord not in checked_overlapping_point) and (coord in hor_lines_coords):
        checked_overlapping_point.append(coord)
        overlapping_points += 1


print(overlapping_points)

