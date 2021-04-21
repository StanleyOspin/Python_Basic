# way_1

line_1 = list(range(160, 177, 2))
line_2 = list(range(162, 181, 3))
line_1.extend(line_2)
line_1.sort()
print(line_1)

# way_2

line_1 = list(range(160, 177, 2))
line_2 = list(range(162, 181, 3))
line_1.extend(line_2)

sorted = True

while sorted:
    sorted = False
    for item in range(len(line_1) - 1):
        if line_1[item] > line_1[item + 1]:
            line_1[item], line_1[item + 1] = line_1[item + 1], line_1[item]

            sorted = True

print(line_1)
