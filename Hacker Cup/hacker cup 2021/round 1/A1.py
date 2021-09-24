T = int(input())
with open('A1_sol.txt','w') as fi:
    for i in range(1, T+1):
        n = int(input())
        w = input()
        current = None
        count = 0
        for j in w:
            if j == 'F':
                continue
            else:
                if not current:
                    current = j
                else:
                    if j != current:
                        current = j
                        count += 1
        fi.write(f'Case #{i}: {count}\n')