import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    counts = Counter(s)
    sorted_counts = sorted(counts, key= lambda x: (counts[x], -1*ord(x)), reverse = True)[0:3]
    for t in sorted_counts:
        print(f'{t} {counts[t]}')
    pass