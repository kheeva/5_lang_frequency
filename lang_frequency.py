#!/usr/bin/env python
import sys
import re
from collections import Counter


def load_data(file_path):
    with open(file_path, 'rb') as text_file:
        text_data = text_file.read().decode('utf-8')
    return text_data


def get_most_frequent_words(text, words_number):
    regex_word = re.compile(r'[^\W\d_]+')
    words = re.findall(regex_word, text.lower())
    return [word for word, count in Counter(words).most_common(words_number)]


def main():
    if len(sys.argv) != 2:
        exit("Usage: python lang_frequency.py path_to_file")

    try:
        loaded_text = load_data(sys.argv[1])
    except FileNotFoundError as error:
        exit(error)
    else:
        print('\nThere are ten most frequent words in descending order:')

        for word in get_most_frequent_words(loaded_text, words_number=10):
            print(' {}'.format(word))


if __name__ == '__main__':
    main()
