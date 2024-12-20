from aocd import get_data


input_data: str = get_data(day=13, year=2024)


def solve(offset: int = 0) -> int:
    machines: list[tuple[int, int, int, int, int, int, int, int, int]] = []
    for machine in input_data.split("\n\n"):
        XA: int = int(machine.splitlines()[0].split()[2][2:-1])
        YA: int = int(machine.splitlines()[0].split()[3][2:])
        XB: int = int(machine.splitlines()[1].split()[2][2:-1])
        YB: int = int(machine.splitlines()[1].split()[3][2:])
        X: int = int(machine.splitlines()[2].split()[1][2:-1]) + offset
        Y: int = int(machine.splitlines()[2].split()[2][2:]) + offset

        tmpA: float = ((XB * Y) - (X * YB)) / ((XB * YA) - (XA * YB))
        tmpB: float = (X - (tmpA * XA)) / XB

        A: int = int(tmpA) if tmpA.is_integer() else None
        B: int = int(tmpB) if tmpB.is_integer() else None

        score: int = 3 * A + B if A is not None and B is not None else 0

        machines.append((XA, XB, YA, YB, X, Y, A, B, score))
    
    return sum([machine[-1] for machine in machines])


print(f"Point 1: {solve()}")
print(f"Point 2: {solve(10000000000000)}")
