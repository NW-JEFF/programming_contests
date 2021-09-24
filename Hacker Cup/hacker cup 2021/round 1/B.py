T = int(input())
with open('B_sol.txt','w') as fi:
    for i in range(1, T+1):
        n, m, a, b = map(int, input().split())
        if m+n-1 > a or m+n-1 > b:
            fi.write(f'Case #{i}: Impossible\n')
            continue

        tl = a-(m+n-2)
        tr = b-(m+n-2)
        fi.write(f'Case #{i}: Possible\n')
        s1 = f'{tl}'
        s2 = '1'
        for j in range(m-2):
            s1 += ' 1'
            s2 += ' 1'
        s1 += f' {tr}'
        s2 += ' 1'
        fi.write(f'{s1}\n')
        for k in range(n-1):
            fi.write(f'{s2}\n')