left = []
right = []

with open('input_1.txt', 'r') as file:
    for line in file:
        li = line.split("   ")
        left.append(li[0])
        right.append(li[1])

total = 0
left.sort()
right.sort()

for number in range(len(left)):
    diff = int(left[number])-int(right[number])
    total += abs(diff)

print(total)