import re
import argparse
import os
import getpass


PATTERN_UP_LETTER = '[A-Z]+'
PATTERN_NUMERIC = '[0-9]'
PATTERN_SYMBOLS = r'\W'


def get_score_regular(regular_exp, password):
    size_coincidences = len(re.findall(regular_exp, password))
    if 0 < size_coincidences < len(password):
        return True
    else:
        return False


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file_handler:
        data_list = file_handler.read().split('\n')
    return data_list


def get_score_black_list(black_list, password):
    password = password.lower()
    for word in black_list:
        if word.lower() in password:
            return False
        else:
            return True


def get_password_strength(black_list, password):
    common_score = sum(
        [get_score_regular(PATTERN_UP_LETTER, password),
         get_score_regular(PATTERN_NUMERIC, password),
         get_score_regular(PATTERN_SYMBOLS, password),
         get_score_black_list(black_list, password)]
    ) * 2.5
    return common_score


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--file',
        default='Most-Popular-Letter-Passes.txt',
        help='command - input file'
    )
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    try:
        black_list = load_data(args.file)
        password = getpass.getpass()
        print('score password: ' +
              password +
              ' : ' +
              str(get_password_strength(black_list, password))
              )
    except ValueError:
        print('not correct format')


if __name__ == '__main__':
    main()
