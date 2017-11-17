#!/usr/bin/env python
import sys
import string
from collections import Counter


def load_data(file_path):
    with open(file_path, 'rb') as text_file:
        text_data = text_file.read().decode('utf-8')
    return text_data


def get_most_frequent_words(text):
    delimiters = string.punctuation + ' '
    counted_words = Counter(map(lambda x: x.strip(delimiters), text.split()))
    return counted_words.most_common(10)


def main():
    if len(sys.argv) != 2:
        exit("Usage: python lang_frequency.py path_to_file")

    try:
        loaded_words = load_data(sys.argv[1])
    except FileNotFoundError as error:
        exit(error)
    else:
        most_frequent_words = get_most_frequent_words(loaded_words)

        for word in most_frequent_words:
            print(word[0])


if __name__ == '__main__':
    main()
