import re
import argparse
import os


def get_pattern_regular(regular_exp):
    lc = re.compile(regular_exp)
    return lc


def get_score_regular(regular_exp, password):
    score_password = 0
    size_coincidences = len(get_pattern_regular(regular_exp).findall(password))
    if 0 < size_coincidences < len(password):
        score_password = 2.5
    return score_password


def load_data(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r') as file_handler:
        data_list = file_handler.read().split(' ')
    return data_list


def get_score_black_list(black_list, password):
    score_password = 0
    password = password.lower()
    for word in black_list:
        if password.find(word.lower()) != -1:
            score_password = 0
            break
        else:
            score_password = 2.5
    return score_password


def get_password_strength(black_list, password):
    common_score = get_score_regular('[A-Z]+', password) + \
                   get_score_regular('[0-9]', password) + \
                   get_score_regular('\\W', password) + \
                   get_score_black_list(black_list, password)
    return common_score


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--file',
        required=True,
        help='command - input file'
    )
    parser.add_argument('-p', '-password', required=True,
                        help='command - password which should check')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    try:
        black_list = load_data(args.file)
        password = args.p
        print(
            'score of password: ',
            get_password_strength(black_list, password)
        )
    except ValueError:
        print('not correct format')


if __name__ == '__main__':
    main()
