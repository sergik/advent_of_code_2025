file_path = "input.txt"

with open(file_path, "r") as f:
    line = f.readline().strip()

data = [item.strip() for item in line.split(",") if item.strip()]



sum = 0

for item in data:
    try:
        a, b = item.split("-", 1)
        start, end = int(a), int(b)
    except ValueError:
        print(f"Skipping invalid item: {item}")
        continue

  
    step = 1
    for n in range(start, end + step, step):
        s = str(n)
     
        if len(s) % 2 == 0:
            half = len(s) // 2
            first_half = s[:half]
            second_half = s[half:]
            if(first_half == second_half):
                sum += n
    
print(sum)

