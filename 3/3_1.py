import re

def find_matches(input_string):
    # Define the regex pattern
    print(input_string)
    pattern=r"mul\((\d{1,3}),(\d{1,3})\)"
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    return matches

result = []
# Example input string
with open('input_1.txt', 'r') as file:
    for stri in file:
        result.extend(find_matches(stri))

final_res = 0
# Print matches
print("Matches found:")
for x, y in result:
    print(x,y)
    final_res += int(x)*int(y)

print(final_res)
