from typing import Tuple


def get_sum(a: int, b: int) -> int:
    sum = a + b
    return sum


def read_input() -> Tuple[int, int]:
    a = int(input())
    b = int(input())
    return a, b


def main():
    a, b = read_input()
    print(get_sum(a, b))


if __name__ == '__main__':
    main()
