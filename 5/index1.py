file_path = "input.txt"

with open(file_path, "r") as f:
    lines = [line.rstrip("\n") for line in f]

# Split on the first empty line: everything before -> `left`, everything after -> `right`.
sep = 0
for i, line in enumerate(lines):
    if line.strip() == "":
        sep = i
        break
    
str_ranges = [line.strip() for line in lines[:sep] if line.strip()]
ids = [int(line.strip()) for line in lines[sep + 1:] if line.strip()]

ranges = []
for str_range in str_ranges:
    a, b = str_range.split("-", 1)
    start, end = int(a), int(b)
    ranges.append([start, end])


ranges.sort(key=lambda r: r[0])


# Merge overlapping or adjacent intervals
merged = []
for start, end in ranges:
    if not merged:
        merged.append([start, end])
        continue
    last_start, last_end = merged[-1]
    if start <= last_end + 1:  # overlap or adjacent
        merged[-1][1] = max(last_end, end)
    else:
        merged.append([start, end])

sum = 0
for id in ids:
    for start, end in merged:
        if start <= id <= end:
            sum += 1
            break

print(sum)
