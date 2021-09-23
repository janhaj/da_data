hodin = 7
mzda = 450
dni = 21

mesicni_prijem = hodin * dni * mzda
print('mesicni prijem:')
print(mesicni_prijem)

pausal = mesicni_prijem * 0.6
dan = (mesicni_prijem - pausal) * 0.15
print('mesicni prijem po zdaneni:')
print(mesicni_prijem - dan)
