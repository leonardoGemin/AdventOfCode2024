from aocd import get_data
from collections import deque


input_data: list[str] = get_data(day=20, year=2024).splitlines()
#input_data = "###############\n#...#...#.....#\n#.#.#.#.#.###.#\n#S#...#.#.#...#\n#######.#.#.###\n#######.#.#...#\n#######.#.###.#\n###..E#...#...#\n###.#######.###\n#...###...#...#\n#.#####.#.###.#\n#.#...#.#.#...#\n#.#.#.#.#.#.###\n#...#...#...###\n###############".splitlines()


start: tuple[int, int]
end: tuple[int, int]
for row in range(len(input_data)):
    for col in range(len(input_data[0])):
        if input_data[row][col] == 'S':
            start = (row, col)
        if input_data[row][col] == 'E':
            end = (row, col)


DIST: dict[tuple[int, int], int] = {}
queue: deque[tuple[int, int, int]] = deque([(0, end[0], end[1])])
while queue:
    d, r, c = queue.popleft()

    if (r, c) in DIST:
        continue
    DIST[(r, c)] = d

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < len(input_data) and 0 <= cc < len(input_data[0]) and input_data[rr][cc] != '#':
            queue.append((d + 1, rr, cc))


def solve(d0: int, CHEAT_TIME: int) -> int:
    ans: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    visited: set[tuple[int, int, tuple[int, int], tuple[int, int], int]] = set()
    SAVE: int = 100

    queue: deque[tuple[int, tuple[int, int], tuple[int, int], int, int]] = deque([(0, None, None, None, start[0], start[1])])
    while queue:
        d, cheat_start, cheat_end, cheat_time, r, c = queue.popleft()

        if d >= d0 - SAVE:
            continue
        
        if (r, c) == end:
            if cheat_end is None:
                cheat_end = (r, c)
            if (cheat_start, cheat_end) not in ans:
                ans.add((cheat_start, cheat_end))
        
        if (r, c, cheat_start, cheat_end, cheat_time) in visited:
            continue
        visited.add((r, c, cheat_start, cheat_end, cheat_time))

        if cheat_start is None:
            queue.append((d, (r, c), None, CHEAT_TIME, r, c))
            
        if cheat_time is not None and input_data[r][c] != '#':
            if DIST[(r, c)] <= d0 - 100 - d:
                ans.add((cheat_start, (r, c)))

        if cheat_time != 0:
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                rr, cc = r + dr, c + dc
                if cheat_time is not None:
                    if 0 <= rr < len(input_data) and 0 <= cc < len(input_data[0]):
                        queue.append((d + 1, cheat_start, None, cheat_time - 1, rr, cc))
                else:
                    if 0 <= rr < len(input_data) and 0 <= cc < len(input_data[0]) and input_data[rr][cc] != '#':
                        queue.append((d + 1, cheat_start, cheat_end, cheat_time, rr, cc))
                        
    return len(ans)


print(f"Point 1: {solve(DIST[start], 2)}")
print(f"Point 2: {solve(DIST[start], 20)}")
