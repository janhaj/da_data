import sys

delenec = int(sys.argv[1])
delitel = int(sys.argv[2])

if delitel == 0:
    print('Nulou delit nelze')
else:
    print(round(delenec / delitel, 3))