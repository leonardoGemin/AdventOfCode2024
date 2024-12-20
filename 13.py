from aocd import get_data


input_data: str = get_data(day=13, year=2024)


def solve(offset: int = 0) -> int:
    score: int = 0
    
    for machine in input_data.split("\n\n"):
        XA: int = int(machine.splitlines()[0].split()[2][2:-1])
        YA: int = int(machine.splitlines()[0].split()[3][2:])
        XB: int = int(machine.splitlines()[1].split()[2][2:-1])
        YB: int = int(machine.splitlines()[1].split()[3][2:])
        X: int = int(machine.splitlines()[2].split()[1][2:-1]) + offset
        Y: int = int(machine.splitlines()[2].split()[2][2:]) + offset

        A: float = ((XB * Y) - (X * YB)) / ((XB * YA) - (XA * YB))
        B: float = (X - (A * XA)) / XB

        score += 3 * int(A) + int(B) if A.is_integer() and B.is_integer() else 0
    
    return score


print(f"Point 1: {solve()}")
print(f"Point 2: {solve(10000000000000)}")
