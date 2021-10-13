from typing import Dict
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}  # base cases

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n < 2:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for i in range(50):
        print(fibonacci(i))
