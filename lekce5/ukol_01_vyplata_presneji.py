import sys

# 1
with open('ukol_01_vykaz.txt', encoding='utf-8') as zadani:
    # strip abych odstranil znak konce radku
    # a nasledne prevedu retezce na cela cisla
    radky = [int(radek.strip()) for radek in zadani]
print(radky)

# 2
hodinova_mzda = int(sys.argv[1])
rocni_vyplata = sum(radky) * hodinova_mzda
print('Rocni vyplata: ' + str(rocni_vyplata))
print('Prumerna mesicni vyplata: ' + str(rocni_vyplata / len(radky)))
