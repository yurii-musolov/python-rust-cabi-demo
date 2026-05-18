from collections.abc import Callable
import time

from rust_bridge import sum_of_squares_rust


def sum_of_squares_python(limit: int) -> int:
    total = 0

    for i in range(limit):
        total += i * i

    return total


LIMIT: int = 100_000


def benchmark(
    name: str,
    fn: Callable[[int], int],
) -> float:
    start = time.perf_counter()

    result: int = fn(LIMIT)

    elapsed = time.perf_counter() - start

    print(f"{name} result: {result}")
    print(f"{name} time  : {elapsed:.4f} sec")
    print()

    return elapsed


def main():
    python_time: float = benchmark(
        "Python",
        sum_of_squares_python,
    )

    rust_time: float = benchmark(
        "Rust",
        sum_of_squares_rust,
    )

    speedup: float = python_time / rust_time

    print(f"Rust is faster ~{speedup:.1f}x")


if __name__ == "__main__":
    main()
