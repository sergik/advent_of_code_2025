file_path = "input.txt"
with open(file_path, "r") as f:
    data = [line.strip() for line in f if line.strip()]


sum = 0
for bank in data:
    first_max = 0
    first_max_index = -1
    for i  in range(0, len(bank) -1):
        batery_voltage = int(bank[i])
        if batery_voltage > first_max:
            first_max = batery_voltage
            first_max_index = i

    second_max = 0
    for i in range(first_max_index + 1, len(bank)):
        batery_voltage = int(bank[i])
        if batery_voltage > second_max:
            second_max = batery_voltage

    voltage = first_max * 10 + second_max
    sum += voltage

print(sum)
