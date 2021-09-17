import sys
casy = [12, 25, 64, 27, 15, 66, 128, 44]

# 3
casy = [int(cislo) for cislo in sys.argv[1:]]

# 1
casy_do_hodiny = [cas for cas in casy if cas <= 60]
print(casy_do_hodiny)

# 2
minut_pres_hodinu = [cas - 60 for cas in casy if cas > 60]
print(minut_pres_hodinu)

