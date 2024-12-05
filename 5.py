from aocd import get_data
from collections import defaultdict


first: int = 0
second: int = 0


input_data: list[str] = get_data(day=5, year=2024).split("\n\n")


before: dict[int, set] = defaultdict(set)
after: dict[int, set] = defaultdict(set)
for line in input_data[0].splitlines():
    x, y = map(int, line.split('|'))
    before[y].add(x)
    after[x].add(y)


for line in input_data[1].splitlines():
    ordering: list[int] = list(map(int, line.split(',')))

    flag: bool = True
    for i, x in enumerate(ordering):
        for j, y in enumerate(ordering):
            if i < j and y in before[x]:
                flag = False
    
    if flag:
        first += (ordering[len(ordering) // 2])

    else:
        ordering_new: list[int] = []
        for elem2insert in ordering:
            index: int = 0
            for i, item2compare in enumerate(ordering_new):
                if elem2insert in after[item2compare]:
                    index = i + 1
            ordering_new = ordering_new[:index] + [elem2insert] + ordering_new[index:]
        second += (ordering_new[len(ordering_new) // 2])


print(f"Point 1: {first}")
print(f"Point 2: {second}")
