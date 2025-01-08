from aocd import get_data
from collections import defaultdict


input_data: str = get_data(day=22, year=2024)


def calcPrices(x: int) -> list[int]:
    res: list[int] = [x]
    for _ in range(2000):
        x = ((x << 6) ^ x) % 16777216
        x = ((x >> 5) ^ x) % 16777216
        x = ((x << 11) ^ x) % 16777216
        res.append(x)
    
    return res


def getScores(prices: list[int], changes: list[int]) -> dict[tuple[int, int, int, int], list[int]]:
    res: dict[tuple[int, int, int, int], list[int]] = {}
    for i in range(len(changes) - 3):
        pattern: tuple[int, int, int, int] = (changes[i], changes[i + 1], changes[i + 2], changes[i + 3])
        if pattern not in res:
            res[pattern] = prices[i + 4]

    return res


first: int = 0
scores: dict[int, int] = defaultdict(int)
for line in input_data.splitlines():
    prices: list[int] = calcPrices(int(line))
    first += prices[-1]

    prices = [x % 10 for x in prices]
    changes: list[int] = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    for k, v in getScores(prices, changes).items():
        scores[k] = scores.get(k, 0) + v


second: int = max(scores.values())


print(f"Point 1: {first}")
print(f"Point 2: {second}")
