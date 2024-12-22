from aocd import get_data


input_data: str = get_data(day=19, year=2024)


words: list[str] = input_data.split("\n\n")[0].split(", ")
targets: list[str] = input_data.split("\n\n")[1].splitlines()


visited: dict[str, int] = {}
def checkTarget(words: str, target: str) -> int:
    if target in visited:
        return visited[target]
    
    res: int = 0
    if not target:
        res = 1

    for word in words:
        if target.startswith(word):
            res += checkTarget(words, target[len(word):])

    visited[target] = res

    return res


first: int = 0
second: int = 0
for target in targets:
    target_ways: int = checkTarget(words, target)
    if target_ways > 0:
        first += 1
    second += target_ways


print(f"Point 1: {first}")
print(f"Point 2: {second}")
