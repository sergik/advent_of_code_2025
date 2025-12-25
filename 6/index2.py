file_path = "input.txt"

with open(file_path, "r") as f:
    lines = [line.rstrip("\n") for line in f]



numbers = lines[:len(lines)-1]
operations = lines[-1].strip().split()
input_length = len(numbers[0])

current_operator = operations[-1]
operators_index = len(operations) - 1
current_subresult = 0 if current_operator == '+' else 1

result = 0

for i in range(input_length-1, -1, -1):
    current_expression = []
    for j in range(len(numbers)):
        if numbers[j][i] != ' ':
            current_expression.append(int(numbers[j][i]))

    if len(current_expression) != 0:
        next_number = 0
        for k in range(len(current_expression)):
            next_number = next_number * 10 + current_expression[k]
        if current_operator == '+':
            current_subresult += next_number
        else:
            current_subresult *= next_number
    else:
        print(current_subresult)
        result += current_subresult
        operators_index -= 1
        current_operator = operations[operators_index]
        current_subresult = 0 if current_operator == '+' else 1

result += current_subresult

print(result)


