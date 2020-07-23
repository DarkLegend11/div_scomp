# Find the prime factors with bruteforce method
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Rebuild the factorization
def print_factorization(factors):
    i = 0
    space_for_one = len(str(n)) - 1
    spaces = len(str(n))
    print('\n')
    num = n
    run = False
    for factor in factors:
        if run == True:
            space = spaces - len(str(num))
            print(' ' * space, end='')
        run = True
        print(num, ' | ', factors[i], end='\n')
        num //= factors[i]
        i += 1
    print(' ' * space_for_one, end='')
    print(1)

#Horizontalize
def horizont():
    i = 2
    SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    print("\n", n, "= ", end="")
    while i < max(factors):
        count = (factors.count(i))
        if count > 1:
            print(i, end="")
            print(str(count).translate(SUP), end=" * ")
            i += 1
        elif count == 1:
            print(i, end=" * ")
            i += 1
        else:
            i += 1
    print(max(factors), end="")
    if (factors.count(max(factors))) > 1:
        print(str(factors.count(max(factors))).translate(SUP))

    # Trovare i divisori
def lista_divisori(n):
    i = 2
    divisori = []
    while i <= n // 2:
        if n % i == 0:
            divisori.append(i)
            i += 1
        else:
            i += 1
    return divisori

# Stampare lista
def stampa_lista_divisori(n, divisori):
    i = 0
    print("I divisori di", n, "sono: 1", end='')
    for divisore in divisori:
        print(",", divisori[i],  end='')
        i += 1
    print(" e", str(n) + ".")

# Div
def div(c):
    if c == 'div' or c == 'Div' or c == 'DIV':
        n = int(input('\nInserisci un numero, troverò i suoi divisori. Numero: '))
        divisori = lista_divisori(n)
        stampa_lista_divisori(n, divisori)
        c = input('\nPer continuare: \'Y\', per passare alla scomposizione: \'scomp\', per uscire qualsiasi altro tasto\n')
        if c == 'scomp':
            scomp(c)
        if c != 'Y' and c != 'y' and c != 'scomp':
            run = False
        

# Scomp
def scomp(c):
    global n
    global factors
    if c == 'scomp' or c == 'Scomp' or c == 'SCOMP':
        n = int(input('\nInserisci un numero, lo scomporrò in fattori primi. Numero: '))
        factors = prime_factors(n)
        print_factorization(factors)
        horizont()
        c = input('\nPer continuare: \'Y\', per passare ai divisori: \'div\', per uscire qualsiasi altro tasto\n')
        if c == 'div':
            div(c)
        if c != 'Y' and c != 'y':
            run = False

# Mcm
#def mcd()

c = (input("\nPer i divisori scrivi: 'div', per la scomposizione in fattori primi scrivi: 'scomp'  "))
run = True
while run:
    div(c)
    scomp(c)
