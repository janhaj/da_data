# vytvori seznam ciselnych hodnot
seznam = [1, 4, 9, 16, 25, 36, 49, 64]
# vytvori novy seznam, kde budou pouze jejich odmocniny
[x**0.5 for x in seznam]
# vytvori novy seznam, kde budou pouze jejich zbytky po deleni dvěmi
[x % 2 for x in seznam]
# vytvori novy seznam, kde kazda polozka bude seznam, kde prvni polozka je
# vysledek celociselneho deleni a druha zbytek po tomto deleni
[[x // 2, x % 2] for x in seznam]