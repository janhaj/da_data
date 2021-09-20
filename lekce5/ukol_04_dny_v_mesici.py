pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 1
with(open('ukol_04_vysledek_1.txt', 'w') as vysledek):
    [vysledek.write(str(pocet) + '\n') for pocet in pocty_dni]

# 2
mesice = ['leden', 'unor', 'brezen', 'duben', 'kveten', 'cerven', 'cervenec', 'srpen', 'zari', 'rijen', 'listopad', 'prosinec']

with(open('ukol_04_vysledek_2.txt', 'w') as vysledek):
    [vysledek.write(str(mesic) + ' ') for mesic in mesice]
    [vysledek.write(str(pocet) + '\n') for pocet in pocty_dni]
