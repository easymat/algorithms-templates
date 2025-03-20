import sys


def counting(quantity_of_players: int, rhyme: int) -> str:
    sequence = [_ for _ in range(1, quantity_of_players + 1)]
    not_winner = 0
    while quantity_of_players > 1:
        print(sequence)
        not_winner += rhyme % quantity_of_players
        not_winner = not_winner % quantity_of_players - 1
        sequence.pop(not_winner)
        print(quantity_of_players, not_winner)
        print(sequence)
        quantity_of_players -= 1

    return str.join('', [str(el) for el in sequence])


if __name__ == '__main__':
    # Получаем данные о количестве претендентов:
    quantity_of_players: int = int(sys.stdin.readline().rstrip())

    # Получаем данные о количестве тактов в считалке:
    rhyme: int = int(sys.stdin.readline().rstrip())

    # Считаем минимальное количество платформ для транспортировки роботов:
    winner = counting(quantity_of_players, rhyme)
    # Выводим результат в файл:
    print(int(winner))
