import sys

hodinova_mzda = int(sys.argv[1])
# 1
with open('ukol_01_vykaz.txt', encoding='utf-8') as zadani:
    # strip abych odstranil znak konce radku
    # a nasledne prevedu retezce na cela cisla
    radky = [int(radek.strip()) for radek in zadani]
[print(radek * hodinova_mzda) for radek in radky]

# 2
with open('ukol_05_vysledek.txt', 'w') as vysledek:
    [vysledek.write(str(radek * hodinova_mzda) + '\n') for radek in radky]
