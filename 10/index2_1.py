file_path = "input.txt"



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

    return solutions

big_num = 9999999

def solve_joltage(joltage, buttons) -> int:
    solved_joltages = {}
    def solve_recursive(joltage, buttons) -> int:
        if(any(x < 0 for x in joltage)):
            return big_num
        if(all(x == 0 for x in joltage)):
            return 0

        if(all(x % 2 == 0 for x in joltage)):
            new_joltage = [x // 2 for x in joltage]
            return 2 * solve_recursive(new_joltage, buttons)


    
        mask = []
        for x in joltage:
            if x % 2 == 1:
                mask.append('#')
                
            else:
                mask.append('.')
        
        solutions = solve_mask(buttons, mask)
        if(len(solutions) == 0):
            return big_num
        
        min_sol = big_num
        for s in solutions:
            new_joltage = joltage.copy()

            for btnIndex in s:
                for ji in buttons[btnIndex]:
                    new_joltage[ji] -= 1
            key = "_".join(map(str, new_joltage))
            if key not in solved_joltages:
                solved_joltages[key] = solve_recursive(new_joltage, buttons)
         
            res = solved_joltages[key]
            min_sol = min(min_sol, res + len(s))

        
        return min_sol
    return solve_recursive(joltage, buttons)



res = 0
for index in range(len(data)):
    line = data[index]
    joltage = [int(x) for x in line[-1][1:len(line[-1])-1].split(',')]
    buttons = line[1:len(line)-1]
    buttons = [[int(x) for x in b[1:len(b)-1].split(',')] for b in buttons]
    res_x = solve_joltage(joltage, buttons)
    print(res_x)
    res += res_x

print(res)






