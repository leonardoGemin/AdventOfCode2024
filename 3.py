from aocd import get_data
import re


first: int = 0
second: int = 0
flag: bool = True


input_data: str = get_data(day=3, year=2024)
for line in input_data.splitlines():
    pattern: str = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
    occurrences: list[str] = re.findall(pattern, line)
    for occurrence in occurrences:
        if occurrence == "do()":
            flag = True
            continue
        if occurrence == "don't()":
            flag = False
            continue
        
        l, r = list(map(int, occurrence[4:-1].split(",")))
        first += (l * r)
        second += (l * r) if flag else 0


print(f"Point 1: {first}")
print(f"Point 2: {second}")
