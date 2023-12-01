import re

with open("input.txt", 'r') as f:
    lines = f.readlines()

def process_number(s):
    if len(s) == 1:
        return str(s)
    else:
        numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        return str(numbers.index(s)+1)
    
total = 0
for line in lines:
    numbers = [process_number(match) for match in re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)]
    total += int(numbers[0] + numbers[-1])
    
print(total)