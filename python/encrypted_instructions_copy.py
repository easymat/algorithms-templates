"""Программа расшифровывает инструкции, поступающие на марсоход в сжатом виде.

Пример:
Команда: 2[и]3[в]ш.
Расшифровка: «иивввш».

ID посылки .
"""
import sys


def read_input() -> str:
    # Получаем строку с зашифрованной инструкцией:
    seq: str = sys.stdin.readline().rstrip()
    return seq


def output_instruction(result):
    with open('to_do_list.txt', 'w') as todo_file:
        todo_file.write(result)


def decrypt(instruction: str) -> str:
    """Функция расшифровывает инструкции."""
    array_of_tasks = [
        task for task in instruction.split(']')
    ]
    result = ''
    for task in array_of_tasks:
        if task == '':
            continue
        count = ''
        action = ''

        for element in task:

            if element.isdigit():
                if flag:
                    

                count += element
                flag = True
            else:
                action += element
        if count == '':
            count = '1'

        result += action.replace('[', '') * int(count)
    return result


if __name__ == '__main__':
    # Получаем инструкцию:
    instruction = read_input()
    # Расшифровываем инструкцию:
    to_do_list = decrypt(instruction)
    # Выводим результат в файл:
    output_instruction(to_do_list)
