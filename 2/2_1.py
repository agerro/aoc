# only decrease or increase
# only if diff is 1 < 3

reports = []

with open('input_1.txt', 'r') as file:
    for report in file:
        levels = report.split(" ")
        levels = [x.strip() for x in report.split(" ")]
        print(levels)
        #checing increasing
        increase = all(int(i) < int(j) for i, j in zip(levels, levels[1:]))
        
        # check decreasing
        decrease = all(int(i) > int(j) for i, j in zip(levels, levels[1:]))

        if increase != decrease:
            #check if not smaller than 1 or greater than 3
            diff = all(1 <= abs(int(i)-int(j)) <= 3 for i, j in zip(levels, levels[1:]))
            if diff:
                #print("safe")
                reports.append("SAFE")
            else:
                #print("OVER UNDER 1,3")
                reports.append("UNSAFE")
        else:
            #print("Not strict inc/dec")
            reports.append("UNSAFE")

#print(reports)
print(reports.count("SAFE"))
