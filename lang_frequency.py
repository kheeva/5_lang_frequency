#!/usr/bin/env python
import sys
import string
from collections import Counter


def load_data(file_path):
    with open(file_path, 'rb') as text_file:
        text_data = text_file.read().decode('utf-8')
    return text_data


def get_most_frequent_words(text, words_number):
    delimiters = string.punctuation + ' '
    counted_words = Counter(map(lambda x: x.strip(delimiters), filter(
        lambda x: x and x[0] and x[-1] not in delimiters, text.split())))
    return dict(counted_words.most_common(words_number))


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
