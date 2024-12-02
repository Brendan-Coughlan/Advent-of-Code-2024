left_input = []
right_input = []

input = open("input.txt", "r")
for line in input:
    line_input = line.strip().split()
    left_input.append(int(line_input[0]))
    right_input.append(int(line_input[1]))

similarity_score = 0
list_size = len(left_input)

for i in range(list_size):
    value = left_input[i]
    occurences = right_input.count(value)
    similarity_score += value * occurences
    
print(similarity_score)