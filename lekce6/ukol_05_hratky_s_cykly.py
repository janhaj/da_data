import sys

cisla = [int(hodnota) for hodnota in sys.argv[1:]]

# 1
print('cast 1:')
for cislo in cisla:
    print(cislo)

# 2
print('cast 2:')
for cislo in cisla:
    print(cislo * -1)

# 3
print('cast 3:')
for cislo in cisla:
    if cislo > 0:
        print(cislo)

# 4
print('cast 4:')
print('reseni 1:')
for cislo in cisla:
    print(abs(cislo))
    
print('reseni 2:')
for cislo in cisla:
    if cislo < 0:
        print(cislo * -1)
    else:
        print(cislo)