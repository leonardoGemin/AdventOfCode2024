from aocd import get_data


first: int = 0
second: int = 0


directions: list[tuple[int, int]] = [
    ( 0,  1),   # Horizontal, from left to right
    ( 0, -1),   # Horizontal, from right to left
    ( 1,  0),   # Vertical, from top to bottom
    (-1,  0),   # Vertical, from bottom to top
    ( 1,  1),   # Oblique, from left to right, from top to bottom
    (-1,  1),   # Oblique, from left to right, from bottom to top
    ( 1, -1),   # Oblique, from right to left, from top to bottom
    (-1, -1)    # Oblique, from right to left, from bottom to top
]


XMAS: str = "XMAS"
def findXMAS(row: int, col: int, delta_row: int, delta_col: int) -> bool:
    for i in range(1, 4):
        new_row: int = row + (delta_row * i)
        new_col: int = col + (delta_col * i)

        if not (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0])):
            return False

        if matrix[new_row][new_col] != XMAS[i]:
            return False
    return True


def findMAS(row: int, col: int) -> bool:
    if not (1 <= row < len(matrix) - 1 and 1 <= col < len(matrix) - 1):
        return False
    
    return (matrix[row - 1][col - 1] + matrix[row][col] + matrix[row + 1][col + 1] in [("MAS"), ("SAM")]) and\
           (matrix[row + 1][col - 1] + matrix[row][col] + matrix[row - 1][col + 1] in [("MAS"), ("SAM")])



input_data: str = get_data(day=4, year=2024)
matrix: list[str] = input_data.splitlines()

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == "X":
            for row_delta, col_delta in directions:
                first += 1 if findXMAS(row, col, row_delta, col_delta) else 0
        
        if matrix[row][col] == "A":
            second += 1 if findMAS(row, col) else 0


print(f"Point 1: {first}")
print(f"Point 2: {second}")
