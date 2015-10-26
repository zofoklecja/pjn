#Częste słowa
# Napisz program freq_words.py który zlicza liczbę wystąpień słów w tekście. Program powinien czytać dowolny tekst ze standardowego wejścia i wypisywać na standardowym wyjściu listę składającą się z par 'liczba wystąpień' i 'słowo' oddzielone znakiem tabulacji. Lista wynikowa powinna być posortowana po liczbie wystąpień. Słowa należy normalizować względem wielkości liter. Które 10 słów najczęściej występuje w napisach filmowych (http://opus.lingfil.uu.se/download.php?f=OpenSubtitles%2Fmono%2FOpenSubtitles.pl.gz)?

#!/usr/bin/python2

import sys
import collections

for line in sys.stdin:
    words = line.split()
    result = {word: words.count(word) for word in set(words)
    print sorted(result.items(),key=operator.itemgetter(1))
