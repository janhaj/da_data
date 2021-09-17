import sys
import statistics

cisla_jako_int = [int(cislo) for cislo in sys.argv[1:]]
print('Prumer: ' + str(statistics.mean(cisla_jako_int)))
print('Median: ' + str(statistics.median(cisla_jako_int)))