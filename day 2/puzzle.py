with open('input.txt') as f:
    inputs = [line.split() for line in f]


def part_one(commands):
    position = 0
    depth = 0

    for command in commands:
        if command[0] == 'forward':
            position += int(command[1])
        if command[0] == 'down':
            depth += int(command[1])
        if command[0] == 'up':
            depth -= int(command[1])

    return position*depth


def part_two(commands):
    position = 0
    depth = 0
    aim = 0

    for command in commands:
        if command[0] == 'forward':
            position += int(command[1])
            depth += aim * int(command[1])
        if command[0] == 'down':
            aim += int(command[1])
        if command[0] == 'up':
            aim -= int(command[1])

    return position * depth


print(part_one(inputs))
print(part_two(inputs))
