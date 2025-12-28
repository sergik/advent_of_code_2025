file_path = "input.txt"
from collections import deque


with open(file_path, "r") as f:
    lines = [line.rstrip('\n') for line in f if line.rstrip('\n') != ""]

data = [line.split(" ") for line in lines]

def get_key(state):
    return "".join(map(str,state))



res = 0
for index in range(len(data)):
    line = data[index]
    print(index)
    joltage = [int(x) for x in line[-1][1:len(line[-1])-1].split(',')]
    buttons = line[1:len(line)-1]
    buttons = [[int(x) for x in b[1:len(b)-1].split(',')] for b in buttons]
    queue = deque()
    queue.append((0, joltage))

    reached_at = -1

    visited = set()
    while len(queue) > 0:
        step, current_state = queue.popleft()
        if all(x == 0 for x in current_state):
            reached_at = step
            break

        if any(x < 0 for x in current_state):
            continue
        print("Step:", step)
        for button in buttons:
            new_state = current_state.copy()
            for i in button:
               new_state[i] -= 1
            if get_key(new_state) in visited:
                continue
            queue.append((step + 1, new_state))
            visited.add(get_key(new_state))
            
    res += reached_at

print(res)






