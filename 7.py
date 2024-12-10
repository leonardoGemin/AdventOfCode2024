from aocd import get_data
from itertools import product


first: int = 0
second: int = 0


input_data: str = get_data(day=7, year=2024)


for line in input_data.splitlines():
    value: int = int(line.split(":")[0])
    equation: list[int] = list(map(int, line.split(":")[1].split()))
    
    for combination in list(product([0, 1], repeat=len(equation) - 1)):
        tmp: int = equation[0]
        for i, elem in enumerate(equation[1:]):
            if combination[i] == 0:
                tmp += elem
            else:
                tmp *= elem
        
        if tmp == value:
            first += tmp
            break

    for combination in list(product([0, 1, 2], repeat=len(equation) - 1)):
        tmp: int = equation[0]
        for i, elem in enumerate(equation[1:]):
            if combination[i] == 0:
                tmp += elem
            elif combination[i] == 1:
                tmp *= elem
            else:
                tmp = int(str(tmp) + str(elem))
        
        if tmp == value:
            second += tmp
            break


print(f"Point 1: {first}")
print(f"Point 2: {second}")
