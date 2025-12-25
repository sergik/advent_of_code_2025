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
        max_chunk = len(s) // 2
        for L in range(1, max_chunk + 1):
            if len(s) % L != 0:
                continue
            chunks = [s[i:i+L] for i in range(0, len(s), L)]
            if all(ch == chunks[0] for ch in chunks):
                sum += n
                break
    
print(sum)

