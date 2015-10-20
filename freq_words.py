#!/usr/bin/python2

import sys
import collections

for line in sys.stdin:
    words = line.split()
    result = {word: words.count(word) for word in set(words)
    print sorted(result.items(),key=operator.itemgetter(1))
