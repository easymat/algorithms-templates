import sys


def devide(array, len_array):
    number_of_blocks = 0
    count = -1
    max_element = 0
    for element in array:
        max_element = max(max_element, element)
        count += 1

        if count == max_element and element <= max_element:
            number_of_blocks += 1
        if element < max_element:
            continue

    return number_of_blocks


if __name__ == '__main__':
    number_of_elements = int(sys.stdin.readline().rstrip())
    array_for_sorting = [
        int(element) for element in sys.stdin.readline().rsplit()
    ]

    result = devide(array_for_sorting, number_of_elements)

    print(result)
