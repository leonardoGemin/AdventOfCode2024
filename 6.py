from aocd import get_data


first: int = 0
second: int = 0


input_data: list[list[str]] = [list(row) for row in get_data(day=6, year=2024).splitlines()]
#input_data = [list(row) for row in "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#...".splitlines()]


directions_coordinates: list[tuple[int, int]] = [(-1,  0), ( 0,  1), ( 1,  0), ( 0, -1)]


starting_row: int = 0
starting_col: int = 0
for row in range(len(input_data)):
    for col in range(len(input_data[0])):
        if input_data[row][col] == '^':
            starting_row, starting_col = row, col


matrix: list[list[str]] = input_data
curr_direction: int = 0
curr_row: int = starting_row
curr_col: int = starting_col
while True:
    if matrix[curr_row][curr_col] != 'X':
        matrix[curr_row][curr_col] = 'X'
        first += 1
    
    tmp_row: int = curr_row + directions_coordinates[curr_direction][0]
    tmp_col: int = curr_col + directions_coordinates[curr_direction][1]

    if not (0 <= tmp_row < len(matrix) and 0 <= tmp_col < len(matrix[0])):
        break

    if matrix[tmp_row][tmp_col] == '#':
        curr_direction = (curr_direction + 1) % 4
        continue

    curr_row, curr_col = tmp_row, tmp_col



def causes_loop(grid: list[list[str]], starting_row: int, starting_col: int, obstruction_row: int, obstruction_col: int) -> bool:
    grid_copy = [row[:] for row in grid]
    grid_copy[obstruction_row][obstruction_col] = "#"
    
    visited = set()
    curr_row, curr_col, curr_direction = starting_row, starting_col, 0
    
    while True:
        state = (curr_row, curr_col, curr_direction)
        if state in visited:
            return True
        visited.add(state)
        
        tmp_row = curr_row + directions_coordinates[curr_direction][0]
        tmp_col = curr_col + directions_coordinates[curr_direction][1]
        
        if not (0 <= tmp_row < len(grid_copy) and 0 <= tmp_col < len(grid_copy[0])):
            return False
        
        if grid_copy[tmp_row][tmp_col] == "#":
            curr_direction = (curr_direction + 1) % 4
            continue
        
        curr_row, curr_col = tmp_row, tmp_col


matrix: list[list[str]] = input_data
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] in ['#', '^']:
            continue
        
        second += 1 if causes_loop(matrix, starting_row, starting_col, row, col) else 0


print(f"Point 1: {first}")
print(f"Point 2: {second}")
