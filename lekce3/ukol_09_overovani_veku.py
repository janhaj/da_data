veky = [35, 12, 44, 11, 18, 21, 28, 18]

# 1
print('do osmnacti:')
do_osmnacti = [18 - vek for vek in veky]
print(do_osmnacti)

# 2
print('starsi 18 let:')
je_starsi_18_let = [vek >= 18 for vek in veky]
print(je_starsi_18_let)

# 3
print('maji presne 18 let:')
ma_presne_18_let = [vek == 18 for vek in veky]
print(ma_presne_18_let)