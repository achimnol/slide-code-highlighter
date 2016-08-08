#! /usr/bin/env python3

import argparse
import io
import sys

import pygments
import pygments.lexers
import pygments.formatters


if __name__ == '__main__':

    argparser = argparse.ArgumentParser()
    argparser.add_argument('-l', '--lang', dest='lexer', default='python3')
    argparser.add_argument('-s', '--style', dest='style', default='bw')
    args = argparser.parse_args()

    input_code = sys.stdin.buffer.read()
    lexer = pygments.lexers.get_lexer_by_name(args.lexer, encoding='utf-8')
    formatter = pygments.formatters.get_formatter_by_name('html',
        encoding='utf-8',
        full=True,
        cssfile='weighted.css',
        noclobber_cssfile=True,
        style=args.style)

    with open('output.html', 'wb') as outfile:
        pygments.highlight(input_code, lexer, formatter, outfile=outfile)

