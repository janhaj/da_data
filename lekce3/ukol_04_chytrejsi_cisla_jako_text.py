hodnoty = '12.1 1.68 7.45 -11.51'

nove_hodnoty = ' '.join([hodnoty.split()[0], hodnoty.split()[1], hodnoty.split()[2], str(float(hodnoty.split()[3]) + 0.25)])
print(nove_hodnoty)