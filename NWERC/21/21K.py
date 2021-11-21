t = int(input())
for _ in range(t):

    n = int(input())
    socks = {}
    socks_map = {'left': 0, 'right': 1, 'any': 2}
    solvable = False
    socks_max = {}
    for _ in range(n):
        i,j,k = input().split()
        k = int(k)
        fit = socks_map[j]
        if not socks.get(i):
            socks[i] = [0,0,0]
            socks[i][fit] = k
            socks_max[i] = 1 if fit==2 else k
            if fit==2:
                k >= 2
                solvable = True
        else:
            solvable = True
            if fit!=2:
                socks_max[i] = max(socks_max[i], k)

    if not solvable:
        print('impossible')
    else:
        print(sum(socks_max.values())+1)