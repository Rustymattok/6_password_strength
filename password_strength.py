import re
import argparse
import os
import getpass


PATTERN_UP_LETTER = '[A-Z]+'
PATTERN_LOW_LETTER = '[a-z]+'
PATTERN_NUMERIC = '[0-9]'
PATTERN_SYMBOLS = r'\W'


def is_password_good_of_regular(regular_exp, password):
    size_coincidences = len(re.findall(regular_exp, password))
    if 0 < size_coincidences < len(password):
        return True
    else:
        return False


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file_handler:
        words_list = file_handler.read().split('\n')
    return words_list


def is_password_in_blacklist(blacklist, password):
    for word in blacklist:
        if word in password:
            return False
    return True


def get_password_strength(blacklist, password):
    if blacklist is None:
        return
    common_score = sum(
        [is_password_good_of_regular(PATTERN_UP_LETTER, password),
         is_password_good_of_regular(PATTERN_NUMERIC, password),
         is_password_good_of_regular(PATTERN_SYMBOLS, password),
         is_password_good_of_regular(PATTERN_LOW_LETTER, password),
         is_password_in_blacklist(blacklist, password)]
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
    blacklist = load_data(args.file)
    password = getpass.getpass()
    print('score password: ' +
          str(get_password_strength(blacklist, password))
          )


if __name__ == '__main__':
    main()
