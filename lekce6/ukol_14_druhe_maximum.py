import sys

cisla = [int(parametr) for parametr in sys.argv[1:]]

if len(cisla) == 0:
    print('Chyba, nebylo zadani zadne cislo!')
    exit()
elif len(cisla) == 1:
    print('Chyba, bylo zadano pouze jedno cislo!')
    exit()
else:
    serazeno = sorted(cisla)
    maximum = serazeno[len(serazeno) - 2]
    print('Druhe maximum je: ' + str(maximum))