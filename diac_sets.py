#!/usr/bin/python

#ą ę
#
#Napisz program diac_sets.py, który wypisze wszystkie takie zbiory wyrazów (jedna linia to jeden zbiór, wyrazy oddzielone spacją, kolejność nieistotna), w których wyrazy po usunięciu znaków diakrytycznych reprezentują to samo słowo (np. bąka, baka, baką). Program powinien czytać ze standardowego wejścia i pisać na standardowe wyjście. Przydatny może okazać się zestaw polskich liter diakrytyzowanych: 'ąćęłńóśźżĄĆĘŁŃÓŚŹŻ'.

import sys
import unicodedata

def rmOgonki(text):
    tab = str.maketrans("ąćęłńóśżźĄĆĘŁŃÓŚŻŹ", "acelnoszzACELNOSZZ")
    return text.translate(tab)

for line in sys.stdin:
   
    words = set("".join((char if char.isalpha() else " ") for char in line).split())
    output = set([rmOgonki(word.lower()) for word in words])
    
    for out in output:
        print("")
        for word in words:
            if rmOgonki(word.lower()) == out:
                print(word, end=" ")  
