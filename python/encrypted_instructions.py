"""Программа расшифровывает инструкции, поступающие на марсоход в сжатом виде.

Пример:
Команда: 2[и]3[в]ш.
Расшифровка: «иивввш».

ID посылки 135296350.
"""
import sys


def read_input() -> str:
    # Получаем строку с зашифрованной инструкцией:
    seq: str = sys.stdin.readline().rstrip()
    return seq


def decrypt(instruction: str) -> str:
    count: str = ''    # Для сбора числа повторений
    number_of_repeating: list[str] = []    # Стек для количества повторений
    action: str = ''    # Собираем последовательность действий для повторения
    task: list[str] = []    # Стек для хранения последовательности действий
    # Перебираем все символы в инструкции:
    for symbol in instruction:
        # Если символ является числом, то записываем его в переменную count:
        if symbol.isdigit():
            count += symbol
        # Если попалась открывающая скобка:
        elif symbol == '[':
            # Последовательность из count сохраняем в стек:
            number_of_repeating.append(count)
            # Последовательность действий сохраняем в стек:
            task.append(action)
            count = ''
            action = ''
        # Если скобка закрылась, повторяем действия в скобках и приписываем
        # к тому, что было за скобками (если было):
        elif symbol == ']':
            action = task.pop() + action * int(number_of_repeating.pop())
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
