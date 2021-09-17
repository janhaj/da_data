jmena = ['Roman', 'Jan', 'Miroslav', 'Petr', 'Gabriel']

# 1
jmena1 = [len(jmeno) for jmeno in jmena]
print(jmena1)

# 2
jmena2 = [jmeno.upper() for jmeno in jmena]
print(jmena2)

# 3
jmena3 = [jmeno + 'a' for jmeno in jmena]
print(jmena3)

# 4
jmena4 = [jmeno.lower() + '@email.cz' for jmeno in jmena]
print(jmena4)