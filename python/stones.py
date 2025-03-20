import sys


def counting(orders_data: list[int], stones_data: list[int]) -> int:
    count = 0
    orders = sorted(orders_data, reverse=True)
    for stone in sorted(stones_data, reverse=True):
        while len(orders) > 0 and stone < orders[0]:
            orders.pop(0)
        if len(orders) == 0:
            break
        count += 1
        orders.pop(0)

    return count


if __name__ == '__main__':
    # Получаем данные о заказах:
    order_count: int = int(sys.stdin.readline().rstrip())
    orders_data: list[int] = [
        int(order_idx)
        for order_idx in sys.stdin.readline().rstrip().split()
    ]

    # Получаем данные о доставленных камнях:
    stones_count: int = int(sys.stdin.readline().rstrip())
    stones_data: list[int] = [
        int(stone_idx)
        for stone_idx in sys.stdin.readline().rstrip().split()
    ]

    # Считаем сколько клиентов смогут получить заказ:
    satisfied = counting(orders_data, stones_data)
    # Выводим результат:
    print(satisfied)
