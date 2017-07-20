#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import argparse

def createParser ():
    parser = argparse.ArgumentParser(
        prog = 'countwords',
        description = '''This program counts the number of words in the input file. Input file should be passed as a parameter.''',
        epilog = '''Author: Mikhail Komakhin'''
    )
    parser.add_argument (
        '-f', '--file', default='./text.txt',
        type=argparse.FileType(
            mode='r',
            encoding='UTF-8'
        ),
        help = 'Input file path. Default: ./text.txt'
    )

    return parser

if __name__ == '__main__':
    parser = createParser()
    parameters = parser.parse_args(sys.argv[1:])
    text = parameters.file.read()
    print(len(text.split()))