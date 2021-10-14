c = 100
for b in range(2,99):
    for a in range(2,99):
        if a**2+b**2<c**2 and (a-1)**2+b**2>(c-1)**2:
            print(a,b)
