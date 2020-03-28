#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse


def create_parser():
    '''Creating CLI'''
    parser = argparse.ArgumentParser(
        prog='replacer',
        description='CLI program to replace text in files',
        epilog='(c) 16 March 2020 Tolstoy Aleksandr'
    )
    parser.add_argument('-o', '--old', required=True, metavar='str', help='what will be replaced')
    parser.add_argument('-n', '--new', required=True, metavar='str', help='on what will be replaced')
    parser.add_argument('-f', '--file', required=True, metavar='str', help='file path')
    return parser


def replacer(old_text: str, new_text: str, file: str):
    """Replaces the old string in the text file on new string everywhere"""
    try:
        with open(file) as old_file:
            _new_file = ''
            for line in old_file:
                if old_text in line:
                    line = line.replace(old_text, new_text)
                _new_file += line

        with open(file, 'w') as new_file:
            new_file.write(_new_file)

    except IOError:
        print('An IOError has occurred!')


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    replacer(namespace.old, namespace.new, namespace.file)

# also you can use
# MacOS : sed -i '' 's/old-text/new-text/g' test.txt
# Linux : sed -i 's/old-text/new-text/g' test.txt