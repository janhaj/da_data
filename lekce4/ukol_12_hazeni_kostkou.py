import random
import sys

# 1
print(random.randint(1, 6))

# 2 
pocet_sten = int(sys.argv[1])
print(random.randint(1, pocet_sten))

# 3 
pocet_hodu = int(sys.argv[2])
print([random.randint(1, pocet_sten) for hod in range(pocet_hodu)])