veky = [35, 12, 44, 11, 18, 21, 28, 18]

# 1
do_osmnacti = [18 - vek for vek in veky]
print(do_osmnacti)

# 2
je_starsi_18_let = [vek >= 18 for vek in veky]
print(je_starsi_18_let)

# 3
ma_presne_18_let = [vek == 18 for vek in veky]
print(ma_presne_18_let)