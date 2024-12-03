input = open("data/day_2_input.txt", "r")
inputs = []
for line in input:
    inputs.append(list(map(int, line.strip().split())))


safe_count = 0
for values in inputs:
    gradual = True
    last_value = None
    asc_sorted_values = sorted(values)
    dsc_sorted_values = sorted(values, reverse=True)
    if values != asc_sorted_values and values != dsc_sorted_values:
        continue
    for value in values:
        if not last_value:
            last_value = value
            continue
        if abs(value - last_value) < 1 or abs(value - last_value) > 3:
            gradual = False
            break
        last_value = value
    if gradual:
        safe_count += 1
print(safe_count)
