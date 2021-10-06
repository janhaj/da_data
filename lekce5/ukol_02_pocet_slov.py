import sys

# 1
with open('ukol_02_praha.txt', encoding='utf-8') as zadani:
    # strip abych odstranil znak konce radku
    radky = [radek.strip() for radek in zadani]

# 2
slova = [radek.split(' ') for radek in radky]

# 3
pocet_slov_na_radcich = [len(radek) for radek in slova]
print('Pocet slov na jednotlivych radcich: ' + str(pocet_slov_na_radcich))


# 4
celkovy_pocet_slov = sum(pocet_slov_na_radcich)
print('Celkovy pocet slov: ' + str(celkovy_pocet_slov))

# vysledek
print('Bylo zadani splneno? ' + str(celkovy_pocet_slov >= 150))