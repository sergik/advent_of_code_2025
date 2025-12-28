file_path = "input.txt"



with open(file_path, "r") as f:
    lines = [line.rstrip('\n') for line in f if line.rstrip('\n') != ""]

data = [line.split(" ") for line in lines]

def get_key(state):
    return "".join(state)


res = 0
for index in range(len(data)):
    line = data[index]
    print(index)
    lights = list(line[0][1:len(line[0])-1])
    buttons = line[1:len(line)-1]
    buttons = [[int(x) for x in b[1:len(b)-1].split(',')] for b in buttons]
    initial_state = ['.'] * len(lights)
    visited = {}
    stack = [(0, initial_state)]

    while len(stack) > 0:
        step, current_state = stack.pop()
        key = get_key(current_state)
        if key in visited:
            val = visited[key]
            if val <= step:
                continue
            
        visited[key] = step
        for button in buttons:
            new_state = current_state.copy()
            for i in button:
              
               
                if new_state[i] == '.':
                    new_state[i] = '#'
                else:
                    new_state[i] = '.'
            stack.append((step + 1, new_state))
   
    # def solve_recursive(step, current_state):
    #     key = get_key(current_state)
    #     if key in visited:
    #         val = visited[key]
    #         if val <= step:
    #             return
            
    #     visited[key] = step
    #     for button in buttons:
    #         new_state = current_state.copy()
    #         for i in button:
              
               
    #             if new_state[i] == '.':
    #                 new_state[i] = '#'
    #             else:
    #                 new_state[i] = '.'
    #         solve_recursive(step + 1, new_state)
               
    #solve_recursive(0, initial_state)
    res += visited[get_key(lights)]

print(res)






