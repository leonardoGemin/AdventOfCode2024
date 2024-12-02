import sys

if len(sys.argv) < 2:
    print("Insert at least one argument.")
    sys.exit()
input_file = sys.argv[1]


def isGood(nums: list[int]) -> bool:
    monotonicity: bool = (nums == sorted(nums)) or (nums == sorted(nums, reverse=True))
    
    flag: bool = True
    for i in range(0, len(nums) - 1):
        if abs(nums[i] - nums[i + 1]) not in [1, 2, 3]:
            flag = False

    return flag and monotonicity


safe: int = 0
dampener: int = 0


input_data = open(input_file, "r")
for line in input_data.readlines():
    nums: list[int] = list(map(int, line.split()))
    
    safe += 1 if isGood(nums) else 0
    
    flag: bool = False
    for i in range(0, len(nums)):
        if isGood(nums[:i] + nums[i + 1:]):
            flag = True
    dampener += 1 if flag else 0
input_data.close()


print(f"Point 1: {safe}")
print(f"Point 2: {dampener}")
