def less_than_num(nums):
    # Ваше решение?
    result = []
    for index in range(len(nums)):
        count = 0
        for _ in range(len(nums)):
            if nums[_] < nums[index]:
                count += 1
            else:
                continue
        result.append(str(count))

    return str.join(' ', result)


if __name__ == '__main__':
    nums = list(map(int, input().strip().split()))

    print(less_than_num(nums))
