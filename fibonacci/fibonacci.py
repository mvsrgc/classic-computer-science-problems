from typing import Generator


def fibonacci(n: int) -> Generator[int, None, None]:
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == "__main__":
    print(list(fibonacci(50)))
