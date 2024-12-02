left = []
right = []

with open('input_1.txt', 'r') as file:
    for line in file:
        li = line.split("   ")
        left.append(li[0].strip())
        right.append(li[1].strip())

total = 0
#left.sort()
#right.sort()

for number in range(len(left)):
    occur = right.count(left[number])
    score = int(left[number])*occur
    total += score

print(total)