game = int(input())
with open('B_sol.txt','w') as fi:
    for i in range(1,game+1):
        n = int(input())
        #board = [[0 for _ in range(n)]] * n
        dot_record = set()
        r_range = set(i for i in range(n))
        c_range = set(i for i in range(n))
        r_dot_count = [0] * n
        c_dot_count = [0] * n
        for j in range(n):
            row = input()
            for k,r in enumerate(row):
                #board[j][k] = r
                if r == 'O':
                    r_range.discard(j)
                    c_range.discard(k)
                if r == '.':
                    dot_record.add((j,k))
                    r_dot_count[j] += 1
                    c_dot_count[k] += 1

        if not r_range and not c_range:
            fi.write(f'Case #{i}: Impossible\n')
            continue

        r_min = float('inf')
        r_index = []
        c_min = float('inf')
        c_index = []
        for p in r_range:
            if r_dot_count[p] < r_min:
                r_min = r_dot_count[p]
                r_index.clear()
                r_index.append(p)
            elif r_dot_count[p] == r_min:
                r_index.append(p)
        for q in c_range:
            if c_dot_count[q] < c_min:
                c_min = c_dot_count[q]
                c_index.clear()
                c_index.append(q)
            elif c_dot_count[q] == c_min:
                c_index.append(q)
        
        if r_min == c_min:
            if r_min != 1:
                result = len(r_index) + len(c_index)
                fi.write(f'Case #{i}: {r_min} {result}\n')
            else:
                result = len(r_index) + len(c_index)
                for x in r_index:
                    for y in c_index:
                        if (x,y) in dot_record:
                            result -= 1
                fi.write(f'Case #{i}: 1 {result}\n')
        else:
            if r_min < c_min:
                fi.write(f'Case #{i}: {r_min} {len(r_index)}\n')
            else:
                fi.write(f'Case #{i}: {c_min} {len(c_index)}\n')