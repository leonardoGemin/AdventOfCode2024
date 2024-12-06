from aocd import get_data


first: int = 0
second: int = 0


input_data: list[list[str]] = [list(row) for row in get_data(day=6, year=2024).splitlines()]
starting_row, starting_col = next((r, c) for r, row in enumerate(input_data) for c, val in enumerate(row) if val == '^')
directions_coordinates: list[tuple[int, int]] = [(-1,  0), ( 0,  1), ( 1,  0), ( 0, -1)]


curr_direction: int = 0
curr_row: int = starting_row
curr_col: int = starting_col
while True:
    if input_data[curr_row][curr_col] != 'X':
        input_data[curr_row][curr_col] = 'X'
        first += 1
    
    tmp_row: int = curr_row + directions_coordinates[curr_direction][0]
    tmp_col: int = curr_col + directions_coordinates[curr_direction][1]

    if not (0 <= tmp_row < len(input_data) and 0 <= tmp_col < len(input_data[0])):
        break

    if input_data[tmp_row][tmp_col] == '#':
        curr_direction = (curr_direction + 1) % 4
        continue

    curr_row, curr_col = tmp_row, tmp_col


for row in range(len(input_data)):
    for col in range(len(input_data[0])):
        has_adjacent_x: bool = False
        for dr, dc in directions_coordinates:
            adj_row, adj_col = row + dr, col + dc
            if 0 <= adj_row < len(input_data) and 0 <= adj_col < len(input_data[0]):
                if input_data[adj_row][adj_col] == 'X':
                    has_adjacent_x = True
                    break
        
        if (not has_adjacent_x) or (input_data[row][col] in ['#', '^']):
            continue
        
        def causes_loop() -> bool:
            visited: set[tuple[int, int, int]] = set()
            curr_row, curr_col, curr_direction = starting_row, starting_col, 0
            
            tmp: str = input_data[row][col]
            input_data[row][col] = '#'
            while True:
                curr_state: tuple[int, int, int] = (curr_row, curr_col, curr_direction)
                if curr_state in visited:
                    input_data[row][col] = tmp
                    return True
                visited.add(curr_state)
                
                tmp_row = curr_row + directions_coordinates[curr_direction][0]
                tmp_col = curr_col + directions_coordinates[curr_direction][1]
                
                if not (0 <= tmp_row < len(input_data) and 0 <= tmp_col < len(input_data[0])):
                    input_data[row][col] = tmp
                    return False
                
                if input_data[tmp_row][tmp_col] == "#":
                    curr_direction = (curr_direction + 1) % 4
                    continue
                
                curr_row, curr_col = tmp_row, tmp_col
        
        second += 1 if causes_loop() else 0


print(f"Point 1: {first}")
print(f"Point 2: {second}")
