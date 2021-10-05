import sys

spravne_jmeno = 'honza'
spravne_heslo = 'nereknu'

jmeno = sys.argv[1]
heslo = sys.argv[2]

if jmeno == spravne_jmeno:
    if heslo == spravne_heslo:
        print('pristup povolen')
    else:
        print('pristup odepren')
else:
    print('pristup odepren')