#!/usr/bin/python

#ą ę
#
#Napisz program diac_sets.py, który wypisze wszystkie takie zbiory wyrazów (jedna linia to jeden zbiór, wyrazy oddzielone spacją, kolejność nieistotna), w których wyrazy po usunięciu znaków diakrytycznych reprezentują to samo słowo (np. bąka, baka, baką). Program powinien czytać ze standardowego wejścia i pisać na standardowe wyjście. Przydatny może okazać się zestaw polskich liter diakrytyzowanych: 'ąćęłńóśźżĄĆĘŁŃÓŚŹŻ'.

import sys

for line in sys.stdin:
    dic = {'ąćęłńóśźżĄĆĘŁŃÓŚŹŻ':'acelnoszzACELNOSZZ'}
   
    words = "".join((char if char.isalpha() else " ") for char in line).split()
    words = set([word.lower() for word in words])
    aski = set([word.translate(dic) for word in words])

    print (words)
    print (aski)
