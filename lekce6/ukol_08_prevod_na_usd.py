import sys

mena = sys.argv[1]
hodnota = int(sys.argv[2])

if mena == 'czk':
    kurz = 0.046
elif mena == 'eur':
    kurz = 1.17
else:
    print('Neznama mena: "' + mena + '"')
    exit()

print(hodnota * kurz)
