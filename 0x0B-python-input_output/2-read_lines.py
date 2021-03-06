#!/usr/bin/python3
""""Function"""


def read_lines(filename="", nb_lines=0):
    """Def function"""
    with open(filename, 'r', encoding="utf-8") as f:
        if nb_lines <= 0:
            read_data = f.read()
            print(read_data, end='')
        else:
            n_lines = 0
            for line in f:
                print(line, end='')
                n_lines += 1
                if n_lines == nb_lines:
                    break
