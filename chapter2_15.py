# -*- coding: utf-8 -*-

import sys

def main():
    n = int(sys.argv[1])
    buf = []

    for line in sys.stdin:
        buf.append(line)
        if len(buf) > n:
            del buf[0]
    
    for line in buf:
        print(line, end='')

if __name__ == "__main__":
    main()
