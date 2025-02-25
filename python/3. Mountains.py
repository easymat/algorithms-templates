from array import array


def valid_mountain_array(data: array) -> bool:
    max_hight = max(data)
    max_hight_index = data.index(max_hight)

    if max_hight_index == 0 or max_hight_index == len(data) - 1:
        return False

    valid_mountain = True if len(data) >= 3 else False

    for index in range(max_hight_index, 0, -1):
        if data[index] <= data[index - 1]:
            valid_mountain = False

    for index in range(max_hight_index, len(data) - 1):

        if data[index] <= data[index + 1]:
            valid_mountain = False

    return valid_mountain


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        data = array('b', list(map(int, file_in.readline().strip().split())))
        result = valid_mountain_array(data)

    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
