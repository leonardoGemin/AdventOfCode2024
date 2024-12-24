from aocd import get_data
from collections import defaultdict
import random


input_data: str = get_data(day=23, year=2024)


connections: dict[str, set[str]] = defaultdict(set)
for line in input_data.splitlines():
    c1, c2 = line.split('-')
    connections[c1].add(c2)
    connections[c2].add(c1)


sorted_keys: list[str] = sorted(connections.keys())


first: int = 0
for i in range(len(sorted_keys)):
    for j in range(i + 1, len(sorted_keys)):
        for k in range(j + 1, len(sorted_keys)):
            a: str = sorted_keys[i]
            b: str = sorted_keys[j]
            c: str = sorted_keys[k]

            if a in connections[b] and a in connections[c] and b in connections[c]:
                first += 1 if a.startswith('t') or b.startswith('t') or c.startswith('t') else 0


best: list[str] = None
for t in range(1000):
    random.shuffle(sorted_keys)

    clique: list[str] = []
    for x in sorted_keys:
        flag: bool = True
        for y in clique:
            if x not in connections[y]:
                flag = False

        if flag:
            clique.append(x)

    if best is None or len(clique) > len(best):
        best = clique

second: str = ','.join(sorted(best))


print(f"Point 1: {first}")
print(f"Point 2: {second}")
