hodnoty = '12.1 1.68 7.45 -11.51'

hodnoty_list = hodnoty.split()
nova_hodnota = float(hodnoty_list[3]) + 0.25
hodnoty_list[3] = str(nova_hodnota)

nove_hodnoty = ' '.join(hodnoty_list)
print(nove_hodnoty)