"""Программа вычисляет минимальное количество платформ для перевозки роботов.

На вход передается массив, каждый элемент которого — это вес робота.
Второй параметр — это значение limit, грузоподъёмность одной платформы.

На одной платформе можно перевезти либо одного робота, либо двух — при условии,
что их совокупный вес не превышает limit. Роботы имеют разный вес.

ID посылки 133973986.
"""
import sys


def nessesary_platforms(robots_weight_data: list[int], max_weight: int) -> int:
    """Функция подсчитывает количество необходимых платформ."""
    # Сортируем по возрастанию данные о весе роботов:
    sorted_weight_data: list[int] = sorted(robots_weight_data)

    # С помощью двух указателей определяем неоходимое количество платформ:
    left_point_index: int = 0
    right_point_index: int = len(sorted_weight_data) - 1

    count: int = 0

    while left_point_index <= right_point_index:
        if (
            sorted_weight_data[right_point_index] +
            sorted_weight_data[left_point_index]
        ) <= max_weight:
            left_point_index += 1

        right_point_index -= 1
        count += 1
    return count


if __name__ == '__main__':
    # Получаем данные о весе роботов:
    robots_weight_data: list[int] = [
        int(robot_index)
        for robot_index in sys.stdin.readline().rstrip().split()
    ]
    # Получаем данные о максимальной нагрузке на транспортную платформу:
    limit: int = int(sys.stdin.readline().rstrip())

    # Считаем минимальное количество платформ для транспортировки роботов:
    min_quantity = nessesary_platforms(robots_weight_data, limit)

    # Выводим результат в файл:
    with open('robot_data.txt', 'w') as delivery_file:
        delivery_file.write(str(min_quantity))
