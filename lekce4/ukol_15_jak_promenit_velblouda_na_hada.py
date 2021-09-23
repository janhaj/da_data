import sys
slovo = sys.argv[1]

vysledek = ''.join([znak.rjust(int(znak.isupper()) + 1, '_') for znak in slovo]).lower()
print(vysledek)