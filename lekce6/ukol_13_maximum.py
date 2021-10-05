import sys

cisla = [int(parametr) for parametr in sys.argv[1:]]

if len(cisla) >= 2:
    serazeno = sorted(cisla)
    maximum = serazeno[len(serazeno) - 1]
    print('Maximum je: ' + str(maximum))
elif len(cisla) == 1:
    maximum = cisla[0]
    print('Maximum je: ' + str(maximum))
else:
    print('Chyba, nebylo zadani zadne cislo!')
    exit()