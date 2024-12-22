from aocd import get_data
from collections import deque


input_data: str = get_data(day=12, year=2024).splitlines()
directions: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]


first: int = 0
second: int = 0


visited: set[tuple[int, int]] = set()
for r in range(len(input_data)):
    for c in range(len(input_data[0])):
        if (r, c) in visited:
            continue
        
        area: int = 0
        perim: int = 0
        perimeters: dict[tuple[int, int], set[tuple[int, int]]] = dict()
        
        queue: deque[tuple[int, int]] = deque([(r, c)])
        while queue:
            r2,c2 = queue.popleft()
            if (r2,c2) in visited:
                continue
            visited.add((r2,c2))
            area += 1
            for dr,dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                rr = r2 + dr
                cc = c2 + dc
                if 0 <= rr < len(input_data) and 0 <= cc < len(input_data[0]) and input_data[rr][cc] == input_data[r2][c2]:
                    queue.append((rr, cc))
                else:
                    perim += 1
                    if (dr, dc) not in perimeters:
                        perimeters[(dr, dc)] = set()
                    
                    perimeters[(dr, dc)].add((r2, c2))

        sides: int = 0
        for k, vs in perimeters.items():
            visited_perimeters: set[tuple[int, int]] = set()
            old_sides: int = sides
            
            for (pr, pc) in vs:
                if (pr, pc) not in visited_perimeters:
                    sides += 1
                    
                    queue: deque[tuple[int, int]] = deque([(pr, pc)])
                    while queue:
                        r2, c2 = queue.popleft()
                        if (r2, c2) in visited_perimeters:
                            continue

                        visited_perimeters.add((r2, c2))
                        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                            rr, cc = r2 + dr, c2 + dc
                            if (rr, cc) in vs:
                                queue.append((rr, cc))

        first += area * perim
        second += area * sides


print(first)
print(second)