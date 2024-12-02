from aocd import get_data


left: list[int] = []
right: list[int] = []
counter: dict[int, int] = {}


input_data: str = get_data(day=1, year=2024)
for line in input_data.splitlines():
    l, r = list(map(int, line.split()))
    left.append(l)
    right.append(r)
    counter[r] = counter.get(r, 0) + 1


left = sorted(left)
right = sorted(right)


distance: int = 0
similarity: int = 0
for (l, r) in zip(left, right):
    distance += abs(l - r)
    similarity += (l * counter.get(l, 0))
print(f"Point 1: {distance}")
print(f"Point 2: {similarity}")
