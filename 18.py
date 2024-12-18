from aocd import get_data
from collections import deque


input_data: list[str] = get_data(day=18, year=2024).splitlines()
dimensions: int = 70


positions: list[tuple[int, int]] = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in input_data]


def solve1(bytes: int) -> int:
    grid: list[list[str]] = [['.' for _ in range(dimensions + 1)] for _ in range(dimensions + 1)]
    for x, y in positions[:bytes]:
        grid[y][x] = '#'

    queue: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
    visited: set[tuple[int, int]] = set()
    while queue:
        x, y, steps = queue.popleft()

        if (x, y) == (len(grid) - 1, len(grid[0]) - 1):
            return steps
        
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[ny][nx] != '#':
                queue.append((nx, ny, steps + 1))
    
    return -1


def solve2() -> str:
    for i, (x, y) in enumerate(positions):
        if solve1(i + 1) == -1:
            return f"{x},{y}"
    
    return None



print(f"Point 1: {solve1(1024)}")
print(f"Point 2: {solve2()}")
