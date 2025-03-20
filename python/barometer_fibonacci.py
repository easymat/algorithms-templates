import sys


def number_of_measurements(
        barometer_version: int,
        ):

    if barometer_version == 0 or barometer_version == 1:
        return 1

    return (
        number_of_measurements(barometer_version - 1) +
        number_of_measurements(barometer_version - 2)
    )


if __name__ == '__main__':
    # Получаем данные о версии барометра:
    barometer_version: int = int(sys.stdin.readline().rstrip())

    # Считаем количество опреаций для данной модели робота
    print(number_of_measurements(barometer_version))
