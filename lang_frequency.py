#!/usr/bin/env python
import sys
import string


def load_data(file_path):
    try:
        with open(file_path, 'rb') as text_file:
            text_data = text_file.read()
    except FileNotFoundError as error:
        print(error)
    else:
        return text_data
    return ''


def get_most_frequent_words(text):
    words_count = {}
    words_delimiters = string.punctuation + ' '

    for word in text:
        word = word.decode('utf-8').strip(words_delimiters).lower()
        if word:
            words_count[word] = words_count.get(word, 0) + 1

    return sorted(words_count.items(), key=lambda x: x[1], reverse=True)[:10]


def main():
    if len(sys.argv) != 2:
        print("Usage: python lang_frequency.py path_to_file.")
        exit(1)
    else:
        loaded_text_file = sys.argv[1]
        loaded_words = load_data(loaded_text_file).split()
        most_frequent_words = get_most_frequent_words(loaded_words)

        for word, count in most_frequent_words:
            print('{0:10}\t{1:5}'.format(word, count))


if __name__ == '__main__':
    main()
