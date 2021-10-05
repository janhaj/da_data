import sys

cisla = [int(hodnota) for hodnota in sys.argv[1:]]

# mozne reseni pres tri oddelene podminky
print('Reseni pres jednotlive podminky')
if cisla[0] > cisla[1]:
    if cisla[0] > cisla[2]:
        print(cisla[0])
if cisla[1] > cisla[0]:
    if cisla[1] > cisla[2]:
        print(cisla[1])
if cisla[2] > cisla[0]:
    if cisla[2] > cisla[1]:
        print(cisla[2])

# mozne reseni pres spojene podminky pomoci operatoru and (musi platit obe podminky)
print('Reseni pres spojene podminky')
if cisla[0] > cisla[1] and cisla[0] > cisla[2]:
    print(cisla[0])
elif cisla[1] > cisla[0] and cisla[1] > cisla[2]:
    print(cisla[1])
else:
    print(cisla[2])


print('Reseni pres serazeny seznam (funguje pro libovolne dlouhy seznam parametru)')
# sorted vrati serazeny seznam
serazeno = sorted(cisla)
# posledni hodnota je na indexu delka pole minus 1
print(serazeno[len(cisla) - 1])