# -*- coding: utf-8 -*-

import sys
import itertools
import math

def main():
    n = int(sys.argv[1])
    lines = sys.stdin.readlines()
    len_chunk = math.ceil(len(lines) / n)
    chunks = [lines[i * len_chunk:(i+1) * len_chunk] for i in range(n)]

    for i in range(len(chunks)):
        with open(f'out_chapter2_16_{i}.txt', 'w') as f:
            f.write(''.join(chunks[i]))

if __name__ == "__main__":
    main()
