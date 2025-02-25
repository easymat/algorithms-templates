def delete_double(line, length):
    numbers = line.split(' ')
    doubles = 0
    numbers_without_double = [numbers[0]]
    for _ in range(1, int(length)):
        if numbers[_] == numbers[_ - 1]:
            doubles += 1
        else:
            numbers_without_double.append(str(numbers[_]))
    return numbers_without_double, doubles


if __name__ == '__main__':
    with open('input.txt', 'r') as file_in:
        length = file_in.readline()
        line = file_in.readline()

    numbers_without_double, doubles = delete_double(
        line.rstrip(), length.rstrip()
    )
    result = str.join(' ', numbers_without_double) + ' _' * doubles

    with open('output.txt', 'w') as file_out:
        file_out.write(str(result))
