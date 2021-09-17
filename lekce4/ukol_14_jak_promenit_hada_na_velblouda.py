import sys

puvodni_pole = sys.argv[1].split('_')
vysledek = puvodni_pole[0] + ''.join([slovo.capitalize() for slovo in puvodni_pole[1:]])
print(vysledek) 