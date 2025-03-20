import sys


def sorting(
        quantity_of_numbers: int,
        arr_for_sorting: list[int],
        quantity_of_sorted_numbers: int,
        example_for_sorting: list[int],
        ) -> list[int]:
    sort_index = 0
    for index in range(quantity_of_sorted_numbers):
        current = example_for_sorting[index]

        for i in range(quantity_of_numbers):
            if arr_for_sorting[i] == current:
                arr_for_sorting[sort_index], arr_for_sorting[i] = (
                    arr_for_sorting[i], arr_for_sorting[sort_index]
                )
                sort_index += 1

    for index in range(sort_index, quantity_of_numbers):
        current = arr_for_sorting[index]

        prev = index - 1
        while (
            prev >= sort_index
            and arr_for_sorting[prev]
        ) > current:
            arr_for_sorting[prev + 1] = arr_for_sorting[prev]
            prev -= 1

        arr_for_sorting[prev + 1] = current

    return arr_for_sorting


if __name__ == '__main__':
    quantity_of_numbers: int = int(sys.stdin.readline().rstrip())
    arr_for_sorting: list[int] = [
        int(number_index)
        for number_index in sys.stdin.readline().rstrip().rsplit()
    ]
    quantity_of_sorted_numbers: int = int(sys.stdin.readline().rstrip())
    example_for_sorting: list[int] = [
        int(number_index)
        for number_index in sys.stdin.readline().rstrip().rsplit()
    ]

    sorted_arr = sorting(
        quantity_of_numbers,
        arr_for_sorting,
        quantity_of_sorted_numbers,
        example_for_sorting
    )

    print(' '.join(str(_) for _ in sorted_arr))
