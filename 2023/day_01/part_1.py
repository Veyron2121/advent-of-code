import re

with open("input.txt", 'r') as f:
    lines = f.readlines()

total = 0
for line in lines:
    numbers = [str(match) for match in re.findall(r"\d", line)]
    total += int(numbers[0] + numbers[-1])
    
print(total)
