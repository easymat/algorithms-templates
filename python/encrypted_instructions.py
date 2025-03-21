"""Программа расшифровывает инструкции, поступающие на марсоход в сжатом виде.

Пример:
Команда: 2[и]3[в]ш.
Расшифровка: «иивввш».

ID посылки 135373421.
"""
import string
import sys


def read_input() -> str:
    # Получаем строку с зашифрованной инструкцией:
    seq: str = sys.stdin.readline().rstrip()
    return seq


def decrypt(instruction: str) -> str:
    count: str = ''    # Для сбора числа повторений
    action: str = ''    # Собираем последовательность действий для повторения
    remember: list[tuple[str, str]] = []    # Стек для хранения действий
    # Перебираем все символы в инструкции:
    for symbol in instruction:
        # Если символ является числом, то записываем его в переменную count:
        if symbol in string.digits:
            count += symbol
        # Если попалась открывающая скобка:
        elif symbol == '[':
            # Ряд действий и количество повторений сохраняем в стек:
            remember.append((action, count))
            count = ''
            action = ''
        # Если скобка закрылась, повторяем действия в скобках и приписываем
        # к тому, что было за скобками (если было):
        elif symbol == ']':
            task, number_of_repeating = remember.pop()
            action = task + action * int(number_of_repeating)
        # Если символ является буквой - добавляем в последовательность действий
        else:
            action += symbol

    return action


if __name__ == '__main__':
    # Получаем инструкцию:
    instruction: str = read_input()
    # Расшифровываем инструкцию:
    to_do_list: str = decrypt(instruction)
    # Выводим результатл:
    print(to_do_list)
