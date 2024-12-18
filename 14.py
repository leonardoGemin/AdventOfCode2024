from aocd import get_data
import re
from collections import deque
import sys


first: int = 0
second: int = 0


input_data: str = get_data(day=14, year=2024).splitlines()


wide: int = 101
tall: int = 103


robots: list[tuple[int, int, int, int]] = []
for line in input_data:
    px, py, vx, vy = [int(x) for x in re.findall('-?\d+', line)]
    robots.append((px, py, vx, vy))


quarters: list[int] = [0, 0, 0, 0]
for iter in range(10000):
    grid: list[list[str]] = [['.' for _ in range(wide)] for _ in range(tall)]

    for i, (px, py, vx, vy) in enumerate(robots):
        px += vx
        py += vy
        px %= wide
        py %= tall
        robots[i] = (px, py, vx, vy)
        grid[py][px] = '#'

        if iter == 100:
            if px < wide // 2 and py < tall // 2:
                quarters[0] += 1
            if px > wide // 2 and py < tall // 2:
                quarters[1] += 1
            if px < wide // 2 and py > tall // 2:
                quarters[2] += 1
            if px > wide // 2 and py > tall // 2:
                quarters[3] += 1
    
    if iter == 100:
        first = quarters[0] * quarters[1] * quarters[2] * quarters[3]

    components = 0
    visited = set()
    for x in range(wide):
        for y in range(tall):
            if grid[y][x] == '#' and (x, y) not in visited:
                sx, sy = x, y
                components += 1
                Q = deque([(sx,sy)])
                while Q:
                    x2,y2 = Q.popleft()
                    if (x2,y2) in visited:
                        continue
                    visited.add((x2,y2))
                    for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                        xx, yy = x2 + dx, y2 + dy
                        if 0 <= xx < wide and 0 <= yy < tall and grid[yy][xx] == '#':
                            Q.append((xx,yy))

    print(f"Iteration {iter}", file=sys.stderr)
    for row in grid:
        for elem in row:
            print(elem, sep='', end='', file=sys.stderr)
        print('', file=sys.stderr)
    print('', file=sys.stderr)
    

print(f"Point 1: {first}")
print(f"Point 2: {second}")
