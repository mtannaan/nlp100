# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.argv[1])

    for i, line in enumerate(sys.stdin):
        if i >= n:
            continue
        
        print(line, end='')


if __name__ == "__main__":
    main()
