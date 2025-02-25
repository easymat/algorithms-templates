def zipper(a: list[int], b: list[int], n: int) -> list[int]:
    zipper_line = []
    for _ in range(n):
        zipper_line.append(a[_])
        zipper_line.append(b[_])

    return zipper_line


def read_input() -> tuple[int, list[int], list[int]]:
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    return n, a, b


n, a, b = read_input()
print(" ".join(map(str, zipper(a, b, n))))
