# only decrease or increase
# only if diff is 1 < 3

reports = []

def is_safe(report_levels):
    report_safe = True
    print(report_levels)
    #checing increasing
    increase = all(int(i) < int(j) for i, j in zip(report_levels, report_levels[1:]))
    
    # check decreasing
    decrease = all(int(i) > int(j) for i, j in zip(report_levels, report_levels[1:]))

    if increase != decrease:
        #check if not smaller than 1 or greater than 3
        diff = all(1 <= abs(int(i)-int(j)) <= 3 for i, j in zip(report_levels, report_levels[1:]))
        if diff:
            print("safe")
            report_safe *= True
        else:
            print("OVER UNDER 1,3")
            report_safe *= False
    else:
        print("Not strict inc/dec")
        report_safe *= False
    return report_safe

with open('input_1.txt', 'r') as file:
    for report in file:
        bad_report = 0
        levels = report.split(" ")
        levels = [x.strip() for x in report.split(" ")]
        report_total_safe = True

        report_total_safe *= is_safe(levels)

        if not report_total_safe:
            for level in range(len(levels)):
                temp_levels = levels.copy()
                temp_levels.pop(level)
                if is_safe(temp_levels):
                    report_total_safe = True
                    break
        if report_total_safe:
            reports.append("SAFE")
        else:
            reports.append("UNSAFE")

print(reports)
print(reports.count("SAFE"))
