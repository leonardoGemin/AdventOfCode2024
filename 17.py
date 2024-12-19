from aocd import get_data


input_data: str = get_data(day=17, year=2024)


A, B, C = [int(line[12:]) for line in input_data.split("\n\n")[0].splitlines()]
programs: list[int] = [int(num) for num in input_data.split("\n\n")[1][9:].split(',')]


def solve1(A: int, B: int, C: int) -> list[int]:
    out: list[int] = []
    instruction_pointer: int = 0
    while instruction_pointer < len(programs):
        if instruction_pointer + 1 >= len(programs):
            break

        opcode: int = programs[instruction_pointer]
        literal: int = programs[instruction_pointer + 1]
        combo: int = 0

        if literal < 4:
            combo = literal
        elif literal == 4:
            combo = A
        elif literal == 5:
            combo = B
        elif literal == 6:
            combo = C

        if opcode == 0:
            A = A // (2 ** combo)
        elif opcode == 1:
            B = B ^ literal
        elif opcode == 2:
            B = combo % 8
        elif opcode == 3 and A != 0:
            instruction_pointer = literal
            continue
        elif opcode == 4:
            B = B ^ C
        elif opcode == 5:
            out.append(combo % 8)
        elif opcode == 6:
            B = A // (2 ** combo)
        elif opcode == 7:
            C = A // (2 ** combo)
        
        instruction_pointer += 2

    return out


def solve2() -> int:
    def simulate_loop(a: int) -> int:
        b: int = a % 8
        b = b ^ 7
        c: int = a >> b
        b = b ^ 7
        b = b ^ c
        return b % 8
    

    stack: list[tuple[int, int]] = [(0, len(programs))]
    possible_solutions: list[int] = []
    while stack:
        a, depth = stack.pop()
        
        if depth == 0:
            possible_solutions.append(a)
            continue

        for b in range(8):
            new_a = (a << 3) | b
            if simulate_loop(new_a) == programs[depth - 1]:
                stack.append((new_a, depth - 1))
    
    return sorted(possible_solutions)[0]


print(f"Point 1: {','.join([str(num) for num in solve1(A, B, C)])}")
print(f"Point 2: {solve2()}")
