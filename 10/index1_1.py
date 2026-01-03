file_path = "example.txt"



with open(file_path, "r") as f:
    lines = [line.rstrip('\n') for line in f if line.rstrip('\n') != ""]

data = [line.split(" ") for line in lines]

def get_key(state):
    return "".join(state)

def all_elements_equal(arr1, arr2):
    return len(arr1) == len(arr2) and all(a == b for a, b in zip(arr1, arr2))
def solve_mask(buttons, pattern):
    solutions = []
    def solve_recursive(index, button_indexes):
        if index == len(buttons):
            state = ['.'] * len(pattern)
            for bi in button_indexes:
                btn = buttons[bi]
                for si in btn:
                    if state[si] == '.':
                        state[si] = '#'
                    else:
                        state[si] = '.'
            
            if(all_elements_equal(pattern, state)):
                solutions.append(button_indexes.copy())
            return
        
        button_indexes.append(index)
        solve_recursive(index + 1, button_indexes)
        button_indexes.pop()
        solve_recursive(index + 1, button_indexes)

    solve_recursive(0, [])

    print(pattern)
    print(solutions)

    min_len = 999999999
    for s in solutions:
        min_len = min(len(s), min_len)

    return min_len


res = 0
for index in range(len(data)):
    line = data[index]
    lights = list(line[0][1:len(line[0])-1])
    buttons = line[1:len(line)-1]
    buttons = [[int(x) for x in b[1:len(b)-1].split(',')] for b in buttons]

    res += solve_mask(buttons, lights)

    

print(res)






