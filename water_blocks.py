towers = [1, 5, 3, 7, 2, 4, 5, 1]

temp = towers[0]
left = list([temp])

for i in range(1, len(towers)):
    if towers[i] > temp: 
        temp = towers[i]
        left.append(temp)
    else: left.append(temp)

print(left)

temp = towers[-1]
right = list([temp])
for i in range(len(towers)-2, -1, -1):
    if towers[i] > temp:
        temp = towers[i]
        right.insert(0, temp)
    else: 
        right.insert(0, temp)

print(right)

sum_of_water = 0

for i in range(0, len(towers)-1):
    sum_of_water += min(left[i], right[i]) - towers[i]

print(sum_of_water)