#!/usr/bin/python2

import sys
import unicodedata

for line in sys.stdin:
    words = set(line.split(' ,.:!?'),"utf-8")
    aski = set([unicodedata.normalize('NFD', unicode(word,"utf-8")).encode('ascii', 'ignore') for word in words])
    for ask in aski:
        for word in words:
			if word==aski:
				print "%s " % word


