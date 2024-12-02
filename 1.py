import sys

if len(sys.argv) < 2:
    print("Insert at least one argument.")
    sys.exit()
input_file = sys.argv[1]


left: list[int] = []
right: list[int] = []
counter: dict[int, int] = {}


input_data = open(input_file, "r")
for line in input_data.readlines():
    l, r = list(map(int, line.split()))
    left.append(l)
    right.append(r)
    counter[r] = counter.get(r, 0) + 1
input_data.close()


left = sorted(left)
right = sorted(right)


distance: int = 0
similarity: int = 0
for (l, r) in zip(left, right):
    distance += abs(l - r)
    similarity += (l * counter.get(l, 0))
print(f"Point 1: {distance}")
print(f"Point 2: {similarity}")
