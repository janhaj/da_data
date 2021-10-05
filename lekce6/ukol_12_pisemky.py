import sys

znamky = [int(parametr) for parametr in sys.argv[1:]]

histogram_znamek = [0, 0, 0, 0, 0]

for znamka in znamky:
    histogram_znamek[znamka - 1] = histogram_znamek[znamka - 1] + 1

for index in range(len(histogram_znamek)):
    print('znamka ' + str(index + 1) + ' byla ' + str(histogram_znamek[index]))