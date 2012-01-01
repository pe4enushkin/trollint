#!/usr/bin/env python
# encoding: utf-8

import sys
import clang.cindex as cindex
from utils import full_text_for_cursor, get_clang_args


def print_cursor_recursive(cur, depth=0):

    token_text = full_text_for_cursor(cur)

    print('{0} {1} | {2}'.format(' ' * 4 * depth, cur.kind, token_text))

    for child in cur.get_children():
        print_cursor_recursive(child, depth + 1)


if __name__ == '__main__':

    filename = sys.argv[1]

    index = cindex.Index.create()
    tu = index.parse(filename, get_clang_args())

    with open(filename) as fi:
        blob = fi.read()

    print_cursor_recursive(tu.cursor)
