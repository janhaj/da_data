with open('ukol_07_pasazeri.txt') as zadani:
    radky = [radek.strip() for radek in zadani]

# 1
jizdy_za_den = [jizda.split(',') for jizda in radky[0].split(' ')]
# jizdy_za_den = [['8', '25'], ['9', '23'], ['30', '6'], ['17', '23']]
tam = sum([int(jizda[0]) for jizda in jizdy_za_den])
print('Tam jelo: ' + str(tam) + ' lidi')
zpet = sum([int(jizda[1]) for jizda in jizdy_za_den])
print('Zpet jelo: ' + str(zpet) + ' lidi')

# 2
# cesty tam
print('Cestou tam za cely tyden jelo: ')
# viceradkove reseni
cesty_tam_vnorene_seznamy = [[int(jizda.split(',')[0]) for jizda in radek.split(' ')] for radek in radky]
print(cesty_tam_vnorene_seznamy)
cesty_tam_seznam = [sum(radek) for radek in cesty_tam_vnorene_seznamy]
print(cesty_tam_seznam)
cesty_tam_celkem = sum(cesty_tam_seznam)
print(cesty_tam_celkem)
# jednoradkove (a pri obrovskych datech rychlejsi) reseni
print(sum([sum([int(jizda.split(',')[0]) for jizda in radek.split(' ')]) for radek in radky]))
# cesty zpet
print('Cestou zpet za cely tyden jelo: ')
print(sum([sum([int(jizda.split(',')[1]) for jizda in radek.split(' ')]) for radek in radky]))