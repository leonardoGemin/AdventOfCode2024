from aocd import get_data
from collections import deque


input_data: str = get_data(day=15, year=2024)


mapping: dict[str, list[str]] = {'#': ['#', '#'], 'O': ['[', ']'], '.': ['.', '.'], '@': ['@', '.']}
grid1: list[list[str]] = [[char for char in row] for row in input_data.split("\n\n")[0].splitlines()]
grid2: list[list[str]] = [[char for elem in row for char in mapping.get(elem, [elem])] for row in input_data.split("\n\n")[0].splitlines()]
moves: str = "".join(input_data.split("\n\n")[1].splitlines())


def solve(grid: list[list[str]]) -> int:
    currROW: int = 0
    currCOL: int = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                grid[row][col] = '.'
                currROW, currCOL = row, col
                break
    
    
    for move in moves:
        deltaROW, deltaCOL = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}[move]
        newROW: int = currROW + deltaROW
        newCOL: int = currCOL + deltaCOL

        if grid[newROW][newCOL] == '#':
            continue
        
        if grid[newROW][newCOL] == '.':
            currROW, currCOL = newROW, newCOL
            continue
        
        if grid[newROW][newCOL] in ['O', '[', ']']:
            queue: deque = deque([(currROW, currCOL)])
            seen: set = set()
            flag: bool = True
            while queue:
                r, c = queue.popleft()
                if (r, c) in seen:
                    continue
                seen.add((r, c))
                
                rr, cc = r + deltaROW, c + deltaCOL
                if grid[rr][cc] == '#':
                    flag = False
                    break
                elif grid[rr][cc] == 'O':
                    queue.append((rr, cc))
                elif grid[rr][cc] == '[':
                    queue.append((rr, cc))
                    queue.append((rr, cc + 1))
                elif grid[rr][cc] == ']':
                    queue.append((rr, cc))
                    queue.append((rr, cc - 1))
            
            if not flag:
                continue

            while len(seen) > 0:
                for r, c in sorted(seen):
                    rr, cc = r + deltaROW, c + deltaCOL
                    if (rr, cc) not in seen:
                        grid[rr][cc] = grid[r][c]
                        grid[r][c] = '.'
                        seen.remove((r, c))
            
            currROW, currCOL = newROW, newCOL


    answer: int = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] in ['O', '[']:
                answer += 100 * row + col
    return answer


print(f"Point 1: {solve(grid1)}")
print(f"Point 2: {solve(grid2)}")
