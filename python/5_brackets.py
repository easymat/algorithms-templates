OPEN_PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    ')': '',
    ']': '',
    '}': ''
}

OPEN_BRACKETS = ('(', '[', '{')


def pair_for_bracket(bracket):
    return OPEN_PAIRS[bracket]


def search_for_inner_pairs(seq):
    if seq[-1] in OPEN_BRACKETS:
        return [-1]

    peeled_seq = []

    while len(seq) > 0:
        peeled_seq.append(seq.pop())

        while len(peeled_seq) != 0:
            if len(seq) == 0:
                break
            if pair_for_bracket(seq[-1]) == peeled_seq[-1]:
                seq.pop()
                peeled_seq.pop()
            else:
                break

    return peeled_seq[::-1]


def is_correct_bracket_seq(seq):

    while True:
        length = len(seq)

        if length == 0:
            return True

        if length % 2 != 0:
            return False

        seq = search_for_inner_pairs(seq)

        if len(seq) == length:
            return False


def read_input():
    with open('input.txt', 'r') as file_in:
        seq = list(map(str, file_in.readline().strip()))
    return seq


def output_answer(result):
    with open('output.txt', 'w') as file_out:
        file_out.write(result)


if __name__ == '__main__':
    seq = read_input()
    result = is_correct_bracket_seq(seq)

    output_answer(str(result))
