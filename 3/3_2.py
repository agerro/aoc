import re

do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

def find_matches(input_string):
    # Define the regex pattern
    #print(input_string)
    pattern=r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    return matches

result = []
total_string = ""

with open('input_2.txt', 'r') as file:
    for stri in file:
        total_string += stri

sections = re.split(f"({dont_pattern}|{do_pattern})", total_string)

should_add = True
final_sec = []
for sect in sections:
    if str(sect) in ["don't()"]:
        should_add = False
    elif str(sect) in ["do()"]:
        should_add = True
    
    if should_add:
        if str(sect) not in ["do()","don't()"]:
            final_sec.append(sect)
print(len(final_sec))

for section in range(len(final_sec)):
    print(final_sec[section])
    result.extend(find_matches(final_sec[section]))

final_res = 0
# Print matches
print("Matches found:")
for x, y in result:
    #print(x,y)
    final_res += int(x)*int(y)

print(final_res)
