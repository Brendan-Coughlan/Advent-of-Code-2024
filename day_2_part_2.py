def check_report(levels: list, dampened_check : bool) -> bool:
    # 0 == Left & 1 == Right
    direction = False if levels[1] - levels[0] < 0 else True
    safe = True
    was_dampened = False
    for i in range(1, len(levels)):
        if abs(levels[i] - levels[i - 1]) < 1 or abs(levels[i] - levels[i - 1]) > 3:
            if was_dampened or dampened_check:
                safe = False
                break
            else:
                dampened_levels = levels.copy()
                dampened_levels.remove(levels[i])
                if check_report(dampened_levels, True):
                    was_dampened = True
                    continue
                else:
                    safe = False
                    break

        current_direction = None
        if levels[i] - levels[i - 1] < 0:
            current_direction = False
        else:
            current_direction = True

        if direction != current_direction:
            if was_dampened or dampened_check:
                safe = False
                break
            else:
                dampened_levels = levels.copy()
                dampened_levels.remove(levels[i])
                if check_report(dampened_levels, True):
                    was_dampened = True
                    continue
                else:
                    safe = False
                    break
    return safe

input = open("data/day_2_input.txt", "r")
reports = []
for line in input:
    reports.append(list(map(int, line.strip().split())))

# reports = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9],
# ]

safe_count = 0
for levels in reports:
    if check_report(levels, False):
        print(levels)
        safe_count += 1
print(safe_count)
