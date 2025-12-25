import math
file_path = "input.txt"

with open(file_path, "r") as f:
    data = [line.strip() for line in f if line.strip()]

current_val = 50

zeros_count = 0

for val in data:
    op = val[0]
    num = int(val[1:]) if len(val) > 1 else 0
    num = num % 100

    if(op == 'R'):
        current_val += num
    else:
        current_val -= num

    if(current_val < 0):
        current_val = 100 + current_val

    current_val = current_val % 100

    if current_val == 0:
        zeros_count += 1
    
print(zeros_count)