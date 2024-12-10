from aocd import get_data
from collections import deque


input_data: list[str] = get_data(day=10, year=2024).splitlines()


def findScores(row: int, col: int) -> int:
    visited: set = set()
    queue: deque = deque([(row, col, 0)])
    reachable9: set = set()

    while queue:
        currROW, currCOL, currHEIGHT = queue.popleft()
        
        if currHEIGHT == 9:
            reachable9.add((currROW, currCOL))
            continue

        for deltaROW, deltaCOL in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            newROW: int = currROW + deltaROW
            newCOL: int = currCOL + deltaCOL
            if 0 <= newROW < len(input_data) and 0 <= newCOL < len(input_data[0]) and\
                int(input_data[newROW][newCOL]) == currHEIGHT + 1 and (newROW, newCOL) not in visited:
                queue.append((newROW, newCOL, int(input_data[newROW][newCOL])))
    
    return len(reachable9)


def findPaths(currROW: int, currCOL: int, currHEIGHT: int, visited: set) -> int:
    if currHEIGHT == 9:
        return 1

    trails = 0
    for deltaROW, deltaCOL in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        newROW: int = currROW + deltaROW
        newCOL: int = currCOL + deltaCOL
        if 0 <= newROW < len(input_data) and 0 <= newCOL < len(input_data[0]) and\
            int(input_data[newROW][newCOL]) == currHEIGHT + 1 and (newROW, newCOL) not in visited:
            visited.add((newROW, newCOL))
            trails += findPaths(newROW, newCOL, currHEIGHT + 1, visited)
            visited.remove((newROW, newCOL))
    
    return trails


first: int = 0
second: int = 0
for row in range(len(input_data)):
    for col in range(len(input_data[0])):
        if int(input_data[row][col]) == 0:
            first += findScores(row, col)
            second += findPaths(row, col, 0, {(row, col)})


print(f"Point 1: {first}")
print(f"Point 2: {second}")
