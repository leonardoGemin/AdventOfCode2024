from aocd import get_data


input_data: str = get_data(day=11, year=2024)


already_visited: dict[tuple[int, int], int] = {}
def blink(num: int, iterations: int) -> int:
    if (num, iterations) in already_visited:
        return already_visited[(num, iterations)]
    
    if iterations == 0:
        already_visited[(num, iterations)] = 1
        return 1
    
    if num == 0:
        tmp: int = blink(1, iterations - 1)
        already_visited[(num, iterations)] = tmp
        return tmp
    
    if len(str(num)) % 2 == 0:
        tmp: str = str(num)
        left: int = blink(int(tmp[:len(str(tmp)) // 2]), iterations - 1)
        right: int = blink(int(tmp[len(str(tmp)) // 2:]), iterations - 1)
        already_visited[(num, iterations)] = left + right
        return left + right
    
    tmp: int = blink(num * 2024, iterations - 1)
    already_visited[(num, iterations)] = tmp
    return tmp


print(f"Point 1: {sum(blink(int(num), 25) for num in input_data.split())}")
print(f"Point 2: {sum(blink(int(num), 75) for num in input_data.split())}")
