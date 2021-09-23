import sys

with open(sys.argv[1]) as zadani:
    # strip abych odstranil znak konce radku
    # split na rozdeleni radku na 2 seznamy
    radky = [radek.strip().split(' ') for radek in zadani]
    # [['2AD:3824', '16.1'], ['6B2:6635', '7.6'], ['4C8:2878', '10,4'], ...

ujete_km = [float(radek[1].replace(',', '.')) for radek in radky]
print('Celkem bylo ujeto: ' + str(sum(ujete_km)))
