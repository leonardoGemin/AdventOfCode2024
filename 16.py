from aocd import get_data
import heapq


input_data: list[str] = get_data(day=16, year=2024).splitlines()


start: tuple[int, int]
end: tuple[int, int]
for row in range(len(input_data)):
    for col in range(len(input_data[0])):
        if input_data[row][col] == 'S':
            start = (row, col)
        if input_data[row][col] == 'E':
            end = (row, col)



visited: set[tuple[int, int, int, tuple[int, int]]] = set()
DIST: dict[tuple[int, int, tuple[int, int]], int] = {}
first: int|None = None

queue: list[tuple[int, int, int, int]] = []
heapq.heappush(queue, (0, start[0], start[1], 1))
while queue:
    d, r, c, dir = heapq.heappop(queue)

    if (r, c, dir) not in DIST:
        DIST[(r, c, dir)] = d

    if (r, c) == end and first is None:
        first = d

    if (r, c, dir) in visited:
        continue
    visited.add((r, c, dir))

    dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][dir]
    rr, cc = r + dr, c + dc
    if 0 <= rr < len(input_data) and 0 <= cc < len(input_data[0]) and input_data[rr][cc] != '#':
        heapq.heappush(queue, (d + 1, rr, cc, dir))

    heapq.heappush(queue, (d + 1000, r, c, (dir + 1) % 4))
    heapq.heappush(queue, (d + 1000, r, c, (dir + 3) % 4))



visited: set[tuple[int, int, int, tuple[int, int]]] = set()
DIST2: dict[tuple[int, int, tuple[int, int]], int] = {}

queue: list[tuple[int, int, int, int]] = []
for dir in range(4):
    heapq.heappush(queue, (0, end[0], end[1], dir))
while queue:
    d, r, c, dir = heapq.heappop(queue)

    if (r, c, dir) not in DIST2:
        DIST2[(r, c, dir)] = d

    if (r, c, dir) in visited:
        continue
    visited.add((r, c, dir))

    dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][(dir + 2) % 4]
    rr, cc = r + dr, c + dc
    if 0 <= rr < len(input_data) and 0 <= cc < len(input_data[0]) and input_data[rr][cc] != '#':
        heapq.heappush(queue, (d + 1, rr, cc, dir))

    heapq.heappush(queue, (d + 1000, r, c, (dir + 1) % 4))
    heapq.heappush(queue, (d + 1000, r, c, (dir + 3) % 4))

second = set()
for r in range(len(input_data)):
    for c in range(len(input_data[0])):
        for dir in range(4):
            if (r, c, dir) in DIST and (r, c, dir) in DIST2 and DIST[(r, c, dir)] + DIST2[(r, c, dir)] == first:
                second.add((r, c))



print(f"Point 1: {first}")
print(f"Point 2: {len(second)}")
