hodnoty = '12.1 1.68 7.45 -11.51'

nove_hodnoty = ' '.join(hodnoty.split()[0:3]) + ' ' + str(float(hodnoty.split()[3]) + 0.25)
print(nove_hodnoty)