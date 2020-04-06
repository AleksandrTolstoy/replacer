#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
from dataclasses import dataclass


def create_parser():
    """Creating CLI"""
    parser = argparse.ArgumentParser(
        prog='replacer',
        description='CLI program to replace text in files',
        epilog='(c) 16 March 2020 Tolstoy Aleksandr'
    )
    parser.add_argument('-o', '--old_text', required=True, metavar='old text', help='what will be replaced')
    parser.add_argument('-n', '--new_text', required=True, metavar='new text', help='on what will be replaced')
    parser.add_argument('-f', '--file_path', required=True, metavar='file path', help='file path')
    parser.add_argument('-i', '--insertion')
    return parser


@dataclass
class Replacer:
    old_text: str
    new_text: str
    file_path: str
    insertion: str = None

    def _search_engine(self, string: str, found: bool):
        new_text_index = string.find(self.new_text)
        # conditions for setting starting values
        if not found:
            if new_text_index != -1:
                string = string[new_text_index:]
                found = True
            else:
                return '', False

        bias = 0
        insertion_length = len(self.old_text) + len(self.insertion) + len(self.new_text)

        while self.old_text in string[bias:]:
            start = string.index(self.old_text, bias) + len(self.old_text)
            try:
                end = string.index(self.new_text, bias)
            except ValueError:
                found = False
                end = len(string)
            else:
                found = True

            part_to_be_trimmed = string[start:end]
            string = string.replace(part_to_be_trimmed, self.insertion)

            try:
                insertion_index = string[bias:].index(f'{self.old_text}{self.insertion}{self.new_text}')
            except ValueError:
                break
            bias += insertion_index + insertion_length

        return string, found

    def run(self):
        """Replaces the old string in the text file on new string everywhere

        If the key --insert used, the text between the old and new
        words will be replaced with the key value everywhere
        """
        try:
            with open(self.file_path) as old_file:
                _new_file = []

                found = True
                for line in old_file:
                    if self.insertion is not None:
                        formatted_string, found = self._search_engine(line, found)
                        _new_file.append(formatted_string)

                    else:
                        if self.old_text in line:
                            _new_file.append(line.replace(self.old_text, self.new_text))
                        else:
                            _new_file.append(line)

            with open(self.file_path, 'w') as new_file:
                new_file.write(''.join(_new_file))
        except IOError:
            print('An IOError has occurred!')


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    command_line_arguments = {key: value for key, value in vars(args).items() if value}
    print(command_line_arguments)
    replacer = Replacer(**command_line_arguments)
    replacer.run()

# also you can use
# MacOS : sed -i '' 's/old-text/new-text/g' test_data1.txt
# Linux : sed -i 's/old-text/new-text/g' test_data1.txt
