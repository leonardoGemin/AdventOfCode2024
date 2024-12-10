from aocd import get_data
from itertools import product
from collections import defaultdict


first: int = 0
second: int = 0


input_data: str = get_data(day=8, year=2024).splitlines()


antennas: dict[str, list[tuple[int, int]]] = defaultdict(list)
for row, col in product(range(len(input_data)), range(len(input_data[0]))):
    if input_data[row][col] != '.':
        antennas[input_data[row][col]].append((row, col))


antennas1: set = set()
antennas2: set = set()
for row, col in product(range(len(input_data)), range(len(input_data[0]))):
    for key, values in antennas.items():
        for (row1, col1), (row2, col2) in product(values, values):
            if (row1, col1) != (row2, col2):
                dist1 = abs(row - row1) + abs(col - col1)
                dist2 = abs(row - row2) + abs(col - col2)

                rowDist1 = row - row1
                rowDist2 = row - row2
                colDist1 = col - col1
                colDist2 = col - col2
                
                if 0 <= row < len(input_data) and 0 <= col < len(input_data[0]) and (rowDist1 * colDist2 == colDist1 * rowDist2):
                    if (dist1 == 2 * dist2 or dist1 * 2 == dist2):
                        antennas1.add((row, col))
                
                    antennas2.add((row, col))


first = len(antennas1)
second = len(antennas2)


print(f"Point 1: {first}")
print(f"Point 2: {second}")
