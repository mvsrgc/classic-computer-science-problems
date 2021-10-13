from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}  # base cases


def fibonacci(n: int) -> int:
    if not n in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]


if __name__ == "__main__":
    for i in range(50):
        print(fibonacci(i))
