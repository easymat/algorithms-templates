def check_element_in_list(ordered_list, desired_element):
    desired_element = int(desired_element)
    for index, item in enumerate(ordered_list):
        item = int(item)
        if item == desired_element:
            return index
        if item > desired_element:
            return index
    return len(ordered_list)


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        ordered_list = file_in.readline().rstrip().split(' ')
        desired_element = file_in.readline().rstrip()

    result = check_element_in_list(ordered_list, desired_element)

    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
