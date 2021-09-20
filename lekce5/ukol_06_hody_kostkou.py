import random
import sys

hody = [random.randint(1,12) for hod in range(10)]
# 3
hody = [random.randint(1,12) for hod in range(int(sys.argv[1]))]

# 1
print(hody)

# 2
hody_str = [str(hod) for hod in hody]
with open('ukol_06_vysledek_2.txt', 'w') as vysledek:
    vysledek.write(', '.join(hody_str))