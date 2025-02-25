def find_max_length_of_uniq_slice(data):
    saspect_max = len(set(map(str, data)))
    if saspect_max == len(data):
        return saspect_max

    uniq_slice = ''
    max_length = 0

    for elements_in_slice in range(1, saspect_max + 1):
        for index in range(elements_in_slice, len(data) + 1):
            print(len(data[index - elements_in_slice:index]), len(set(data[index - elements_in_slice:index])))
            print(data[index - elements_in_slice:index])
            if len(data[index - elements_in_slice:index]) == len(set(data[index - elements_in_slice:index])):
                max_length = elements_in_slice
            else:
                continue

    return max_length


if __name__ == '__main__':
    data = 'fprarfpoz'
    print(find_max_length_of_uniq_slice(data))
