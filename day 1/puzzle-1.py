with open('input-puzzle-1.txt', 'r') as f:
    measurements = [int(line.rstrip()) for line in f]

count = 0
for i in range(len(measurements)-1):
    if measurements[i+1] > measurements[i]:
        count += 1
print(count)


count = 0
for i in range(len(measurements)-3):
    sum_first_window = measurements[i] + measurements[i+1] + measurements[i+2]
    sum_second_window = measurements[i+1] + measurements[i+2] + measurements[i+3]
    if sum_second_window > sum_first_window:
        count += 1
print(count)
