from aocd import get_data


input_data: str = get_data(day=9, year=2024)


def point1() -> int:
    disk: list[str] = []
    for i, char in enumerate(input_data):
        if i % 2 == 0:
            disk += [str(i // 2) for _ in range(int(char))]
        else:
            disk += ['.' for _ in range(int(char))]


    answer: int = 0
    i: int = 0
    while i < len(disk):
        if disk[i] == '.':
            while disk[-1] == '.':
                disk = disk[:-1]
            disk = disk[:i] + [disk[-1]] + disk[i + 1: -1]
        
        answer += (i * int(disk[i]))
        i += 1
    return answer


def point2() -> int:
    disk: list[int] = []
    files: list[tuple[int, int, int]] = []
    spaces: list[tuple[int, int]] = []
    pos: int = 0
    for i, char in enumerate(input_data):
        if i % 2 == 0:
            files.append((i // 2, pos, int(char)))
            disk += [i // 2 for _ in range(int(char))]
        else:
            if int(char) > 0:
                spaces.append((pos, int(char)))
                disk += [None for _ in range(int(char))]
        pos += int(char)


    for (fileID, pos, size) in reversed(files):
        for spaceID, (spacePOS, spaceSIZE) in enumerate(spaces):
            if (spacePOS < pos) and (size <= spaceSIZE):
                for i in range(size):
                    assert disk[pos + i] == fileID, f'{disk[pos + i]=}'
                    disk[pos + i] = None
                    disk[spacePOS + i] = fileID
                spaces[spaceID] = (spacePOS + size, spaceSIZE - size)
                break

    answer: int = 0
    for i, char in enumerate(disk):
        if char is not None:
            answer += i * char
    return answer


print(f"Point 1: {point1()}")
print(f"Point 2: {point2()}")
