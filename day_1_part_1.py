left_input = []
right_input = []

input = open("data/day_1_input.txt", "r")
for line in input:
    line_input = line.strip().split()
    left_input.append(int(line_input[0]))
    right_input.append(int(line_input[1]))

total_distance = 0
list_size = len(left_input)

for i in range(list_size):
    smallest_left = min(left_input)
    left_input.remove(smallest_left)
    smallest_right = min(right_input)
    right_input.remove(smallest_right)
    distance = abs(smallest_right - smallest_left)
    total_distance += distance

print(total_distance)