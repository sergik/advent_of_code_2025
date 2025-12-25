file_path = "input.txt"
with open(file_path, "r") as f:
    data = [line.strip() for line in f if line.strip()]


sum = 0
for bank in data:
    start_index = -1
    voltages = []
    for num in range(11, -1, -1):
        max_for_index = 0
        index_of_max_for_index = start_index
        
        for i  in range(start_index + 1, len(bank) - num):
            batery_voltage = int(bank[i])
            if batery_voltage > max_for_index:
                max_for_index = batery_voltage
                index_of_max_for_index = i

        voltages.append(max_for_index)
        sum += max_for_index * (10 ** num)
        start_index = index_of_max_for_index
    print(voltages)

print(sum)
