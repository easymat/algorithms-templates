def check_element_in_list(ordered_list, desired_element):
    desired_element = int(desired_element)
    left = 0
    right = len(ordered_list)
    while left <= right:
        mid = (left + right) // 2
        print(mid)
        if mid == len(ordered_list):
            return mid
        if int(ordered_list[mid]) == desired_element:
            print(ordered_list[mid], desired_element, '=')
            return mid
        if int(ordered_list[mid]) > desired_element:
            print(ordered_list[mid], desired_element, '>')
            right = mid - 1
        else:
            print(ordered_list[mid], desired_element, 'else')
            left = mid + 1
    return mid


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        ordered_list = file_in.readline().rstrip().split(' ')
        desired_element = file_in.readline().rstrip()

    result = check_element_in_list(ordered_list, desired_element)

    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))

#не работает